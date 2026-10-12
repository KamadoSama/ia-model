import json
import os

notebook_path = '/Users/kamado/Documents/one_day_one_technology/ia-model/dog_cat_recognize/dog_cat_recognition.ipynb'

with open(notebook_path, 'r', encoding='utf-8') as f:
    nb = json.load(f)

# Replace all occurrences of .h5 with .keras in all cells
for cell in nb['cells']:
    if 'source' in cell:
        new_source = []
        for line in cell['source']:
            new_line = line.replace('dog_cat_model_local.h5', 'dog_cat_model_local.keras')
            new_source.append(new_line)
        cell['source'] = new_source

# Write back to file
with open(notebook_path, 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=1, ensure_ascii=False)

print("Notebook updated to use .keras format successfully.")
