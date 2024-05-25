def is_armstrong(n):
    return sum(int(i)**len(str(n)) for i in str(n)) == n
n=int(input())
print(is_armstrong(n))
