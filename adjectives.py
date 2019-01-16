from bs4 import BeautifulSoup
import requests


def adjectives():
    source = requests.get('https://www.talkenglish.com/vocabulary/top-500-adjectives.aspx')
    soup = BeautifulSoup(source.text, 'lxml')

    table = soup.find(id='GridView3')  # defines table
    word = table.find_all(width="120")  # finds adjective html
    types = table.find_all(width="300")  # finds type html

    # defines empty dictionary to store wordadjectives and values(verb,adj,noun,proverb etc)
    adjectives_dict = {}
    adjectives = []  # defines empty list to store wordadjectives
    test1 = []
    test2 = []
    for i in word:
        test1.append(i.text)

    for i in test1:
        i = BeautifulSoup(i, 'lxml')
        test2.append(i.text)

    for i in test2:
        empt = ''
        for m in i:
            if m != '\n':
                empt += m
        adjectives.append(empt)
    # print(len(verbs))

    # above defines list of readable verbs

    # adds verbs(keys) to dictionary with no values
    for i in adjectives:
        adjectives_dict[i] = None

    # below code defines list of correseponding types verb, adj, noun etc

    test = []
    for i in types:
        m = i.text
        test.append(m)

    count = 0
    for i in adjectives_dict:
        type = []
        if 'adjective' in test[count]:
            type.append('adjective')
            if 'noun' in test[count]:
                type.append('noun')
                if 'verb' in test[count]:
                    type.append('verb')
                    if 'auxiliary' in test[count]:
                        type.append('auxiliary')
                        if 'interjection' in test[count]:
                            type.append('interjection')
                            if 'pronoun' in test[count]:
                                type.append('pronoun')
                                if 'adverb' in test[count]:
                                    type.append('adverb')
                                    if 'conjunction' in test[count]:
                                        type.append('conjunction')
                                        if 'idiom' in test[count]:
                                            type.append('idiom')
                                            if 'preposition' in test[count]:
                                                type.append('preposition')
                                                if 'past particple' in test[count]:
                                                    type.append('past particple')
            elif 'verb' in test[count]:
                type.append('verb')
                if 'auxiliary' in test[count]:
                    type.append('auxiliary')
                    if 'interjection' in test[count]:
                        type.append('interjection')
                        if 'pronoun' in test[count]:
                            type.append('pronoun')
                            if 'adverb' in test[count]:
                                type.append('adverb')
                                if 'conjunction' in test[count]:
                                    type.append('conjunction')
                                    if 'idiom' in test[count]:
                                        type.append('idiom')
                                        if 'preposition' in test[count]:
                                            type.append('preposition')
                                            if 'past particple' in test[count]:
                                                type.append('past particple')
            elif 'auxiliary' in test[count]:
                type.append('auxiliary')
                if 'interjection' in test[count]:
                    type.append('interjection')
                    if 'pronoun' in test[count]:
                        type.append('pronoun')
                        if 'adverb' in test[count]:
                            type.append('adverb')
                            if 'conjunction' in test[count]:
                                type.append('conjunction')
                                if 'idiom' in test[count]:
                                    type.append('idiom')
                                    if 'preposition' in test[count]:
                                        type.append('preposition')
                                        if 'past particple' in test[count]:
                                            type.append('past particple')
            elif 'interjection' in test[count]:
                type.append('interjection')
                if 'pronoun' in test[count]:
                    type.append('pronoun')
                    if 'adverb' in test[count]:
                        type.append('adverb')
                        if 'conjunction' in test[count]:
                            type.append('conjunction')
                            if 'idiom' in test[count]:
                                type.append('idiom')
                                if 'preposition' in test[count]:
                                    type.append('preposition')
                                    if 'past particple' in test[count]:
                                        type.append('past particple')
            elif 'pronoun' in test[count]:
                type.append('pronoun')
                if 'adverb' in test[count]:
                    type.append('adverb')
                    if 'conjunction' in test[count]:
                        type.append('conjunction')
                        if 'idiom' in test[count]:
                            type.append('idiom')
                            if 'preposition' in test[count]:
                                type.append('preposition')
                                if 'past particple' in test[count]:
                                    type.append('past particple')
            elif 'adverb' in test[count]:
                type.append('adverb')
                if 'conjunction' in test[count]:
                    type.append('conjunction')
                    if 'idiom' in test[count]:
                        type.append('idiom')
                        if 'preposition' in test[count]:
                            type.append('preposition')
                            if 'past particple' in test[count]:
                                type.append('past particple')
            elif 'conjunction' in test[count]:
                type.append('conjunction')
                if 'idiom' in test[count]:
                    type.append('idiom')
                    if 'preposition' in test[count]:
                        type.append('preposition')
                        if 'past particple' in test[count]:
                            type.append('past particple')
            elif 'idiom' in test[count]:
                type.append('idiom')
                if 'preposition' in test[count]:
                    type.append('preposition')
                    if 'past particple' in test[count]:
                        type.append('past particple')
            elif 'preposition' in test[count]:
                type.append('preposition')
                if 'past particple' in test[count]:
                    type.append('past particple')
            elif 'past particple' in test[count]:
                type.append('past particple')

        adjectives_dict[i] = type
        count += 1

    return adjectives_dict
