import pickle

influencer = [
    "mrs_dgoe", "lisamarie_schiffner", "thestilettomeup",
    "kates.diary", "maria.digeronimo", "inalovesstyle",
    "sarah.harrison.official", "danielakatzenberger", "sarellax3",
    "karokauer", "ivy_ik", "novalanalove", "jetsetsam_"
]

pickle.dump(influencer, open("influencer.txt", "wb"))