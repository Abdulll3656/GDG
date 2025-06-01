
def checker():
    num = int(input("Enter a number:"))
    result = ("The number is odd","The number is even")[num % 2 == 0]
    print(result)

if __name__ == "__main__":
    checker()


