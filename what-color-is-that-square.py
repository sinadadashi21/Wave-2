oddLet = "a", "c", "e", "g"
evenLet = "b", "d", "f", "h"
oddNum = 1, 3, 5, 7
evenNum = 2, 4, 6, 8

letInput = input("Pick any letter including and between a and h: ")
numInput = int(input("Pick your integer including and between 1 and 8 : "))

if letInput.lower() in oddLet and numInput in oddNum:
    print("The square is black.")
elif letInput.lower() in oddLet and numInput in evenNum:
    print("The square is white.")
elif letInput.lower() in evenLet and numInput in evenNum:
    print("The square is black.")
elif letInput.lower() in evenLet and numInput in oddNum:
    print("The square is white.")