![banner](images/project-banner.png)

# About
Easybooks-api utilizes a BeautifulSoup webscraper that parses the [goodreads](https://www.goodreads.com/?ref=nav_hom) website to obtain details about various book titles

I decided to start development on this project because I needed a straightforward alternative to the *OpenLibraryAPI*, with only a minimal set of features due to an issue I encountered with foreign languages in the former Api responses

**Rate-limiting** is enabled by default, set at 10 requests per minute

**Work in progress, additional features are planned**

## User guide
The api is deployed using Render's FastAPI services, however rates are limited and requests might be slow.  For best performance I would recommend following the **installation** directions and running this program on your personal machine

[![icon](images/render-icon.png)](https://goodreads-api.onrender.com)

Root endpoint is *https://goodreads-api.onrender.com*

### Current requests
1. `/search/{book_title}`
  ```json
  [
    {
      "results_length": 4
    },
    [
      {
          "title": "Spice & Wolf, Vol. 01",
          "author": "Isuna Hasekura"
      },
      {
          "title": "Spice & Wolf, Vol. 1 (Spice & Wolf: Manga, #1)",
          "author": "Isuna Hasekura"
      },
      {
          "title": "Spice & Wolf, Vol. 02",
          "author": "Isuna Hasekura"
      },
      {
          "title": "Spice & Wolf, Vol. 03",
          "author": "Isuna Hasekura"
      }
    ]
  ]
  ```
2. `/details/{book_title}`
  ```json
  {
    "title": "Pale Fire",
    "author": "Vladimir Nabokov",
    "description": "The American poet John Shade is dead. His last poem, 'Pale Fire', is put into a book, together with a preface, a lengthy commentary and notes by Shade's editor, Charles Kinbote. Known on campus as the 'Great Beaver', Kinbote is      haughty, inquisitive, intolerant, but is he also mad, bad - and even dangerous? As his wildly eccentric annotations slide into the personal and the fantastical, Kinbote reveals perhaps more than he should be.Nabokov's darkly witty, richly           inventive masterpiece is a suspenseful whodunit, a story of one-upmanship and dubious penmanship, and a glorious literary conundrum.Part of a major new series of the works of Vladimir Nabokov, author of Lolita and Pale Fire, in Penguin    Classics.",
    "image_url": "https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1388155863i/7805.jpg"
  }
  ```
3. `/quotes/random/{book_title}`
```json
{
    "quote": "“And blood-black nothingness began to spin. A system of cells interlinked, within cells interlinked, within cells interlinked within one stem. And dreadfully distinct against the dark, a tall white fountain played.” ― Vladimir     Nabokov, Pale Fire"
}
```
4. `/quotes/all/{book_title}`
```json
[
    {
        "results_length": 20
    },
    [
        {
            "quote": "“There's no one thing that's true. It's all true.” ― Ernest Hemingway, For Whom the Bell Tolls"
        },
        {
            "quote": "“No man is an island, entire of itself; every man is a piece of the continent, a part of the main. If a clod be washed away by the sea, Europe is the less, as well as if a promontory were, as well as if a manor of thy friend's or of thine own were: any man's death diminishes me, because I am involved in mankind, and therefore never send to know for whom the bells tolls; it tolls for thee.” ― John Donne, No man is an island â€“ A selection from the prose"
        },
        {
            "quote": "“There is nothing else than now. There is neither yesterday, certainly, nor is there any tomorrow. How old must you be before you know that? There is only now, and if now is only two days, then two days is your life and everything in it will be in proportion. This is how you live a life in two days. And if you stop complaining and asking for what you never will get, you will have a good life. A good life is not measured by any biblical span.” ― Ernest Hemingway, For Whom the Bell Tolls"
        }
    ]
]
```
5. *Additional endpoints are planned for the future...*
   - Recommendation algorithm for finding book based on previously read genres is being worked on

## Installation
Simply clone this repository onto your local machine, then locate and run the **main.py** file

**NOTE:** In order to run the application you will need the following:

### Dependencies
- For list of dependencies see the **requirements.txt** file located in the project repository
- To **install** the dependecies, navigate to project directory and run the following command:
  `pip3 install -r requirements.txt`
  - For **Windows** users the command might be: `pip install -r requirements.txt`
