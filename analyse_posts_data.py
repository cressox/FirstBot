import pickle

def key_words(sentence):
    keys = pickle.load(open("keywords.json", "rb"))
    # filtert nach worten die in weywords stehen #
    for key in keys:
        if key in sentence:
            return True

    return False

post_data = pickle.load(open("posts.json", "rb"))

for name, posts in post_data.items():
    # beschreibungen in sätzen #
    for num, post in posts.items():
        post = post[1].split(".")
        for i in range(len(post)):
            if key_words(post[i]):
            # key word im satz gefunden #
                print(f"{name}: {post[i]}.")
