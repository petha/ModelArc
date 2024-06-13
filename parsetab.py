
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ARROW BOOLEAN BOOLEAN_TYPE COMMA DATE DATE_TYPE ENUM EQUALS EXTENDS GT IDENTIFIER IMPORT INSTANCE LBRACE LBRACKET LIST_TYPE LT NAMESPACE NUMBER NUMBER_TYPE OF RBRACE RBRACKET STRING STRING_TYPE TRANSFORMATION TYPE USINGmodel_arc : imports namespaceimports : import imports\n               | emptydefinitions : definition definitions\n                    | emptydefinition : type_definition\n                  | instance\n                  | enum\n                  | transformationenum : ENUM IDENTIFIER LBRACE enum_values RBRACEenum_values : enum_value COMMA enum_values\n                   | enum_valueenum_value : IDENTIFIERtransformation : TRANSFORMATION IDENTIFIER IDENTIFIER ARROW IDENTIFIER LBRACE transformation_properties RBRACEtransformation_properties : transformation_property transformation_properties\n                                 | emptytransformation_property : IDENTIFIER ARROW IDENTIFIER\n                               | value ARROW IDENTIFIER\n                               | IDENTIFIER ARROW IDENTIFIER USING IDENTIFIERinstance : INSTANCE IDENTIFIER OF IDENTIFIER LBRACE instance_properties RBRACEinstance_properties : instance_property instance_properties\n                           | emptyinstance_property : IDENTIFIER EQUALS valuevalue : simple_value\n             | complex_value\n             | list_value\n             | referencelist_value : LBRACKET list_values RBRACKETlist_values : value COMMA list_values\n                   | valuereference : IDENTIFIERsimple_value : STRING\n                    | NUMBER\n                    | BOOLEAN\n                    | DATEcomplex_value : LBRACE instance_properties RBRACEtype_definition : TYPE IDENTIFIER LBRACE type_properties RBRACE\n        | TYPE IDENTIFIER EXTENDS IDENTIFIER LBRACE type_properties  RBRACE type_properties : type_property type_properties\n                       | emptytype_property : type_declaration_listtype_declaration_list : type_prop type_declaration_list\n                            | emptytype_prop : type_declaration IDENTIFIER\n                    | IDENTIFIER LBRACE type_properties RBRACEtype_declaration :   primitive_type_declaration\n                            | user_defined_type_declarationuser_defined_type_declaration : IDENTIFIERprimitive_type_declaration : STRING_TYPE\n            | NUMBER_TYPE\n            | BOOLEAN_TYPE\n            | DATE_TYPE\n            | LIST_TYPE LT type_declaration GTimport : IMPORT STRINGnamespace : NAMESPACE IDENTIFIER LBRACE definitions RBRACEempty :'
    
