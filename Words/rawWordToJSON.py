import json
import os


def generate_word_json(word_file, topic_name="SCIENCE", output_file="Words/output.json"):
    topic_name = topic_name.upper()

    with open(word_file, "r") as f:
        words = [line.strip() for line in f if line.strip()]

    word_pool = set(words)
    used_words = set()

    def get_unique_words(count, min_len, max_len, max_long_words=None):
        nonlocal word_pool, used_words
        selection = []
        long_words_count = 0
        available_words = list(word_pool - used_words)

        for word in available_words:
            if len(word) > max_len:
                continue
            if min_len <= len(word) <= max_len:
                if max_long_words and len(word) > 8 and long_words_count >= max_long_words:
                    continue
                selection.append(word)
                if len(word) > 8:
                    long_words_count += 1
                used_words.add(word)
                if len(selection) == count:
                    break

        if len(selection) < count:
            required = count - len(selection)
            return selection, required
        return selection, 0

    data = {topic_name: {
        "Normal": [],
        "Hard": [],
        "Bonus": {"Normal": [], "Hard": []}
    }}

    # Normal mode - 10 lists of 10 words each
    for _ in range(10):
        selection, needed = get_unique_words(10, 4, 11, max_long_words=3)
        if needed:
            print(f"Normal mode requires {needed} more unique words.")
        data[topic_name]["Normal"].append(selection)

    # Hard mode - 5 lists of 15 words each
    for _ in range(5):
        selection, needed = get_unique_words(15, 6, 15)
        if needed:
            print(f"Hard mode requires {needed} more unique words.")
        data[topic_name]["Hard"].append(selection)

    # Bonus Normal (Normal) - 1 list of 10 words
    bonus_normal, needed = get_unique_words(10, 4, 11, max_long_words=3)
    if needed:
        print(f"Bonus Normal requires {needed} more unique words.")
    data[topic_name]["Bonus"]["Normal"].append(bonus_normal)

    # Bonus Hard (Hard) - 1 list of 15 words
    bonus_hard, needed = get_unique_words(15, 6, 15)
    if needed:
        print(f"Bonus Hard requires {needed} more unique words.")
    data[topic_name]["Bonus"]["Hard"].append(bonus_hard)

    # with open("Words/output.json", "w") as json_file:
    #     json.dump(data, json_file, indent=2)

    if os.path.exists(output_file):
        with open(output_file, "r") as f:
            existing_data = json.load(f)
        
        existing_data.update(data)
        
        with open(output_file, "w") as f:
            json.dump(existing_data, f, indent=2)
        print(f"Appended topic to {output_file}.")
    else:
        with open(output_file, "w") as f:
            json.dump(data, f, indent=2)
        print(f"Created new file {output_file} with initial data.")


topic = input("Enter the topic name: ").title()
generate_word_json(f"Words/{topic}.txt", topic_name=topic, output_file="Words/words.json")