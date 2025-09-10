import os
import shutil

source_folder = "test_files"

destinations = {
    "Documents": [".pdf", ".docx", ".txt"],
    "Images": [".jpg", ".png"],
    "Audio": [".mp3", ".wav"],
    "Others": []
}

for folder in destinations.keys():
    os.makedirs(os.path.join(source_folder, folder), exist_ok=True)
print("Subpastas criadas (ou já existiam).")

for file in os.listdir(source_folder):
    file_path = os.path.join(source_folder, file)
    if os.path.isfile(file_path):
        moved = False
        for folder, extensions in destinations.items():
            if any(file.lower().endswith(ext) for ext in extensions):
                shutil.move(file_path, os.path.join(source_folder, folder, file))
                print(f"✅ Movido {file} para {folder}")
                moved = True
                break
        if not moved:
            shutil.move(file_path, os.path.join(source_folder, "Others", file))
            print(f"⚠️ {file} movido para Others")
