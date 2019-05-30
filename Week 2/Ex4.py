a= list(map(int, input().split(' ')))
b= list(map(int, input().split(' ')))

My_list=[i for i in set(a) if i in set(b)]
print(My_list)