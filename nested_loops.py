# Nested loops are loops inside other loops. The inner loop will be executed one time for each iteration of the outer loop.
# In this example, i am trying to print all Domino tiles.
for left in range(7):
    for right in range(left, 7):
        print("[" + str(left) + "|" + str(right) + "]", end=" ")
    print()

# Now i will try to print time table for football league. The league has 4 teams and each team will play against each other team twice (home and away).    
print("______________________________________")
print("Football League Schedule:")
teams = ['Barcelona', 'Real Madrid', 'Manchester City', 'Arsenal']
for home in teams:
    for away in teams:
        if home != away:
            print(home + " vs " + away)