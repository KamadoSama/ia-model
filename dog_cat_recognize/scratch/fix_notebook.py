import json
import os

notebook_path = '/Users/kamado/Documents/one_day_one_technology/ia-model/dog_cat_recognize/dog_cat_recognition.ipynb'

with open(notebook_path, 'r', encoding='utf-8') as f:
    nb = json.load(f)

# Define the new environment check cell
env_check_cell = {
    "cell_type": "code",
    "execution_count": None,
    "metadata": {},
    "outputs": [],
    "source": [
        "import os\n",
        "import sys\n",
        "import tensorflow as tf\n",
        "\n",
        "print(f\"Python : {sys.version}\")\n",
        "print(f\"TensorFlow : {tf.__version__}\")\n",
        "\n",
        "# GPU Metal Check\n",
        "gpu_devices = tf.config.list_physical_devices('GPU')\n",
        "if gpu_devices:\n",
        "    print(f\"✅ GPU Détecté : {gpu_devices[0]}\")\n",
        "else:\n",
        "    print(\"⚠️ Aucun GPU détecté. L'entraînement sera lent sur CPU.\")\n",
        "\n",
        "# OpenMP conflict resolution\n",
        "os.environ['KMP_DUPLICATE_LIB_OK'] = 'True'"
    ]
}

# Insert at second position (after first markdown)
nb['cells'].insert(1, env_check_cell)

# Clean up crash tracebacks and reset execution counts
for cell in nb['cells']:
    if cell['cell_type'] == 'code':
        cell['outputs'] = []  # Clear previous errors
        cell['execution_count'] = None

# Update the introductory markdown cell
if nb['cells'][0]['cell_type'] == 'markdown':
    nb['cells'][0]['source'] = [
        "# Reconnaissance de Chiens et Chats (Version Locale)\n",
        "\n",
        "Ce notebook gère l'extraction automatique du dataset `dogs-vs-cats.zip` et l'entraînement d'un modèle **MobileNetV2** sur votre machine locale.\n",
        "\n",
        "**Étapes :**\n",
        "1. Vérification de l'environnement (Stable TF + Metal)\n",
        "2. Configuration et Extraction du Dataset\n",
        "3. Organisation automatique des dossiers\n",
        "4. Chargement et Augmentation des données\n",
        "5. Construction et Entraînement du modèle\n",
        "6. Prédiction"
    ]

# Write back to file
with open(notebook_path, 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=1, ensure_ascii=False)

print("Notebook updated successfully.")
