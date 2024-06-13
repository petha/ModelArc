class ASTNode:
    def __init__(self, type, children=None, value=None):
        self.type = type
        self.children = children if children else []
        self.value = value

class ProcessNode(ASTNode):
    def __init__(self, name, tasks):
        super().__init__('process', children=tasks, value=name)

class TaskNode(ASTNode):
    def __init__(self, name, actions):
        super().__init__('task', children=actions, value=name)

class ActionNode(ASTNode):
    def __init__(self, name, command, inputs=None, outputs=None):
        super().__init__('action', value=name)
        self.command = command
        self.inputs = inputs or []
        self.outputs = outputs or []

def build_ast(parse_tree):
    if not parse_tree:
        return None
    if parse_tree[0] == 'program':
        return ASTNode('program', children=[build_ast(child) for child in parse_tree[1:]])
    elif parse_tree[0] == 'namespace':
        return ASTNode('namespace', children=[build_ast(child) for child in parse_tree[2]], value=parse_tree[1])
    elif parse_tree[0] == 'process':
        tasks = [build_ast(task) for task in parse_tree[2]]
        return ProcessNode(parse_tree[1], tasks)
    elif parse_tree[0] == 'task':
        actions = [build_ast(action) for action in parse_tree[2]]
        return TaskNode(parse_tree[1], actions)
    elif parse_tree[0] == 'action':
        return ActionNode(parse_tree[1], parse_tree[2], parse_tree[3], parse_tree[4])
    return ASTNode(parse_tree[0], value=parse_tree[1])
