import json
import random


def word_to_json(file_path="Words/words.txt"):
    def filter_words(words, min_len, max_len):
        return [word for word in words if min_len <= len(word) <= max_len]

    with open(file_path, 'r') as file:
        data = file.read()

    sections = data.split('====================')
    result = {}
    warnings = []

    for section in sections:
        if section.strip():
            lines = section.strip().splitlines()
            topic = lines[0].strip('>').strip()
            words = [word.strip() for word in lines[1:] if word.strip()]

            normal_words = filter_words(words, 4, 11)
            hard_words = filter_words(words, 6, 15)

            topic_result = {"Normal": [], "Hard": [], "Bonus": {}}

            # Generate lists for Normal mode
            for i in range(10):
                if len(normal_words) >= 10:
                    topic_result["Normal"].append(
                        random.sample(normal_words, 10))
                else:
                    topic_result["Normal"].append(normal_words[:])
                    warnings.append(f"Topic '{topic}' Normal mode, Puzzle number {
                                    i+1} is lacking {10 - len(normal_words)} words.")

            # Generate lists for Hard mode
            for i in range(5):
                if len(hard_words) >= 15:
                    topic_result["Hard"].append(random.sample(hard_words, 15))
                else:
                    topic_result["Hard"].append(hard_words[:])
                    warnings.append(f"Topic '{topic}' Hard mode, Puzzle number {
                                    i+1} is lacking {15 - len(hard_words)} words.")

            # Generate lists for Bonus mode
            if len(normal_words) >= 10:
                topic_result["Bonus"]["Normal"] = [
                    random.sample(normal_words, 10)]
            else:
                topic_result["Bonus"]["Normal"] = [normal_words[:]]
                warnings.append(f"Topic '{topic}' Bonus Normal mode is lacking {
                                10 - len(normal_words)} words.")

            if len(hard_words) >= 15:
                topic_result["Bonus"]["Hard"] = [random.sample(hard_words, 15)]
            else:
                topic_result["Bonus"]["Hard"] = [hard_words[:]]
                warnings.append(f"Topic '{topic}' Bonus Hard mode is lacking {
                                15 - len(hard_words)} words.")

            result[topic] = topic_result

    if warnings:
        print("\nWarnings:")
        for warning in warnings:
            print(warning)

    with open("Words/words.json", "w") as f:
        json.dump(result, f, indent=4)


if __name__ == '__main__':
    word_to_json("Words/words.txt")
