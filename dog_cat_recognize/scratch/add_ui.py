import json
import os

notebook_path = '/Users/kamado/Documents/one_day_one_technology/ia-model/dog_cat_recognize/dog_cat_recognition.ipynb'

with open(notebook_path, 'r', encoding='utf-8') as f:
    nb = json.load(f)

# Define the Interactive UI cell
ui_cell = {
    "cell_type": "code",
    "execution_count": None,
    "metadata": {},
    "outputs": [],
    "source": [
        "import ipywidgets as widgets\n",
        "from IPython.display import display, clear_output\n",
        "import io\n",
        "from PIL import Image\n",
        "import numpy as np\n",
        "import tensorflow as tf\n",
        "import matplotlib.pyplot as plt\n",
        "\n",
        "# 1. Chargement du modèle (si pas déjà fait)\n",
        "try:\n",
        "    if 'model' not in globals():\n",
        "        model = tf.keras.models.load_model('./dog_cat_model_local.h5')\n",
        "        print(\"✅ Modèle chargé avec succès.\")\n",
        "except Exception as e:\n",
        "    print(f\"❌ Erreur lors du chargement : {e}\")\n",
        "\n",
        "# 2. Widgets de l'interface\n",
        "uploader = widgets.FileUpload(accept='image/*', multiple=False)\n",
        "output = widgets.Output()\n",
        "label_res = widgets.Label(value=\"Attente d'une image...\")\n",
        "\n",
        "def on_upload_change(change):\n",
        "    with output:\n",
        "        clear_output()\n",
        "        if not uploader.value:\n",
        "            return\n",
        "        \n",
        "        # Récupérer l'image uploadée\n",
        "        uploaded_file = list(uploader.value.values())[0]\n",
        "        content = uploaded_file['content']\n",
        "        img = Image.open(io.BytesIO(content))\n",
        "        \n",
        "        # Pré-traitement pour le modèle\n",
        "        img_resized = img.resize((160, 160))\n",
        "        img_array = tf.keras.utils.img_to_array(img_resized)\n",
        "        img_array = tf.expand_dims(img_array, 0)\n",
        "        \n",
        "        # Prédiction\n",
        "        prediction = model.predict(img_array, verbose=0)\n",
        "        score = tf.nn.sigmoid(prediction[0])\n",
        "        \n",
        "        # Analyse du résultat\n",
        "        is_dog = score[0] > 0.5\n",
        "        class_name = \"CHIEN\" if is_dog else \"CHAT\"\n",
        "        confidence = score[0] if is_dog else 1 - score[0]\n",
        "        \n",
        "        # Affichage\n",
        "        plt.figure(figsize=(6, 6))\n",
        "        plt.imshow(img)\n",
        "        plt.axis('off')\n",
        "        color = 'green' if confidence > 0.8 else 'orange'\n",
        "        plt.title(f\"Résultat : {class_name} ({100*confidence:.1f}%)\", color=color, fontsize=16, fontweight='bold')\n",
        "        plt.show()\n",
        "        \n",
        "        label_res.value = f\"Dernière analyse : C'est un {class_name} !\"\n",
        "\n",
        "uploader.observe(on_upload_change, names='value')\n",
        "\n",
        "# Mise en page\n",
        "ui = widgets.VBox([\n",
        "    widgets.HTML(\"<h2>🖼️ Testeur de Chiens et Chats</h2>\"),\n",
        "    widgets.HTML(\"<p>Sélectionnez une image sur votre ordinateur pour l'analyser :</p>\"),\n",
        "    uploader,\n",
        "    output,\n",
        "    label_res\n",
        "])\n",
        "\n",
        "display(ui)"
    ]
}

# Add a header markdown cell
header_cell = {
    "cell_type": "markdown",
    "metadata": {},
    "source": [
        "## 6. Interface de Prédiction Interactive\n",
        "Exécutez la cellule ci-dessous pour lancer l'interface de test."
    ]
}

# Append to cells
nb['cells'].append(header_cell)
nb['cells'].append(ui_cell)

# Write back
with open(notebook_path, 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=1, ensure_ascii=False)

print("Interface cell added successfully.")
