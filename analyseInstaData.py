import pickle
# sdfk
def key_words(sentence):
    keys = ["gutschein", "Gutschein", "rabatt", "Rabatt", "Code", "code"]
    # filtert nach worten die in keys stehen #
    for key in keys:
        if key in sentence:
            return True

    return False

instData = pickle.load(open("instaData.txt", "rb"))

for name, posts in instData.items():
    #text = text.split(".")
    # beschreibungen in sätzen #
    for num, post in posts.items():
        post = post.split(".")
        for i in range(len(post)):
            if key_words(post[i]):
            # key word im satz gefunden #
                print(f"{name}: {post[i]}.")
