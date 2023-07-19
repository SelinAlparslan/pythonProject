# without sqlparse

def writeTable(c):
    table_file = open('tables.txt', 'w')
    for c in CUID:

        for w in c[1]:
            table_file.write("\n")
            table_file.write(c[0])
            #table_file.write("\n")
            table_file.write("\t")
            table_file.write(w)


import pandas as pd

ex_data = pd.read_excel('DATA.xlsx')
CUIDS = ex_data['CUID'].values.tolist()
list = ex_data['SQL'].values.tolist()
start = 0
end = 0
TABLE_NAMES = []
CUID = []
i = 0
for l in list:
    sorgu_select_to_where = ''.join(l)
    words = sorgu_select_to_where.split()
    # print(words)

    #SORGUDA FROM ILE WHERE INDEXLERINI ALIR
    for w in words:
        if w == "FROM":
            start = words.index(w) + 1
        if w == "WHERE":
            end = words.index(w)
            break
    newWords = words[start:end]

    #SORGU ICINDE TABLOLAR ARASI FAZLA VIRGUL SILER VE TABLO OLMAYANLARI CIKARTIR
    for w in newWords:
        if w[len(w) - 1] != "," and newWords.index(w) != len(newWords) - 1:
            newWords.pop(newWords.index(w) + 1)
        newWords[newWords.index(w)] = w.replace(",", "")
    CUID.append([
        CUIDS[i],
        newWords
    ])
    i += 1


writeTable(CUID)

# print(CUID)
