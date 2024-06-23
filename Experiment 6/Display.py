def display(jug_A, jug_B):
    jug_A = str(jug_A)
    jug_B = str(jug_B)
    A_len = len(jug_A)
    B_len = len(jug_B)

    padding = 2
    print(f'''
    │{' '*(A_len+padding*2)}│ │{' '*(B_len+padding*2)}│
    │{jug_A.center(A_len+padding*2)}│ │{jug_B.center(B_len+padding*2)}│
    └{'─'*(A_len+padding*2)}┘ └{'─'*(B_len+padding*2)}┘
    {'A'.center(2+A_len+padding*2)} {'B'.center(2+B_len+padding*2)}
    ''')