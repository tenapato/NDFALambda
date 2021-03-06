'''
    Patricio Tena Zozaya A01027293
    Francisco Acuña Franco A01027294

    The following program evaluates a given string in and NDFA-lambda automata given by a text file and returns if the string
    is accepted or rejected.
    Input should be as follows: bba, abb, bcb, abzca 

    *Notes: 
    - The string is not separated by commas
    - At the beginig of the program, all *.txt files will be displayed and you'll have to select the file to use by the index of it
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
    """
    Method for parsing the given text file
    """
    
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
    
# Method for creating the dictionaries of the automatas with any kind of symbols
def buildDictionary(Automata):
    """
    Method for creating the dictionaries of the automatas with any kind of symbols
    """
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

    print("Symbols"  + str(Automata.symbols))
    
    
    for i in range(len(transitionMatrix)):
        #print("TM: " + str(transitionMatrix[i][1]) + " Symbols: " + str(j))
        if transitionMatrix[i][1]  == "lambda":
            test += [{"lambda": transitionMatrix[i][2]}]
        elif transitionMatrix[i][1] in Automata.symbols:
            test += [{transitionMatrix[i][1]: transitionMatrix[i][2]}]
            #print(transitionMatrix[i][1])


    zip_it = zip(comparar, test)

    dictAutomata = dict(zip_it)

    #print(dictAutomata)
    repetidos = []


    repetidos = [x for n, x in enumerate(comparar) if x in comparar[:n]]  #find any state that has more than one transition and add the to a string
    # Compares if any string that is al ready in th dictionary has more than 1 returning state, if so, it adds the missing states to the dictionary
    for r in repetidos:
        for rep in range(len(transitionMatrix)):
            if r == transitionMatrix[rep][0]:
                dictAutomata[r][transitionMatrix[rep][1]] = transitionMatrix[rep][2] 

    return dictAutomata

def lambdaClosure(states):  
    """
    Method that recives a set of states, applies lambda closure, and returns a set of states
    
    args:
        states([String]): Check lambda closure four each recieved state
    
    return:
        list of lambda closure for each states
    """
    
    returnStates = []
    if states is not None:
        for state in states:
            if dictAutomata.get(state, {}).get("lambda"):
                returnStates += dictAutomata.get(state, {}).get("lambda")
            if state not in returnStates:
                returnStates.append(state)
        print("(LC) Lambda closure of: " + str(states) + " returns: " + str(returnStates))
        
    return returnStates

def transitionFunction(state, char): 
    """
    Method that recieves a state, and a char, applies the transition function and returns a state
    
    args:
        state(string): State used as a key value in the automata dictionary
        char(string): Letter of the given string used as key value in the automata dictionary
    
    return:
        the state of applying the transition fucntion as a string
    """
    
    temp = dictAutomata.get(state, {}).get(char)
    if temp:
        print("(TF) State: " + str(state) + " with char "+ "'"+ str(char) +"'"+ " returns: " + str(dictAutomata.get(state, {}).get(char)))
        #temp2 = dictAutomata.get(state, {}).get(char)
        return (dictAutomata.get(state, {}).get(char))
    
def extendedTransitionFunction(state, string): # 
    """
    Recursive function that receives a state and retrurns a set of strings
    
    args:
        state(string): Initial state used as a key value for the transition function
        string(string): String to validate in the given automata
    
    return:
        A set of states
    """
    if len(string) == 0:  # Base case
        res = lambdaClosure(state)
        return res
    else:
        # Cut string
        print("String: " + str(string))
        temp = string[-1]
        string.pop(len(string)-1)
        print("String after cut: " + str(string))
        var = extendedTransitionFunction(state, string)

        res = []
        if var is not None:
            for v in var:
                var2 = transitionFunction(v, temp)
                res += lambdaClosure(var2)  
            
        return res


def help():
    
    while True:
        print("Enter the index of the function you want know more about:")
        print("0) Lambda Closure")
        print("1) Transition Function")
        print("2) Extended Transition Function")
        print("3) Exit\n")
        index = int(input("Index: "))
        
        
        if(index) == 0:
            print(lambdaClosure.__doc__)
        if(index) == 1:
            print(transitionFunction.__doc__)
        if(index) == 2:
            print(extendedTransitionFunction.__doc__)
        if(index) == 3:
            return False



if __name__ == "__main__":


    op = input("Would you like help? (y/n) ")
    
    if op == "y":
        help()

    print("Select file to use (*.txt): " )
    files = glob.glob("./automataFiles/*.txt")  # Fetches all .txt files from the local directory
    i = 1

    #print("0) Help")

    for f in files:  # Display each txt file as a menu 
        print(str(i) + ") " + str(f[16:]))
        i+=1
    
    
    selectedFile = int(input("Index of file: "))
    
    Automata = buildAutomata(files[selectedFile-1]) #Method that receives the name of the file to use and returns an Automata class

    dictAutomata = buildDictionary(Automata) #Method that receives an Automata class and turns it into a dictionary of dictionaries
    
    print("Dictionary" + str(dictAutomata))
    string = input("Enter the string to validate: ")
    stringToSend = []
    for s in string:
        stringToSend.append(s)

    string2 = []
    for s in string:
        string2.append(s)

    ans = extendedTransitionFunction(Automata.initialState, stringToSend) # Calling the Recursive Extended Transition Function

    print("Final returning states: " + str(ans))
    if ans is not None:
        if any (x in ans for x in Automata.finalState):
                print("The string "+ str(string2) +" is accepted")
                
        else:
            print("The string "+ str(string2) +" is rejected")
    
    
