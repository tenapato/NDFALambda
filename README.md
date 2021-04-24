# Authors
  ##### Commit version: 691efbb3c087d1aeed6648959fcfe440db93f22c
  
- Patricio Tena Zozaya A01027293
- Francisco Acuña Franco A01027294
## About the program:
The following program evaluates a given string in and NDFA-lambda automata given by a text file and returns if the string
is accepted or rejected.

## Notes: 
- To this version of the program, it only evaluates a normal NDFA automata.
- Further changes are needed to implement the lambda closure and fix remaning bugs
- More info about the versions of the program at: https://github.com/tenapato/NDFALambda


# Documentation
- Function for parsing the given text file
> buildAutomata(file)
- Function for validating strings:
> transitionFunction(state, string)
- For more detailed information refer to the file main.py