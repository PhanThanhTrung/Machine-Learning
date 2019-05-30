Input_str=input() 
W = int(input())
List=[Input_str[i:min(i+W,len(Input_str))] for i in range(0,len(Input_str),W)]