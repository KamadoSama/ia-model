# 🧠 IA Models - One Day One Technology

Collection de projets et d'expérimentations en Intelligence Artificielle, Vision par Ordinateur (Computer Vision) et Deep Learning.

---

## 📁 Architecture du Dépôt

Le projet est structuré sous forme de monorepo modulaire regroupant plusieurs cas d'usage :

```text
ia-model/
├── dog_cat_recognize/           # Classification d'images Chiens vs Chats (Keras / TensorFlow)
│   ├── dog_cat_recognition.ipynb # Notebook d'entraînement et d'évaluation
│   ├── environment_tf.yml       # Configuration de l'environnement Conda TensorFlow
│   └── sampleSubmission.csv     # Exemple de soumission de format Kaggle
│
├── phone_use_detection/         # Détection d'usage du smartphone en temps réel
│   ├── backend/                 # API FastAPI + Inférence YOLOv11 & WebSockets
│   │   ├── main.py              # Serveur WebSocket et pipeline de détection
│   │   └── requirements.txt     # Dépendances Python (FastAPI, OpenCV, Ultralytics)
│   └── frontend/                # Interface web interactive React + TypeScript (Vite)
│       ├── src/                 # Composants d'affichage et flux webcam
│       └── package.json         # Dépendances Node.js
│
├── yolo/                        # Expérimentations & Fine-tuning YOLOv11
│   ├── data.yaml                # Configuration des classes et chemins du dataset
│   ├── environment.yml          # Environnement Conda pour Ultralytics YOLO
│   ├── train_model.py           # Script d'entraînement YOLO
│   └── vision_debug.py          # Script de test et débogage visuel
│
├── .gitignore                   # Exclusion des datasets lourds, poids (*.pt, *.h5) et environnements
└── .gitattributes              # Normalisation des fins de ligne (LF) et fichiers binaires
```

---

## 🚀 Démarrage Rapide

### 1. Classification Chien / Chat (`dog_cat_recognize`)
Nécessite TensorFlow et Jupyter :
```bash
cd dog_cat_recognize
conda env create -f environment_tf.yml
conda activate tensorflow_env
jupyter notebook dog_cat_recognition.ipynb
```

### 2. Détection d'Usage de Téléphone (`phone_use_detection`)

#### Backend (FastAPI + YOLOv11) :
```bash
cd phone_use_detection/backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python main.py
```

#### Frontend (React + Vite) :
```bash
cd phone_use_detection/frontend
npm install
npm run dev
```

### 3. Entraînement YOLOv11 (`yolo`)
```bash
cd yolo
conda env create -f environment.yml
conda activate yolo_env
python train_model.py
```

---

## 🛡️ Bonnes Pratiques Git & Données

- **Modèles & Poids (`*.pt`, `*.h5`, `*.keras`)** : Exclus du versioning Git par défaut pour garder le dépôt léger et rapide. Ultralytics télécharge automatiquement les poids de base (`yolo11n.pt`) lors du premier appel.
- **Datasets (`train/`, `organized_data/`)** : Exclus de Git. Téléchargez ou générez vos données localement selon la documentation de chaque sous-projet.
- **Conventions de Commit** :
  - `feat(phone-detect): ...` : Ajout d'une fonctionnalité
  - `fix(yolo): ...` : Correction de bug
  - `docs: ...` : Mise à jour de la documentation
  - `chore: ...` : Tâches de maintenance, dépendances
