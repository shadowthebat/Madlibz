import wikipedia
from bs4 import BeautifulSoup
import requests
import json
import random

article_max_length = 1500  # defines max characters for summary to be played with
max_words = 6  # sets maximum blank spaces

source = requests.get("https://en.wikipedia.org/wiki/Special:Random")
soup = BeautifulSoup(source.text, 'lxml')

title = soup.title.text  # isolates title from random wikipedia page
title = title[:-12]  # removes wikipedia from title
tlen = len(title)  # defines length of title

psummary = wikipedia.summary(title)
# if len(psummary) > article_max_length:

blankspace = '_'*tlen
question = psummary[tlen:]
answer = title

summary_words = psummary.split()

split_t = title.split()
split_t_len = len(split_t)
compare_t = summary_words[:split_t_len]
compare_concat = ''
for i in compare_t:
    compare_concat += i + ' '
c_concat = compare_concat[:-1]

# initializes verb and adjective python dictionaries
with open('verbs.json', 'r') as v:  # opens verbs.json
    verb_dict = json.load(v)  # assigns the json string a variable

with open('adjectives.json', 'r') as a:  # opens adjectives.json
    adj_dict = json.load(a)  # assigns the json string to to a variable

verb_dict = json.loads(verb_dict)  # converts the json string to a python dictionary
adj_dict = json.loads(adj_dict)  # converts the json string to a python dictionary

qsplit = question.split()
new_q = qsplit[1:]

###


def mad(summary_words):
    # make dictionary to store key(word), value(index of word in list of words
    v_index_dict = {}
    a_index_dict = {}

    # for i in summary_words:
    # compare i to m in verbs, adjectives
    for i in range(len(summary_words)):
        for m in verb_dict:
            if m == summary_words[int(i)]:  # if we match word in article with a verb
                # puts index in dict (value will be user input)
                v_index_dict[i] = None

    for i in range(len(summary_words)):
        for m in adj_dict:
            if m == summary_words[int(i)]:  # if we match word in article with a verb
                # puts index in dict (value will be user input)
                a_index_dict[i] = None

    v_a_index_set = set()  # to store index's of verbs and adjectives
    for i in v_index_dict:  # adds verb index's to list
        v_a_index_set.add(i)
    for i in a_index_dict:  # adds adjective index's to list
        v_a_index_set.add(i)

    v_a_i_list = list(v_a_index_set)  # converts set to list because random.choice
    v_a_index_list = []  # initializes empty list to store index's
    # sorts index's so that theyre asked in order based on original text
    v_a_index_list = sorted(v_a_index_list)
    result_summary = []
    for i in summary_words:
        result_summary.append(i)
    for i in range(max_words):  # specifies max number of words to be used for input(gameplay)
        v_a_index_list.append(random.choice(v_a_i_list))
    v_a_index_set = set(v_a_index_list)
    v_a_index_set = list(v_a_index_set)

    # prompts user to input either verb or adjective and replaces original word in summary
    for i in range(len(v_a_index_set)):
        if v_a_index_list[i] in v_index_dict:
            result_summary[v_a_index_list[i]] = result_summary[v_a_index_list[i]].upper()
            x = input('Enter a verb: ')
            summary_words[v_a_index_list[i]] = x.upper()
        elif v_a_index_list[i] in a_index_dict:
            result_summary[v_a_index_list[i]] = result_summary[v_a_index_list[i]].upper()
            x = input('Enter an adjective: ')
            summary_words[v_a_index_list[i]] = x.upper()

    x = input('ready to see final result?')
    blank_summary = ' '.join(summary_words)
    print(blank_summary)  # prints final result
    x = input('Continue to original text?')
    finale_summary = ' '.join(result_summary)
    print(finale_summary)


if c_concat == title:
    print(f'{blankspace}{question}')
    x = input('Fill in the blank:')
    print(title)
else:
    mad(summary_words)
