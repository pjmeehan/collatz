# the number we will perform the Collatz operations on
n = int(input("enter a positive integer : "))

# keep looping intil we reach 1
# note : this assumes the Collatz conjecture is true.

while n != 1:
    # print the current value of n.
    print(n)
# check if n is even.
    if n % 2 == 0:
        # if n is even, divide it by two.
       n =  n // 2
    else:
        #if n is odd, multiply by three and add 1.
       n = (3 * n) + 1
# Finally, print the 1.
print(n)           