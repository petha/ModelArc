import os

imports = []

def read_file(filename):
    with open(filename, 'r') as f:
        return f.read()
    
def preprocessor(filename):
   base_path = os.path.dirname(os.path.abspath(filename))
   filename = os.path.basename(filename)
   return preprocess(filename, base_path)

def preprocess(filename, base_path):
    global imports
    
    if filename in imports:
        return ""
    imports.append(filename)

    full_path = os.path.join(base_path, filename)
    source_code = read_file(full_path)
    
    expanded_code = []

    lines = source_code.splitlines()
    for line in lines:
        if line.startswith("import"):
            import_file = line.split()[1].strip('"')
            imported_code = preprocess(import_file, os.path.dirname(full_path))
            expanded_code.append(imported_code)
        else:
            expanded_code.append(line)
    
    return "\n".join(expanded_code)


