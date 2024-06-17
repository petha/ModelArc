class SymbolCollector:
    def __init__(self, symbol_table):
        self.symbol_table = symbol_table
        
    def _enter_scope(self, name):
        self.symbol_table = self.symbol_table.enter_scope(name)
    
    def _leave_scope(self):
        self.symbol_table = self.symbol_table.leave_scope()

    def visit(self, node):
        return node.accept(self)
    
    def visit_ArcAST(self, node):
        for namespace in node.namespaces:
            self.visit(namespace)

    def visit_Namespace(self, node):
        self._enter_scope(node.name)             
        for definition in node.definitions:
            self.visit(definition)
        self._leave_scope()

    def visit_TypeDefinition(self, node):
        self.symbol_table.define(node.name, node)
        self._enter_scope(node.name)
        for field in node.fields:
            self.visit(field)
        self._leave_scope()

    def visit_EnumDefinition(self, node):
        self.symbol_table.define(node.name, node)

        # Enum values are defined in the global scope
        for value in node.values:
            self.symbol_table.define(f"{node.name}.{value}", value)

    def visit_RecordDefinition(self, node):
        self.symbol_table.define(node.name, node)
        self._enter_scope(node.name)
        for field in node.fields:
            self.visit(field)
        self._leave_scope()

    def visit_PropertyDefinition(self, node):
        self.symbol_table.define(node.name, node)
        self.visit(node.type)
        
    def visit_UserDefinedType(self, node):
        pass

    def visit_Instance(self, node):
        self.symbol_table.define(node.name, node)
        self._enter_scope(node.name)
        
        for property in node.properties:
            self.visit(property)

        self._leave_scope()
    
    def visit_InstanceProperty(self, node):
        self.symbol_table.define(node.name, node)
        self.visit(node.value)

    def visit_Transformation(self, node):
        self.symbol_table.define(node.name, node)
        
    def visit_ListType(self, node):
        pass

    def visit_PrimitiveType(self, node):
        pass

    def visit_SimpleValue(self, node):
        pass

    def visit_ListValue(self, node):
        pass

    def visit_Reference(self, node):
        pass

    def visit_RecordValue(self, node):
        pass