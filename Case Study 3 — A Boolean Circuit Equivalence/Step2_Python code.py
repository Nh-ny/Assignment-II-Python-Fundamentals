# myCircuit.py
# Name: Nayeon Kim
# Student ID: u3309753
# Date: 17-09-2025

def circuit_a(A, B, C):
    return ((not A and not C) and not C) or (B and C)

def circuit_b(A, B, C):
    return A and (not B or C)

print("A B C | X | Y | X==Y")
for A in [0, 1]:
    for B in [0, 1]:
        for C in [0, 1]:
            X = circuit_a(A, B, C)
            Y = circuit_b(A, B, C)
            print(f"{A} {B} {C} | {int(X)} | {int(Y)} | {X == Y}")
