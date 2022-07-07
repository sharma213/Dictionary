# stu={101:"raj",102:"rahul",103:"ankit"}
# it=stu.items()
# print(it)


# l=[1,2,3,4]
# i=0
# b=[]
# while i<len(l)-1:
#     s=l[i]+l[i+1]
#     b.append(s)
#     i=i+1
# print(b)

import requests

x = requests.get('https://w3schools.com/python/demopage.htm')

print(x.text)

