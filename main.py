'''
    Patricio Tena Zozaya A01027293
    Francisco Acuña Franco A01027294

    The following program evaluates a given string in and NDFA-lambda automata given by a text file and returns if the string
    is accepted or rejected.

    *Notes: 
    - To this version of the program, it only evaluates a normal NDFA automata.
    - Further changes are needed to implement the lambda closure and fix remaning bugs
    - more info about the versions of the program at: https://github.com/tenapato/NDFALambda

'''

from os import listdir
from os.path import join, isfile
import glob
# Automata class for saving the information extacted from the text file


class Automata:
    states = []
    symbols = []
    initialState = ""
    finalState = []
    transitionTable = []

# Method for parsing the given text file
def buildAutomata(file):
    with open(file) as f:
            lines = f.readlines();

    A1 = Automata()

    count = 0
    for line in lines:
        count += 1


    #separating each state and adding it to an array
    states = lines[0].split(",")
    states = ','.join(states).strip()
    states = states.split(",")

    A1.states = states

    A1.states = states

    #Separate alphabet symbols
    symbols = lines[1].split(",")
    symbols = ','.join(symbols).strip()
    symbols = symbols.split(",")
    A1.symbols = symbols

    #Assign inital state
    initialState = lines[2].split(",")
    initialState = ''.join(initialState).strip()
    initialState = initialState.split(",")
    A1.initialState =  initialState


    #Assign final state
    finalState = lines[3].split(",")
    finalState = ','.join(finalState).strip()
    finalState = finalState.split(",")

    A1.finalState = finalState;


    #Create the transition
    transitionTable = []

    for j in range(count):
        #print(j)
        if j > 3:
            transitionTable += lines[j].split('\n')

    while("" in transitionTable):
        transitionTable.remove("")

    sizeOfTT = len(transitionTable) #Save the size of the transition table to a variable
    A1.transitionTable = transitionTable

    return A1

def buildDictionary(Automata):
    p = str(Automata.states)
    # ---------- Create the automate dictionary ----------- #
    transitionMatrix = []
    comparar = []
    count = 0
    for i in Automata.transitionTable:
        var1, var2 = Automata.transitionTable[count].split("=>")
        nextState = var2.split(",")
        state, symbol = var1.split(",")
        transitionMatrix += [[state, symbol, nextState]]
        comparar += [state]
        count+=1

    test = []
    #print("----- Transition Matrix---------")
    #print(transitionMatrix)


    #print("------Dictionary 1 --------- ")
    for i in range(len(transitionMatrix)):
        if transitionMatrix[i][1] == "lambda":
            test += [{"lambda": transitionMatrix[i][2]}]
        elif transitionMatrix[i][1] == "b":
            test += [{"b": transitionMatrix[i][2]}]
        elif transitionMatrix[i][1] == "a":
            test += [{"a": transitionMatrix[i][2]}]


    zip_it = zip(comparar, test)

    dictAutomata = dict(zip_it)

    repetidos = []


    repetidos = [x for n, x in enumerate(comparar) if x in comparar[:n]]  #find any state that has more than one transition and add the to a string
    # Compares if any string that is al ready in th dictionary has more than 1 returning state, if so, it adds the missing states to the dictionary
    for r in repetidos:
        for rep in range(len(transitionMatrix)):
            if r == transitionMatrix[rep][0]:
                dictAutomata[r][transitionMatrix[rep][1]] = transitionMatrix[rep][2] 

    return dictAutomata


def lambdaClosure(states):  #Method that recives a set of states, applies lambda closure, and returns a set of states
    #print(dictAutomata.get(states[0], {}).get("lambda"))
    returnStates = []
    for state in states:
        if dictAutomata.get(state, {}).get("lambda"):
            returnStates += dictAutomata.get(state, {}).get("lambda")
        if state not in returnStates:
            returnStates.append(state)

    #print(returnStates)
    print("Lambda closure of: " + str(states) + " returns: " + str(returnStates))
    return returnStates

def transitionFunction(state, char): #Method that recieves a state, and a char, applies the transition function and retusn a state
    #print(dictAutomata.get(state, {}).get(char))
    temp = dictAutomata.get(state, {}).get(char)
    if temp:
        print("State: " + str(state) + " with char "+ str(char) + " returns: " + str(dictAutomata.get(state, {}).get(char)))
        return (dictAutomata.get(state, {}).get(char))
    
def extendedTransitionFunction(state, string): 
    
    if len(string) > 0:
        list = lambdaClosure(state)
        tempStates = []
        
        #print(list)
        #list = ["q4", "q3"]
        #print(list)
        print("String: " +str(string))
        char = string[0]
        for s in list:
            temp = transitionFunction(s, char)
            if temp:
                tempStates+= temp
        #print(tempStates)
        lambdaClosure(tempStates)
        string.pop(0)
        #print(string)
        extendedTransitionFunction(tempStates, string)
    else:
        #print("Se acabo de checar el string")
        if any (x in state for x in Automata.finalState):
            print("El string se acepta")
        else:
            print("El string se rechaza")

if __name__ == "__main__":

    print("Select file to use (*.txt): " )
    files = glob.glob("*.txt")
    #print(files)
    i = 0
    for f in files:
        print(str(i) + ") " + str(f))
        i+=1
    selectedFile = int(input())

    Automata = buildAutomata(files[selectedFile]) #Method that receives the name of the file to use and returns an Automata class

    dictAutomata = buildDictionary(Automata) #Method that receives an Automata class and turns it into a dictionary of dictionaries

    string = input("Enter the string to validate, separated by commas: ")

    string = string.split(",")

    extendedTransitionFunction(Automata.initialState, string)
    
