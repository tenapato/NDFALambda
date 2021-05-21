# Authors
  ##### Commit version: 58aa459d509673a0d5ab4ab03a0a14fd0d14955e
  
- Patricio Tena Zozaya A01027293
- Francisco Acuña Franco A01027294
## About the program:
The following program evaluates a given string in and NDFA-lambda automata given by a text file and returns if the string
is accepted or rejected.

## Notes: 
- The string is not separated by commas
- Example Input: "bba" , "cbzpao"
- At the beginig of the program, all *.txt files will be displayed and you'll have to select the file to use by the index of it
- Print Glossary:
  - (TF) : Output of transition function
  - (LC) : Output of lambda closure
- More info about the versions of the program at: https://github.com/tenapato/NDFALambda


# Documentation
- Function for parsing the given text file:
> buildAutomata(file)
- Method for creating the dictionaries of the automatas with any kind of symbols:
> buildDictionary(Automata)
- Method that recives a set of states, applies lambda closure, and returns a set of states:
> lambdaClosure(states)
- Method that recieves a state, and a char, applies the transition function and retusn a state:
> transitionFunction(state, char)
- Recursive function that receives a state and retrurns a set of strings:
> extendedTransitionFunction(state, string)
- For more detailed information refer to the file main.py