class ASTNode:
    def accept(self, visitor):
        method_name = 'visit_' + self.__class__.__name__
        visitor_method = getattr(visitor, method_name, None)
        if visitor_method:
            return visitor_method(self)
        else:
            return self.default_accept(visitor)
        
    def default_accept(self, visitor):
        raise ValueError(f"No visitor method found for {self.__class__.__name__}")
    
    def __repr__(self):
        return f"{self.__class__.__name__}({', '.join(repr(x) for x in self.__dict__.values())})"
    
class TypeDefinition(ASTNode):
    def __init__(self, name, fields, extends=None):
        self.name = name
        self.fields = fields
        self.extends = extends

class PropertyDefinition(ASTNode):
    def __init__(self, name, type):
        self.name = name
        self.type = type

class RecordDefinition(ASTNode):
    def __init__(self, name, fields):
        self.name = name
        self.fields = fields

class PrimitiveType(ASTNode):
    def __init__(self, name):
        self.name = name

class UserDefinedType(ASTNode):
    def __init__(self, name):
        self.name = name

class Instance(ASTNode):    
    def __init__(self, name, type_name, properties):
        self.name = name
        self.type_name = type_name
        self.properties = properties

class InstanceProperty(ASTNode):
    def __init__(self, name, value):
        self.name = name
        self.value = value

class ListValue(ASTNode):
    def __init__(self, values):
        self.values = values

class SimpleValue(ASTNode):
    def __init__(self, value):
        self.value = value

class RecordValue(ASTNode):
    def __init__(self, properties):
        self.properties = properties

class EnumDefinition(ASTNode):
    def __init__(self, name, values):
        self.name = name
        self.values = values

class Transformation(ASTNode):
    def __init__(self, name, input_type, output_type, properties):
        self.name = name
        self.input_type = input_type
        self.output_type = output_type
        self.properties = properties

class TransformationProperty(ASTNode):
    def __init__(self, source, target, using_transformation=None):
        self.source = source
        self.target = target
        self.using_transformation = using_transformation

class Namespace(ASTNode):
    def __init__(self, name, definitions):
        self.name = name
        self.definitions = definitions

class ListType(ASTNode):
    def __init__(self, type_name):
        self.type_name = type_name

class Reference(ASTNode):
    def __init__(self, name):
        self.name = name

class ArcAST(ASTNode):
    def __init__(self, namespaces=[]):
        self.namespaces = namespaces
