#!/usr/bin/env python3

import json

PAGE_TEMPLATE = """

<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8" content="text/html" http-equiv="Content-Type" />
    <meta content="width=device-width, initial-scale=1.0" name="viewport" />
    <link rel="stylesheet" media="screen" href="../index.css" debug="false" />
    <title>
    {}
    </title>
  </head>
  <body class="bg-secondary">
    <nav class="navbar navbar-default navbar-fixed-top">
      <div class="container">
        <div class="navbar-header">
          <button
            class="navbar-toggle collapsed"
            data-target="#app-navbar-collapse"
            data-toggle="collapse"
          >
            <span class="sr-only">Toggle navigation</span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
          </button>
          <a
            alt="Magoosh Logo"
            class="navbar-brand"
            href="/flashcards/vocabulary"
          >
            Magoosh
          </a>
        </div>
        <div class="collapse navbar-collapse" id="app-navbar-collapse">
          <ul class="nav navbar-nav" role="navigation"></ul>
        </div>
      </div>
    </nav>
    <div class="container u-margin-T-xl">
      <div class="row">
        <div class="col-sm-10 col-sm-offset-1 col-md-8 col-md-offset-2">
          <h3 class="clearfix mobile-header">
            <a href="../index.html">&larr; {}</a>
            <small class="text-white pull-right">
              <i class="fa fa-random"></i>
              Words you don't know will reappear later
            </small>
          </h3>
          <div class="flashcard-container u-margin-V-m">
            <div class="flashcard">
              <div class="front card flashcard-card">
                <a href="#back"
                  ><div class="card-block flashcard-content">
                    <div class="label label-flashcard label-danger">
                      learning
                    </div>
                    <h1 class="text-gray text-center flashcard-word">
                      gregarious
                    </h1>
                  </div> </a
                ><a
                  class="card-footer text-center"
                  data-loading-text="Loading definition..."
                  href="#back"
                  >Click to see meaning &rarr;
                </a>
              </div>
              <div class="back card flashcard-card">
                <div class="card-block flashcard-content">
                  <div class="label label-flashcard label-danger">learning</div>
                  <h3 class="flashcard-word"></h3>
                  <div class="flashcard-text"></div>
                  <span class="flashcard-status" style="display: none"></span>
                </div>
                <a
                  class="card-footer card-footer-success text-center know-word"
                  data-loading-text="Loading next word..."
                  href="#"
                  ><i class="fa fa-check"></i> I knew this word </a
                ><a
                  class="card-footer card-footer-danger text-center dont-know-word"
                  data-loading-text="Loading next word..."
                  href="#"
                  ><i class="fa fa-remove"></i>
                  I didn't know this word
                </a>
              </div>
            </div>
          </div>
          <div class="text-white">
            You have mastered <span id="mastered-flashcards-count">0</span> out
            of {} words
          </div>
          <div class="progress">
            <div
              id="mastered-flashcards-progress"
              class="progress-bar progress-bar-success"
              style="width: 0.00%;"
            ></div>
          </div>
          <div class="text-white">
            You are reviewing <span id="reviewing-flashcards-count">0</span> out
            of {} words
          </div>
          <div class="progress">
            <div
              id="reviewing-flashcards-progress"
              class="progress-bar progress-bar-warning"
              style="width: 0.00%;"
            ></div>
          </div>
          <div class="text-white">
            You are learning <span id="learning-flashcards-count">0</span> out
            of {} words
          </div>
          <div class="progress">
            <div
              id="learning-flashcards-progress"
              class="progress-bar progress-bar-danger"
              style="width: 0.00%;"
            ></div>
          </div>
          <br />
        </div>
      </div>
    </div>
    <script>
      var words = {};
    </script>
    <script src="../script/index.js" debug="false"></script>
    <script src="../script/custom.js" debug="false"></script>
  </body>
</html>

""".strip()


