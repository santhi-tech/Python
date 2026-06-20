#functions are blocks of reusable code that perform a specific task. 
# In Python, functions are defined using the `def` keyword, followed by the function name and parentheses. 
# Functions can take parameters (inputs) and can return values.

def greet(name):
    """This function greets the person passed in as a parameter."""
    return f"Hello, {name}!"

argument = "Santhi"
greeting = greet(argument) 
print(greeting)

def prime_numbers(n):
    """This function returns a list of prime numbers up to n."""
    primes = []
    for num in range(2, n + 1):
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes

primes_list = prime_numbers(20)
print(primes_list)

#prime numers using list comprehension
prime_numbers_list_comprehension = [num for num in range(1000, 1020) if prime_numbers(num)]     
print(prime_numbers_list_comprehension)