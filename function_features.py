# 1
# arb-args - Takes in any number of arguments and prints them one at a time.
def arb_args(*args):
    for item in args:
        print(item)


arb_args('1', 'abc', 'Two')

# 2
# inner_func - Takes in two strings: a student's name and their lunch preference.
# The function should print both strings. If a lunch preference is not given,
# "Mystery Meat" should be printed instead.


def inner_func(num1, num2):
    def add(n1, n2):
        return n1 + n2

    def sub(n1, n2):
        return n1 - n2

    result = add(num1, num2) + sub(num1, num2)

    return result


print(inner_func(5, 6))

# 3
# lunch_lady - Takes in two strings: a student's name and their lunch preference.
# The function should print both strings. If a lunch preference is not given,
# "Mystery Meat" should be printed instead.


def lunch_lady(student_name, lunch_pref="Mystery Meat"):
    print(student_name)
    print(lunch_pref)


lunch_lady('Eshita', 'Salmon')
lunch_lady('Ayana')

# 4
# sum_n_product - Accepts two integers and returns both the sum and the product.


def sum_n_product(n1, n2):
    sum = n1 + n2
    product = n1 * n2
    return sum, product


print(sum_n_product(2, 3))
print(sum_n_product(5, 6))

# 5
# alias_arb_args - Should be arb_args but assigned an alias.
# Remember, variables can hold functions in Python just like they can in JS.
# Alternatively, you can call a function from inside another function.
alias_arb_args = arb_args
alias_arb_args('b', 'c', 'd')

# 6
# arb_mean - Accepts any number of integers and prints their average.


def arb_mean(*args):
    sum = 0
    for num in args:
        sum = sum + num

    return sum / len(args)


print(arb_mean(1, 2, 3, 4, 5))

# 7
# arb_longest_string - Accepts any number of strings and returns the longest one.


def arb_longest_string(*args):
    longest = ''
    for arg in args:
        if len(arg) > len(longest):
            longest = arg

    return longest


print(arb_longest_string('not so happy day',
      'abc', 'had a bad day today', 'good day'))
