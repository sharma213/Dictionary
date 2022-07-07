

d1={'a':100,'b':200,'c':300}
d2={'a':300,'b':200,'d':400}
for i in d1:
    if i in d2:
        d2[i]=d1[i]+d2[i]
d1.update(d2)
print(d1)




str1='w3school'
my_dic={}
for letter in str1:
    my_dic[letter]=my_dic.get(letter,0)+1
print(my_dic)



 
n=int(input("enter your number"))
my_dic={}
for x in range(n+1):
    my_dic[x]=x*x
print(my_dic)


n=int(input("enter your number"))
my_dic={}
for x in range(n+1):
    my_dic[x]=x*x
print(my_dic)


d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
print('Original dictionary : ',d)
sorted_d = sorted(d.items(), key=operator.itemgetter(1))
print('Dictionary in ascending order by value : ',sorted_d)
sorted_d = dict( sorted(d.items(), key=operator.itemgetter(1),reverse=True))
print('Dictionary in descending order by value : ',sorted_d)


dic={"abhishek":[10,20,30]
    "richa":[30,40,50]
     }