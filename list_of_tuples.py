list = input("Enter the list of tuples (comma-separated): ")
tuple_elements = list.split(",")
tuples = [tuple(map(int, tpl.split())) for tpl in tuple_elements]

sorted_tuples = sorted(tuples, key=lambda x: x[-1])

print("Sorted Tuples:")
print(sorted_tuples)
