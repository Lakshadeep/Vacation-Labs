#Solution for task 2

#Given an input FILE consisting of numbers separated by spaces,
#write a program which displays the frequency distribution for
#the given input. 

#Submitted by Lakshadeep Naik

############################################################################



with open("DATA.txt") as f:
    for line in f:                    #line is every string in text file
        numbers_str = line.split(' ') #separate the  based on white
                                      #space and store in an array

        #typecasting (converting characters to integer)
        #and storing them in new array
        numbers_int = [int(x) for x in numbers_str]




numbers_int.sort()   #sorting numbers_int array

num = []             #array for storing all distinct numbers
frequency = []       #array for storing their frequency

count = 0            #temporary variable

#uncomment below line to print all numbers in text file
#print numbers_int    



for i in range(len(numbers_int)):
    if(i==0):
        num.append(numbers_int[i])
        count = 1
        
    else:
       
        if(numbers_int[i-1] == numbers_int[i]):
            count+=1
        else:
            frequency.append(count)
            num.append(numbers_int[i])
            count = 1

        if(i == len(numbers_int)-1):
            frequency.append(count)
        
                           
        
            
#print all the distinct numbers in text file    
print num

#print frequency of all the distinct numbers
print frequency

    


