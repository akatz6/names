import random
def bubbleSort(list):
	for element in range(0, len(list)):
		for items in range(element + 1, len(list)):
			if list[element] > list[items]:
				temp = list[element]
				list[element] = list[items]
				list[items] = temp

list = []
for element in range(0, 100):
	random_num = random.random();
	random_num *= 1000
	random_num = round(random_num)
	list.append(int(random_num))

print list
bubbleSort(list)
print list
