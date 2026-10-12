---
name: remotion-best-practices
description: "Meilleures pratiques pour Remotion - Création de vidéos en React"
risk: minimal
source: community
tags: "remotion, video, react, animation, composition"
date_added: "2026-02-28"
---

## Objectif

Cette compétence centralise les meilleures pratiques et patterns pour le développement avec **Remotion** (création de vidéos par le code en React). Elle fournit un accès direct à une bibliothèque de règles spécifiques pour gérer l'audio, la vidéo, les animations, la 3D, et plus encore.

## Quand utiliser cette compétence ?

Vous devez **OBLIGATOIREMENT** utiliser cette compétence à chaque fois que vous êtes confronté à du code générant ou manipulant de la vidéo via Remotion.
Cela inclut :
- Le calcul de dimensions ou durées vidéo/audio.
- Les animations de texte ou les transitions de scène.
- L'importation d'assets (images, lottie, srt).
- L'utilisation de TailwindCSS dans un composant Remotion.

## Comment utiliser cette compétence

Plutôt que de contenir toutes les instructions dans ce seul fichier, cette compétence agit comme un index. 
**Vous devez consulter (lire) le fichier `.md` spécifique dans le dossier `rules/` correspondant à votre besoin actuel.**

Voici le catalogue des règles disponibles :

*   [rules/3d.md](rules/3d.md) - Contenu 3D dans Remotion utilisant Three.js et React Three Fiber.
*   [rules/animations.md](rules/animations.md) - Compétences fondamentales d'animation pour Remotion.
*   [rules/assets.md](rules/assets.md) - Importation d'images, vidéos, audio et polices.
*   [rules/audio.md](rules/audio.md) - Utilisation de l'audio et du son (import, découpe, volume, vitesse, pitch).
*   [rules/calculate-metadata.md](rules/calculate-metadata.md) - Définir dynamiquement la durée, les dimensions et les props d'une composition.
*   [rules/can-decode.md](rules/can-decode.md) - Vérifier si une vidéo peut être décodée par le navigateur (Mediabunny).
*   [rules/charts.md](rules/charts.md) - Modèles de graphiques et de visualisation de données.
*   [rules/compositions.md](rules/compositions.md) - Définition des compositions, images fixes, dossiers et métadonnées dynamiques.
*   [rules/display-captions.md](rules/display-captions.md) - Affichage de sous-titres avec des pages style TikTok et surbrillance des mots.
*   [rules/extract-frames.md](rules/extract-frames.md) - Extraction de frames à partir de vidéos à des horodatages spécifiques.
*   [rules/fonts.md](rules/fonts.md) - Chargement de Google Fonts et de polices locales.
*   [rules/get-audio-duration.md](rules/get-audio-duration.md) - Obtenir la durée d'un fichier audio en secondes.
*   [rules/get-video-dimensions.md](rules/get-video-dimensions.md) - Obtenir la largeur et la hauteur d'un fichier vidéo.
*   [rules/get-video-duration.md](rules/get-video-duration.md) - Obtenir la durée d'un fichier vidéo en secondes.
*   [rules/gifs.md](rules/gifs.md) - Affichage de GIFs synchronisés avec la timeline Remotion.
*   [rules/images.md](rules/images.md) - Intégration d'images en utilisant le composant `Img`.
*   [rules/import-srt-captions.md](rules/import-srt-captions.md) - Importation de fichiers de sous-titres `.srt`.
*   [rules/lottie.md](rules/lottie.md) - Intégration d'animations Lottie.
*   [rules/measuring-dom-nodes.md](rules/measuring-dom-nodes.md) - Mesure des dimensions des éléments du DOM.
*   [rules/measuring-text.md](rules/measuring-text.md) - Mesure des dimensions du texte, ajustement aux conteneurs.
*   [rules/sequencing.md](rules/sequencing.md) - Modèles de séquençage (délai, découpe, limitation de la durée).
*   [rules/tailwind.md](rules/tailwind.md) - Utilisation de TailwindCSS dans Remotion.
*   [rules/text-animations.md](rules/text-animations.md) - Typographie et modèles d'animation de texte.
*   [rules/timing.md](rules/timing.md) - Courbes d'interpolation (linéaire, easing, spring animations).
*   [rules/transcribe-captions.md](rules/transcribe-captions.md) - Transcription audio pour générer des sous-titres.
*   [rules/transitions.md](rules/transitions.md) - Modèles de transition de scènes.
*   [rules/trimming.md](rules/trimming.md) - Modèles de découpe pour couper le début ou la fin des animations.
*   [rules/videos.md](rules/videos.md) - Intégration de vidéos (découpe, volume, vitesse, boucle).

## Critères de Qualité (Checklist)

Avant de valider du code Remotion, vérifiez :
- [ ] Avez-vous lu la règle correspondante dans le dossier `rules/` ?
- [ ] Les imports d'assets (vidéos, polices) respectent-ils les formats recommandés pour Remotion ?
- [ ] Les animations `spring` ou `interpolate` sont-elles couplées correctement à la `frame` actuelle ?
- [ ] Les compositions ont-elles des identifiants (`id`) uniques ?
