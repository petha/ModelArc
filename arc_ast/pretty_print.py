# Use the visitor pattern to pretty print the AST. 
# This will allow us to add more pretty print methods without modifying the AST classes.
class PrettyPrint:
    def __init__(self):
        self.indent = 0

    def visit(self, node):
        return node.accept(self)
    
    def visit_TypeDefinition(self, node):
        print(" " * self.indent + f"Type: {node.name}")
        self.indent += 2
        for field in node.fields:
            self.visit(field)
        self.indent -= 2

    def visit_PropertyDefinition(self, node):
        print(" " * self.indent + node.name)
        self.indent += 2
        self.visit(node.type)
        self.indent -= 2
    
    def visit_EnumDefinition(self, node):
        values = ", ".join(node.values)
        print(" " * self.indent + node.name + "<" + values + ">")
        
    def visit_RecordDefinition(self, node):
        print(" " * self.indent + node.name)
        self.indent += 2
        for field in node.fields:
            self.visit(field)
        self.indent -= 2

    def visit_PrimitiveType(self, node):
        print(" " * self.indent + node.name)

    def visit_ListType(self, node):
        print(" " * self.indent + "List")
        self.visit(node.type_name)

    def visit_UserDefinedType(self, node):
        print(" " * self.indent + node.name)
    
    def visit_Instance(self, node):
        print(" " * self.indent + '@' + node.name)
        self.indent += 2
        for property in node.properties:
            self.visit(property)
        self.indent -= 2

    def visit_InstanceProperty(self, node):
        print(" " * self.indent + node.name)
        self.indent += 2
        self.visit(node.value)
        self.indent -= 2

    def visit_ListValue(self, node):
        self.indent += 2
        for value in node.values:
            self.visit(value)
        self.indent -= 2

    def visit_SimpleValue(self, node):
        print(" " * self.indent + str(node.value))

    def visit_Transformation(self, node):
        print(" " * self.indent + "Transformation: " + node.name)
        self.indent += 2
        for property in node.properties:
            self.visit(property)
        self.indent -= 2

    def visit_TransformationProperty(self, node):
        self.indent += 2
        self.visit(node.source)
        mapping_to = f" -> {node.target} using {node.using_transformation}"
        print(" " * self.indent + mapping_to)
        self.indent -= 2

    def visit_RecordValue(self, node):
        self.indent += 2
        for property in node.properties:
            self.visit(property)
        self.indent -= 2

    def visit_Reference(self, node):
        print(" " * self.indent + "#" + node.name)

    def visit_Namespace(self, node):
        print(" " * self.indent + f"Namespace: {node.name}")
        self.indent += 2
        for definition in node.definitions:
            self.visit(definition)
        self.indent -= 2

    def visit_ArcAST(self, node):
        for namespace in node.namespaces:
            self.visit(namespace)
        