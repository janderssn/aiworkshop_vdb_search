from vdb import current_collection, add_embeddings, find_most_similar_embeddings
from embed import encode_string, encode_image, encode_image_from_path
from pathlib import Path
import json

data_file = "data.json"
products_dir = Path("products")
# Iterate through the dirs to get each product data, products_dir contains directories with two files data.json and 0.png
# The data.json file contains the product data and the 0.png is the image
for product_dir in products_dir.iterdir():
    if product_dir.is_dir():
        pid = product_dir.name
        product_data = json.loads((product_dir / data_file).read_text())
        product_title = product_data["title"]
        product_category = product_data["category"]
        product_url = product_data["url"]
        product_pid = product_data["pid"]
        product_image_path = product_data["image"]
        if product_pid != pid:
            raise ValueError(f"Product id in data.json does not match the directory name: {pid}")   
        image_path = Path(product_image_path)
        if not image_path.exists():
            raise ValueError(f"Image file does not exist: {image_path}")
        
        image_embeddings = encode_image_from_path(product_image_path)
        add_embeddings(embeddings=image_embeddings,
                       metadatas=product_data)


# Extract the pid, title, category, url, and image
# Create embeddings for images and add to the collection with the product data as metadata
