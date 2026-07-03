import os
from PIL import Image, ImageOps

def crop_image_bounds(src_path, dest_path):
    print(f"Cropping transparent margins for {src_path}...")
    if not os.path.exists(src_path):
        print(f"Error: {src_path} does not exist!")
        return False
    
    with Image.open(src_path) as img:
        if img.mode != 'RGBA':
            img = img.convert('RGBA')
        
        alpha = img.split()[-1]
        bbox = alpha.getbbox()
        if bbox:
            # Crop to bounding box
            cropped = img.crop(bbox)
            cropped.save(dest_path, "PNG")
            print(f"Saved cropped image to {dest_path} (size: {cropped.size})")
            return True
        else:
            print("Warning: Image is fully transparent, copying as is.")
            img.save(dest_path, "PNG")
            return True

def create_collage(folder_path, dest_path):
    print(f"Creating collage from images in {folder_path}...")
    if not os.path.isdir(folder_path):
        print(f"Error: {folder_path} directory does not exist!")
        return False
    
    # List images
    valid_exts = ('.jpg', '.jpeg', '.png', '.webp')
    img_files = [f for f in os.listdir(folder_path) if f.lower().endswith(valid_exts)]
    print("Found files:", img_files)
    
    if len(img_files) < 5:
        print("Error: Need at least 5 images for the collage!")
        # Fallback if there are fewer images
        if len(img_files) == 0:
            return False
    
    # Let's map the images
    # We want a 1920x1080 canvas
    canvas_w, canvas_h = 1920, 1080
    collage = Image.new("RGB", (canvas_w, canvas_h), (5, 2, 6))
    
    # Let's sort or assign files to specific slots
    # Standard assignments (we have 5 files, let's sort them to ensure consistent layout)
    img_files.sort()
    
    # Slots configuration:
    # Column 1 (Left): width 600px
    #   Slot 0 (Top): height 540px, x=0, y=0
    #   Slot 1 (Bottom): height 540px, x=0, y=540
    # Column 2 (Center): width 720px
    #   Slot 2 (Middle): height 1080px, x=600, y=0
    # Column 3 (Right): width 600px
    #   Slot 3 (Top): height 540px, x=1320, y=0
    #   Slot 4 (Bottom): height 540px, x=1320, y=540
    
    slots = [
        {"x": 0, "y": 0, "w": 600, "h": 540, "file": img_files[0]},
        {"x": 0, "y": 540, "w": 600, "h": 540, "file": img_files[1]},
        {"x": 600, "y": 0, "w": 720, "h": 1080, "file": img_files[2] if len(img_files) > 2 else img_files[0]},
        {"x": 1320, "y": 0, "w": 600, "h": 540, "file": img_files[3] if len(img_files) > 3 else img_files[0]},
        {"x": 1320, "y": 540, "w": 600, "h": 540, "file": img_files[4] if len(img_files) > 4 else img_files[0]},
    ]
    
    for i, slot in enumerate(slots):
        file_path = os.path.join(folder_path, slot["file"])
        try:
            with Image.open(file_path) as img:
                print(f"Fitting {slot['file']} into slot {i} ({slot['w']}x{slot['h']})...")
                # Use ImageOps.fit to resize and crop to fill the slot nicely
                fitted_img = ImageOps.fit(img, (slot["w"], slot["h"]), method=Image.Resampling.LANCZOS)
                collage.paste(fitted_img, (slot["x"], slot["y"]))
        except Exception as e:
            print(f"Error loading {slot['file']}: {e}")
            
    # Save the final collage image
    collage.save(dest_path, "JPEG", quality=90)
    print(f"Collage successfully saved to {dest_path} (size: {collage.size})")
    return True

if __name__ == "__main__":
    src_img = os.path.join("home", "image 1.png")
    dest_img = os.path.join("home", "image_1_cropped.png")
    crop_image_bounds(src_img, dest_img)
    
    explanation_folder = os.path.join("home", "Explanation")
    collage_dest = os.path.join("home", "collage.jpg")
    create_collage(explanation_folder, collage_dest)
