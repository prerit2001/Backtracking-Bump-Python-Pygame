
N = int(input('Please Enter N For a Matrix of ( N x N ) '))

Chess = list()

for _ in range(N) :
    Chess.append(0)

for _ in range(N) :
    Chess[_] = list()
    for i in range(N) :
        Chess[_].append(0)

Left_diogonal = list ()
Right_diogonal = list ()
Coloumn_check = list ()

for _ in range(100000) :
    Left_diogonal.append(0)
    Right_diogonal.append(0)
    Coloumn_check.append(0)

def Solve(Chess_Borad,Coloumn) :

    if Coloumn >= N :
        return True

    for Current_Position in range(N) :
        if Coloumn_check[Current_Position] == 0 :
            if Right_diogonal[Current_Position + Coloumn] == 0 :
                if Left_diogonal[Current_Position - Coloumn + N - 1] == 0 :

                    Chess_Borad[Current_Position][Coloumn] = 1
                    Coloumn_check[Current_Position] = 1
                    Right_diogonal[Current_Position + Coloumn] = 1
                    Left_diogonal[Current_Position - Coloumn + N - 1] = 1



                    if Solve(Chess_Borad,Coloumn+1) :
                        return True

                    Chess_Borad[Current_Position][Coloumn] = 0
                    Coloumn_check[Current_Position] = 0
                    Right_diogonal[Current_Position + Coloumn] = 0
                    Left_diogonal[Current_Position - Coloumn + N - 1] = 0

    return False

Solve(Chess,0)

for i in range(N) :
    for j in range(N) :
        print(Chess[i][j],end=" ")
    print()