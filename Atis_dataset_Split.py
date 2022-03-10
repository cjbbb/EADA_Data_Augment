'''
    This is a script used for handling atis dataset.
    Input: atis/active_packages, atis/active_entities
    Output: atis/label, atis/seq.in, atis/seq.out
'''

import random
import os


def read_data():
    '''
    This part is responsible for reading data from active_packages and active_entities
    '''

    intentSet = set()
    entitySet = set()
    intentFile = os.listdir('atis/active_packages')
    entityFile = os.listdir('atis/active_entities')
    for i in intentFile:
        i = i[0:-5]
        if i not in intentSet:
            intentSet.add(i)
    print("load " + str(len(intentSet)) + " intents")

    for i in entityFile:
        if i not in entitySet:
            entitySet.add(i)
    print("load " + str(len(entitySet)) + " entities")
    print(entitySet)

    mapSent = {}  # intent->sent
    mapSlots = {}  # sent->slots
    mapQuerySlots = {}  # sent->not entity words

    listTest = []
    listDev = []
    for key in mapSent:
        count = len(mapSent[key]) / 2
        i = 0
        for value in mapSent[key]:
            i += 1
            if (i <= count):
                listTest.append({
                    'intent': key,
                    'value': value,
                    'slots': mapSlots[value]
                })
            else:
                listDev.append({
                    'intent': key,
                    'value': value,
                    'slots': mapSlots[value]
                })
    random.shuffle(listTest)
    random.shuffle(listDev)
    with open("atis/label", 'w') as wtLabel:
        with open("atis/seq.in", 'w') as wtSent:
            with open("atis/seq.out", 'w') as wtSlots:
                for i in listTest:
                    wtLabel.write(i['intent'] + '\n')
                    wtSent.write(i['value'] + '\n')
                    words = i['value']
                    for j in mapSlots[i['value']]:
                        if ' ' in j:
                            splits = j.split(' ')
                            strAns = 'B-' + mapSlots[i['value']][j]
                            for count in range(len(splits) - 1):
                                strAns += ' I-' + mapSlots[i['value']][j]

                            words = words.replace(j, strAns, 1)
                        else:
                            wordSplits = words.split(' ')
                            for temp in range(len(wordSplits)):
                                if wordSplits[temp] == j:
                                    wordSplits[temp] = 'B-' + str(mapSlots[i['value']][j])

                            words = ' '.join(wordSplits)

                    wordSlots = words.split(' ')
                    ans = []
                    for i in wordSlots:
                        if len(i) >= 2:
                            if ((i[0] == 'I') | (i[0] == 'B')) & (i[1] == '-'):
                                ans.append(i)
                            else:
                                ans.append('O')
                        else:
                            ans.append('O')
                    words = ' '.join(ans)
                    wtSlots.write(words + '\n')


def write_to_data():
    '''
        this function is responsible for generating label&seq.in&seq.out
    '''

    with open("atis/label", 'w') as wtLabel:
        with open("atis/seq.in", 'w') as wtSent:
            with open("atis/seq.out", 'w') as wtSlots:
                for i in listDev:
                    wtLabel.write(i['intent'] + '\n')
                    wtSent.write(i['value'] + '\n')
                    words = i['value']
                    for j in mapSlots[i['value']]:
                        if ' ' in j:
                            splits = j.split(' ')
                            strAns = 'B-' + mapSlots[i['value']][j]
                            for count in range(len(splits) - 1):
                                strAns += ' I-' + mapSlots[i['value']][j]

                            wordSplits = words.split(' ')
                            wordSplits = words.split(' ')
                            for temp in range(len(wordSplits)):
                                if wordSplits[temp] == j:
                                    wordSplits[temp] = strAns
                            words = ' '.join(wordSplits)
                        else:
                            wordSplits = words.split(' ')
                            for temp in range(len(wordSplits)):
                                if wordSplits[temp] == j:
                                    wordSplits[temp] = 'B-' + str(mapSlots[i['value']][j])
                            words = ' '.join(wordSplits)

                    wordSlots = words.split(' ')
                    ans = []
                    for i in wordSlots:
                        if len(i) >= 2:
                            if ((i[0] == 'I') | (i[0] == 'B')) & (i[1] == '-'):
                                ans.append(i)
                            else:
                                ans.append('O')
                        else:
                            ans.append('O')
                    words = ' '.join(ans)
                    wtSlots.write(words + '\n')


if __name__ == "__main__":
    read_data()
    write_to_data()
