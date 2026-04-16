# Input three integers
x = int(input("Enter x: "))
y = int(input("Enter y: "))
z = int(input("Enter z: "))

# Ensure x is the smallest
if x > y:
    x, y = y, x
if x > z:
    x, z = z, x

# Ensure y is smaller than or equal to z
if y > z:
    y, z = z, y

# Output in ascending order
print(f"Sorted order: {x},<= {y},<= {z}")