my_dict={"bijender":45,"deepak":60,"param":20,"anjali":30,"roshini":50}
sorted_dict=my_dict.keys()
sorted_dict=sorted(sorted_dict)
print("sorted dictionary using sorted() and keys() is:")
for key in sorted_dict:
    print(key,":", my_dict[key])