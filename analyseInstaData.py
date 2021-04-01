import pickle

def key_words(sentence):
    keys = ["Nothing", "more"]
    # filtert nach worten die in keys stehen #
    for key in keys:
        if key in sentence:
            return True

    return False

instData = pickle.load(open("instaData.txt", "rb"))
count = 0
for name, text in instData.items():
    text = text.split(".")
    # beschreibungen in sätzen #

    for i in range(len(text)):
        if key_words(text[i]):
        # key word im stzt gefunden #
            print(f"{name}: {text[i]}.")