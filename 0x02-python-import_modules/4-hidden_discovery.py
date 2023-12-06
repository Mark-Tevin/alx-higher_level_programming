import hidden_4

def print_module_names():
    module_names = [name for name in dir(hidden_4) if not name.startswith("__")]
    module_names.sort()

    for name in module_names:
        print(name)

if  __name__ ++ "main__":
    print_module_names()
