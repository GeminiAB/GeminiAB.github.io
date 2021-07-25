
test = lambda x: "even" if(x%2 == 0) else "odd"
print(test(103))


even_num = list(filter(lambda x: x%2==0, [1,2,3,4,5,6]))
print(even_num)