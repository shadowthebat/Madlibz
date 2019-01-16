from bs4 import BeautifulSoup
import requests


def verbs():
    source = requests.get('https://www.talkenglish.com/vocabulary/top-1000-verbs.aspx')
    soup = BeautifulSoup(source.text, 'lxml')

    table = soup.find(id='GridView3')  # defines table
    word = table.find_all(width="120")  # finds verb html
    types = table.find_all(width="300")  # finds type html

    verb_dict = {}  # defines empty dictionary to store wordverbs and values(verb,adj etc)
    verbs = []  # defines empty list to store wordverbs
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
        verbs.append(empt)
    verbs[0] = 'is'
    verbs[155] = 'rid'
    # print(len(verbs))

    # above defines list of readable verbs

    # adds verbs(keys) to dictionary with no values
    for i in verbs:
        verb_dict[i] = None

    # below code defines list of correseponding types verb, adj, noun etc

    test = []
    for i in types:
        m = i.text
        test.append(m)

    count = 0
    type = []
    for i in verb_dict:
        type = []
        if 'verb' in test[count]:
            type.append('verb')
            if 'noun' in test[count]:
                type.append('noun')
                if 'adjective' in test[count]:
                    type.append('adjective')
                    if 'auxiliary' in test[count]:
                        type.append('auxiliary')
                        if 'interjection' in test[count]:
                            type.append('interjection')

            elif 'adjective' in test[count]:
                type.append('adjective')
                if 'auxiliary' in test[count]:
                    type.append('auxiliary')
                    if 'interjection' in test[count]:
                        type.append('interjection')

            elif 'auxiliary' in test[count]:
                type.append('auxiliary')
                if 'interjection' in test[count]:
                    type.append('interjection')
            elif 'interjection' in test[count]:
                type.append('interjection')

        verb_dict[i] = type
        count += 1

    return verb_dict
