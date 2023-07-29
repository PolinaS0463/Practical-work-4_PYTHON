from random import randint

length = int(input("Введите длину массива: "))
list = [randint(1, 11) for i in range(length)]
print(list)

max_sum = 0
sum = 0

# I. Способ:

list_count = []
for index in range(len(list)):
       list_count.append(list[index-2] + list[index-1] + list[index])
print(max(list_count))

# II. Способ:

for elem in range(length):
    for index in range(elem, elem + 3):
        sum += list[index % length]
    if(sum > max_sum):
        max_sum = sum
    sum = 0

print(max_sum)