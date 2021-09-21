def ToPercentage(decimalTal):
    return decimalTal * 100.0


while True:
    tal = float(input("Mata in decimaltal mellan 0-1"))
    print(ToPercentage(tal))