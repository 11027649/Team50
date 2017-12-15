numberArray = []

def recursieveFunctie(value):
    if value == 1:
        for i in range(6):
            numberArray[value - 1] = i
            print(list(reversed(numberArray)))
    else:

        for i in range(6):
            numberArray[value - 1] = i
            recursieveFunctie(value - 1)


len = 10


for i in range (len - 2):
    numberArray.append(0)

iterations = pow(6, len - 2)

for i in range (len - 2):
    iterations = (int) (iterations - (2 / 3) * pow(6, i + 1))

print(iterations)

for i in range(1, len - 2):

    numberArray = []
    for j in range (len - 2):
        numberArray.append(0)

    numberArray[i] = 1

    recursieveFunctie(i)


print("done")
