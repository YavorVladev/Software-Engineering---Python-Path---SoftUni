from math import pi

figure = input()

if figure == "square":
    duljina_str = float(input())
    lice = duljina_str * duljina_str
    print(round(lice, 3))
elif figure == "rectangle":
    strana_a = float(input())
    strana_b = float(input())
    lice = strana_b * strana_a
    print(round(lice, 3))
elif figure == "circle":
    radius = float(input())
    lice = pi * radius * radius
    print(round(lice, 3))
elif figure == "triangle":
    strana_a = float(input())
    visochina = float(input())
    lice = (visochina * strana_a) / 2
    print(round(lice, 3))