for i in range(1, 100):
    if i % 2 == 0 and i >= 20:
        print("Not Weird", i, "this is from first condition")
    elif i % 2 == 0 and 6 <= i <= 20:
        print("Weird", i, "this is from second condition")
    elif i % 2 == 0 and 2 <= i < 5:
        print("Not Weird", i, "this is from last condition")
    else:
        print(i, "is a odd number")
