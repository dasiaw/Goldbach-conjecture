import math

def isEven (i):
	if i%2==0:
	    return True
	    print("helloworld")

	else:
		return False
		print("helloworldd")


def isPrime(i):
     from math import sqrt
     if i == 0 or i == 1:
         flag = False
         print("if start")
     elif i == 2:
         flag = True  
     else:
         for i in range(2, i):
             if i % i == 0:
                 flag = False
                 break
             else:
                 flag = True
                 return flag

def isnum( string ):
    if string.isdigit():
       return True
    else:
        return False





def main():

    print("helloworld")


for i in xrange(1,10):
    
    if i%2==0:
        
        print(i)
        
            i_list = []

            for i in range(1,Uinput):
                    
                    j = Uinput - i #Break down into two numbers
                
                if isPrime(i) and isPrime(j):
                    
                    i_list.append(i) #Record displayed numbers
                    
                    if j in i_list:
                            
                            pass
                    
                    else:
                            
                            print( '{0} = {1} + {2}'.format(Uinput, i, j))
        
        else:
            
            print('Input error!')

       
    else:
        print("helloworldd")
    

    
	
if __name__=="__main__":
    main()




