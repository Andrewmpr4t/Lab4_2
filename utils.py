def fact(a):
    if a==1 or a==0:
        return 1
    else:
        return a * fact(a-1)
    def find_gcd(a, b):
        while b:
            a, b = b, a%b
            return a 
    
