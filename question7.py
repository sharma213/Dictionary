d=[{"first":"1"}, {"second": "2"}, {"third": "1"}, {"four": "5"}, {"five":"5"}, {"six":"9"},{"seven":"7"}]
i=1
a=[]
while i<len(d):
    for j in d[i]:
        if d[i][j] not in a:
            a.append(d[i][j])
    i=i+1
print(a)