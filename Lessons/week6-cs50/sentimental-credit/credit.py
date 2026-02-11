def main():

    # Repeatedly ask for input until correct one is given:
    while True:
        try:
            card_number = int(input("Your card number: "))
            break
        except ValueError:
            pass

    valid = False

    card = which_card(card_number)

    # Skipping applying validity check on incorrect format number:
    if card != "INVALID":
        valid = is_valid(card_number)

    if valid == True:
        print(card)

    else:
        print("INVALID")


def which_card(n):
    digits = 1

    while n > 9:
        if 10 <= n < 100:
            first_two = n
        n = n // 10
        digits += 1

    first_one = n

    if digits == 15 and (first_two == 34 or first_two == 37):
        return "AMEX"
    elif digits == 13 and first_one == 4:
        return "VISA"
    elif digits == 16:
        if first_one == 4:
            return "VISA"
        elif first_two > 50 and first_two < 56:
            return "MASTERCARD"
        else:
            return "INVALID"
    else:
        return "INVALID"


def is_valid(n):
    length = 1 # Accounts for last digit 1-9
    total_first = 0 # Every odd digit
    total_second = 0 # Every other/even digit

    # Separate variable for counting length without overwriting:
    m = n
    while m > 9:
        m = m / 10
        length += 1

    # i -> index of which digit we're iterating over and exponent value
    # Going from right to left
    for i in range(length):
        mod = 10**(i + 1) # Remove digits on the left with
        div = 10**i # Remove digits on the right with

        digit = (n % mod) // div

        if (i % 2) != 0: # Every other digit
            digit *= 2
            if digit > 9:
                # Adding digits together for two-digit products
                digit = (digit % 10) + (digit // 10)
                total_second = total_second + digit
            else:
                total_second = total_second + digit

        else: # Every odd digit:
            total_first = total_first + digit

    total = total_first + total_second

    if total % 10 == 0:
        return True
    else:
        return False


if __name__ == "__main__":
    main()
