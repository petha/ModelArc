import ply.lex as lex


tokens = (
    'IMPORT', 'NAMESPACE', 'TYPE', 'INSTANCE',
    'LIST_TYPE', 'LT', 'GT',
    'USING',
    'COMMA', 'LBRACKET', 'RBRACKET',
    'TRANSFORMATION', 'STRING', 'IDENTIFIER', 'NUMBER', 'BOOLEAN', 'DATE',
    'ENUM',
    'OF','LBRACE', 'RBRACE', 'ARROW', 'EXTENDS', 'EQUALS', 'STRING_TYPE', 'NUMBER_TYPE', 'BOOLEAN_TYPE', 'DATE_TYPE'
)


# Reserved words
reserved = {
    'import': 'IMPORT',
    'extends': 'EXTENDS',
    'namespace': 'NAMESPACE',
    'Type': 'TYPE',
    'Instance': 'INSTANCE',
    'using': 'USING',
    'Transformation': 'TRANSFORMATION',
    'String': 'STRING_TYPE',
    'Enum': 'ENUM',
    'Number': 'NUMBER_TYPE',
    'Boolean': 'BOOLEAN_TYPE',
    'List': 'LIST_TYPE',
    'Date': 'DATE_TYPE',
    'of': 'OF'
}
t_LT= r'\<'
t_GT= r'\>'
t_COMMA = r','
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_ignore = ' \t\n'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_ARROW = r'->'
t_EQUALS = r'='
t_ignore_COMMENT = r'//.*'

def t_STRING(t):
    r'"[^"]*"'
    t.value = t.value[1:-1]
    return t

def t_NUMBER(t):
    r'\d+(\.\d+)?'
    if '.' in t.value:
        t.value = float(t.value)
    else:
        t.value = int(t.value)
    return t

def t_BOOLEAN(t):
    r'true|false'
    t.value = True if t.value == 'true' else False
    return t

def t_DATE(t):
    r'"[0-9]{4}-[0-9]{2}-[0-9]{2}"'
    t.value = t.value[1:-1]
    return t

def t_IDENTIFIER(t):
    # Regexp for identifiers
    # It must start with a letter or underscore, then it can have any number of letters, numbers or underscores
    # the identifier can have a dot in the middle but not at the end or beginning
    r'[a-zA-Z_][a-zA-Z_0-9]*(\.[a-zA-Z_0-9]+)*'
    
    t.type = reserved.get(t.value, 'IDENTIFIER')  # Check for reserved words
    return t

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += 1

def t_error(t):
    print(f"Illegal character {t.value[0]}")
    t.lexer.skip(1)

lexer = lex.lex()