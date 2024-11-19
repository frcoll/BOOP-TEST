title = input("Title: ").title()

# import re

# with open("Words/words.txt", 'r') as file:
#     content = file.read()
    
# words = re.findall(r'"(.*?)"', content)

# print(words)
# print(len(words))


with open(f"Words/{title}.txt", "r") as f:
    data = f.read().splitlines()
    words = []
    for word in data:
        if (len(word) > 3 and len(word) < 15) and " " not in word.replace("-", " "):
            words.append(word)

words = list(set(words))

print(words)
print(len(words))

with open(f"Words/{title}.txt", "w") as f:
    for word in words:
        f.write(word + "\n")


