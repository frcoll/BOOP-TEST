# BOOP – Book Of Organized Puzzles

Welcome to **BOOP**, a fully automated solution to generate your personalized puzzle book. From title pages to solution pages, everything is crafted seamlessly. Just provide the words, and it’ll do the magic!

## 🔧 Features
- Automatically generates a full-fledged puzzle book (PDF format).
- Includes:
  - **Title Page**
  - **Index Page**
  - **Puzzle Pages** (unique identifiers for each page).
  - **Solution Pages**.
- Puzzles are categorized **Topic-wise** and further divided into:
  - **Normal Mode**: 10 puzzles.
  - **Hard Mode**: 5 puzzles.
  - **Bonus Mode**: 2 puzzles.

## 🗂 Project Structure
```plaintext
Assets/              # Includes backgrounds, title page templates, etc.
  ├── Cover.png            # Cover image
  ├── pageBackground.png   # Page background image
Words/               # Folder for word input and processing
  ├── rawWordToJSON.py     # Converts words.txt to JSON
  ├── words.json           # Processed JSON of words
  ├── words.txt            # Input file (your word list, atleast 200 words per topic)
appendImage.py       # Handles adding images to pages
generatePuzzle.py    # Core puzzle generation logic
index.py             # Creates the index page
main.py              # The main driver script
README.md            # Documentation
```

## 🚀 Getting Started
1. Place your word list in `Words/words.txt` (200 words per topic).
2. Run the script:
   ```bash
   python main.py
   ```
3. Voilà! Your puzzle book is ready in PDF format.

## 📖 How It Works
1. The word list is processed into categorized JSON using `rawWordToJSON.py`.
2. Puzzles are generated with specific rules for Normal, Hard, and Bonus modes.
3. Pages are styled and compiled into a professionally designed book format.

## 📖 Puzzle Types
- **Normal Puzzle**: A 13x13 word search.
- **Hard Puzzle**: A 17x17 word search with more complexity.
- **Bonus Puzzle**: Special patterns and challenges.

## ❓ FAQ
### What happens if I don’t provide enough words?
The program will still generate puzzles but will warn you about missing words.

### Can I add more topics?
Absolutely! Just add your words in the `Words/words.txt` and rerun the `main.py` script.

## 🧑‍💻 Contributions
Feel free to fork this repository and make a pull request.
