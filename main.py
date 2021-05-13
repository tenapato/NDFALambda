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


# For documentation refer to line 192
def transitionFunctionMala(state, string):
    print("State to check: "+ str(state))
    #print("Current string to check: "+ str(string))

    if string:
        letter = string[0]



        print("Using letter: " + str(letter))
        if len(state)>1: #This if is accessed if the list of states to validate is more than one
            estado = str(state[0]).strip("'[]'")
            for key, values in dictAutomata.get(estado, {}).items():
               print("")
            if estado in dictAutomata: # compares if the given state has a valid transition in the transition table
                l = dictAutomata.get(estado, {}).get("lambda") # if it does, it adds the value to a new variiable to return
                a = dictAutomata.get(estado, {}).get("a")
                b = dictAutomata.get(estado, {}).get("b")
                #print("Lambda: " + str(l) + " a: " + str(a) + " b: " + str(b))
                if l and key == letter and not a and not b: # this set of ifs ensures that the returning state is the one corresponding to the letter being evaluated
                    estadoTemp = l
                    state.pop(0)
                    state += estadoTemp
                    string.pop(0)
                    transitionFunction(state, string)
                elif a and key == letter and not l and not b:
                    estadoTemp = a
                    state.pop(0)
                    state += estadoTemp
                    string.pop(0)
                    transitionFunction(state, string)
                elif b and key == letter and not l and not a:
                    estadoTemp = b
                    state.pop(0)
                    string.pop(0)
                    state += estadoTemp
                    transitionFunction(state, string)
                else:  # if it doesnt find a valid state, then it removes the state from the states to validate and returns the next state and the same letter
                    print("No se encontro una transicion con este estado, sacando " + str(state[0]))
                    if len(state)<1:
                        string.pop(0)
                    state.pop(0)
                    transitionFunction(state, string)
                
        else: #if the state to validate is only one, then it enters the same logic as stated above
            estado = str(state).strip("'[]'")
            for key, values in dictAutomata.get(estado, {}).items():
                   print("")     

            if estado in dictAutomata:
                l = dictAutomata.get(estado, {}).get("lambda")
                a = dictAutomata.get(estado, {}).get("a")
                b = dictAutomata.get(estado, {}).get("b")
                if l and key == letter:
                    string.pop(0)
                    transitionFunction(l, string)
                elif a and key == letter:
                    string.pop(0)
                    transitionFunction(a, string)
                elif b and key == letter:
                    string.pop(0)
                    transitionFunction(b, string)
                else:
                    print("No se encontro una transicion con este estado, sacando " + str(state[0]))
                    string.pop(0)
                    state.pop(0)
                    transitionFunction(state, string)
    else:
        print("Ya no hay más letras que validar")
        #print(Automata.finalState)
        if any (x in state for x in Automata.finalState): #if any the states when there are no more letter to validate is final, the the string is accepted
            print("El string se acepta")
        else: # else, the string is rejected
            print("El string se rechaza")


def lambdaClosure(states):
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


def transitionFunction(state, char):
    #print(dictAutomata.get(state, {}).get(char))
    temp = dictAutomata.get(state, {}).get(char)
    if temp:
        print("State: " + str(state) + " with char "+ str(char) + " returns: " + str(dictAutomata.get(state, {}).get(char)))
        return (dictAutomata.get(state, {}).get(char))
    


def extendedTransitionFunction(state, string):
    list = lambdaClosure(state)
    tempStates = []
    print(list)
    
    for s in list:
        transitionFunction(s, 'b')
    


if __name__ == "__main__":
    
    Automata = buildAutomata('test1.txt') #Method that receives the name of the file to use and returns an Automata class
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


# This function receives the following values = transitionFunction(State, ['string'] )
# State in this case is the initial state for the automata accessed by calling the attribute from the class : Automata.initialState
# The second atribute is a list of the string to validate, starting with lamba and separated by commas : ['lambda', 'a','b'...,]
#transitionFunction(Automata.initialState, ['lambda', 'b', 'b', 'a'])


print("Initial State: " + str(Automata.initialState))
print("Final States: " + str(Automata.finalState))

print("Dictionary: " +str(dictAutomata))

#lambdaClosure(Automata.initialState)
#lambdaClosure(['q0', 'q3'])

#print(transitionFunction('q4', 'a'))

extendedTransitionFunction(Automata.initialState, 'b, b, a')
    
