"""
Please make note of the following rule to work out limiting matrix for absorbing markov chains:

If a standard form P for an absorbing Markov chain in partitioned as:

P = [ I  0 ]
    [ R  Q ] (a standard form)

then P^k approaches a limiting matrix J as k increases, where

J = [ I  0 ]
    [ FR 0 ]  and F = (I - Q)^-1

F is called the fundamental matrix for P
"""
import math

def solution(m):

    m = probability_converter(m)

    r_matrix = find_r_matrix(m)
    
    q_matrix = find_q_matrix(m)

    f_matrix = inverse(identity_minus_matrix(q_matrix))

    FR_matrix = matrix_multiplication(f_matrix, r_matrix) # The answer is the first row of the FR_matrix

    answer = correct_format(m, FR_matrix)

    return answer

def find_r_matrix(m):

    r_matrix = []
    for x in range(len(m)):
        if states_reachable(m)[x] and not states_terminal(m)[x]:
            row = []
            for y in range(len(m)):
                if states_reachable(m)[y] and states_terminal(m)[y]:
                    row.append(m[x][y])
            r_matrix.append(row)
        
    return r_matrix

def find_q_matrix(m):

    q_matrix = []
    for x in range(len(m)):
        if states_reachable(m)[x] and not states_terminal(m)[x]:
            row = []
            for y in range(len(m)):
                if states_reachable(m)[y] and not states_terminal(m)[y]:
                    row.append(m[x][y])
            q_matrix.append(row)

    return q_matrix

def determinant (m):
    
    answer = 0
    if len(m) == 2:
        answer = m[0][0]*m[1][1] - m[0][1]*m[1][0]
        return answer
    else:
        negative = -1
        for x in range(len(m[0])):
            smaller_matrix = smaller_determinate_matrix(m, 0, x)
            negative = negative * -1
            answer = answer + negative * m[0][x] * determinant(smaller_matrix)
    
    return answer

def smaller_determinate_matrix(m, row, col):
    
    new_matrix = []
    for x in range(len(m)):
        if x == row:
            continue
        else:
            matrix_row = []
            for y in range(len(m[x])):
                if y == col:
                    continue
                else:
                    matrix_row.append(m[x][y])
        new_matrix.append(matrix_row)
    
    return new_matrix

def states_reachable(m):

    states_reachable = [False] * len(m)

    states_reachable[0] = True

    for i in range(len(m)):
        if states_reachable[i]:
            for j in range(len(m[i])):
                if m[i][j] > 0:
                    states_reachable[j] = True
    
    return states_reachable

def states_terminal(m):

    terminal = [True] * len(m)

    for i in range(len(m)):
        for j in range(len(m[i])):
            if (m[i][j] > 0 and i != j):
                terminal[i] = False
                break
    
    return terminal

def probability_converter(m):

    for x in range(len(m)):
        total = row_total(m, x)
        if total > 0:
            for y in range(len(m[x])):
                m[x][y] = m[x][y] / total
    return m

def row_total (m, row_number):

    total = 0
    for value in m[row_number]:
        total = total + value
    return total

def matrix_of_minors (m):

    matrix_minors = []
    for x in range(len(m)):
        matrix_row = []
        for y in range(len(m[x])):
            minor = determinant(smaller_determinate_matrix(m,x,y))
            matrix_row.append(minor)
        matrix_minors.append(matrix_row)

    return matrix_minors

def matrix_of_cofactors (m):

    negative = -1
    for x in range(len(m)):
        negative = math.pow(-1,x)
        for y in range(len(m[x])):
            m[x][y] = m[x][y]*negative
            negative = negative * -1

    return m

def transpose (m):

    copy_matrix = []
    for x in range(len(m)):
        copy_matrix_row = []
        for y in range(len(m[x])):
            copy_matrix_row.append(m[y][x])
        copy_matrix.append(copy_matrix_row)

    return copy_matrix

def matrix_multiplication (m ,n):

    answer = []

    for x in range(len(m)):
        answer_row = []
        for y in range(len(n[0])):
            total = 0
            for z in range(len(n)):
                total += m[x][z] * n[z][y]
            answer_row.append(total)
        answer.append(answer_row)

    return answer

def identity_minus_matrix (m):

    for x in range(len(m)):
        for y in range(len(m[0])):
            if x == y:
                m[x][y] = 1 - m[x][y]
            else:
                m[x][y] = 0 - m[x][y]

    return m

def matrix_multiplication_by_constant(m, constant):

    for x in range(len(m)):
        for y in range(len(m[0])):
            m[x][y] = m[x][y] * constant

    return m

def inverse (m):
    
    new_matrix = []
    if len(m) == 2:
        new_matrix_row = []
        new_matrix_row.append(m[1][1])
        new_matrix_row.append(-m[0][1])
        new_matrix.append(new_matrix_row)
        new_matrix_row = []
        new_matrix_row.append(-m[1][0])
        new_matrix_row.append(m[0][0])
        new_matrix.append(new_matrix_row)
    else:
        minors = matrix_of_minors(m)
        cofactors = matrix_of_cofactors(minors)
        new_matrix = transpose(cofactors)

    determinant_of_m = determinant(m)
    answer = matrix_multiplication_by_constant(new_matrix, 1/determinant_of_m)

    return answer

def correct_format(m, FR_matrix): # Method to return answer in correct format

    numerators = []  
    i = 0
    for x in range(len(m)):
        if states_terminal(m)[x] and not states_reachable(m)[x]:
            numerators.append(0)
        if states_terminal(m)[x] and states_reachable(m)[x]:
            numerators.append(FR_matrix[0][i])
            i += 1
     
    denomenators = []
    for num in numerators:
        if (num == 0):
            denomenators.append(1)
        else:
            multiplier = 2
            while True:
                newNum = num * multiplier
                if (round(newNum,4) - round(newNum,0) == 0):
                    denomenators.append(multiplier)
                    break
                multiplier += 1
                newNum = 1

    lcm_denomenator = 1
    for i in range(1,len(denomenators)):
        lcm_denomenator = lcm(denomenators[i-1],denomenators[i])
        
    answer = []
    for num in numerators:
        answer.append(round(num*lcm_denomenator))
    
    answer.append(lcm_denomenator)

    return answer

def lcm(a,b):

    if a > b:
        greater = a
    else:
        greater = b
    
    while True:
        if((greater % a == 0) and (greater % b == 0)):
            lcm = greater
            break
        greater += 1
    
    return lcm

answer1 = solution([[0, 2, 1, 0, 0], [0, 0, 0, 3, 4], [0, 0, 0, 0, 0], [0, 0, 0, 0,0], [0, 0, 0, 0, 0]])
answer2 = solution([[0, 1, 0, 0, 0, 1], [4, 0, 0, 3, 2, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]])

print(answer1)
print(answer2)