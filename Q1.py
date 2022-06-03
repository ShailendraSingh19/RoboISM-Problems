def list_sort(list1,mode):
     #list1 ios string and mode is string
    if (mode=='asc'):
        list1.sort()
    elif (mode == 'desc'):
        list1.sort(reverse=True)
    elif(mode =='none'):
       pass
    return(list1)
list1 = [1,2,3,4,53,2,6,8,9]
list2 = [3,56,98,0,43,-21,-31]
print(list_sort(list1,'asc'))
print(list_sort(list2,'desc'))




        
         
