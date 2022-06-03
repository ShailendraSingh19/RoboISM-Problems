a = input("Enter the String")
a_list = list(a)
a_list.sort()
a_new = ''
for x in a_list:
    a_new += x
print(a_new)
