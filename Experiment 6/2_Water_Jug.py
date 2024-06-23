from Display import display
import os

inputMsg = '''Choose the operation number:
1) Fill the jug A completely
2) Fill the jug B completely
3) Empty the jug A on to the ground
4) Empty the jug B on to the ground
5) Pour the water from jug A to jug B
6) Pour the water from jug B to jug A
'''

jug_A_Capacity = int(input("Enter max capacity of jug A : "))
jug_B_Capacity = int(input("Enter max capacity of jug B : "))
jug_A = int(input("Enter initial water in jug A : "))
jug_B = int(input("Enter initial water in jug B : "))
jug_AF = int(input("Enter final capacity of jug A : "))

while(jug_A != jug_AF):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(inputMsg)
    display(jug_A, jug_B)
    op = int(input("Enter operation number :"))

    match op:
        case 1:
            jug_A = jug_A_Capacity
        case 2:
            jug_B = jug_B_Capacity
        case 3:
            jug_A = 0
        case 4:
            jug_B = 0
        case 5:
            if jug_B_Capacity - jug_B > jug_A:
                jug_B += jug_A
                jug_A = 0
            else:
                jug_A -= (jug_B_Capacity-jug_B)
                jug_B = jug_B_Capacity
        case 6:
            if jug_A_Capacity - jug_A > jug_B:
                jug_A += jug_B
                jug_B = 0
            else:
                jug_B -= (jug_A_Capacity-jug_A)
                jug_A = jug_A_Capacity
        case _:
            print("Invalid operation number")
    
os.system('cls' if os.name == 'nt' else 'clear')
print("Goal achieved!")
display(jug_A, jug_B)