INDEX_TEMPLATE = """
<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8" content="text/html" http-equiv="Content-Type" />
    <meta content="width=device-width, initial-scale=1.0" name="viewport" />
    <link rel="stylesheet" media="screen" href="./index.css" debug="false" />
    <title>
      GRE Vocabulary Flashcards - MerGRE
    </title>
  </head>

  <body class="bg-secondary">
    <nav class="navbar navbar-default navbar-fixed-top">
      <div class="container">
        <div class="navbar-header">
          <button
            class="navbar-toggle collapsed"
            data-target="#app-navbar-collapse"
            data-toggle="collapse"
          >
            <span class="sr-only">Toggle navigation</span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
          </button>
          <a alt="MerGRE Logo" class="navbar-brand" href="./index.html">
            MerGRE
          </a>
        </div>
      </div>
    </nav>
    <div class="container u-margin-T-xl">
      <h2 class="text-white mobile-header">GRE Vocabulary Flashcards</h2>
      <div class="row">
        <div class="col-sm-6 u-margin-B-s">
          <div class="card flashcard-card">
            <a href="./pages/freq-6.html">
              <div class="card-block">
                <h3 class="card-title">Frequency 6 Words</h3>
                <p class="card-text">0 of 41 words mastered</p>
                <div class="progress">
                  <div
                    class="progress-bar progress-bar-success"
                    style="width:0.0%"
                  ></div>
                </div>
              </div>
              <a
                class="card-footer text-center"
                data-loading-text="Loading deck..."
                href="./pages/freq-6.html"
                >Practice this deck &rarr;</a
              >
            </a>
          </div>
        </div>
        <div class="col-sm-6 u-margin-B-s">
          <div class="card flashcard-card">
            <a href="./pages/freq-5.html">
              <div class="card-block">
                <h3 class="card-title">Frequency 5 Words</h3>
                <p class="card-text">0 of 110 words mastered</p>
                <div class="progress">
                  <div
                    class="progress-bar progress-bar-success"
                    style="width:0.0%"
                  ></div>
                </div>
              </div>
              <a
                class="card-footer text-center"
                data-loading-text="Loading deck..."
                href="./pages/freq-5.html"
                >Practice this deck &rarr;</a
              >
            </a>
          </div>
        </div>
        <div class="col-sm-6 u-margin-B-s">
          <div class="card flashcard-card">
            <a href="./pages/freq-4.html">
              <div class="card-block">
                <h3 class="card-title">Frequency 4 Words</h3>
                <p class="card-text">0 of 186 words mastered</p>
                <div class="progress">
                  <div
                    class="progress-bar progress-bar-success"
                    style="width:0.0%"
                  ></div>
                </div>
              </div>
              <a
                class="card-footer text-center"
                data-loading-text="Loading deck..."
                href="./pages/freq-4.html"
                >Practice this deck &rarr;</a
              >
            </a>
          </div>
        </div>
        <div class="col-sm-6 u-margin-B-s">
          <div class="card flashcard-card">
            <a href="./pages/freq-3-i.html">
              <div class="card-block">
                <h3 class="card-title">Frequency 3-i Words</h3>
                <p class="card-text">0 of 96 words mastered</p>
                <div class="progress">
                  <div
                    class="progress-bar progress-bar-success"
                    style="width:0.0%"
                  ></div>
                </div>
              </div>
              <a
                class="card-footer text-center"
                data-loading-text="Loading deck..."
                href="./pages/freq-3-i.html"
                >Practice this deck &rarr;</a
              >
            </a>
          </div>
        </div>
        <div class="col-sm-6 u-margin-B-s">
          <div class="card flashcard-card">
            <a href="./pages/freq-3-ii.html">
              <div class="card-block">
                <h3 class="card-title">Frequency 3-ii Words</h3>
                <p class="card-text">0 of 96 words mastered</p>
                <div class="progress">
                  <div
                    class="progress-bar progress-bar-success"
                    style="width:0.0%"
                  ></div>
                </div>
              </div>
              <a
                class="card-footer text-center"
                data-loading-text="Loading deck..."
                href="./pages/freq-3-ii.html"
                >Practice this deck &rarr;</a
              >
            </a>
          </div>
        </div>
        <div class="col-sm-6 u-margin-B-s">
          <div class="card flashcard-card">
            <a href="./pages/freq-3-iii.html">
              <div class="card-block">
                <h3 class="card-title">Frequency 3-iii Words</h3>
                <p class="card-text">0 of 95 words mastered</p>
                <div class="progress">
                  <div
                    class="progress-bar progress-bar-success"
                    style="width:0.0%"
                  ></div>
                </div>
              </div>
              <a
                class="card-footer text-center"
                data-loading-text="Loading deck..."
                href="./pages/freq-3-iii.html"
                >Practice this deck &rarr;</a
              >
            </a>
          </div>
        </div>
        <div class="col-sm-6 u-margin-B-s">
          <div class="card flashcard-card">
            <a href="./pages/freq-2-i.html">
              <div class="card-block">
                <h3 class="card-title">Frequency 2-i Words</h3>
                <p class="card-text">0 of 99 words mastered</p>
                <div class="progress">
                  <div
                    class="progress-bar progress-bar-success"
                    style="width:0.0%"
                  ></div>
                </div>
              </div>
              <a
                class="card-footer text-center"
                data-loading-text="Loading deck..."
                href="./pages/freq-2-i.html"
                >Practice this deck &rarr;</a
              >
            </a>
          </div>
        </div>
        <div class="col-sm-6 u-margin-B-s">
          <div class="card flashcard-card">
            <a href="./pages/freq-2-ii.html">
              <div class="card-block">
                <h3 class="card-title">Frequency 2-ii Words</h3>
                <p class="card-text">0 of 98 words mastered</p>
                <div class="progress">
                  <div
                    class="progress-bar progress-bar-success"
                    style="width:0.0%"
                  ></div>
                </div>
              </div>
              <a
                class="card-footer text-center"
                data-loading-text="Loading deck..."
                href="./pages/freq-2-ii.html"
                >Practice this deck &rarr;</a
              >
            </a>
          </div>
        </div>
        <div class="col-sm-6 u-margin-B-s">
          <div class="card flashcard-card">
            <a href="./pages/freq-2-iii.html">
              <div class="card-block">
                <h3 class="card-title">Frequency 2-iii Words</h3>
                <p class="card-text">0 of 98 words mastered</p>
                <div class="progress">
                  <div
                    class="progress-bar progress-bar-success"
                    style="width:0.0%"
                  ></div>
                </div>
              </div>
              <a
                class="card-footer text-center"
                data-loading-text="Loading deck..."
                href="./pages/freq-2-iii.html"
                >Practice this deck &rarr;</a
              >
            </a>
          </div>
        </div>
        <div class="col-sm-6 u-margin-B-s">
          <div class="card flashcard-card">
            <a href="./pages/freq-2-iv.html">
              <div class="card-block">
                <h3 class="card-title">Frequency 2-iv Words</h3>
                <p class="card-text">0 of 98 words mastered</p>
                <div class="progress">
                  <div
                    class="progress-bar progress-bar-success"
                    style="width:0.0%"
                  ></div>
                </div>
              </div>
              <a
                class="card-footer text-center"
                data-loading-text="Loading deck..."
                href="./pages/freq-2-iv.html"
                >Practice this deck &rarr;</a
              >
            </a>
          </div>
        </div>
        <div class="col-sm-6 u-margin-B-s">
          <div class="card flashcard-card">
            <a href="./pages/freq-2-v.html">
              <div class="card-block">
                <h3 class="card-title">Frequency 2-v Words</h3>
                <p class="card-text">0 of 98 words mastered</p>
                <div class="progress">
                  <div
                    class="progress-bar progress-bar-success"
                    style="width:0.0%"
                  ></div>
                </div>
              </div>
              <a
                class="card-footer text-center"
                data-loading-text="Loading deck..."
                href="./pages/freq-2-v.html"
                >Practice this deck &rarr;</a
              >
            </a>
          </div>
        </div>
        <div class="col-sm-6 u-margin-B-s">
          <div class="card flashcard-card">
            <a href="./pages/freq-2-vi.html">
              <div class="card-block">
                <h3 class="card-title">Frequency 2-vi Words</h3>
                <p class="card-text">0 of 99 words mastered</p>
                <div class="progress">
                  <div
                    class="progress-bar progress-bar-success"
                    style="width:0.0%"
                  ></div>
                </div>
              </div>
              <a
                class="card-footer text-center"
                data-loading-text="Loading deck..."
                href="./pages/freq-2-vi.html"
                >Practice this deck &rarr;</a
              >
            </a>
          </div>
        </div>
        <div class="col-sm-6 u-margin-B-s">
          <div class="card flashcard-card">
            <a href="./pages/other-important-words-i.html">
              <div class="card-block">
                <h3 class="card-title">Other Important Words-i</h3>
                <p class="card-text">0 of 79 words mastered</p>
                <div class="progress">
                  <div
                    class="progress-bar progress-bar-success"
                    style="width:0.0%"
                  ></div>
                </div>
              </div>
              <a
                class="card-footer text-center"
                data-loading-text="Loading deck..."
                href="./pages/other-important-words-i.html"
                >Practice this deck &rarr;</a
              >
            </a>
          </div>
        </div>
        <div class="col-sm-6 u-margin-B-s">
          <div class="card flashcard-card">
            <a href="./pages/other-important-words-ii.html">
              <div class="card-block">
                <h3 class="card-title">Other Important Words-ii</h3>
                <p class="card-text">0 of 79 words mastered</p>
                <div class="progress">
                  <div
                    class="progress-bar progress-bar-success"
                    style="width:0.0%"
                  ></div>
                </div>
              </div>
              <a
                class="card-footer text-center"
                data-loading-text="Loading deck..."
                href="./pages/other-important-words-ii.html"
                >Practice this deck &rarr;</a
              >
            </a>
          </div>
        </div>
        <div class="col-sm-6 u-margin-B-s">
          <div class="card flashcard-card">
            <a href="./pages/other-important-words-iii.html">
              <div class="card-block">
                <h3 class="card-title">Other Important Words-iii</h3>
                <p class="card-text">0 of 81 words mastered</p>
                <div class="progress">
                  <div
                    class="progress-bar progress-bar-success"
                    style="width:0.0%"
                  ></div>
                </div>
              </div>
              <a
                class="card-footer text-center"
                data-loading-text="Loading deck..."
                href="./pages/other-important-words-iii.html"
                >Practice this deck &rarr;</a
              >
            </a>
          </div>
        </div>
        {}
        <!-- <div class="col-sm-6 u-margin-B-s">
          <div class="card flashcard-card">
            <a href="./pages/freq-1.html">
              <div class="card-block">
                <h3 class="card-title">Frequency 1 Words</h3>
                <p class="card-text">0 of 1743 words mastered</p>
                <div class="progress">
                  <div
                    class="progress-bar progress-bar-success"
                    style="width:0.0%"
                  ></div>
                </div>
              </div>
              <a
                class="card-footer text-center"
                data-loading-text="Loading deck..."
                href="./pages/freq-1.html"
                >Practice this deck &rarr;</a
              >
            </a>
          </div>
        </div> -->

      </div>
    </div>
    <script src="./script/index.js" debug="false"></script>
  </body>
</html>
""".strip()

