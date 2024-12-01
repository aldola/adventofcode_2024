file = open("part2.txt", "r")
first_list = []
second_list = []
similarity_score = 0
for line in file:
   column_a,column_b = line.split()
   first_list.append(int(column_a))
   second_list.append(int(column_b))

first_list.sort()
second_list.sort()

for column in range(len(first_list)):
   similarity_score += first_list[column] * second_list.count(first_list[column])

print (similarity_score)