'''
devoriales.com
description: This is a battle between Python 3.10 and Python 3.11 to see which one is faster.
'''

# function that will compute squareroot of a number


def fibonacci(n):
  if n <= 1:
    return n
  else:
    return fibonacci(n-1) + fibonacci(n-2)

def prime_factorization(n):
  # initialize a list to store the prime factors
  prime_factors = []

  # Divide the number by 2 until it is reduced to 1
  while n % 2 == 0:
    prime_factors.append(2)
    n = n // 2
  
  # Divide the number by odd numbers until it is reduced to 1
  for i in range(3, n + 1, 2):
    while n % i == 0:
      prime_factors.append(i)
      n = n // i
  
  # Return the list of prime factors
  return prime_factors

if __name__ == '__main__': # main function that only runs when the file is executed, not imported
  round = 36 # how many rounds to run
  current_round = 1 # initialize the round number
  for i in range(1, round, 1): # loop from 1 to 50

    print(f"Round {current_round}:") # print the round number
    print(prime_factorization(fibonacci(i))) # print the prime factorization of the fibonacci number
    current_round += 1 # increment the round number
    if current_round == round:
      print("Done!")
