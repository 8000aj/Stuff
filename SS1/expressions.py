words = ['a', 'aa', 'b', 'b', 'c', 'c', 'd', 'd', 'aa', 'bb', 'bb', 'cc', 'cc']
stopwords = ['a', 'c']
# for word in list(words):  # iterating on a copy since removing will mess things up
#    if word in stopwords:
#        words.remove(word)

fwords = []
slist = ['']

x = 0
n = 0
while x < len(words):
    if len(words[x]) == 2:
        while n < len(slist):
            if slist[n] == words[x]:
                fwords.append(words[x])
            else:
                slist.append(words[x])
            n += 1
    else:
        fwords.append(words[x])
    x += 1

print("slist: ")
for l in slist:
    print(l)

print("fwords: ")
for l in fwords:
    print(l)
