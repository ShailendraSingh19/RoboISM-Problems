print("Put the array of intergers speperated by spaces ")
txt = input()
list1=list(txt.split(" "))
list2 = [0]*99
for i in range(0, 100):
    list1[i] = int(list1[i])
for i in range(0,100):
    ele=(list1[i]-1)
    (list2[ele])=(list2[ele])+1
#print(list1)
#print(list2)
for i in range(0,100):
    if list2[i]==2:
        print("Repeated no. is: "+str(i+1))
        break