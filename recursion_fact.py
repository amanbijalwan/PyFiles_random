n1 = int(input("Enter number: "))

def fact(n):
    if n == 1:
        print(n)
        return n
        
    else:
        return n * fact(n-1)

fact(n1)