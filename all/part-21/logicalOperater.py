# Logical AND: True if both operations are true (x and y)
# Logical OR: True if either of the operands is true (x or y)
# Logical NOT: True if the operand is false (not x)

ssc = 99
hsc = 75
criminal = False

if not criminal:  # Corrected to use `not` for readability
    print("Eligible")
else:
    print("Not eligible")

if ssc >= 60 and hsc >= 60:
    print("Eligible")
else:
    print("Not eligible")
