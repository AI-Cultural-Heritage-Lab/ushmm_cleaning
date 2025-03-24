# ushmm_cleaning

This repository manages the scripts and data organization used in the USHMM PDF cleaning project.

---

## 📁 Repository Structure

- `Completed_Scripts/` – Finalized scripts for inspection and cleaning.  
- `HTML_files/` – Original HTML documents to be cleaned.  
- `HTML_txtfolder/` – Extracted text versions of HTML files.  
- `Aileen_JSON_files/` – Processed JSON files by Aileen 
- `Phase2_Folders/` – Organized data after Phase 2 processing.  
                    – Functions for extracting data from 030 series PDFs and reprocessing.
- `temporary_dir/` – Temporary working folder for intermediate files.  
- `ushmm-pdfs/` – Original PDF documents.  
- `HTML_filtering.py` – Script to clean unwanted data patterns.  
- `.DS_Store` – MacOS file (can be ignored or deleted).  

---

## 🛠 How to Use This Repository (for Beginners)

### 1. Clone the Repository

If you're using GitHub for the first time, you’ll need Git installed on your computer. Then, open your terminal and run:

```bash
git clone https://github.com/AI-Cultural-Heritage-Lab/ushmm_cleaning.git
```

This downloads the whole project to your computer.

### 2. Make Local Changes
You can edit or add your files/scripts in the downloaded folder. For example, if you want to work on HTML_filtering.py, you can open it in VS Code, Jupyter Notebook, etc.

### 3. Save Your Changes Locally
Use the following commands:

```bash
git add .
git commit -m "your message here"
```

Replace "your message here" with a brief note on what you changed.

### 4. Update Your Local Copy Before Pushing
Important: Before pushing, always pull first to avoid overwriting remote changes:

```bash
git pull origin main
```

### 5. Push to GitHub
git push origin main
This uploads your changes to the online repo.

### 🧠 Tips

Never skip git pull before pushing.
Keep commit messages short but meaningful.
If you mess up, you can recover past versions using git log or git reflog.


