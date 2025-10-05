from analyzer import LexicalAnalyzer

def run_test(analyzer, code, expected):
	result = analyzer.lex(code)
	assert result == expected, f"Failed:\nInput: {code}\nExpected: {expected}\nGot: {result}"

analyzer = LexicalAnalyzer()

test_cases = {
	"Basic math and assignment": (
		"x <- 5 + 3 * y - 2 / z",
		[
			('IDENT', 'x'),
			('ASSIGN', '<-'),
			('NUMBER', '5'),
			('PLUS', '+'),
			('NUMBER', '3'),
			('TIMES', '*'),
			('IDENT', 'y'),
			('MINUS', '-'),
			('NUMBER', '2'),
			('DIVIDE', '/'),
			('IDENT', 'z'),
		]
	),
	"Relational operators": (
		"a <= b >= c < d > e",
		[
			('IDENT', 'a'),
			('LEQ', '<='),
			('IDENT', 'b'),
			('GEQ', '>='),
			('IDENT', 'c'),
			('LESS', '<'),
			('IDENT', 'd'),
			('GREATER', '>'),
			('IDENT', 'e'),
		]
	),
	"IS, IS NOT, and ISNOT": (
		"x IS NOT y\nx IS y\nx ISNOT y",
		[
			('IDENT', 'x'),
			('INEQUAL', 'IS NOT'),
			('IDENT', 'y'),
			('NEWLINE', '\n'),
			('IDENT', 'x'),
			('EQUAL', 'IS'),
			('IDENT', 'y'),
			('NEWLINE', '\n'),
			('IDENT', 'x'),
			('IDENT', 'ISNOT'),
			('IDENT', 'y'),
		]
	),
	"Keywords and identifiers": (
		"for item in list do while loop if iffy",
		[
			('KEYWORD', 'for'),
			('IDENT', 'item'),
			('KEYWORD', 'in'),
			('IDENT', 'list'),
			('KEYWORD', 'do'),
			('KEYWORD', 'while'),
			('IDENT', 'loop'),
			('KEYWORD', 'if'),
			('IDENT', 'iffy'),
		]
	),
	"Boolean literals and assignment": (
		"flag <- TRUE\nother <- FALSE",
		[
			('IDENT', 'flag'),
			('ASSIGN', '<-'),
			('TRUE', 'TRUE'),
			('NEWLINE', '\n'),
			('IDENT', 'other'),
			('ASSIGN', '<-'),
			('FALSE', 'FALSE'),
		]
	),
	"Tabs and indentation": (
		"if condition\n\tx <- 1",
		[
			('KEYWORD', 'if'),
			('IDENT', 'condition'),
			('NEWLINE', '\n'),
			('TAB', '\t'),
			('IDENT', 'x'),
			('ASSIGN', '<-'),
			('NUMBER', '1'),
		]
	),
	"Brackets and comma": (
		"[a, b, c]",
		[
			('LBRACKET', '['),
			('IDENT', 'a'),
			('COMMA', ','),
			('IDENT', 'b'),
			('COMMA', ','),
			('IDENT', 'c'),
			('RBRACKET', ']'),
		]
	),
	"Whitespace ignored": (
		"x    <-    42",
		[
			('IDENT', 'x'),
			('ASSIGN', '<-'),
			('NUMBER', '42'),
		]
	),
	"Mismatched characters": (
		"x <- 5 $", "Unexpected character: '$'"
	),
}

for name, (code,expected) in test_cases.items():
	print(f"Running test: {name}")
	result = run_test(analyzer, code, expected)
	print("Test passed")

