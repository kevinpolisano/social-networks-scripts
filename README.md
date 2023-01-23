# Social Networks Scripts

## Facebook comments extraction

### Description

- If you [download a copy of your Facebook data ](https://www.facebook.com/help/212802592074644) then you will find **only your own comments** but not those of your friends, even if these comments were made on your own posts.

- As well, it is not possible to extract these comments from the [Facebook Graph-API](https://developers.facebook.com/docs/graph-api/changelog/version3.0#comments-edge):

> **Comments Edge**. When read with a User access token, the `/comments` edge returns empty data for the following nodes: Album, Photo, Post, Video

- [Scraping](https://about.fb.com/news/2021/04/how-we-combat-scraping/) is not allowed by Facebook.

However, you may occasionally need to extract and archive a particular conversation taking place in the comments of a Facebook post.

The python script `facebook-comments.py` parses the html page of the post to extract the comments, without using the dedicated Python libraries requiring authentication.

### How to export the HTML page

Preliminary steps to save the file `post.html`:
1. Click on the post you want to extract comments
2. [Expand all comments](http://com.hemiola.com/bookmarklet/)
3. Save as HTML page

### Usage

  ```bash
  python facebook-comments.py -i post.html > comments.txt
                                    [--dialogue True]
  ```
```bash
Optional argument: 
  --d, dialogue DIALOGUE   Format text comments to fit the Dialogue Obsidian Plugin if DIALOGUE=True
```

The optional argument `--dialogue True` adds some symbols before author names and paragraphs to be compatible with the syntax of [Obsidian Dialogue plugin](https://github.com/holubj/obsidian-dialogue-plugin).
