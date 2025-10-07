
1. Problem Statement: Finding the Average
    A. Given a set of numbers, how can we find their average?
    B. Example: Given the numbers [5, 8, 12, 4, 10], calculate the average.
Iterate over the input array "[5, 8, 12, 4, 10]"
Sum each value and count the total number of values
Divide the sum by the total number of values

2. Develop pseudo code to solve the problem statement outlined in Step 1.
    A. Use descriptive variable names and comments to enhance readability and understanding.
<br>
Pseudocode: 
```
input <- [5, 8, 12, 4, 10]
count <- 0
total <- 0
for x in input do
    count <- count + 1
    total <- total + x 
average <- total / count
```

3. Write a Backus-Naur Form (BNF) grammar to describe the syntax of the problem statement.
```
<program> ::= <statement_list>
<statement_list> ::= <statement> | <statement> <statement_list>
<statement> ::= <declaration> | <for_loop>
<declaration> ::= <identifier> "<-" <expression>
<for_loop> ::= "for" <identifier> "in" <identifer> "do" <stmts>
<identifier> ::= <letter> { <letter> }
<letter> ::= "a" | "b" .. "z" | "A" .. "Z"
<expression> ::= <number> | <identifier> | <expression> <operator> <expression> | <list>
<list> ::= "[" <number> { "," <number> } "]"
<operator> ::= "*" | "/" | "-" | "+"
<number> ::= <digit> { <digit> }
<digit> ::= "0" | "1" .. "8" | "9"
```

4. Construct a parse tree based on the BNF grammar to visualize the syntactic structure of the problem.
See Syntax tree.png

5. Examine the parse tree constructed in Step 4 to determine if the BNF grammar is ambiguous.
    A. Identify any areas where multiple interpretations are possible.
        Because this parse tree contains simple statements and expressions with no more than 1 operator, it isn't ambiguous anywhere
    B. Provide examples or scenarios to illustrate potential ambiguities and their implications.
        Grammar can be ambiguous when multiple different parse trees can be drawn from a string and no precedence is defined. For example: 1 + 3 / 2. This can either be interpreted as (1 + 3) / 2 or 1 + (3 / 2)

6. Rewrite the BNF grammar using Extended Backus-Naur Form (EBNF) to enhance readability and expressiveness.
    A. Explain the benefits of using EBNF over traditional BNF, particularly in terms of readability and clarity.
    B. Remove any ambiguity present in the BNF grammar through syntax modifications in the EBNF version.

7. Use the EBNF grammar to reconstruct a parse tree, demonstrating how the revised syntax resolves any ambiguities present in the original BNF grammar.
    A. Analyze and compare the parse trees from Steps 4 and 7 to understand the impact of syntax modifications on the parse tree structure.
