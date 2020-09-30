iterationMatrix = [
    [1, 1],
    [1, 0]
]
finalMatrix = [
    [1, 1],
    [1, 0]
]
def multiplyMatrix(m1, m2):
    finalMatrix = [[0, 0], [0, 0]]
    for x in range(0, 2):
        for y in range(0, 2):
            total = 0
            for z in range(0, 2):
                total += m1[x][z] * m2[z][y]
            finalMatrix[x][y] = total
    return finalMatrix
bit = 1
print("Please enter the index of the fibonacci number you're finding")
index = int(input())
while bit <= index:
    if bit & index:
        finalMatrix = multiplyMatrix(iterationMatrix, finalMatrix)
    bit *= 2
    iterationMatrix = multiplyMatrix(iterationMatrix, iterationMatrix)
print(finalMatrix[1][1])
