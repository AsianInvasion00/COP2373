def main():
    # This calls the other functions and the answer should display as 35.
    answer = division(multiplication(addition(5, 2), 10), 2)
    print(f"The answer to ((5+2)x10)/2 is {answer}.")

def addition(a, b):
    # adds 2 integers together
    answer = a + b
    return answer

def multiplication(a, b):
    # multiplies 2 integers together
    answer = a * b
    return answer
def division(a, b):
    # divides 2 integers together
    answer = a / b
    return answer

if __name__ == "__main__":
    main()
