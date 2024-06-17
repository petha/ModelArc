class SymbolTable:
    def __init__(self,):
        self.global_symbols = {}
        self.scopes = {}
        self.current_scope = Scope()

    def define (self, name, node):
        qualified_name = self.fully_qualified_name(name)
        if qualified_name in self.global_symbols:
            raise ValueError(f"Symbol {qualified_name} already defined")
        
        self.global_symbols[qualified_name] = node
        self.current_scope.define(name, node)

    def fully_qualified_name(self, name):
        return self.current_scope.get_scope_name() + '.' + name

    def resolve(self, name):
        full_name = self.fully_qualified_name(name)
        
        if full_name in self.global_symbols:
            return self.global_symbols[full_name]
        elif name in self.global_symbols:
            return self.global_symbols[name]
        else:
            return self.current_scope.resolve(name)
    
    def enter_scope(self, name):
        scope_name = self.fully_qualified_name(name)
        
        if not scope_name in self.scopes.keys():
            self.scopes[scope_name] = self.current_scope.enter_scope(name)

        self.current_scope = self.scopes[scope_name]
        return self
    
    def leave_scope(self):
        self.current_scope = self.current_scope.leave_scope()
        return self


class Scope:
    def __init__(self, parent=None, scope_name=''):
        self.symbols = {}
        self.parent = parent
        self.scope_name = scope_name

    def define(self, name, node):
        if name in self.symbols:
            raise ValueError(f"Symbol {name} already defined")
        self.symbols[name] = node
        
    def resolve(self, name):
        if name in self.symbols:
            return self.symbols[name]
        elif self.parent:
            return self.parent.resolve(name)
        else:
            raise ValueError(f"Symbol {name} not found")

    def get_scope_name(self):
        if self.parent:
            return f"{self.parent.get_scope_name()}.{self.scope_name}".removeprefix('.')
        else:
            return self.scope_name

    def enter_scope(self, name):
        return Scope(parent=self, scope_name=name)

    def leave_scope(self):
        if not self.parent:
            raise ValueError("Cannot leave root scope")
        return self.parent