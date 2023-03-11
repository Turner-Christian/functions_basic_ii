# countdown
def countdown(n):
    arr = []
    if n <= 0:
        return False
    for n in range(n, 0-1, -1):
        arr.append(n)
    return arr
# print(countdown(10))

#print and return
def print_and_return(n):
    if len(n) != 2:
        return False
    print(n[0])
    return n[1]
# print(print_and_return([1,2]))

#first plus length
def first_plus_length(n):
    first_plus = n[0] + (len(n)-1)
    return first_plus
# print(first_plus_length([1,2,3]))

#values greater than second
def greater_than_second(n):
    if len(n) < 2:
        return False
    arr = []
    greater_than_count = 0
    for i in range(len(n)):
        if n[i] > n[1]:
            greater_than_count += 1
            arr.append(n[i])
    print(greater_than_count)
    return arr
# print(greater_than_second([1,2,3,4,5,6,7,8,9]))

#this length, that value
def this_length_that_value(n,x):
    arr = []
    for i in range(0 , n):
        arr.append(x)
    return arr
# print(this_length_that_value(6,2))
