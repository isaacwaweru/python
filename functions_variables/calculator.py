def main():
    x = int(input("What's x? "))
    print("Square of x is", square(x))
  
def square(n):
    return pow(n, 2)

main()