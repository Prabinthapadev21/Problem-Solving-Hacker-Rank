n = 6

def staircase(n):
    for i in range(1, n + 1):
        # Print spaces first (n - i)
        for j in range(n - i):
            print(" ", end="")     # no newline
        
        # Print hashes (#) next
        for k in range(i):
            print("#", end="")     # no newline
        
        # Move to next line after each row
        print()

staircase(n)
