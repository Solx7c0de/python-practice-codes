def rec(n):
    if(n == 0 or n ==1):
        return 1
    a = (n * rec(n-1))
    return a

n = int(input(f"enter a number : "))
fact = rec(n)
print(f"factorial of {n} = {fact}")