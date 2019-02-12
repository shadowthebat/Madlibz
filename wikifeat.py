from bs4 import BeautifulSoup
import requests
import re
from difflib import get_close_matches


source = requests.get('https://en.wikipedia.org/wiki/Main_Page')
soup = BeautifulSoup(source.text, 'lxml')

div = soup.find(id='mp-tfa')  # finds the div for featured article wikipedia front page
divp = div.p  # isolates the target paragraph
p = divp.text  # makes paragraph readable
p = p[:-19]  # removes (Full Article) link at the end of the article
thtml = divp.b  # title tags

title = thtml.text  # title

def question():
    answer = input('Fill in the blank: ')
    lst = [title]
    close = get_close_matches(answer.lower(), lst)
    if answer.lower() == title.lower():
        print('You win!')
    elif close:
        print(f'{answer.upper()} is worth half a point!\nWe were expecting {title.upper()}')
    else:
        print('You lose, game over.')

blankspace = '_'*len(title)  # creates blankspace appropriate in length to missing title
newp = p.replace(title, blankspace) # replaces title with blankspace
print(newp)
question()
