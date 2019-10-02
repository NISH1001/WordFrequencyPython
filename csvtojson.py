#!/usr/bin/env python3

import pandas as pd
import json


def main():
    data = pd.read_csv('WordLists/words.csv')
    wmap = {}
    for d in data.iterrows():
        word = d[1]['Word']
        meaning  = d[1]['Meaning']
        wmap[word] = meaning
    with open('output/words.json', 'w') as f:
        json.dump(wmap, f, indent=4)


if __name__ == "__main__":
    main()

