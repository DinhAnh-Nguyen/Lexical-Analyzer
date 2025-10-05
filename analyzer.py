import re
from typing import Union, List, Tuple

class LexicalAnalyzer:
  def __init__(self):
    # define regex rules for parsing
    self.tokens = [
      ('NUMBER',     r'\d+'), # a number of 1 or greater length
      ('ASSIGN',     r'<-'),
      ('LBRACKET',   r'\['),
      ('RBRACKET',   r'\]'),
      ('PLUS',       r'\+'),
      ('MINUS',      r'-'),
      ('TIMES',      r'\*'),
      ('DIVIDE',     r'/'),
      ('LEQ',        r'<='),
      ('GEQ',        r'>='),
      ('LESS',       r'<'),
      ('GREATER',    r'>'),
      ('INEQUAL',    r'\bIS\s+NOT\b'),
      ('EQUAL',      r'\bIS\b'),
      ('TRUE',       r'\bTRUE\b'),
      ('FALSE',      r'\bFALSE\b'),
      ('NEWLINE',    r'\n'),
      ('COMMA',      r','),
      ('KEYWORD',    r'\b(for|in|do|while|if)\b'), # match any defined keyword
      ('IDENT',      r'[A-Za-z_]\w*'), #any string identifier
      ('TAB',        r'\t'), #tabs are significant in language that doesnt use brackets for blocks
      ('WHITESPACE', r'\s+'), #whitespaces are matched but skipped in the end
      ('MISMATCH',   r'.') # anything that didnt match is a syntax error
    ]
    #join the regex rules into a single regex pattern
    self.regex = re.compile(
      '|'.join(f'(?P<{name}>{pattern})' for name, pattern in self.tokens)
    )

  #this function takes in a string of code and returns a list of tuples
  def lex(self, code: str) -> Union[str, List[Tuple[str, str]]]:
    tokens = []
    pos = 0

    #iterate through input string
    while pos < len(code):
      #try to match it against regex
      match = self.regex.match(code, pos)
      if not match:
        return f'Unexpected character at position {pos}'
      kind = match.lastgroup
      value = match.group()
      
      if kind == 'MISMATCH':
        return f'Unexpected character: {value!r}'
      # whitespaces arent syntactically significant but theyre matched anyways so that they dont cause MISMATCH
      elif kind == 'WHITESPACE':
        pass
      else:
        #if it matched, append it to the result array
        tokens.append((kind, value))
      #move the position forward
      pos = match.end()
    return tokens

