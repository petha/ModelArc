import arc_ast.ast as AST 

class SemanticAnalyzer:
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
        pass

    def visit_EnumDefinition(self, node):
        pass
    
    def visit_RecordDefinition(self, node):
        pass

    def visit_PropertyDefinition(self, node):
        pass
        
    def visit_UserDefinedType(self, node):
        pass

    def visit_Instance(self, node):
        self._enter_scope(node.name)
        # Check that all properties are defined from the type
        type = self.symbol_table.resolve(node.type_name)
        type_map = self.collect_extended_fields(type)

        #Extract the names of the properties
        property_names = {item.name for item in node.properties}

        # Find additional and missing fields using set operations
        additional_fields = property_names - type_map.keys()
        missing_fields = type_map.keys() - property_names
        
        if additional_fields or missing_fields:
            raise ValueError(f"Additional fields {additional_fields} or missing fields {missing_fields} in instance {node.name}")
        
        for property in node.properties:
            self.check_instance_property(type, type_map, property)
        
        self._leave_scope()
    
    def collect_extended_fields(self, type_def):
        field_map = self.convert_fields_to_map(type_def.fields)
        
        while type_def.extends:
            type_def = self.symbol_table.resolve(type_def.extends)
            # Add any non existing fields to the map
            for field in type_def.fields:
                if field.name not in field_map:
                    field_map[field.name] = field
        return field_map
    
    def convert_fields_to_map(self, fields):
        return {field.name: field for field in fields}

    # Check that the property is defined in the type
    def check_instance_property(self, type_def, type_map, instance_prop):
        if instance_prop.name not in type_map:
            raise ValueError(f"Property {instance_prop.name} is not defined in type #{type_def.name}")
        
        # Check that the value is of the correct type
        if isinstance(type_map[instance_prop.name], AST.PropertyDefinition):
            self.check_value_type(type_map[instance_prop.name].type, instance_prop.value)
        elif isinstance(type_map[instance_prop.name], AST.RecordDefinition):
            self.check_record_value(type_map[instance_prop.name].fields, instance_prop.value)
        else:
            raise ValueError(f"Unknown property type {type_map[instance_prop.name]}")

    def check_value_type(self, expected_type, value):
        if(isinstance(expected_type, AST.PrimitiveType)):
            self.check_primitive_value(expected_type, value)
        elif(isinstance(expected_type, AST.UserDefinedType)):
            self.check_user_defined_value(expected_type, value)
        elif(isinstance(expected_type, AST.ListType)):
            self.check_list_value(expected_type, value)
        else:
            raise ValueError(f"Unknown type {expected_type} {value}")

    def check_list_value(self, expected_type, value):
        if not isinstance(value, AST.ListValue):
            raise ValueError(f"Expected {expected_type} value but got {value}")
       
        for item in value.values:
            self.check_value_type(expected_type.type_name, item)

    def check_user_defined_value(self, user_defined_type, value):
        if not isinstance(value, AST.Reference):
            raise ValueError(f"Expected reference but got {value}")
        
        expected_reference_type = self.symbol_table.resolve(user_defined_type.name)
        
        if isinstance(expected_reference_type, AST.TypeDefinition):
            reference_type = self.symbol_table.resolve(self.symbol_table.resolve(value.name).type_name)
            if reference_type is expected_reference_type:
                raise ValueError(f"Expected reference to {expected_reference_type} but got {reference_type}")

        elif isinstance(expected_reference_type, AST.EnumDefinition):
            if value.value not in expected_reference_type.values:
                raise ValueError(f"Expected value in {expected_reference_type} but got {value}")
        else:
            raise ValueError(f"Unknown type {expected_reference_type}")
        
        
    def check_record_value(self, expected_fields, value):
        if not isinstance(value, AST.RecordValue):
            raise ValueError(f"Expected record value but got {value}")
        
        type_map = self.convert_fields_to_map(expected_fields)

        #Check that all fields are defined
        field_names = {item.name for item in value.properties}
        additional_fields = field_names - type_map.keys()
        missing_fields = type_map.keys() - field_names

        if additional_fields or missing_fields:
            raise ValueError(f"Additional fields {additional_fields} or missing fields {missing_fields} in record value")

        for value in value.properties:
            self.check_instance_property(None, type_map, value  )
        

    def check_primitive_value(self, expected_type, value):
        if not isinstance(value, AST.SimpleValue):
            raise ValueError(f"Expected simple value but got {value}")
        if expected_type.name == 'String' and not isinstance(value.value, str):
            raise ValueError(f"Expected string but got {value}")
        if expected_type.name == 'Number' and not isinstance(value.value, (int, float)):
            raise ValueError(f"Expected number but got {value}")
        if expected_type.name == 'Boolean' and not isinstance(value.value, bool):
            raise ValueError(f"Expected boolean but got {value}")
        if expected_type.name == 'Date' and not isinstance(value.value, str):
            raise ValueError(f"Expected date but got {value}")

    def visit_Transformation(self, node):
        self.symbol_table.resolve(node.input_type)
        self.symbol_table.resolve(node.output_type)
        
        # TODO: Implement transformation validation
        # Check that all output types are defined in the input, since we would endup with a partial transformation if not
        # Ensure that the types are compatible
        # Check that all properties are defined in the input type

        for property in node.properties:
            self.visit(property)
    
    def visit_TransformationProperty(self, node):
        pass

    def visit_ListType(self, node):
        self.visit(node.type_name)

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