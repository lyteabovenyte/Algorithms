def trial_division(n):
    factors = []
    
    # Divide by 2 until it's an odd number
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    
    # Try dividing by odd numbers starting from 3
    for i in range(3, int(n**0.5) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n //= i
    
    # If n is a prime number greater than 2
    if n > 2:
        factors.append(n)
    
    return factors


# Example Usage
number_to_factorize = 85
result = trial_division(number_to_factorize)
print(f"The factors of {number_to_factorize} are: {result}")