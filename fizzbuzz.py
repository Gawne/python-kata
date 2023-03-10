def fizzbuzz(number):

    response = number

    # check whether divisible by 3

    if(is_fizz(number)):
        response = "fizz"

    # check whether divisible by 5, then 3 and 5

    if(is_buzz(number)):
        if(response != number):
            response = "fizzbuzz"
        else:
            response = "buzz"

    return response

def is_fizz(number):
    if(number % 3) == 0:
        return True

def is_buzz(number):
    if(number % 5) == 0:
        return True

assert fizzbuzz(1) == 1
assert fizzbuzz(2) == 2
assert fizzbuzz(3) == "fizz"
assert fizzbuzz(4) == 4
assert fizzbuzz(5) == "buzz"
assert fizzbuzz(6) == "fizz"
assert fizzbuzz(8) == 8
assert fizzbuzz(9) == "fizz"
assert fizzbuzz(15) == "fizzbuzz"
