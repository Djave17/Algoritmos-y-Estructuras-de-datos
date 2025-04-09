#Ejemplo de recursión 
#factorial 

#iterativamente 
def factorial(n):
    r = 1 
    i = 2 
    while i <= n: 
        r *= i 
        i += 1 
    
    return r  

factorial1 = factorial(5)
print(factorial1)

def factorial_recursivo(n): 
    if n == 1:
        return 1
    else:
        return n * factorial_recursivo(n-1)
#factorial_recursivo(5)

factorial_recursivo1 = factorial_recursivo(5)
print(factorial_recursivo1)


#Ejemplo de recursión
#Ejemplo de Fibonacci
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

fibonacci1 = fibonacci(5)
print(fibonacci1)

#Ejemplo de Fibonacci
def fibonacci_iterativo(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

#print de todas las recursiones 
fibonacci1 = fibonacci(5)
print("Fibonacci:", fibonacci1)
print("Factorial: ", factorial1)

