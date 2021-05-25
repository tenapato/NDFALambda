# Authors
  ##### Commit version: beca649ab670552cd0150c26e2d8adc091c666d1
  
- Patricio Tena Zozaya A01027293
- Francisco Acuña Franco A01027294
## About the program:
The following program evaluates a given string in and NDFA-lambda automata given by a text file and returns if the string
is accepted or rejected.

## Notes: 
- Programm will first ask if you want help: 

      Would you like help? (y/n)
      
    - If you enter "Yes (y)", then the menu will appear:

          Enter the index of the function you want know more about:
            0) Lambda Closure
            1) Transition Function
            2) Extended Transition Function
            3) Exit

            Index:
        > It will continue to display until you enter the exit option
    - If you enter "No (n)" or exit, the rest of the code will continue
- The string is not separated by commas
- Example Input:

      Enter the string to validate: bba
  


- At the beginig of the program, all *.txt files will be displayed and you'll have to select the file to use by the index of it

        Select file to use (*.txt): 
        0) test1.txt
        1) test2.txt

      Index of file: 0  
- Print Glossary:
  - (TF) : Output of transition function
  - (LC) : Output of lambda closure
- Final Sample Output:

      The string ['b', 'b', 'a'] is accepted
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
- For more detailed information refer to the file main.py and say yes to the help menu