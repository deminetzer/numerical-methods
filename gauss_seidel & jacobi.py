'''
    Program to solve linear systems of equations by Gauss-Seidel and Jacobi methods.
'''


# Part 1 - jacobi method :
def jacobiMethod(m,b,n,e):
    print("\n\n*** JACOBI METHOD ***\n")
    if not isDDM(m, n):
        return False
    f1 = lambda x, y, z: (b[0][0] - m[0][1]*y - m[0][2]*z) / m[0][0]
    f2 = lambda x, y, z: (b[1][0] - m[1][0]*x - m[1][2]*z) / m[1][1]
    f3 = lambda x, y, z: (b[2][0] - m[2][0]*x - m[2][1]*y) / m[2][2]

    # Initial setup
    x0 = 0
    y0 = 0
    z0 = 0
    count = 1

    # Implementation of Jacobi Iteration
    print('\nCount\tx\ty\tz\n')

    condition = True

    while condition:
        x1 = f1(x0, y0, z0)
        y1 = f2(x0, y0, z0)
        z1 = f3(x0, y0, z0)
        print('%d\t%0.4f\t%0.4f\t%0.4f\n' % (count, x1, y1, z1))
        e1 = abs(x0 - x1)
        e2 = abs(y0 - y1)
        e3 = abs(z0 - z1)

        count += 1
        x0 = x1
        y0 = y1
        z0 = z1

        condition = e1 > e and e2 > e and e3 > e

    print(f'\nSolution: a = {x1}, b ={y1} , c ={z1} \n')


# Part 2 - Gauss Seidel method:
def gauss_seidel(m,b,n,e):
    print("\n\n*** GAUSS SEIDEL METHOD ***\n")
    if not isDDM(m, n):
        return
    f1 = lambda x, y, z: (b[0][0] - m[0][1]*y - m[0][2]*z) / m[0][0]
    f2 = lambda x, y, z: (b[1][0] - m[1][0]*x - m[1][2]*z) / m[1][1]
    f3 = lambda x, y, z: (b[2][0] - m[2][0]*x - m[2][1]*y) / m[2][2]

    # Initial setup
    x0 = 0
    y0 = 0
    z0 = 0
    count = 1

    # Implementation of Gauss Seidel Iteration
    print('\nCount\tx\ty\tz\n')

    condition = True

    while condition:
        x1 = f1(x0, y0, z0)
        y1 = f2(x1, y0, z0)
        z1 = f3(x1, y1, z0)
        print('%d\t%0.4f\t%0.4f\t%0.4f\n' % (count, x1, y1, z1))
        e1 = abs(x0 - x1)
        e2 = abs(y0 - y1)
        e3 = abs(z0 - z1)

        count += 1
        x0 = x1
        y0 = y1
        z0 = z1

        condition = e1 > e and e2 > e and e3 > e

    print(f'\nSolution: a = {x1}, b ={y1} , c ={z1} \n')


# Check whether given matrix is Diagonally Dominant Matrix.
def isDDM(m, n):
    # for each row
    for i in range(0, n):

        # for each column, finding sum of each row.
        sum = 0
        for j in range(0, n):
            sum = sum + abs(m[i][j])

        # removing the diagonal element.
        sum = sum - abs(m[i][i])

        # checking if diagonal element is less than
        # sum of non-diagonal element.
        if (abs(m[i][i]) < sum):
            print("There is not a diagonally Dominant Matrix\n")
            return False

    return True


# Driver Code
size = 3
print("lets scan a 3x3 matrix, enter value after value")
matrix = []
for i in range(0, size):
    matrix.append([])
    for j in range(0, size):
        matrix[i].append(0)

for i in range(size):
    for j in range(size):
        matrix[i][j] = input()
        matrix[i][j] = float(matrix[i][j])

print("enter the b vector")
vectorb = []
for i in range(size):
    vectorb.append([0])
    vectorb[i][0] = (input())
    vectorb[i][0] = float(vectorb[i][0])


e = float(input('Enter tolerable error: '))

jacobiMethod(matrix,vectorb,size, e)
gauss_seidel(matrix,vectorb,size, e)