CARD_TEMPLATE = """
<div class="col-sm-6 u-margin-B-s">
    <div class="card flashcard-card">
    <a href="./pages/{}">
        <div class="card-block">
        <h3 class="card-title">{}</h3>
        <p class="card-text">0 of {} words mastered</p>
        <div class="progress">
            <div
            class="progress-bar progress-bar-success"
            style="width:0.0%"
            ></div>
        </div>
        </div>
        <a
        class="card-footer text-center"
        data-loading-text="Loading deck..."
        href="./pages/{}"
        >Practice this deck &rarr;</a
        >
    </a>
    </div>
</div>
""".strip()

def create_page(page_name, title, data):
    n = len(data)
    page = PAGE_TEMPLATE.format(title, title, n, n, n, data)
    path = "public/pages/{}".format(page_name)
    print("Creating HTML Page :: {}".format(path))
    with open(path, 'w') as f:
        f.write(page)

def create_card(page_name, title, num_words):
    return CARD_TEMPLATE.format(page_name, title, num_words, page_name)

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

def write_index(path, cards):
    print("Writing Index to :: {}".format(path))
    index = INDEX_TEMPLATE.format('\n'.join(cards))
    with open(path, 'w') as f:
        f.write(index)

def create_all(jsonpath, prefix):
    with open(jsonpath) as f:
        data = json.load(f)

    splitted = split_dict(data)
    card = ""
    cards = []
    for i, d in enumerate(splitted):
        page_name = '{}-{}.html'.format(prefix, i+1)
        name = '{}-{}'.format(prefix, i+1)
        create_page(page_name, name, d)
        cards.append(create_card(page_name, name, len(d)))
    write_index('public/index.html', cards)


def main():
    path = "output/collected-words.json"
    create_all(path, 'collected-words')
    # create_page('test.html', 'test', data)
    # print(create_card('test.html', 'test', len(data)))

if __name__ == "__main__":
    main()

