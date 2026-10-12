import cv2
import torch
from ultralytics import YOLO
import time

def main():
    print("🚀 Initialisation du système de Vision...")
    
    # Vérification de l'accélération matérielle Apple Silicon (M4 Pro)
    device = 'mps' if torch.backends.mps.is_available() else 'cpu'
    print(f"✅ Dispositif utilisé pour l'IA : {device.upper()}")

    # Chargement du modèle YOLOv11 "nano" (le plus rapide, parfait pour le temps réel)
    # Si le fichier yolov11n.pt n'est pas là, il sera téléchargé automatiquement.
    # Note: Le modèle de base détecte 80 classes (dont 'person'). 
    # Plus tard, nous entraînerons notre propre modèle spécifiquement pour 'face'.
    print("🧠 Chargement du modèle de base YOLOv11...")
    model = YOLO("yolo11n.pt")  

    # Initialisation de la webcam (0 est la caméra par défaut)
    cap = cv2.VideoCapture(0)
    
    if not cap.isOpened():
        print("❌ Erreur : Impossible d'accéder à la webcam.")
        return

    print("🎥 Webcam activée. Appuyez sur 'q' pour quitter.")
    
    # Création d'une fenêtre redimensionnable
    cv2.namedWindow("IA Vision - Detection Temps Reel", cv2.WINDOW_NORMAL)
    # On définit une taille par défaut raisonnable (ex: 800x600)
    cv2.resizeWindow("IA Vision - Detection Temps Reel", 800, 600)
    
    # Pour calculer les FPS
    prev_time = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            print("⚠️ Impossible de lire l'image de la webcam.")
            break

        # --- LOGIQUE DE SURVEILLANCE ---
        # Classes d'intérêt : 0 (personne), 24 (sac à dos), 26 (sac à main), 43 (couteau), 67 (téléphone)
        classes_surveillance = [0, 24, 26, 43, 67]

        # On utilise model.track (au lieu de predict) pour suivre les individus
        # persis=True pour garder les IDs entre les frames
        results = model.track(source=frame, device=device, persist=True, verbose=False, classes=classes_surveillance)

        # Zone d'infraction (Forbidden Zone) : rectangle en haut à gauche
        # Format [x1, y1, x2, y2]
        zone_interdite = [50, 100, 300, 400] 
        intrusion_alerte = False

        # Dessiner la zone interdite sur l'image (en bleu transparent ou contour)
        cv2.rectangle(frame, (zone_interdite[0], zone_interdite[1]), 
                      (zone_interdite[2], zone_interdite[3]), (255, 0, 0), 2)
        cv2.putText(frame, "ZONE INTERDITE", (zone_interdite[0], zone_interdite[1] - 10), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2)

        # Analyser les résultats
        if results[0].boxes.id is not None:
            boxes = results[0].boxes.xyxy.cpu().numpy()
            clss = results[0].boxes.cls.cpu().numpy()
            
            for box, cls in zip(boxes, clss):
                # Vérifier si c'est une personne (classe 0)
                if cls == 0:
                    # Calculer le centre ou les bords pour détecter l'intrusion
                    x1, y1, x2, y2 = box
                    # On considère intrusion si le centre de la boîte est dans la zone
                    cx, cy = (x1 + x2) / 2, (y1 + y2) / 2
                    
                    if (zone_interdite[0] < cx < zone_interdite[2]) and \
                       (zone_interdite[1] < cy < zone_interdite[3]):
                        intrusion_alerte = True
        
        # Le résultat contient l'image avec les boîtes dessinées par YOLO
        annotated_frame = results[0].plot()

        # Affichage de l'alerte de sécurité
        if intrusion_alerte:
            cv2.rectangle(annotated_frame, (0, 0), (annotated_frame.shape[1], 100), (0, 0, 255), -1)
            cv2.putText(annotated_frame, "!!! INTRUSION DETECTEE !!!", (50, 70), 
                        cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255, 255, 255), 4)

        # Calcul et affichage des FPS
        current_time = time.time()
        fps = 1 / (current_time - prev_time)
        prev_time = current_time
        
        cv2.putText(annotated_frame, f"FPS: {int(fps)}", (20, 50), 
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        cv2.putText(annotated_frame, f"Device: {device.upper()}", (20, 90), 
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2)

        # Affichage
        cv2.imshow("IA Vision - Detection Temps Reel", annotated_frame)

        # Quitter si on appuie sur 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Nettoyage
    cap.release()
    cv2.destroyAllWindows()
    print("🛑 Arrêt du système.")

if __name__ == "__main__":
    main()
