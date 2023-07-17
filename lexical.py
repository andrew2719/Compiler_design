import re


def analyze_c_program(file_path):
    keywords = set(['auto', 'break', 'case', 'char', 'const', 'continue', 'default',
                    'do', 'double', 'else', 'enum', 'extern', 'float', 'for', 'goto',
                    'if', 'int', 'long', 'register', 'return', 'short', 'signed', 'sizeof',
                    'static', 'struct', 'switch', 'typedef', 'union', 'unsigned', 'void',
                    'volatile', 'while'])

    identifiers = set()
    operators = set(['+', '-', '*', '/', '%', '=', '==', '!=', '<', '>', '<=', '>=',
                     '&&', '||', '!', '++', '--', '+=', '-=', '*=', '/=', '%='])
    special_chars = set(['(', ')', '{', '}', '[', ']', ',', ';'])

    with open(file_path, 'r') as file:
        content = file.read()

        
        content = re.sub(re.compile(r'/\*.*\*/', re.DOTALL), '', content)
        
        content = re.sub(re.compile(r'//.*\n'), '', content)

        
        tokens = re.findall(r'\b\w+\b|[^\s\w]', content)
        print(tokens)
        
        for token in tokens:
            if token in keywords:
                print(token ,"-> keyword")
            elif token.isidentifier() and not token[0].isdigit():
                identifiers.add(token)
                print(token ,"-> identifier")
            elif token in operators:
                print('Operator:', token)
            elif token in special_chars:
                print('Special Char:', token)
            
            elif token.isdigit():
                print(token ,"-> number")

        # print('\nIdentifiers:')
        # for identifier in identifiers:
        #     print(identifier)


# Usage example
file_path = 'E:\\college\\coding\\programing\\Compiler_design\\test.txt'
analyze_c_program(file_path)
