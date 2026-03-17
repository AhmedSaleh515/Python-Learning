# Nested loops are loops inside other loops. The inner loop will be executed one time for each iteration of the outer loop.
# In this example, i am trying to print all Domino tiles.
for left in range(7):
    for right in range(left, 7):
        print("[" + str(left) + "|" + str(right) + "]", end=" ")
    print()

    