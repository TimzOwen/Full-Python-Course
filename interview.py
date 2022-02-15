# quiz one
# using print statements, print a word stored in a variable called hello to output" hello world!"

hello = "hello world!"
print(hello)

## 2
#Given an integer, , perform the following conditional actions:

#If  is odd, print Weird
#If  is even and in the inclusive range of  to , print Not Weird
#If  is even and in the inclusive range of  to , print Weird
#If  is even and greater than , print Not Weird

n = int(raw_input())

if n%2==0 and (n in range(2,6) or n>20 ):
    print "Not",

print "Weird"

# soln 2
n = int(input())

if (n%2==0):
    if(n in range(2,5)):
        print("Not Weird")
    elif(n in range(6,20)):
        print("Weird")
    elif(n > 20):
        print("Not Weird")
else:
    print("Weird")