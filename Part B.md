
1. Problem Statement: Finding the Average
    Given a set of numbers, how can we find their average?
    Example: Given the numbers [5, 8, 12, 4, 10], calculate the average.
Add them together and count the number of inputs
Divide the total by the no. of inputs
2. Develop pseudo code to solve the problem statement outlined in Step 1.
    Use descriptive variable names and comments to enhance readability and understanding.
<br>
Pseudocode: 
```
input <- [5, 8, 12, 4, 10]
count <- len(input)
total <- 0
for x in input do
    total <- x + total
average <- total / count
```
3. Write a Backus-Naur Form (BNF) grammar to describe the syntax of the problem statement.
4. Construct a parse tree based on the BNF grammar to visualize the syntactic structure of the problem.
5. Examine the parse tree constructed in Step 4 to determine if the BNF grammar is ambiguous.
    Identify any areas where multiple interpretations are possible.
    Provide examples or scenarios to illustrate potential ambiguities and their implications.
6. Rewrite the BNF grammar using Extended Backus-Naur Form (EBNF) to enhance readability and expressiveness.
    Explain the benefits of using EBNF over traditional BNF, particularly in terms of readability and clarity.
    Remove any ambiguity present in the BNF grammar through syntax modifications in the EBNF version.
7. Use the EBNF grammar to reconstruct a parse tree, demonstrating how the revised syntax resolves any ambiguities present in the original BNF grammar.
    Analyze and compare the parse trees from Steps 4 and 7 to understand the impact of syntax modifications on the parse tree structure.
