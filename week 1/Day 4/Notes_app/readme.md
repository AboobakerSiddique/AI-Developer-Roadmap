# Notes App

A simple command-line Notes App built with Python that allows users to create and view notes stored as text files.

## Features

- Add new notes
- View existing notes
- Stores notes as `.txt` files
- Menu-driven interface using a `while` loop
- Uses functions for modular code
- Saves files relative to the script location using the `os` module

## Concepts Used

- Functions
- if, elif, else
- while loop
- File Handling (`open`, `read`, `write`, `append`)
- `with open()`
- `os.path.abspath()`
- `os.path.dirname()`
- `os.path.join()`

## Project Structure

```
Day 4/
├── notes_app.py
├── README.md
├── Shopping.txt
├── Gym.txt
└── College.txt
```

## How to Run

```bash
python notes_app.py
```

## Future Improvements

- Delete notes
- Edit existing notes
- Search notes
- View all available notes
- Add timestamps to notes
- Password-protect notes