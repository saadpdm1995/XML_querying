# How to find similartiies between two lists, this is helpful if you have to map one list to another

# Part1: Look for the same exact elements
# Import Libraries
import pandas as pd
from fuzzywuzzy import fuzz

# define your lists
list1 = ['a', 'b', 'c', 'x']
list2 = ['x', 'y', 'z', 'a']

# function to make lists of tags lowercase
def makeLower(list):
    lowList = [x.lower() for x in list]
    return lowList

# run the function on both lists
all_used = makeLower(list1)
all_new_all = makeLower(list2)

# find Exact matches (spellMatch) and non matches (stillRemain)
spell_match = [x for x in all_used if x in all_new_all]
still_remain = [x for x in all_used if x not in all_new_all]


# Part2: Find the nearest match for the remaining items
# fuzzymatch all the tags that have no match so far
def get_fuzz(l, allNew_all):
    ratio_list = []
    for words in l:
        for texts in allNew_all:
            if words != texts:
                ratio = fuzz.ratio(words.lower(), texts.lower())
                rat_dict = {'word':words, 'match':texts, 'fuzz_score': ratio}
                ratio_list.append(rat_dict)
    return ratio_list

fuz_match = get_fuzz(still_remain, list1)

# Create a df of the values, group them and then keep only the maximum value
fuzz_db = pd.DataFrame(fuz_match)
fuzz_db = fuzz_db.loc[fuzz_db.groupby('word')['fuzz_score'].idxmax()]
fuzz_db = fuzz_db.sort_values(by=['fuzz_score'], ascending=False)
print(fuzz_db)
