import pickle

influencer = [
    "mrs_dgoe", "lisamarie_schiffner", "thestilettomeup",
    "kates.diary", "maria.digeronimo", "inalovesstyle",
    "sarah.harrison.official", "danielakatzenberger", "sarellax3",
    "karokauer", "ivy_ik", "novalanalove", "jetsetsam_"
]

keywords = ["gutschein", "Gutschein", "rabatt", "Rabatt", "Code", "code"]

pickle.dump(influencer, open("influencer.json", "wb"))
pickle.dump(keywords, open("keywords.json", "wb"))