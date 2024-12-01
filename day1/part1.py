file = open("part1.txt", "r")
first_list = []
second_list = []
distance = 0
for line in file:
   column_a,column_b = line.split()
   first_list.append(int(column_a))
   second_list.append(int(column_b))

first_list.sort()
second_list.sort()

for column in range(len(first_list)):
   print (second_list[column] - first_list[column])
   distance += abs(second_list[column] - first_list[column])

print (distance)