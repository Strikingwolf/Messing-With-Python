def check(n):
    if n % 2 == 0:
        return "even"
    else:
        return "odd"


def get_evens(number_wanted):
    evens = []
    a = -1
    while a < number_wanted:
        a += 1
        if check(a) == "even":
            evens.append(a)
    return evens


def get_odds(number_wanted):
    odds = []
    a = -1
    while a < number_wanted:
        a += 1
        if check(a) == "odd":
            odds.append(a)
    return odds


def run():
    odd_even = input("Do you want to print the odd or even numbers? (odd or even)")
    number_wanted = int(input("How many do you want to print? (must be positive)"))
    if odd_even == "odd":
        for num in get_odds(number_wanted):
            print(num)
    elif odd_even == "even":
        for num in get_evens(number_wanted):
            print(num)


if __name__ == "__main__":
    run()