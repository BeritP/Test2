import turtle as tu
lines = 100

with open("1_million_digits_of_pi.txt.txt", "r") as f: 
    pi = f.read()

for n in range(lines):
    zahl = int(pi[n])
    rotation = zahl * 36
    tu.setheading(rotation)
    tu.forward(3)
turtle.done()