# Comprendre l'IA : La Détection de Visages avec YOLOv11

Ce projet n'est pas qu'un morceau de code, c'est une plongée dans la **Vision par Ordinateur** (Computer Vision). 

Ton Mac M4 Pro va exécuter des millions d'opérations mathématiques par seconde pour "voir". Voici comment ça marche sous le capot.

## 1. Comment l'IA voit-elle une image ?

Pour toi, une image c'est des pixels avec des couleurs. Pour l'IA, c'est une gigantesque **matrice de nombres** (un tableau 3D de taille `Largeur x Hauteur x 3 canaux RVB`).

### Les Convolutions (CNN)
Le principe fondamental de YOLO (et de toutes les IA visuelles) s'appelle les **Réseaux de Neurones Convolutifs** (CNN). 
L'IA passe de petits "filtres" mathématiques (ex: matrice 3x3) sur toute l'image. 
- Au début, les filtres repèrent des **lignes et des coins** (gradients).
- Plus on s'enfonce dans le réseau, plus ces caractéristiques s'assemblent pour trouver des formes complexes (ex: **des yeux, un nez**).

## 2. Le fonctionnement de YOLO (You Only Look Once)

Historiquement, l'IA balayait l'image plusieurs fois pour trouver des objets (très lent).
**YOLO** divise l'image entière en une grille (ex: 7x7 ou 13x13). 

Pour chaque case de cette grille, l'IA essaie de prédire deux choses simultanément :
1. **La "Boîte Englobante" (Bounding Box)** : Coordonnées (x, y) du centre de l'objet, sa largeur, et sa hauteur (par rapport à la case).
2. **La Confiance et la Classe** : « *À 95%, je suis sûr qu'il y a un visage dans cette boîte.* »

> [!NOTE]
> C'est pour cela que ça s'appelle **You Only Look Once** (Tu ne regardes qu'une seule fois). L'image passe une seule fois dans le réseau neuronal, et toutes les probabilités sortent instantanément. C'est parfait pour la robotique en temps réel.

## 3. Qu'est-ce que l'Entraînement ? (Train Model)

Le modèle de base (yolov11n.pt) sait déjà reconnaître 80 classes générales (personne, voiture, bouteille) car il a été entraîné sur le dataset **COCO** par des chercheurs.

Cependant, il ne sait pas faire la différence entre *un corps humain entier* et juste *un visage*. 

### L'Apprentissage par Transfert (Transfer Learning)
Au lieu d'entraîner un modèle à partir de zéro (ce qui prendrait des mois), on utilise le modèle de base qui sait déjà "voir", et on lui dit de se spécialiser sur des visages.

Pour ça, on modifie juste la toute fin du réseau neuronal. Pendant l'entraînement (`train_model.py`), l'IA va regarder des milliers de photos de visages, comparer ses prédictions avec les "vraies" réponses (les étiquettes que nous lui fournissons dans notre dataset), et ajuster ses calculs internes (**Rétropropagation du gradient**) pour minimiser son "erreur".

## 4. L'Avantage du M4 Pro (MPS)

L'entraînement et l'inférence demandent de faire des **multiplications matricielles** géantes. Les processeurs standards (CPU) font ça lentement, une chose à la fois.

Les puces Apple Silicon ont un GPU intégré sur la même puce mémoire (Mémoire Unifiée). PyTorch utilise **MPS** (Metal Performance Shaders) pour diviser ces calculs sur des centaines de cœurs parallèles. C'est ce qui te permet de faire de la Computer Vision sans acheter une énorme carte graphique NVIDIA.
