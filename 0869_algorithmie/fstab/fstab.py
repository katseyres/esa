FSTAB_PATH = "./fstab"

def read(file:str):
    with open(file, "r") as f:
        return f.read()

def required_parameters(raw_data:str):
    required_params = []
    filter = raw_data.split("<")[1:]
    for f in filter:
        required_params.append(f.split(">")[0])
    return required_params

def check_cmdline(cmdline:str, required_params:list):
    args = list(filter(lambda x: x is not "", line.split(" ")))
    return len(args) == len(required_params)

if "__main__" == __name__:
    raw_data = read(FSTAB_PATH)
    required_params = required_parameters(raw_data)
    print(len(required_params))

    active_lines = list(filter(lambda x: x.startswith("#") is False, raw_data.split("\n")))
    for line in active_lines:
        print(check_cmdline(line, required_params))
