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

def display_hosts(hosts):
    return json.dumps(hosts, sort_keys=True, indent=4)

def get_hosts(hosts:list, param=""):
    if param is "":
        return hosts
    if not dict(hosts[0]).__contains__(param):
        return False
    
    return list(map(lambda x: x[param], hosts))

def hosts_counter(hosts):
    return len(hosts)

def match_counter(needle:str, haystack:list):
    check_pattern = list((needle in h for h in haystack))
    return len(list(filter(lambda x: x is True, check_pattern)))

if __name__ == "__main__":
    hosts = ssh_hosts(PATH_HOSTS)

    # print(hosts_counter(hosts))
    # print(get_hosts(hosts, param="Host"))
    # print(display_hosts(hosts))
    # print(match_counter("etd-esa", list(map(lambda x: x["User"], hosts))))
