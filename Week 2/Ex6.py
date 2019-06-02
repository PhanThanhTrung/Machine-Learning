my_str=input() 
W = int(input())
List=[my_str[i:min(i+W,len(my_str))] for i in range(0,len(my_str),W)]
print(*List,sep='\n')