L = [n*5 for n in range (15) if (n*5)%2==1]

l = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

def argument(n,l):
    if n in l:
            return(True)
    else:
            return(False)


    
print(argument(3,L))