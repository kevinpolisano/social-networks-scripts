"""Extract all the comments from the HTML page of a Facebook post

Usage: 
   python python facebook-comments.py -i post.html > comments.txt
                                    [--dialogue True]

Optional argument: 
  --d, dialogue DIALOGUE   Format text comments to fit the Dialogue Obsidian Plugin if DIALOGUE=True
"""

from bs4 import BeautifulSoup
import re
import sys
import argparse

# Create an ArgumentParser object
parser = argparse.ArgumentParser()

# Add command line arguments
parser.add_argument("-i", "--input", help="HTML page to parse", required=True)
parser.add_argument("-d", "--dialogue", help="Format text comments to fit the Dialogue Obsidian Plugin", default=False)

# Parse the command line arguments
args = parser.parse_args()

# Open the HTML source code
with open(args.input) as f:
  soup = BeautifulSoup(f, "lxml")

# Find the comments section under the Facebook post starting by: <ul><li><div aria-label="Comment by ***"
comments_section = soup.find('ul')

# For each commentator
for commentator in comments_section.find_all('div', { "aria-label" : re.compile("Comment by") }):
  # Print the name of who wrote this comment...
  name = commentator.find("span", {"dir": "auto"}).text
  if args.dialogue:
    name = "left:" + name
  print(name)
  # ... and the corresponding text made of one or more paragraphs
  comment = commentator.find_all('div', {"dir": "auto", "style": "text-align: start;"})
  for paragraph in comment:
    temp = paragraph.text
    if args.dialogue:
      temp = "< " + temp # left and < in order to vizualize the parent
    print(temp) 
  print("\n")
  # Find the replies to this comment
  replies_section = commentator.find_next_sibling('div')
  # For each replier
  for replier in replies_section.find_all('div', { "aria-label" : re.compile("Reply by") }):
    # Print the name of who replied to this comment...
    name = replier.find("span", {"dir": "auto"}).text
    if args.dialogue:
      name = "right:" + name
    print(name)
    # ... and the corresponding text made of one or more paragraphs
    comment = replier.find_all('div', {"dir": "auto", "style": "text-align: start;"})
    for paragraph in comment:
      temp = paragraph.text
      if args.dialogue:
        temp = "< " + temp # right and > in order to vizualize the children arborescence
      print(temp) 
    print("\n")
