# A function to check if a number is prime
def if_prime(n):
  # Corner cases
  if n <= 1:
    return False
  if n == 2:
    return True
  if n % 2 == 0:
    return False

  # Check from 3 to sqrt(n)
  i = 3
  while i * i <= n:
    if n % i == 0:
      return False
    i += 2
  return True

# A function to find two prime numbers whose sum is equal to the given even number
def primes_pair(n):
  # Corner cases
  if n % 2 != 0 or n <= 2:
    return None

  # Start from the smallest prime number 2
  p = 2
  while p <= n // 2:
    # Check if p and n-p are both prime
    if if_prime(p) and if_prime(n - p):
      # Return the lexicographically smaller solution
      return (p, n - p)
    # Increment p for next loop
    p += 1
  # No solution
  return None

# Test
n = 58
primes = primes_pair(n)
print(primes)

# The time complexity of this code depends on the input size n and the number of prime numbers less than or equal to n.
# The biggest possible input: the primes_pair function will loop from 2 to n/2, and the if_prime function will loop from 3 to sqrt(n).
# Therefore, the time complexity of the code is O(n * sqrt(n)).

#The space complexity of this code is O(1), because it does not use any additional memory that depends on the input size n. The function primes_pair only uses two variables, p and primes, which are constant in size.
# The function if_prime also uses only one variable, i, which is also constant in size. Therefore, the code uses a constant amount of space regardless of the input.