_lr_action_items = {'IMPORT':([0,3,9,],[5,5,-54,]),'NAMESPACE':([0,2,3,4,8,9,],[-56,7,-56,-3,-2,-54,]),'$end':([1,6,23,],[0,-1,-55,]),'STRING':([5,75,79,85,96,106,108,110,113,],[9,92,92,92,92,-17,-18,92,-19,]),'IDENTIFIER':([7,19,20,21,22,28,29,30,31,32,34,36,37,38,39,40,41,42,43,44,45,46,53,54,57,58,59,60,61,62,64,72,75,76,77,79,83,85,88,89,90,91,92,93,94,95,96,97,98,99,103,106,107,108,109,110,111,113,],[10,25,26,27,28,33,34,48,49,50,-48,34,-43,-41,34,59,-46,-47,-49,-50,-51,-52,65,34,-42,-43,-44,68,34,70,50,70,82,-45,-53,97,70,82,-24,-25,-26,-27,-32,-33,-34,-35,97,-31,-23,106,108,-17,-36,-18,-28,97,113,-19,]),'LBRACE':([10,25,27,34,48,49,65,75,79,85,96,106,108,110,113,],[11,29,32,54,61,62,75,83,83,83,83,-17,-18,83,-19,]),'RBRACE':([11,12,13,14,15,16,17,18,24,29,35,36,37,38,39,50,51,52,54,55,56,57,58,59,61,62,63,66,69,71,72,73,74,75,76,78,80,81,83,84,85,86,88,89,90,91,92,93,94,95,97,98,100,101,102,106,107,108,109,113,],[-56,23,-56,-5,-6,-7,-8,-9,-4,-56,55,-56,-40,-41,-56,-13,63,-12,-56,-37,-39,-42,-43,-44,-56,-56,-10,76,78,80,-56,-22,-11,-56,-45,-38,-20,-21,-56,101,-56,-16,-24,-25,-26,-27,-32,-33,-34,-35,-31,-23,107,-14,-15,-17,-36,-18,-28,-19,]),'TYPE':([11,13,15,16,17,18,55,63,78,80,101,],[19,19,-6,-7,-8,-9,-37,-10,-38,-20,-14,]),'INSTANCE':([11,13,15,16,17,18,55,63,78,80,101,],[20,20,-6,-7,-8,-9,-37,-10,-38,-20,-14,]),'ENUM':([11,13,15,16,17,18,55,63,78,80,101,],[21,21,-6,-7,-8,-9,-37,-10,-38,-20,-14,]),'TRANSFORMATION':([11,13,15,16,17,18,55,63,78,80,101,],[22,22,-6,-7,-8,-9,-37,-10,-38,-20,-14,]),'EXTENDS':([25,],[30,]),'OF':([26,],[31,]),'STRING_TYPE':([29,36,37,38,39,54,57,58,59,60,61,76,],[43,43,-43,-41,43,43,-42,-43,-44,43,43,-45,]),'NUMBER_TYPE':([29,36,37,38,39,54,57,58,59,60,61,76,],[44,44,-43,-41,44,44,-42,-43,-44,44,44,-45,]),'BOOLEAN_TYPE':([29,36,37,38,39,54,57,58,59,60,61,76,],[45,45,-43,-41,45,45,-42,-43,-44,45,45,-45,]),'DATE_TYPE':([29,36,37,38,39,54,57,58,59,60,61,76,],[46,46,-43,-41,46,46,-42,-43,-44,46,46,-45,]),'LIST_TYPE':([29,36,37,38,39,54,57,58,59,60,61,76,],[47,47,-43,-41,47,47,-42,-43,-44,47,47,-45,]),'ARROW':([33,82,87,88,89,90,91,92,93,94,95,107,109,],[53,99,103,-24,-25,-26,-27,-32,-33,-34,-35,-36,-28,]),'GT':([41,42,43,44,45,46,67,68,77,],[-46,-47,-49,-50,-51,-52,77,-48,-53,]),'LT':([47,],[60,]),'COMMA':([50,52,88,89,90,91,92,93,94,95,97,105,107,109,],[-13,64,-24,-25,-26,-27,-32,-33,-34,-35,-31,110,-36,-28,]),'EQUALS':([70,],[79,]),'NUMBER':([75,79,85,96,106,108,110,113,],[93,93,93,93,-17,-18,93,-19,]),'BOOLEAN':([75,79,85,96,106,108,110,113,],[94,94,94,94,-17,-18,94,-19,]),'DATE':([75,79,85,96,106,108,110,113,],[95,95,95,95,-17,-18,95,-19,]),'LBRACKET':([75,79,85,96,106,108,110,113,],[96,96,96,96,-17,-18,96,-19,]),'RBRACKET':([88,89,90,91,92,93,94,95,97,104,105,107,109,112,],[-24,-25,-26,-27,-32,-33,-34,-35,-31,109,-30,-36,-28,-29,]),'USING':([106,],[111,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'model_arc':([0,],[1,]),'imports':([0,3,],[2,8,]),'import':([0,3,],[3,3,]),'empty':([0,3,11,13,29,36,39,54,61,62,72,75,83,85,],[4,4,14,14,37,37,58,37,37,73,73,86,73,86,]),'namespace':([2,],[6,]),'definitions':([11,13,],[12,24,]),'definition':([11,13,],[13,13,]),'type_definition':([11,13,],[15,15,]),'instance':([11,13,],[16,16,]),'enum':([11,13,],[17,17,]),'transformation':([11,13,],[18,18,]),'type_properties':([29,36,54,61,],[35,56,66,69,]),'type_property':([29,36,54,61,],[36,36,36,36,]),'type_declaration_list':([29,36,39,54,61,],[38,38,57,38,38,]),'type_prop':([29,36,39,54,61,],[39,39,39,39,39,]),'type_declaration':([29,36,39,54,60,61,],[40,40,40,40,67,40,]),'primitive_type_declaration':([29,36,39,54,60,61,],[41,41,41,41,41,41,]),'user_defined_type_declaration':([29,36,39,54,60,61,],[42,42,42,42,42,42,]),'enum_values':([32,64,],[51,74,]),'enum_value':([32,64,],[52,52,]),'instance_properties':([62,72,83,],[71,81,100,]),'instance_property':([62,72,83,],[72,72,72,]),'transformation_properties':([75,85,],[84,102,]),'transformation_property':([75,85,],[85,85,]),'value':([75,79,85,96,110,],[87,98,87,105,105,]),'simple_value':([75,79,85,96,110,],[88,88,88,88,88,]),'complex_value':([75,79,85,96,110,],[89,89,89,89,89,]),'list_value':([75,79,85,96,110,],[90,90,90,90,90,]),'reference':([75,79,85,96,110,],[91,91,91,91,91,]),'list_values':([96,110,],[104,112,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> model_arc","S'",1,None,None,None),
  ('model_arc -> imports namespace','model_arc',2,'p_model_arc','arc_parser.py',7),
  ('imports -> import imports','imports',2,'p_imports','arc_parser.py',12),
  ('imports -> empty','imports',1,'p_imports','arc_parser.py',13),
  ('definitions -> definition definitions','definitions',2,'p_definitions','arc_parser.py',22),
  ('definitions -> empty','definitions',1,'p_definitions','arc_parser.py',23),
  ('definition -> type_definition','definition',1,'p_definition','arc_parser.py',32),
  ('definition -> instance','definition',1,'p_definition','arc_parser.py',33),
  ('definition -> enum','definition',1,'p_definition','arc_parser.py',34),
  ('definition -> transformation','definition',1,'p_definition','arc_parser.py',35),
  ('enum -> ENUM IDENTIFIER LBRACE enum_values RBRACE','enum',5,'p_enum','arc_parser.py',39),
  ('enum_values -> enum_value COMMA enum_values','enum_values',3,'p_enum_values','arc_parser.py',45),
  ('enum_values -> enum_value','enum_values',1,'p_enum_values','arc_parser.py',46),
  ('enum_value -> IDENTIFIER','enum_value',1,'p_enum_value','arc_parser.py',55),
  ('transformation -> TRANSFORMATION IDENTIFIER IDENTIFIER ARROW IDENTIFIER LBRACE transformation_properties RBRACE','transformation',8,'p_transformation','arc_parser.py',59),
  ('transformation_properties -> transformation_property transformation_properties','transformation_properties',2,'p_transformation_properties','arc_parser.py',66),
  ('transformation_properties -> empty','transformation_properties',1,'p_transformation_properties','arc_parser.py',67),
  ('transformation_property -> IDENTIFIER ARROW IDENTIFIER','transformation_property',3,'p_transformation_property','arc_parser.py',76),
  ('transformation_property -> value ARROW IDENTIFIER','transformation_property',3,'p_transformation_property','arc_parser.py',77),
  ('transformation_property -> IDENTIFIER ARROW IDENTIFIER USING IDENTIFIER','transformation_property',5,'p_transformation_property','arc_parser.py',78),
  ('instance -> INSTANCE IDENTIFIER OF IDENTIFIER LBRACE instance_properties RBRACE','instance',7,'p_instance','arc_parser.py',82),
  ('instance_properties -> instance_property instance_properties','instance_properties',2,'p_instance_properties','arc_parser.py',89),
  ('instance_properties -> empty','instance_properties',1,'p_instance_properties','arc_parser.py',90),
  ('instance_property -> IDENTIFIER EQUALS value','instance_property',3,'p_instance_property','arc_parser.py',99),
  ('value -> simple_value','value',1,'p_value','arc_parser.py',104),
  ('value -> complex_value','value',1,'p_value','arc_parser.py',105),
  ('value -> list_value','value',1,'p_value','arc_parser.py',106),
  ('value -> reference','value',1,'p_value','arc_parser.py',107),
  ('list_value -> LBRACKET list_values RBRACKET','list_value',3,'p_list_value','arc_parser.py',111),
  ('list_values -> value COMMA list_values','list_values',3,'p_list_values','arc_parser.py',115),
  ('list_values -> value','list_values',1,'p_list_values','arc_parser.py',116),
  ('reference -> IDENTIFIER','reference',1,'p_reference','arc_parser.py',125),
  ('simple_value -> STRING','simple_value',1,'p_simple_value','arc_parser.py',129),
  ('simple_value -> NUMBER','simple_value',1,'p_simple_value','arc_parser.py',130),
  ('simple_value -> BOOLEAN','simple_value',1,'p_simple_value','arc_parser.py',131),
  ('simple_value -> DATE','simple_value',1,'p_simple_value','arc_parser.py',132),
  ('complex_value -> LBRACE instance_properties RBRACE','complex_value',3,'p_complex_value','arc_parser.py',136),
  ('type_definition -> TYPE IDENTIFIER LBRACE type_properties RBRACE','type_definition',5,'p_type_definition','arc_parser.py',140),
  ('type_definition -> TYPE IDENTIFIER EXTENDS IDENTIFIER LBRACE type_properties RBRACE','type_definition',7,'p_type_definition','arc_parser.py',141),
  ('type_properties -> type_property type_properties','type_properties',2,'p_type_properties','arc_parser.py',150),
  ('type_properties -> empty','type_properties',1,'p_type_properties','arc_parser.py',151),
  ('type_property -> type_declaration_list','type_property',1,'p_type_property','arc_parser.py',160),
  ('type_declaration_list -> type_prop type_declaration_list','type_declaration_list',2,'p_type_declaration_list','arc_parser.py',164),
  ('type_declaration_list -> empty','type_declaration_list',1,'p_type_declaration_list','arc_parser.py',165),
  ('type_prop -> type_declaration IDENTIFIER','type_prop',2,'p_type_prop','arc_parser.py',174),
  ('type_prop -> IDENTIFIER LBRACE type_properties RBRACE','type_prop',4,'p_type_prop','arc_parser.py',175),
  ('type_declaration -> primitive_type_declaration','type_declaration',1,'p_type_declaration','arc_parser.py',183),
  ('type_declaration -> user_defined_type_declaration','type_declaration',1,'p_type_declaration','arc_parser.py',184),
  ('user_defined_type_declaration -> IDENTIFIER','user_defined_type_declaration',1,'p_user_defined_type_declaration','arc_parser.py',188),
  ('primitive_type_declaration -> STRING_TYPE','primitive_type_declaration',1,'p_primitive_type_declaration','arc_parser.py',192),
  ('primitive_type_declaration -> NUMBER_TYPE','primitive_type_declaration',1,'p_primitive_type_declaration','arc_parser.py',193),
  ('primitive_type_declaration -> BOOLEAN_TYPE','primitive_type_declaration',1,'p_primitive_type_declaration','arc_parser.py',194),
  ('primitive_type_declaration -> DATE_TYPE','primitive_type_declaration',1,'p_primitive_type_declaration','arc_parser.py',195),
  ('primitive_type_declaration -> LIST_TYPE LT type_declaration GT','primitive_type_declaration',4,'p_primitive_type_declaration','arc_parser.py',196),
  ('import -> IMPORT STRING','import',2,'p_import','arc_parser.py',205),
  ('namespace -> NAMESPACE IDENTIFIER LBRACE definitions RBRACE','namespace',5,'p_namespace','arc_parser.py',211),
  ('empty -> <empty>','empty',0,'p_empty','arc_parser.py',217),
]
