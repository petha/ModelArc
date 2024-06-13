import unittest
from arc_lexer import lexer

class TestLexer(unittest.TestCase):
    def test_lexer(self):
        data = 'import "test_file";'
        lexer.input(data)
        tokens = list(lexer)
        print(tokens)

if __name__ == '__main__':
    unittest.main()