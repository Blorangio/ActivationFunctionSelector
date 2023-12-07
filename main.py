storedCode = open("RNNCode.txt", "r")
codeFile = open("myAI.py", "w")
lines = storedCode.readlines()
# sigmoid - relu - elu - tanh
index = -1
epochCount = "5"
accuracy = 0


def next_activation(index_a):
    index_a += 1
    return "activationFunction["+str(index_a)+"]"

educatedGuess = input("Do you want educated guess (1) or brute force (0)")
if educatedGuess == "0":
    firstIteration = True
    functionCount = 0
    for i in lines:
        if firstIteration:
            codeFile.write("def callAI(activationFunction):\n")
            firstIteration = False

        functionCount += i.count("$a")
        codeFile.write("\t" + i.replace("$a", next_activation(index)).replace("$e", epochCount))
        firstIteration = False

    codeFile.write("\n\treturn accuracy")

    insertCode = open("insertCode.txt", "r")

    lines = insertCode.readlines()

    codeFile.write("\n\n\nfunctionCount = "+str(functionCount)+"\n")

    for i in lines:
        codeFile.write(i)

else:
    modelType = input("What is your model type MLP (0), CNN(1), RNN(2)")
    modelActivations = []
    if modelType == "0":
        print("MLP model")
        modelActivations = ['relu', 'elu']
    elif modelType == "1":
        print("CNN model")
        modelActivations = ['relu', 'tanh']
    elif modelType == "2":
        print("RNN model")
        modelActivations = ['tanh', 'sigmoid', 'elu']
    else:
        print("ERROR")
    if len(modelActivations) > 1:
        firstIteration = True
        for i in lines:
            if firstIteration:
                firstIteration = False
                codeFile.write("def callAI(activationFunction):\n")
            codeFile.write("\t" + i.replace("$a", "activationFunction").replace("$e", epochCount))
        codeFile.write("\n\treturn accuracy")
        codeFile.write("\n\nactivationAccuracy = []")
        for i in modelActivations:
            codeFile.write("\n\nactivationAccuracy.append(callAI('" + i +"'))")
        codeFile.write("\n\nprint(activationAccuracy)")
    else:
        print(modelActivations[0])


storedCode.close()
codeFile.close()

import myAI