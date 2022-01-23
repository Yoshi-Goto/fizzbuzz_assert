def fizzbuzz_convert(param):
    if param % 15 == 0:
        return 'FizzBuzz'
    elif param % 3 == 0:
        return 'Fizz'
    elif param % 5 == 0:
        return 'Buzz'

    return param


assert fizzbuzz_convert(1) == 1
assert fizzbuzz_convert(2) == 2
assert fizzbuzz_convert(3) == 'Fizz'
assert fizzbuzz_convert(6) == 'Fizz'
assert fizzbuzz_convert(5) == 'Buzz'
assert fizzbuzz_convert(10) == 'Buzz'
assert fizzbuzz_convert(15) == 'FizzBuzz'
assert fizzbuzz_convert(30) == 'FizzBuzz'
