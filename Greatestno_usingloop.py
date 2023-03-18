n=int(input("enter the no of integers you want to compare\n"))
input_list = list()
for i in range(n):
    input_value=int(input("enter the numbers\n"))
    input_list.append(input_value)
    print(input_list)
    max =input_list[ 0 ]
    for a in input_list:
        if a > max:
            max = a
print("greatest number is",a)
