# Random Username Generator

## Overview
This project provides a Python-based application for generating random usernames. The program combines randomly selected adjectives and nouns to create unique usernames, with options to customize them further by adding numbers, special characters, and truncating the length.

### Features:
- Combines adjectives and nouns from a dataset to generate usernames.
- Allows customization with:
  - Numbers
  - Special characters
  - Adjustable length.
- Saves generated usernames to a specified folder.
- User-friendly interface for repeated username generation.

---

## Files in the Project

### 1. **`adjective_noun_dataset.csv`**
This CSV file contains a dataset of adjectives and nouns used to generate usernames.
- Columns: `adjective`, `noun`
- Example rows:
  ```
  adjective,noun
  Brave,Dragon
  Happy,Tiger
  ```

### 2. **`dataset.py`**
This script generates the `adjective_noun_dataset.csv` file by creating 1,000 random adjective-noun pairs.
#### Key Highlights:
- A predefined list of adjectives and nouns.
- Randomly pairs them to form the dataset.
- Saves the dataset to `adjective_noun_dataset.csv`.

### 3. **`Username.py`**
This is the main script for generating random usernames.
#### Key Functions:
- `load_data(filename)`: Loads the adjectives and nouns from the CSV file.
- `generate_username(include_numbers, include_specials, length, adjectives, nouns)`: Generates usernames based on user preferences.
- `save_usernames_to_file(usernames, folder_path, filename)`: Saves generated usernames to a file in the specified directory.
- `main()`: Provides a user interface for customization and manages the overall workflow.

---

## How to Use

### 1. Generate the Dataset
Run `dataset.py` to generate the `adjective_noun_dataset.csv` file. This file is required for the main script to work.
```bash
python dataset.py
```

### 2. Run the Username Generator
Run the `Username.py` script to start generating usernames:
```bash
python Username.py
```

### 3. Customize Options
When prompted:
1. Choose whether to include numbers or special characters.
2. Set a maximum username length (optional).
3. Specify how many usernames to generate.
4. View generated usernames and save them to a file.

---

## Example
1. Input:
   - Include numbers: Yes
   - Include special characters: No
   - Maximum length: 12
   - Number of usernames: 3

2. Output:
   ```
   Generated Usernames:
   CoolTiger88
   BraveWolf12
   HappyFox32
   
   Usernames saved to C:\Users\User\Desktop\73772226111\Project\usernames.txt
   ```

---

## Dependencies
- Python 3.6+
- Modules: `csv`, `random`, `os`, `string`

---

## File Structure
```
Project Directory
|-- adjective_noun_dataset.csv
|-- dataset.py
|-- Username.py
|-- usernames.txt (Generated usernames will be saved here)
```

---

## Notes
- Ensure the dataset file (`adjective_noun_dataset.csv`) is in the same directory as `Username.py` or provide the correct path in the script.
- Modify the `save_folder` variable in `Username.py` to customize where usernames are saved.

---

## License
This project is open-source and available for modification and distribution.
