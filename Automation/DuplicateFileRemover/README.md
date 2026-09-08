# Duplicate File Remover

## 📌 Project Description

This project is a Python-based automation tool that identifies duplicate files from a specified directory using **MD5 checksum** and automatically removes duplicate files.

The program scans the given directory and its subdirectories, calculates the checksum of each file, groups files having the same checksum, and deletes the duplicate copies while keeping the first occurrence.

## 🛠️ Technologies Used

* Python
* `os` module
* `hashlib` module
* File Handling
* Dictionary
* Lambda Function
* Filter Function

## ⚙️ Features

* Accepts a directory as input
* Validates whether the given path exists
* Checks whether the path is a directory
* Traverses directories and subdirectories
* Calculates MD5 checksum for each file
* Identifies duplicate files
* Deletes duplicate files automatically
* Displays the total number of deleted files

## 🔄 Working

1. The program takes the directory name.
2. It checks whether the directory exists.
3. It traverses the directory using `os.walk()`.
4. The MD5 checksum of every file is calculated.
5. Files having the same checksum are considered duplicates.
6. The first file is retained.
7. The remaining duplicate files are deleted.
8. The total number of deleted files is displayed.

## ▶️ How to Run

Open Command Prompt or Terminal and navigate to the project directory.

```bash
python DuplicateFileRemover.py
```

Make sure the `Test` directory exists in the appropriate location before running the program.

## 📂 Project Structure

```text
Duplicate-File-Remover/
│
├── DuplicateFileRemover.py
├── README.md
└── Screenshots/
    └── Output.png
```

## 🖥️ Sample Output

```text
Total deleted files : 3
```

## 📸 Screenshots

Screenshots demonstrating the execution and output of the project are included in the `Screenshots` folder.

## 🎯 Learning Outcomes

* Understanding Python file handling
* Understanding directory traversal
* Working with MD5 checksum
* Using Python dictionaries
* Using lambda and filter functions
* Automating duplicate file removal
* Working with the `os` module

## 👩‍💻 Author

Sharvari Bhosale

