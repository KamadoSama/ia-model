import cv2
import json
import asyncio
import time
from datetime import datetime
from typing import List
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
from ultralytics import YOLO
import threading

app = FastAPI()

# Enable CORS for the frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load YOLO model
model = YOLO("yolo11n.pt")

# Camera initialization
camera = cv2.VideoCapture(0)

# Global state for sharing between threads
latest_detections = []
latest_frame_bytes = None
frame_width = 640
frame_height = 480
state_lock = threading.Lock()

def video_capture_loop():
    global latest_detections, latest_frame_bytes, frame_width, frame_height
    
    # Get initial dimensions
    success, frame = camera.read()
    if success:
        frame_height, frame_width, _ = frame.shape

    while True:
        success, frame = camera.read()
        if not success:
            time.sleep(0.1)
            continue
        
        # 1. Run Inference
        results = model(frame, verbose=False)[0]
        
        current_detections = []
        for box in results.boxes:
            b = box.xyxy[0].tolist()  # [x1, y1, x2, y2]
            conf = float(box.conf[0])
            cls = int(box.cls[0])
            name = results.names[cls]
            
            current_detections.append({
                "box": b,
                "confidence": conf,
                "class": name
            })
            
            # Auto-save screenshot if phone detected (use a copy to be safe)
            if name == "cell phone" and conf > 0.8:
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                filename = f"../screenshots/alert_{timestamp}.jpg"
                cv2.imwrite(filename, frame.copy())
                print(f"ALERT: Smartphone detected! Screenshot saved to {filename}")

        # 2. Encode frame for MJPEG
        _, buffer = cv2.imencode('.jpg', frame)
        frame_bytes = buffer.tobytes()

        # 3. Update global state
        with state_lock:
            latest_detections = current_detections
            latest_frame_bytes = frame_bytes
        
        # Control FPS to avoid excessive CPU usage
        time.sleep(0.01)

# Start single capture thread
capture_thread = threading.Thread(target=video_capture_loop, daemon=True)
capture_thread.start()

async def gen_frames():
    while True:
        with state_lock:
            if latest_frame_bytes is None:
                frame_out = None
            else:
                frame_out = latest_frame_bytes
        
        if frame_out:
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame_out + b'\r\n')
        
        await asyncio.sleep(0.03) # ~30 FPS for the stream

@app.get("/video_feed")
async def video_feed():
    return StreamingResponse(gen_frames(), media_type="multipart/x-mixed-replace; boundary=frame")

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            with state_lock:
                await websocket.send_json({
                    "detections": latest_detections,
                    "width": frame_width,
                    "height": frame_height
                })
            await asyncio.sleep(0.1)  # Send metadata every 100ms
    except WebSocketDisconnect:
        print("Websocket disconnected")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
