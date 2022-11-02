def is_prime(n):
  for i in range(2,int(n/2)):   # the only factor of n that is greater than n/2 is n itself
    if (n%i) == 0:
      return False
  return True


number = int(input())
print(is_prime(number))
