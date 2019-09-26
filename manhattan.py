#!/usr/bin/env python3

"""
    A module to get those words which are in Manhattan
    and not in 2,3,4,5,6 Frequency Words
"""

import json

def get_words(filename):
    print("Loading words from : {}".format(filename))
    wordmap = {}
    with open(filename, encoding="ISO-8859-1") as f:
        for line in f:
            line = line.strip().lower()
            tokens = line.split(':')
            wordmap[tokens[0]] = ' '.join(tokens[1:])
    return wordmap

def get_frquency_json(filename):
    print("Loading frquency json from : {}".format(filename))
    with open(filename) as f:
        return json.load(f)

def merge_wordmap(wordmap):
    res = {}
    for f, wmap in wordmap.items():
        res.update(wmap)
    return res

def filter_wordmap(wordmap1, wordmap2):
    res = {}
    difference = set(wordmap1) - set(wordmap2)
    for word in difference:
        res[word] = [wordmap1[word]]
    return res

def main():
    manhattan_words= get_words("WordLists/Manhattan.txt")
    frequency_files = { i : 'output/{}.json'.format(i) for i in range(2, 7) }
    print(frequency_files)
    frequency_wordmap = {i : get_frquency_json(frequency_files[i]) for i in range(2, 7) }
    merged = merge_wordmap(frequency_wordmap)
    filtered = filter_wordmap(manhattan_words, merged)
    print("Total number of new words : {}".format(len(list(filtered.keys()))))
    savefile = "output/manhattan.json"
    print("Saving to : {}".format(savefile))
    with open(savefile, 'w') as f:
        json.dump(filtered, f, indent=4)

if __name__ == "__main__":
    main()

