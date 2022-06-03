def cred(n_str):
    try:
        if (type(int(n_str)==int)):
          if (len(n_str) == 16):
            t = n_str[len(n_str)-4:len(n_str)]
            ret_str = '*'*(len(n_str)-4)+t
          if(len(n_str) != 16):
            ret_str = 'Not a valid number'
    except:
        ret_str = 'You have not a valid number'      
    return(ret_str)
n = '7658534627664735'
n1 = '2345216'
a = '1A23fg'
print(cred(n))
print(cred(n1))
print(cred(a))