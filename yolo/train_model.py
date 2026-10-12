from ultralytics import YOLO
import sys
import torch

def setup_training():
    """Configuration et lancement de l'entraînement du modèle sur le Mac M4 Pro."""
    
    # 1. Verification de l'accélération (MPS pour M4 Pro)
    device = 'mps' if torch.backends.mps.is_available() else 'cpu'
    print(f"✅ Dispositif utilisé pour l'IA : {device.upper()}")
    
    if device == 'cpu':
        print("⚠️ Avertissement: Vous n'utilisez pas l'accélération du M4 Pro. Vérifiez l'installation de PyTorch.")

    # 2. Choix du modèle de base
    # Nous commençons par yolov11n.pt (Nano) car il est rapide à entraîner
    # Il a déjà appris à "voir" des formes (bords, textures) sur des millions d'images
    # Nous allons faire du "Transfer Learning" (Apprentissage par transfert)
    print("🧠 Chargement du modèle pré-entraîné YOLOv11n...")
    model = YOLO("yolo11n.pt")

    # 3. Lancement de l'entraînement
    # Note: 'data.yaml' doit spécifier les chemins vers vos images de visages et les étiquettes.
    # On télécharge un dataset gratuit sur Roboflow par exemple.
    try:
        print("🚀 Lancement de l'entraînement sur le dataset de visages...")
        
        # Hyperparamètres d'entraînement pour la SURVEILLANCE
        model.train(
            # On utilise notre nouveau fichier data.yaml
            data="data.yaml", 
            
            # 100 epochs pour une bonne convergence sur des classes complexes (vol/agression)
            epochs=100, 
            
            # On garde 640 pour le compromis vitesse/précision sur M4 Pro
            imgsz=640, 
            
            # Augmenter le batch si la RAM le permet (M4 Pro a beaucoup de RAM unifiée)
            batch=32, 
            
            # Utilisation du GPU Apple (MPS)
            device=device,
            
            # Dossier dédié à la sécurité
            project="Surveillance_IA",
            name="train_securite_v1",
            
            # Paramètres spécifiques à la surveillance : 
            # On augmente la mosaïque et le flou pour simuler des caméras CCTV
            mosaic=1.0,  
            blur=0.1,
        )
        
        print("✨ Entraînement terminé ! Modèle sécurisé sauvegardé dans Surveillance_IA/train_securite_v1/weights/best.pt")

    except Exception as e:
        print(f"❌ Erreur lors de l'entraînement : {e}")
        print("\nNote : Pour l'entraînement, vous devez créer les dossiers 'images/train' et 'labels/train' avec vos données.")

if __name__ == "__main__":
    setup_training()
