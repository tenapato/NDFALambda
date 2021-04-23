class Automata:
    states = []
    symbols = []
    initialState = ""
    finalState = []
    transitionTable = []


def buildAutomata(file):
    with open(file) as f:
            lines = f.readlines();

    A1 = Automata()

    count = 0
    for line in lines:
        count += 1
        #print(f'line {count}: {line}')

    #print("Total de lineas: " + str(count))

    #separating each state and adding it to an array
    states = lines[0].split(",")
    states = ','.join(states).strip()
    states = states.split(",")

    #print(transitionTable)
    A1.states = states
    #print("States: " + str(states))

    A1.states = states

    #Separate alphabet symbols
    symbols = lines[1].split(",")
    #print("Symbols: " + str(symbols))
    symbols = ','.join(symbols).strip()
    symbols = symbols.split(",")
    A1.symbols = symbols

    #Assign inital state
    initialState = lines[2].split(",")
    initialState = ''.join(initialState).strip()
    initialState = initialState.split(",")
    #print("Initial State: " + str(initialState))
    A1.initialState =  initialState


    #Assign final state
    finalState = lines[3].split(",")
    #print("Final State: " + str(finalState))
    finalState = ','.join(finalState).strip()
    finalState = finalState.split(",")
    #print("Final state 2: " + str(finalState))

    A1.finalState = finalState;

    #for i in range(8):
    #    print(lines[i+4])

    #Create the transition
    transitionTable = []

    for j in range(count):
        #print(j)
        if j > 3:
            transitionTable += lines[j].split('\n')

    while("" in transitionTable):
        transitionTable.remove("")

    sizeOfTT = len(transitionTable) #Save the size of the transition table to a variable
    #print(transitionTable)
    A1.transitionTable = transitionTable

    return A1



def transitionFunction(state, string):
    print("State to check: "+ str(state))
    string = string.split(",")
    print("String: "+ str(string))
    letter = string[0]
    print("Leter: " + str(letter))
    estado = str(state).strip("'[]'")
    #print(estado)
    if string:
        if estado in dictAutomata:
            l = dictAutomata.get(estado, {}).get("lambda")
            a = dictAutomata.get(estado, {}).get("a")
            b = dictAutomata.get(estado, {}).get("b")
            print("Lambda: " + str(l) + " a: " + str(a) + " b: " + str(b))
            if l:
                string.pop(0)
                transitionFunction(l, letter)


if __name__ == "__main__":
    
    Automata = buildAutomata('test1.txt') #Method that receives the name of the file to use and returns an Automata class
    #print(Automata.states)
    #print(Automata.symbols)
    #print(Automata.initialState)
    #print(Automata.finalState)
    #print(Automata.transitionTable)
    p = str(Automata.states)
    #print(p)

    # ---------- Create the automate dictionary ----------- #
    transitionMatrix = []
    comparar = []
    count = 0
    #print("Los strings son iguales")
    for i in Automata.transitionTable:
        var1, var2 = Automata.transitionTable[count].split("=>")
        #var1 = "".join(var1)
        #var1.strip("=")
        nextState = var2.split(",")
        #print("Var1: " + str(var1))
        state, symbol = var1.split(",")
        #print(count)
        #print("State: "+ str(state)+ " Symbol: "+ str(symbol) + " Regresa:" + str(nextState))
        transitionMatrix += [[state, symbol, nextState]]
        comparar += [state]
        count+=1

    test = []
    print("----- Transition Matrix---------")
    print(transitionMatrix)


    print("------Dictionary 1 --------- ")
    for i in range(len(transitionMatrix)):
        if transitionMatrix[i][1] == "lambda":
            test += [{"a": 0, "b": 0, "lambda": transitionMatrix[i][2]}]
        elif transitionMatrix[i][1] == "b":
            test += [{"b": transitionMatrix[i][2]}]
        elif transitionMatrix[i][1] == "a":
            test += [{"a": transitionMatrix[i][2]}]


    zip_it = zip(comparar, test)

    dictAutomata = dict(zip_it)

    repetidos = []
    
    print(dictAutomata)
    
    repetidos = [x for n, x in enumerate(comparar) if x in comparar[:n]]  #find any state that has more than one transition
   

    for r in repetidos:
        for rep in range(len(transitionMatrix)):
            if r == transitionMatrix[rep][0]:
                dictAutomata[r][transitionMatrix[rep][1]] = transitionMatrix[rep][2]    
print("------Dictionary 2 --------- ")
print(dictAutomata)


transitionFunction(Automata.initialState, 'b,b,a')

    
