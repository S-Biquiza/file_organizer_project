 -File Organizer (Python)

 -Description
This is a simple **Python script** that automatically organizes files in a folder into subfolders based on their **file extensions**.  

- Example:  
- `.pdf`, `.docx`, `.txt` → **Documents/**  
- `.jpg`, `.png` → **Images/**  
- `.mp3`, `.wav` → **Audio/**  
- Any other file types → **Others/**  

---

How to Use

1. Clone the repository
git clone https://github.com/S-Biquiza/file_organizer_project.git
cd file_organizer_project

2. Prepare test files

Create a folder named test_files/.

Place some random files inside (PDFs, images, text files, MP3s, etc.).

3. Run the script
python main.py

4. Organized result

The script will automatically move files into the correct subfolders.

 -Technologies Used

Python 3.10+

Standard Libraries:

os → file and folder operations

shutil → move/copy files

-Example Output

Terminal:

 Moved invoice_001.pdf to Documents
 Moved photo.png to Images
 Moved song.mp3 to Audio
 unknown.xyz moved to Others


Folder structure after running:

test_files/
 ├── Documents/
 │    └── invoice_001.pdf
 ├── Images/
 │    └── photo.png
 ├── Audio/
 │    └── song.mp3
 ├── Others/
 │    └── unknown.xyz

- Optional Features

If you extend the script, you can add:

File counters per category.

A report.txt file showing the summary of moved files.

Input option to choose the source folder.

Handling for duplicate filenames (add suffix (1), (2), etc.).

- Key Learnings

Using dictionaries to map categories to file extensions.

Applying os and shutil for file manipulation.

Automating simple daily tasks with Python.

Importance of documentation and publishing projects on GitHub.

- Future Improvements

Support for more categories (e.g., Spreadsheets, Presentations, Archives).

Add command-line arguments with argparse.

Generate detailed logs or reports in .txt or .csv.

Create a GUI version with Tkinter or PyQt.

- Author

Created by Shelton Biquiza
📧 Email: sheltonbiquiza99@gmail.com
