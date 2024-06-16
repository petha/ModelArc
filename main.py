import argparse

from arc_preprocessor import preprocessor
from arc_lexer import lexer
from arc_parser import arc_parser
from arc_ast import pretty_print
#from arc_ast import build_ast, validate_ast, print_ast

def print_ast(ast):
    pretty_printer = pretty_print.PrettyPrint()
    ast.accept(pretty_printer)

target_functions = {
    'print': print_ast
}

def main():
    arg_parser = argparse.ArgumentParser(description='Compile ModelArc code')

    arg_parser.add_argument('input_file', type=str, help='Input file to compile')
    
    target_function_keys = list(target_functions.keys())
    arg_parser.add_argument('--target',
                            type=str, 
                            default=target_function_keys[0], 
                            choices=target_function_keys, 
                            help='Target output format')

    args = arg_parser.parse_args()
    
    source_code = preprocessor(args.input_file)
    lexer.input(source_code)
    parse_tree = arc_parser.parse(source_code, lexer=lexer, tracking=True)
  
    #ast = build_ast(parse_tree)
    #validate_ast(ast)

    if args.target in target_functions:
        target_functions[args.target](parse_tree)
    else:
        raise ValueError(f"Invalid target {args.target}")


if __name__ == '__main__':
    main()
