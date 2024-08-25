def color_code(first_color, second_color, third_color):
    a, b, c = 0, 0, 0
    
    if first_color == "black":
        a = 0
    elif first_color == "brown":
        a = 1
    elif first_color == "red":
        a = 2
    elif first_color == "orange":
        a = 3
    elif first_color == "yellow":
        a = 4
    elif first_color == "green":
        a = 5
    elif first_color == "blue":
        a = 6
    elif first_color == "violet":
        a = 7
    elif first_color == "grey":
        a = 8
    elif first_color == "white":
        a = 9
        
    if second_color == "black":
        b = 0
    elif second_color == "brown":
        b = 1
    elif second_color == "red":
        b = 2
    elif second_color == "orange":
        b = 3
    elif second_color == "yellow":
        b = 4
    elif second_color == "green":
        b = 5
    elif second_color == "blue":
        b = 6
    elif second_color == "violet":
        b = 7
    elif second_color == "grey":
        b = 8
    elif second_color == "white":
        b = 9

    if third_color == "black":
        c = 1
    elif third_color == "brown":
        c = 10
    elif third_color == "red":
        c = 100
    elif third_color == "orange":
        c = 1000
    elif third_color == "yellow":
        c = 10000
    elif third_color == "green":
        c = 100000
    elif third_color == "blue":
        c = 1000000
    elif third_color == "violet":
        c = 10000000
    elif third_color == "grey":
        c = 100000000
    elif third_color == "white":
        c = 1000000000
    
    return (a * 10 + b) * c
    
first_color = input()
second_color = input()
third_color = input()

print(color_code(first_color, second_color, third_color))