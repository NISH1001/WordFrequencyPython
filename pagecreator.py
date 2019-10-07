#!/usr/bin/env python3

import json

def create_page(page_name, title, data, template):
    n = len(data)
    page = template.format(title, title, n, n, n, data)
    path = "public/pages/{}".format(page_name)
    print("Creating HTML Page :: {}".format(path))
    with open(path, 'w') as f:
        f.write(page)

def create_card(page_name, title, num_words, template):
    return template.format(page_name, title, num_words, page_name)

def split_dict(data):
    res = []
    num_words = len(data)
    if num_words < 100:
        return [data]
    items = list(data.items())
    i = 0
    n = num_words
    step = 75
    while i < n:
        d = items[i : i+step]
        res.append(dict(d))
        i += step
    return res

def write_index(path, cards, template):
    print("Writing Index to :: {}".format(path))
    index = template.format('\n'.join(cards))
    with open(path, 'w') as f:
        f.write(index)

def create_all(jsonpath, prefix, templates):
    with open(jsonpath) as f:
        data = json.load(f)

    splitted = split_dict(data)
    card = ""
    cards = []
    for i, d in enumerate(splitted):
        page_name = '{}-{}.html'.format(prefix, i+1)
        name = '{}-{}'.format(prefix, i+1)
        create_page(page_name, name, d, templates['page'])
        cards.append(create_card(page_name, name, len(d), templates['card']))
    write_index('public/index.html', cards, templates['index'])

def load_templates():
    res = {}
    with open('public/templates/page.html') as f:
        res['page'] = f.read()
    with open('public/templates/index.html') as f:
        res['index'] = f.read()
    with open('public/templates/card.html') as f:
        res['card'] = f.read()
    return res


def main():
    templates = load_templates()
    path = "output/collected-words.json"
    create_all(path, 'collected-words', templates)
    # create_page('test.html', 'test', data)
    # print(create_card('test.html', 'test', len(data)))

if __name__ == "__main__":
    main()

