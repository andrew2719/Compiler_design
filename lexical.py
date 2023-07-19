import re
import pandas as pd
def print_table(key,op,ids,special,nums,single):
    elements = {'keywords':list(key),'operators':list(op),'identifiers':list(ids),'special':list(special),'numbers':list(nums),'single':list(single)}
    
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

def analyze_c_program(file_path):
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

    key,ids,op,special,nums,single = [[] for i in range(6)]
    with open(file_path, 'r') as file:
        content = file.read()

        
        content = re.sub(re.compile(r'/\*.*\*/', re.DOTALL), '', content)
        
        content = re.sub(re.compile(r'//.*\n'), '', content)

        escaped_operators = [re.escape(op) for op in operators]
        escaped_single_operators = [re.escape(op) for op in single_operators]
        escaped_special_chars = [re.escape(special_char) for special_char in special_chars]

        operators_re = '|'.join(escaped_operators)
        single_operators_re = '|'.join(escaped_single_operators)
        special_re = '|'.join(escaped_special_chars)

        # print(escaped_operators)
        # print(operators_re)
        # tokens = re.findall(r'\b\w+\b|[^\s\w]', content)
        tokens = re.findall(r'\b\w+\b'+'|'+operators_re+'|'+single_operators_re+'|'+special_re, content)
        
        
        print(tokens)
        
        for token in tokens:
            if token in keywords:
                print(token ,"-> keyword")
                key.append(token)
            elif token.isidentifier() and not token[0].isdigit():
                # identifiers.add(token)
                print(token ,"-> identifier")
                ids.append(token)
            elif token in operators:
                print('Operator:', token)
                op.append(token)
            elif token in single_operators:
                print('Single Operator:', token)
                single.append(token)
                
            elif token in special_chars:
                print('Special Char:', token)
                special.append(token)
            elif token.isdigit():
                print(token ,"-> number")
                nums.append(token)

        print("lists")
        print(key,ids,op,special,nums,single)

        key,ids,op,special,nums,single = set(key),set(ids),set(op),set(special),set(nums),set(single)
        print_table(key,op,ids,special,nums,single)


# Usage example
# file_path = 'E:\\college\\coding\\programing\\Compiler_design\\test.txt'
# analyze_c_program(file_path)
analyze_c_program("test.txt")