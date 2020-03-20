"""results = [["1", ""], ["2", "a"]]
p = ""
for x in range(0, 2, 1):
    print(x)
    # if ((p) != ""):
    if ((results[x][1]) != ""):
        # print(results[x][0])
        print("something")

    else:
        print("none")"""

""""""
master = []

one = ["1", "one"]
two = ["2", "two"]

master.append(one)
master.append(two)

for x in master:
    print(x)

print(master)
""""""


"""def conv_list(x):
    l = []
    for v in x:
        if ((v[-1]) == "M"):

            conv_m = ((float(v[:-1])) * 1000000)
            l.append(conv_m)

        elif ((v[-1]) == "B"):
            conv_m = ((float(v[:-1])) * 1000000000)
            l.append(conv_m)
        else:
            pass
    return (l)


nums = ["900M", "800B"]

t = conv_list(nums)

print(t)"""
