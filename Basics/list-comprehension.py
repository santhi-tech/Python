#list Comprehension
#syntax :

#[<expression>  for <item> in <items> <conditional>]

value = [ x for x in range(1,10) if x % 2 == 0 ]

print(value)

# add a value by 1
numbers = [1,2,3,4,5,6,7,8]
num = [number + 1 for number in numbers]
print(num)

# square
square = [ number * number  for number in range(1,10) if number % 2 == 0 ]
print(square)

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

# primes_list = prime_numbers(20)
# print(primes_list)

# Genrators are similar to list comprehensions, 
# but they use parentheses instead of square brackets.
# It is a special python function which return values as they are found
# It's a function with a yield statement (it return only one value) but not return 
def prime_numbers_range_gen(start=0, stop=10):
    for number in range(start, stop):
        if prime_numbers(number):
            yield number
    
for prime_number in prime_numbers_range_gen(10,50):
    print(prime_number * 2)