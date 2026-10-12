import os
import tensorflow as tf

IMG_SIZE = (160, 160)
BATCH_SIZE = 32
train_dir = '/Users/kamado/Documents/one_day_one_technology/ia-model/dog_cat_recognize/organized_data/train'

if not os.path.exists(train_dir):
    print(f"❌ Error: {train_dir} does not exist.")
    exit(1)

try:
    train_ds = tf.keras.utils.image_dataset_from_directory(
        train_dir,
        validation_split=0.2,
        subset="training",
        seed=123,
        image_size=IMG_SIZE,
        batch_size=BATCH_SIZE)
    print(f"✅ Successfully loaded training dataset: {len(train_ds)} batches.")
    
    for images, labels in train_ds.take(1):
        print(f"Batch shape: {images.shape}")
        print(f"Labels: {labels.numpy()[:5]}")
        
except Exception as e:
    print(f"❌ Error loading dataset: {e}")
