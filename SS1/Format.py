# import txt file
# store each line into list
# filters txt file
# append / concatenate appropriately
# output
#
#
#
#
#
import re

list = []
flist = []
# filtered out all line breaks
fflist = []
# contains the final reconstructed version
ffflist = []


def EmptyValue(x):
    if x == '':
        return False
    else:
        return True


# filter removes \n, \x0c, x from the txt file
with open('FormatText.txt') as f:
    for line in f:
        filtered1 = re.sub('\n', '', line)
        filtered2 = re.sub('\x0c', '', filtered1)
        filtered3 = re.sub('x', '', filtered2)
        list.append(filtered3)


# filter removes empty strings
flist = (filter(EmptyValue, list))

#
for x in flist:
    fflist.append(x)
    print(x)

# final list creation:
# add the time stamp to the final list(3)
ffflist.append(fflist[0])
# modifies the final list(3):
# loop, iterate through the disarranged, [5] appends to [1], then [6] to [2]
# ...rearranging to a consistent format
for x in range(1, 5, 1):
    ffflist.append(fflist[x] + " " + fflist[4 + x])

# prints out the modified list
for x in range(5):
    print(ffflist[x])
