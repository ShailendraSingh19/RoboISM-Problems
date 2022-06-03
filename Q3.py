def operation(n1,b,n2):
    if (b=='+'):
        t = n1+n2
    if (b == '-'):
        t = n1 - n2
    if (b == '*'):
        t = n1*n2
    if ( b== '/'):
        t = n1/n2
    return(t)
print(operation(23,'+',98))