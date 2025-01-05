# program to check if a number is power of 4

def powerOf4(number):
    
    count = 0
    
    # if only 1 set bit exists 
    if number == (number & (~(number - 1))):
        while (number > 1):
            number >>= 1
            count = count +  1
        if count % 2 == 0:
            print("4^", count//2)
            return True
        else:
            return False
        
number = int(input("Enter your number: "))
if(powerOf4(number)):
    print(number, 'is power of 4')
else:
    print(number, 'is not power of 4')