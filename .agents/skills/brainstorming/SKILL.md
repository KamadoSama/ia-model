---
name: brainstorming
description: Compétence OBLIGATOIRE avant tout travail créatif (création de fonctionnalités, composants, modification de comportement). Permet d'explorer l'intention de l'utilisateur, les exigences et la conception avant toute ligne de code.
---

# Brainstorming : Des Idées vers la Conception

## Aperçu

Transformez les idées en conceptions et spécifications complètes via un dialogue collaboratif naturel.

Commencez par comprendre le contexte actuel du projet, puis posez des questions une par une pour affiner l'idée. Une fois que vous avez compris ce que vous construisez, présentez la conception et obtenez l'approbation de l'utilisateur.

<HARD-GATE>
**N'invoquez AUCUNE compétence d'implémentation, n'écrivez AUCUN code, ne générez AUCUNE ressource** tant que vous n'avez pas présenté une conception et que l'utilisateur ne l'a pas approuvée. Ceci s'applique à TOUS les projets, quelle que soit leur simplicité apparente.
</HARD-GATE>

## Anti-Pattern : "C'est trop simple pour nécessiter une conception"

Chaque projet passe par ce processus. Une todo list, un utilitaire à fonction unique, un changement de configuration — tous. Les projets "simples" sont ceux où les suppositions non examinées causent le plus de travail inutile. La conception peut être courte (quelques phrases pour les projets vraiment simples), mais vous DEVEZ la présenter et obtenir l'approbation.

## Checklist de Brainstorming

Vous DEVEZ accomplir ces tâches dans l'ordre :

1. **Explorer le contexte du projet** — vérifiez les fichiers, la documentation, les commits récents.
2. **Poser des questions de clarification** — une à la fois, comprenez l'objectif/les contraintes/les critères de succès.
3. **Proposer 2-3 approches** — avec leurs compromis et votre recommandation.
4. **Présenter la conception** — par sections adaptées à leur complexité, demandez l'approbation de l'utilisateur après chaque section.
5. **Rédiger le document de conception** — (Optionnel selon la taille de la tâche) sauvegardez dans un dossier `docs/` ou un artefact et commitez.
6. **Transition vers l'implémentation** — invoquez la compétence `planification` (writing-plans) pour créer le plan d'implémentation.

## Le Processus en Détail

**Comprendre l'idée :**
- Posez des questions une à la fois pour affiner l'idée.
- Privilégiez les questions à choix multiples lorsque c'est possible, mais les questions ouvertes sont acceptables.
- Une seule question par message - si un sujet nécessite plus d'exploration, divisez-le en plusieurs questions.
- Concentrez-vous sur la compréhension : objectif, contraintes, critères de succès.

**Explorer les approches :**
- Proposez 2 à 3 approches différentes avec des compromis.
- Présentez les options de manière conversationnelle avec votre recommandation et votre raisonnement.
- Mettez en avant l'option recommandée et expliquez pourquoi.

**Présenter la conception :**
- Une fois que vous pensez avoir compris ce que vous construisez, présentez la conception.
- Adaptez chaque section à sa complexité : quelques phrases si c'est simple, jusqu'à 200-300 mots si c'est nuancé.
- Demandez après chaque section si cela semble correct jusqu'à présent.
- Couvrez : architecture, composants, flux de données, gestion des erreurs, tests.
- Soyez prêt à revenir en arrière et à clarifier si quelque chose n'a pas de sens.

## Instructions Post-Conception

**L'implémentation :**
- Invoquez la compétence `planification` (writing-plans) pour créer un plan d'implémentation détaillé.
- N'invoquez AUCUNE autre compétence. La `planification` est toujours l'étape suivante.

## Principes Clés

- **Une question à la fois** - Ne submergez pas l'utilisateur avec plusieurs questions.
- **Choix multiples privilégiés** - Plus faciles à répondre que des questions ouvertes.
- **YAGNI rigoureusement (You Aren't Gonna Need It)** - Supprimez les fonctionnalités inutiles de toutes les conceptions.
- **Validation incrémentale** - Présentez, obtenez l'approbation, puis avancez.
