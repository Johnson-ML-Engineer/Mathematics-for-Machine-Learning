"""Python program to solve a system of linear equations using
the Gaussian Elimination method without using any external libraries"""

def forward_elimination(matrix,n):
    for i in range(n):
        if matrix[i][i]==0:
            for k in range(i+1,n):
                if matrix[k][i]!=0:
                    matrix[k],matrix[i]=matrix[i],matrix[k]
                    break
        pivot=matrix[i][i]
        #normalise the row
        for j in range(n+1):
            matrix[i][j]/=pivot
        #eliminate the row
        for k in range(n):
            if k==i:
                continue
            factor=matrix[k][i]
            for j in range(n+1):
                matrix[k][j]-=factor*matrix[i][j]

def back_substitution(matrix,n):
    solution=[0]*n
    for i in range(n-1,-1,-1):
        solution[i]=matrix[i][n]
        for j in range(i+1,n):
            solution[i]-=matrix[i][j]*solution[j]
    return solution    


def solve_linear_equations(matrix):
    n=len(matrix)
    forward_elimination(matrix,n)
    solution=back_substitution(matrix,n)
    return solution

# Example system of linear equations:
    # 2x + 3y - z = 7
    # 4x - 2y + 2z = 4
    # -2x + y + 2z = -10
matrix = [
           [2, 3, -1, 7],
           [4, -2, 2, 4],
           [-2, 1, 2, -10]
         ]
solution=solve_linear_equations(matrix)
for i,s in enumerate(solution):
    print(f"X{i+1}= ",s)