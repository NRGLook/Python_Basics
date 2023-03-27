# Task 1: Calculate statistics of the text.
You are given a text as an input (or you can read it from file).
## Calculate:
a) amount of sentences in the text;    
b) amount of non-declarative sentences in the text;     
c) average length of the sentence in characters (words count only);      
d) average length of the word in the text in characters;     
e) top-K repeated N-grams in the text (K and N are taken from input if needed; by default K=10, N=4). 
## Input: 
 Text of letters, numbers and separators. 
 Only Latin letters and numbers must be processed.    
 Only numbers (‘123’) is not a word, combination of letters and numbers (‘a1b2c3’) is a word.       
 Abbreviations may appear in the input and must also be processed (check  here)     
 Declarative sentence is a sentence ending with ‘.’ or ‘...’ separators.      

 Each helper function or a function that calculates something must be covered with tests including extreme values. You can use any test lib (pytest, unittest). 
	Use dict() and string operations to complete the task in the easiest way.

# Task 2: Create a container of unique elements.
Create an interactive CLI program which is going to play the role of a storage for unique elements and support a list of the following comands...
## Commands:    
a) add <key> [key, …] – add one or more elements to the container (if the element is already in there then don’t add);      
b) remove <key> – delete key from container;      
c) find <key> [key, …] – check if the element is presented in the container, print each found or “No such elements” if nothing is;      
d) list – print all elements of container;    
e) grep <regex> – check the value in the container by regular expression, print each found or “No such elements” if nothing is;   
f) save/load – save container to file/load container from file;   
g) switch – switches to another user.   

## User-flow: 
 Input username to CLI, the program then loads a container connected to the user if presented.    
 Then the program works in interactive mode: I can enter each command as much as I want.    
 Switching to another user must be possible without stopping the program.     
 Before the program stops or the user is switched there must be an offer to save the container.    
 When the user is chosen there must be an offer to load the container.    
 If the user wants to load the container in the middle of the session – active and loaded containers must be concatenated.    

 Implementation can be only class-based. 
Use set() as the main container here and another collection for associating the container with the user. Remember about values that can be kept in a set.
