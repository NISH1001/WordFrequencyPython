#!/usr/bin/env python3

import pandas as pd
import json


def main():
    data = pd.read_csv('WordLists/collected-words.csv')
    data = data.fillna(0)
    wmap = {}
    for d in data.iterrows():
        word = d[1]['Word']
        meanings  = [d[1]['Meaning']]
        example = d[1]['Example']
        synonyms = d[1]['Synonyms']
        if synonyms:
            meanings.append(synonyms)
        if example:
            meanings.append("Example:: {}".format(example))
        wmap[word] = meanings
    with open('output/collected-words.json', 'w') as f:
        json.dump(wmap, f, indent=4)


if __name__ == "__main__":
    main()

