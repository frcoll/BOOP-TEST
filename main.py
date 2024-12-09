from appendImage import append_page, append_puzzle_page
from index import create_title_page
from generatePuzzle import create_all_puzzles, create_individual_puzzle

# Global book_name
book_name = "Where's Word-o"



def main():
    global book_name
    image_path = "Assets/Cover.png"
    background_image = "Assets/Background.png"
    puzzle_background_image = "Assets/pageBackground.png"
    word_json_path = "Words/words.json"
    puzzle_folder = "generated_puzzles"

    print(f"Creating book '{book_name}'.\n\n")

    start_puzzle = input("Enter the puzzle number to start from (default 1): ") or "1"
    if not start_puzzle.isdigit():
        print("Invalid puzzle number. Exiting...")
        return
    else:
        start_puzzle = int(start_puzzle)

    delete_puzzles = input("Delete puzzles after making the book? (y/n, default n): ").lower() or 'n'
    if delete_puzzles not in ['y', 'n']:
        print("Invalid input. Exiting...")
        return


    if start_puzzle == 1:
        print("Adding cover image.\n")
        append_page(book_name, image_path)

        print("Creating title page.\n")
        create_title_page(book_name, word_json_path,
                          background_image=background_image)

    print("\nGenerating puzzles and adding to the book.")
    fail_count = create_all_puzzles(
        word_json_path, puzzle_background_image, puzzle_folder, start_puzzle)

    if fail_count:
        print(f"Failed to create {fail_count} puzzles.")
        create_individual_puzzle(
            fail_count, word_json_path, puzzle_folder, background_image=puzzle_background_image)

    print("All puzzles are made. Adding to the book...")

    append_puzzle_page(f"{book_name}.pdf", puzzle_folder,
                       background_image=puzzle_background_image)

    print("All puzzles added to the book.")

    if delete_puzzles == 'y':
        print("Deleting puzzles...")
        import shutil
        shutil.rmtree(puzzle_folder)
        print("Puzzles deleted.")

    print(f"Book '{book_name}' created successfully.")


if __name__ == '__main__':
    main()
