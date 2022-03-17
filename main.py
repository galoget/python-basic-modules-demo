import greeting

if __name__ == "__main__":
  # Message printed only if this file is being executed:
  # python3 main.py
  print("This file is being executed: main.py")

  # Greeting
  greeting.welcome("Maria")
  greeting.welcome("Joseph")

  # Add 2 numbers
  num1 = 5
  num2 = 7
  print("The sum of %s + %s is %s." % (num1, num2, greeting.add(num1, num2)))

else:
  # Message printed only if this file is being imported as module:
  print("This file is being imported as module: main.py")
