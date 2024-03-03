#write a program to compute quotient and reminder of a number without using division operator and modulus operator . Also mentioned procedure for calculating.

def divide_without_operator(dividend, divisor):
    # Initialize quotient
    quotient = 0
    # Subtract the divisor from the dividend until it's less than the divisor
    while dividend >= divisor:
        dividend -= divisor
        quotient += 1
    # Return quotient and remainder
    return quotient, dividend

dividend = int(input("Enter the dividend: "))
divisor = int(input("Enter the divisor: "))

quotient, remainder = divide_without_operator(dividend, divisor)
print("Quotient:", quotient)
print("Remainder:", remainder)
