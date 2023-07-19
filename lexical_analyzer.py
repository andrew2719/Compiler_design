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
        self.keywords = set()
        self.identifiers = set()
        self.operators = set()
        self.single_operators = set()
        self.special_chars = set()
        self.integers = set()
        self.floats = set()
        self.exponentials = set()
        
    def print_table(self):
        # elements = {'keywords':list(key),'operators':list(op),
        #             'identifiers':list(ids),'special':list(special),'numbers':list(nums),'single':list(single)}
        elements = {'keywords':list(self.keywords),'operators':list(self.operators),'single_operators':list(self.single_operators)
                    ,'identifiers':list(self.identifiers),'special_char':list(self.special_chars)
                    ,'integers':list(self.integers),'floats':list(self.floats),'exponential':list(self.exponentials)}
        # all the elements are not of same length so we need to make them of same length 
        # so that we can make a dataframe out of it
        max_len = 0
        for i in elements:
            if len(elements[i]) > max_len:
                max_len = len(elements[i])


        for i in elements:
            while len(elements[i]) < max_len:
                elements[i].append('')

        # print(elements)
        df = pd.DataFrame(elements)
        print(df)

    def analyze_c_program(self):
        #initializing the lists as [] for all the six symbols
        # key,ids,op,special,nums,single = [[] for i in range(6)]

        #reading the contents
        content = self.text

        content = re.sub(re.compile(r'/\*.*\*/', re.DOTALL), '', content) # remove all occurance streamed comments (/*COMMENT */) from string
        content = re.sub(re.compile(r'//.*\n'), '', content) # remove all occurance singleline comments (//COMMENT\n ) from string


        escaped_operators = [re.escape(op) for op in all_elements.operators] # escape all the operators by regex
        escaped_single_operators = [re.escape(op) for op in all_elements.single_operators] # escape all the single operators by regex
        escaped_special_chars = [re.escape(special_char) for special_char in all_elements.special_chars] # escape all the special characters by regex
        # re.escape() converts to the regex equivalent of the string


        # join all the escaped operators by |, the formed string for example ++|--|+=|-=|*=|/=|%=|==|!=|<=|>=|&&|\\|\\|
        operators_re = '|'.join(escaped_operators)


        # join all the escaped single operators by |, the formed string for example +|-|*|/|%|=|<|>|!|&|||^|~|?|: 
        single_operators_re = '|'.join(escaped_single_operators)


        # join all the escaped special characters by |, the formed string for example (|)|{|}|[|]|,|;
        special_re = '|'.join(escaped_special_chars)


        #tokenize the content with regex findall
        tokens = re.findall(r'\b\d+\.\d+\b|\b\w+\b'+'|'+operators_re+'|'+single_operators_re+'|'+special_re, content)

        print(tokens)

        for token in tokens:
            if token in all_elements.keywords:
                # print(token ,"-> keyword")
                # key.append(token)
                self.keywords.add(token)
            elif token.isidentifier() and not token[0].isdigit():
                # identifiers.add(token)
                # print(token ,"-> identifier")
                # ids.append(token)
                self.identifiers.add(token)
            elif token in all_elements.operators:
                # print('Operator:', token)
                # op.append(token)
                self.operators.add(token)
            elif token in all_elements.single_operators:
                # print('Single Operator:', token)
                # single.append(token)
                self.single_operators.add(token)
                
            elif token in all_elements.special_chars:
                # print('Special Char:', token)
                # special.append(token)
                self.special_chars.add(token)
            elif token[0].isdigit():
                if '.' in token:
                    # print('Float:', token)
                    # nums.append(token)
                    self.floats.add(token)
                elif 'e' in token or 'E' in token:
                    # print('Exponential:', token)
                    # nums.append(token)
                    self.exponentials.add(token)
                else:
                    # print('Integer:', token)
                    # nums.append(token)
                    self.integers.add(token)


        # key,ids,op,special,nums,single = set(key),set(ids),set(op),set(special),set(nums),set(single)
        
        # Lexical_analyzer.print_table(key,op,ids,special,nums,single)

        

        Lexical_analyzer.print_table(self)


def convert_file_to_content(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    return content

text = convert_file_to_content('test.txt')

la  = Lexical_analyzer(text)
la.analyze_c_program()
