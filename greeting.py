def welcome(name):
  print("Hello %s, Welcome to Hackem!" % (name))

def add(num1, num2):
  return num1 + num2

if __name__ == "__main__":
  # Message printed only if this file is being executed:
  # python3 greeting.py
  print("This file is being executed: greeting.py")
else:
  # Message printed only if this file is being imported as module:
  # import greeting
  print("This file is being imported as module: greeting.py")