my_dict = {'a': 9, 'b': 1, 'c': 12, 'd': 7}

#List={ key: value for key,value in sorted(my_dict.items(),key= lambda x: x[1])}.keys()
#print(List)
print(sorted(my_dict, key=my_dict.get))
