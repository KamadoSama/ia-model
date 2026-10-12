---
name: planification
description: À utiliser lorsque vous avez une spécification ou des exigences approuvées pour une tâche à étapes multiples, et ce, avant de toucher au code. Transforme la conception en plan d'action.
---

# Planification (Writing Plans)

## Aperçu

Rédigez des plans d'implémentation complets en supposant que l'ingénieur qui lira le plan n'a aucun contexte sur notre base de code. Documentez tout ce qu'il a besoin de savoir : quels fichiers modifier pour chaque tâche, le code, les tests, la documentation qu'il pourrait avoir à vérifier, et comment tester. Donnez-lui le plan complet sous forme de petites tâches de 2 à 5 minutes. Appliquez les principes DRY, YAGNI, TDD, et les commits fréquents.

**Annoncez au début :** "J'utilise la compétence `planification` pour créer le plan d'implémentation."

## Granularité des Tâches (Petites Étapes)

**Chaque étape est une action de 2 à 5 minutes :**
- "Écrire le test qui échoue" - étape
- "L'exécuter pour s'assurer qu'il échoue" - étape
- "Implémenter le code minimal pour faire passer le test" - étape
- "Exécuter les tests et s'assurer qu'ils passent" - étape
- "Commit" - étape

## En-tête du Document de Plan

**Chaque plan DOIT commencer par cet en-tête (utilisez le système d'Artefacts ou créez un fichier `implementation_plan.md`) :**

```markdown
# Plan d'implémentation : [Nom de la Fonctionnalité]

**Objectif :** [Une phrase décrivant ce que cela construit]

**Architecture :** [2-3 phrases sur l'approche]

**Tech Stack :** [Technologies clés/bibliothèques]

---
```

## Structure d'une Tâche

````markdown
### Tâche N : [Nom du Composant]

**Fichiers concernés :**
- Créer : `chemin/exact/vers/fichier.py`
- Modifier : `chemin/exact/vers/existant.py:123-145`
- Test : `tests/chemin/exact/vers/test.py`

**Étape 1 : Écrire le test qui échoue**

```python
def test_comportement_specifique():
    resultat = fonction(entree)
    assert resultat == attendu
```

**Étape 2 : Exécuter le test pour vérifier l'échec**

Exécuter : `pytest tests/chemin/test.py::nom_test -v`
Attendu : FAIL avec "fonction non définie"

**Étape 3 : Implémentation minimale**

```python
def fonction(entree):
    return attendu
```

**Étape 4 : Exécuter le test pour vérifier le succès**

Exécuter : `pytest tests/chemin/test.py::nom_test -v`
Attendu : PASS

**Étape 5 : Commit**

```bash
git add tests/chemin/test.py src/chemin/fichier.py
git commit -m "feat: ajout de la fonctionnalité spécifique"
```
````

## À retenir
- Les chemins de fichiers doivent toujours être exacts.
- Le code complet doit être dans le plan (pas de simples "ajouter la validation").
- Les commandes exactes avec la sortie attendue.
- Respect strict des principes : DRY, YAGNI, TDD, commits fréquents.

## Passage à l'exécution

Une fois le plan sauvegardé et approuvé par l'utilisateur, et seulement à ce moment-là, l'implémentation peut commencer. Demandez toujours si l'utilisateur souhaite modifier ou valider le plan avant de générer le code.
