import ply.yacc as yacc
from arc_lexer import tokens

# Grammar rules

def p_model_arc(p):
    '''model_arc : namespaces'''
    p[0] = ('module', p[1])    

def p_namespaces(p):
    '''namespaces : namespace namespaces
                  | empty'''
    if len(p) == 3:
        # p[1] is a single 'namespace'
        # p[2] is the rest of the 'namespaces'
        p[0] = [p[1]] + p[2]
    else:
        p[0] = []

# Single 'namespace' definition
def p_namespace(p):
    'namespace : NAMESPACE IDENTIFIER LBRACE definitions RBRACE'
    # p[2] is the name of the namespace
    # p[4] is the list of 'definitions' inside the namespace
    p[0] = ('namespace', p[2], p[4])

def p_definitions(p):
    '''definitions : definition definitions
                    | empty'''
    if len(p) == 3:
        # p[1] is a single 'definition'
        # p[2] is the rest of the 'definitions'
        p[0] = [p[1]] + p[2]
    else:
        p[0] = []

def p_definition(p):
    '''definition : type_definition
                  | instance
                  | enum
                  | transformation'''
    p[0] = p[1]

def p_enum(p):
    '''enum : ENUM IDENTIFIER LBRACE enum_values RBRACE'''
    # p[2] is the name of the enum
    # p[4] is the list of 'values' inside the enum
    p[0] = ('enum', p[2], p[4])

def p_enum_values(p):
    '''enum_values : enum_value COMMA enum_values
                   | enum_value'''
    if len(p) == 4:
        # p[1] is a single 'enum_value'
        # p[3] is the rest of the 'enum_values'
        p[0] = [p[1]] + p[3]
    else:
        p[0] = [p[1]]

def p_enum_value(p):
    '''enum_value : IDENTIFIER'''
    p[0] = p[1]

def p_transformation(p):
    '''transformation : TRANSFORMATION IDENTIFIER IDENTIFIER ARROW IDENTIFIER LBRACE transformation_properties RBRACE'''
    # p[2] is the name of the transformation
    # p[4] is the name of the input type
    # p[6] is the list of 'properties' inside the transformation
    p[0] = ('transformation', p[2], p[3], p[5], p[7])

def p_transformation_properties(p):
    '''transformation_properties : transformation_property transformation_properties
                                 | empty'''
    if len(p) == 3:
        # p[1] is a single 'transformation_property'
        # p[2] is the rest of the 'transformation_properties'
        p[0] = [p[1]] + p[2]
    else:
        p[0] = []

def p_transformation_property(p):
    '''transformation_property : IDENTIFIER ARROW IDENTIFIER
                               | value ARROW IDENTIFIER
                               | IDENTIFIER ARROW IDENTIFIER USING IDENTIFIER'''
    p[0] = ('transformation_property', p[1], p[3], p[5] if len(p) == 6 else None)

def p_instance(p):
    '''instance : INSTANCE IDENTIFIER OF IDENTIFIER LBRACE instance_properties RBRACE'''
    # p[2] is the name of the instance
    # p[4] is the name of the type
    # p[6] is the list of 'properties' inside the instance
    p[0] = ('instance', p[2], p[4], p[6])

def p_instance_properties(p):
    '''instance_properties : instance_property instance_properties
                           | empty'''
    if len(p) == 3:
        # p[1] is a single 'instance_property'
        # p[2] is the rest of the 'instance_properties'
        p[0] = [p[1]] + p[2]
    else:
        p[0] = []

def p_instance_property(p):
    '''instance_property : IDENTIFIER EQUALS value'''
    
    p[0] = ('instance_property', p[1], p[3])

def p_value(p):
    '''value : simple_value
             | complex_value
             | list_value
             | reference'''
    p[0] = p[1]

def p_list_value(p):
    '''list_value : LBRACKET list_values RBRACKET'''
    p[0] = ('list_value', p[2])

def p_list_values(p):
    '''list_values : value COMMA list_values
                   | value'''
    if len(p) == 4:
        # p[1] is a single 'value'
        # p[3] is the rest of the 'list_values'
        p[0] = [p[1]] + p[3]
    else:
        p[0] = [p[1]]
    
def p_reference(p):
    '''reference : IDENTIFIER'''
    p[0] = ('reference', p[1])

def p_simple_value(p):
    '''simple_value : STRING
                    | NUMBER
                    | BOOLEAN
                    | DATE'''
    p[0] = ('simple_value', p[1])

def p_complex_value(p):
    '''complex_value : LBRACE instance_properties RBRACE'''
    p[0] = ('complex_value', p[2])

def p_type_definition(p):
    '''type_definition : TYPE IDENTIFIER LBRACE type_properties RBRACE
        | TYPE IDENTIFIER EXTENDS IDENTIFIER LBRACE type_properties  RBRACE '''
    # p[2] is the name of the type
    # p[4] is the list of 'definitions' inside the type
    if(len(p) == 6):
        p[0] = ('type', p[2], p[4])
    else:
        p[0] = ('extended_type', p[2], p[4], p[6])
    
def p_type_properties(p):
    '''type_properties : type_prop type_properties
                       | empty'''
    if len(p) == 3:
        # p[1] is a single 'type_property'
        # p[2] is the rest of the 'type_properties'
        p[0] = [p[1]] + p[2]
    else:
        p[0] = []

def p_type_prop(p):
    '''type_prop : type_declaration IDENTIFIER
                    | IDENTIFIER LBRACE type_properties RBRACE'''

    if(len(p) ==  3):
        p[0] = ('property', p[1], p[2])
    else:
        p[0] = ('record', p[1], p[3]) 

def p_type_declaration(p):
    '''type_declaration :   primitive_type_declaration
                            | user_defined_type_declaration'''
    p[0] = p[1]

def p_user_defined_type_declaration(p):
    '''user_defined_type_declaration : IDENTIFIER'''
    p[0] = ('user_defined_type_declaration', p[1])

def p_primitive_type_declaration(p):
    '''primitive_type_declaration : STRING_TYPE
            | NUMBER_TYPE
            | BOOLEAN_TYPE
            | DATE_TYPE
            | LIST_TYPE LT type_declaration GT'''

    if(len(p) == 2):
        p[0] = ('primitive_type_declaration', p[1])
    else:
        p[0] = ('list_type_declaration', p[3])

def p_empty(p):
    'empty :'
    pass

# Error rule for syntax errors
def p_error(p):
    #Find column and line number of the error
    if p:
        p.lexer.skip(1)

    raise ValueError(f"Syntax error at token {p.type}, {p.value} in line {p.lineno} column {p.lexpos}")

# Build the parser
arc_parser = yacc.yacc()
