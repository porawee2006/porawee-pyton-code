direction = input("what is tour conversion direction (1: THB to USD, 2: USD to THB):")
amount = float(input("amount to convert:"))
if direction == "1":
    result = amount /35.5
    print("result : ", result, "USD")
if direction == "2":
    result = amount * 35.5
    print("result : ", result, "THB")