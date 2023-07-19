import re
import pandas as pd

class all_elements:
    keywords = set(['auto', 'break', 'case', 'char', 'const', 'continue', 'default',
                    'do', 'double', 'else', 'enum', 'extern', 'float', 'for', 'goto',
                    'if', 'int', 'long', 'register', 'return', 'short', 'signed', 'sizeof',
                    'static', 'struct', 'switch', 'typedef', 'union', 'unsigned', 'void',
                    'volatile', 'while'])

    identifiers = set()
    operators = set([ '==', '!=',  '<=', '>=',
                     '&&', '||', '++', '--', '+=', '-=', '*=', '/=', '%='])
    single_operators = set(['+', '-', '*', '/', '%', '=', '<', '>', '!', '&', '|', '^', '~', '?', ':'])
    special_chars = set(['(', ')', '{', '}', '[', ']', ',', ';'])


class Lexical_analyzer(all_elements):
    
    def __init__(self,text):
        self.text = text

    def analyze_c_program():
        #initializing the lists as [] for all the six symbols
        key,ids,op,special,nums,single = [[] for i in range(6)]

        #reading the contents
        content = self.text
        content = re.sub(re.compile(r'/\*.*\*/', re.DOTALL), '', content) # remove all occurance streamed comments (/*COMMENT */) from string
        content = re.sub(re.compile(r'//.*\n'), '', content) # remove all occurance singleline comments (//COMMENT\n ) from string

        escaped_operators = [re.escape(op) for op in operators] # escape all the operators by regex
        escaped_single_operators = [re.escape(op) for op in single_operators] # escape all the single operators by regex
        escaped_special_chars = [re.escape(special_char) for special_char in special_chars] # escape all the special characters by regex

        # join all the escaped operators by |, the formed string for example ++|--|+=|-=|*=|/=|%=|==|!=|<=|>=|&&|\\|\\|
        operators_re = '|'.join(escaped_operators)

        # join all the escaped single operators by |, the formed string for example +|-|*|/|%|=|<|>|!|&|||^|~|?|: 
        single_operators_re = '|'.join(escaped_single_operators)

        # join all the escaped special characters by |, the formed string for example (|)|{|}|[|]|,|;
        special_re = '|'.join(escaped_special_chars)

        #tokenize the content with regex findall
        tokens = re.findall(r'\b\w+\b'+'|'+operators_re+'|'+single_operators_re+'|'+special_re, content)

        for token in tokens:
            if token in keywords:
                # print(token ,"-> keyword")
                key.append(token)
            elif token.isidentifier() and not token[0].isdigit():
                # identifiers.add(token)
                # print(token ,"-> identifier")
                ids.append(token)
            elif token in operators:
                # print('Operator:', token)
                op.append(token)
            elif token in single_operators:
                # print('Single Operator:', token)
                single.append(token)
                
            elif token in special_chars:
                # print('Special Char:', token)
                special.append(token)
            elif token.isdigit():
                # print(token ,"-> number")
                nums.append(token)

        key,ids,op,special,nums,single = set(key),set(ids),set(op),set(special),set(nums),set(single)