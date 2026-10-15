"""
this code is a calculator
"""


def calculator():
    """
    this function is calculation any integer numbers with this operators ('+', '_', '/', '*', '%')
    """
    amalgar = input("enter a amalgar = ")
    n = int(input("tedad adad ha = "))
    my_list = []
    for _ in range(n):
        number = int(input("enter numbers = "))
        my_list.append(number)
    first = my_list[0]
    for j in range(1, n):
        if amalgar == "+":
            first += my_list[j]
        elif amalgar == "-":
            first -= my_list[j]
        elif amalgar == "/":
            first /= my_list[j]
        elif amalgar == "*":
            first *= my_list[j]
        elif amalgar == "%":
            first %= my_list[j]
    print(f"your final resault is {first}")


calculator()
