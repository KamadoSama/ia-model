import React, { useState, useEffect, useRef } from 'react';
import './index.css';

interface Detection {
  box: [number, number, number, number];
  class: string;
  confidence: number;
}

interface WSData {
  detections: Detection[];
  width: number;
  height: number;
}

interface DeviceLog {
  id: string;
  time: string;
  text: string;
  type: 'alert' | 'info';
}

const App: React.FC = () => {
  const [detections, setDetections] = useState<Detection[]>([]);
  const [frameDim, setFrameDim] = useState({ width: 640, height: 480 });
  const [alertActive, setAlertActive] = useState(false);
  const [logs, setLogs] = useState<DeviceLog[]>([]);
  const [timestamp, setTimestamp] = useState(new Date().toLocaleTimeString());
  
  const audioRef = useRef<HTMLAudioElement | null>(null);
  const lastAlertTime = useRef<number>(0);
  const alertActiveRef = useRef(false);
  const lastLoggedObjects = useRef<Set<string>>(new Set());

  const addLog = (text: string, type: 'alert' | 'info') => {
    const newLog: DeviceLog = {
      id: Math.random().toString(36).substr(2, 9),
      time: new Date().toLocaleTimeString(),
      text,
      type
    };
    setLogs(prev => [newLog, ...prev].slice(0, 50));
  };

  useEffect(() => {
    addLog("SYSTEM INITIALIZED", 'info');
    addLog("LINKING SECURE CAMERA FEED...", 'info');

    const ws = new WebSocket('ws://localhost:8000/ws');
    
    ws.onopen = () => {
      addLog("SERVER CONNECTION ESTABLISHED", 'info');
    };

    ws.onmessage = (event) => {
      const data: WSData = JSON.parse(event.data);
      setDetections(data.detections);
      setFrameDim({ width: data.width, height: data.height });
      
      const hasPhone = data.detections.some(d => d.class === 'cell phone' && d.confidence > 0.8);
      
      // Handle PHONE Alert Logic
      if (hasPhone && !alertActiveRef.current) {
        const now = Date.now();
        if (now - lastAlertTime.current > 3000) {
          addLog("CRITICAL: UNAUTHORIZED DEVICE DETECTED", 'alert');
          lastAlertTime.current = now;
          if (audioRef.current) {
            audioRef.current.play().catch(e => console.error("Audio blocked", e));
          }
        }
      } else if (!hasPhone && alertActiveRef.current) {
        addLog("SURVEILLANCE STATUS: SECURE", 'info');
      }
      
      // Handle General Detection Logs (Throttled)
      const currentObjects = new Set(data.detections.filter(d => d.class !== 'cell phone').map(d => d.class));
      currentObjects.forEach(obj => {
        if (!lastLoggedObjects.current.has(obj)) {
          addLog(`${obj.toUpperCase()} ENTERED VIEW`, 'info');
        }
      });
      lastLoggedObjects.current = currentObjects;

      alertActiveRef.current = hasPhone;
      setAlertActive(hasPhone);
    };

    ws.onerror = () => {
      addLog("SIGNAL LOST: CHECKING BACKEND STATUS", 'alert');
    };

    const timer = setInterval(() => {
      setTimestamp(new Date().toLocaleTimeString());
    }, 1000);

    return () => {
      ws.close();
      clearInterval(timer);
    };
  }, []);

  return (
    <div className="dashboard-grid">
      {/* Overlay Effects */}
      <div className="overlay-fx"></div>

      {/* Main Camera Module */}
      <div className="module camera-section">
        <div className="module-header">
          <div style={{ display: 'flex', gap: '8px', alignItems: 'center' }}>
            <div className="recording-dot"></div>
            LIVE SURVEILLANCE - FEED_01
          </div>
          <div>{timestamp}</div>
        </div>
        
        <div className="video-container">
          <div 
            className="display-wrapper" 
            style={{ aspectRatio: `${frameDim.width} / ${frameDim.height}` }}
          >
            <img 
              src="http://localhost:8000/video_feed" 
              className="video-feed" 
              alt="Live Feed" 
            />
            
            <div className="boxes-layer">
              {detections.map((det, index) => {
                const isPhone = det.class === 'cell phone';
                const color = isPhone ? 'var(--alert-red)' : 'var(--safe-green)';
                
                return (
                  <div 
                    key={index}
                    className="bounding-box"
                    style={{
                      left: `${(det.box[0] / frameDim.width) * 100}%`,
                      top: `${(det.box[1] / frameDim.height) * 100}%`,
                      width: `${((det.box[2] - det.box[0]) / frameDim.width) * 100}%`,
                      height: `${((det.box[3] - det.box[1]) / frameDim.height) * 100}%`,
                      borderColor: color,
                      boxShadow: `0 0 10px ${color}33`
                    }}
                  >
                    <div 
                      className="label-container" 
                      style={{ backgroundColor: color }}
                    >
                      {det.class.toUpperCase()} {Math.round(det.confidence * 100)}%
                    </div>
                  </div>
                );
              })}
            </div>
          </div>
          
          {alertActive && <div className="critical-alert-overlay"></div>}
        </div>
      </div>

      {/* Stats Module */}
      <div className="module stats-section">
        <div className="module-header">SYSTEM METRICS</div>
        <div style={{ marginTop: '12px' }}>
          <div className="stat-row">
            <span>STATUS</span>
            <span className="stat-value" style={{ color: alertActive ? 'var(--alert-red)' : 'var(--safe-green)' }}>
              {alertActive ? 'ALERT' : 'OPTIMAL'}
            </span>
          </div>
          <div className="stat-row">
            <span>LATENCY</span>
            <span className="stat-value">14MS</span>
          </div>
          <div className="stat-row">
            <span>ACTIVE OPS</span>
            <span className="stat-value">{detections.length}</span>
          </div>
          <div className="stat-row">
            <span>ENGINE</span>
            <span className="stat-value">YOLOv11n</span>
          </div>
        </div>
      </div>

      {/* Logs Module */}
      <div className="module logs-section">
        <div className="module-header">ACTIVITY LOGS</div>
        <div className="logs-container">
          {logs.map(log => (
            <div key={log.id} className={`log-entry ${log.type}`}>
              <span className="log-time">[{log.time}]</span>
              <span>{log.text}</span>
            </div>
          ))}
          {logs.length === 0 && (
            <div style={{ opacity: 0.3, fontSize: '10px', textAlign: 'center', marginTop: '20px' }}>
              WAITING FOR SYSTEM EVENTS...
            </div>
          )}
        </div>
      </div>

      <audio ref={audioRef} src="https://actions.google.com/sounds/v1/alarms/beep_short.ogg" />
    </div>
  );
};

export default App;
