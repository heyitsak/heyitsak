import os
import random
import shutil
import hashlib

def main():
    banners_dir = "banners"
    target = "banner.jpg"

    if not os.path.exists(banners_dir):
        print(f"Error: {banners_dir} directory not found.")
        return

    banner_files = sorted([
        f for f in os.listdir(banners_dir)
        if f.lower().endswith(('.jpg', '.jpeg', '.png'))
    ])

    if not banner_files:
        print("No banner images found in banners directory.")
        return

    current_hash = None
    if os.path.exists(target):
        with open(target, "rb") as f:
            current_hash = hashlib.md5(f.read()).hexdigest()

    # Filter out current active banner so it always swaps to a new one
    available_choices = []
    for b in banner_files:
        path = os.path.join(banners_dir, b)
        with open(path, "rb") as f:
            h = hashlib.md5(f.read()).hexdigest()
        if h != current_hash:
            available_choices.append(b)

    if not available_choices:
        available_choices = banner_files

    selected = random.choice(available_choices)
    shutil.copyfile(os.path.join(banners_dir, selected), target)
    print(f"Successfully rotated banner to: {selected}")

if __name__ == "__main__":
    main()
