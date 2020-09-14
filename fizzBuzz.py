# Solution for challange in readme


def fizzbuzz(num):
  for i in range(1, num+1):
    if (i % 3 == 0 and i % 5 == 0):
      print(f"('{i} % 3 == 0', '{i} % 5 == 0', 'fizzbuzz')")
    elif ( i % 3 == 0):
      print(f"('{i} % 3 == 0', 'fizz')")
    elif (i % 5 == 0):
      print(f"('{i} % 5 == 0', 'buzz')")
    else:
      print(i)


fizzbuzz(20)