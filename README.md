## Lexical Analyzer

This program is a lexical analyzer designed to parse the following pseudocode:
```
input <- [5, 8, 12, 4, 10]
count <- 0
total <- 0
for x in input do
    count <- count + 1
    total <- total + x 
average <- total / count
```
It uses the UI library [Tkinter](https://docs.python.org/3/library/tkinter.html) which should be available by default on Windows, but might need to be installed manually on Macos and Linux. 
### Usage
Interactive ui with: ```python ui.py``` or commandline tests with: ```python tests.py```