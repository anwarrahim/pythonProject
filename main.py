



n = 3
# if n is an odd number
if n % 2 == 1:
    print("n is an odd number")
    # If  is even and in the inclusive range of  to , print Not Weird
elif n % 2 == 0 and n in range(2, 6):
    print("Not Weird")
    # If  is even and in the inclusive range of  to , print Weird
elif n % 2 == 0 and n in range(6, 21):
    print("Weird")
    # If  is even and greater than , print Not Weird
elif n % 2 == 0 and n > 20:
    print("Not Weird")