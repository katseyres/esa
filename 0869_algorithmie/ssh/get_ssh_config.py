import json

PATH_TEMPLATE = "ssh_config_template"
PATH_HOSTS = "ssh_config"

def ssh_config_template(file:str):
    output = {}
    
    with open(file, "r") as f:
        configs = f.read().split("Host *\n")[1].split("\n")

        for config in configs:
            if config[0] is "#":
                config = config[1:].strip()
                output[config.split(" ")[0]] = config.split(" ")[1:]

    return output

def ssh_hosts(file:str):
    output = []
    
    with open(file, "r") as f:
        raw_hosts = f.read().split("\n\n")
        for raw_host in raw_hosts:
            configs = raw_host.split("\n")
            host = {}
            for config in configs:
                if len(config.strip()) > 0:
                    print(f"> {config.strip()}")
                    host[config.strip().split(" ")[0]] = config.strip().split(" ")[1]
            output.append(host)

    return output

# configs = ssh_config_template(PATH_TEMPLATE)
# for config in configs:
#     print(f"{config} {configs[config]}")

hosts = ssh_hosts(PATH_HOSTS)
print(json.dumps(hosts, sort_keys=True, indent=4))