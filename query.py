import urllib.request
import json
from argparse import ArgumentParser
from termcolor import colored


def format_serverdata(data, indent=0):
    result = ""
    for item in data:
        if isinstance(item, list):
            result += format_serverdata(item, indent+1)
        elif isinstance(item, dict):
            for key, value in item.items():
                if isinstance(value, dict):
                    result += " " * 4 * indent + colored(f"{key}: ", "white", attrs=["bold"])
                    result += format_serverdata([value], indent+1)
                elif isinstance(value, list):
                    result += " " * 4 * indent + colored(f"{key}: ", "white", attrs=["bold"])
                    result += format_serverdata(value, indent+1)
                else:
                    result += " " * 4 * indent + colored(f"{key}: {value}", "white", attrs=["bold"]) + "\n"
        else:
            result += " " * 4 * indent + colored(item, "red", attrs=["bold"]) + "\n"
    return result


def get_servers(name=None, address=None, branch="production", official="0", platform="mac", page="0"):
    if name is not None and address is not None:
        raise ValueError("Only one argument per query is supported.")
    if name is not None:
        url = f"https://servers.alderongames.com/pathOfTitans?filter[name]={name}&filter[branch]={branch}&filter[official]={official}&filter[platform]={platform}&page={page}"
    elif address is not None:
        url = f"https://servers.alderongames.com/pathOfTitans?filter[ip_address]={address}&filter[branch]={branch}&filter[official]={official}&filter[platform]={platform}&page={page}"
    else:
        raise ValueError("Must provide either name or address.")
    with urllib.request.urlopen(url) as url:
        if url.getcode() == 200:
            serverdata = json.load(url)
            return serverdata
        else:
            raise ValueError(f"Failed to retrieve server data (status code {url.getcode()}).")


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("-n", "--name", dest="name",
                        help="Get servers by name", metavar="NAME")
    parser.add_argument("-ip", "--address", dest="address",
                        help="Get servers by IP address", metavar="ADDRESS")
    parser.add_argument("-b", "--branch", dest="branch", default="production",
                        help="Filter by branch (default: production)", metavar="BRANCH")
    parser.add_argument("-o", "--official", dest="official", default="0",
                        help="Filter by official (default: 0)", metavar="OFFICIAL")
    parser.add_argument("-p", "--platform", dest="platform", default="mac",
                        help="Filter by platform (default: mac)", metavar="PLATFORM")
    parser.add_argument("-pg", "--page", dest="page", default="0",
                        help="Page of results to retrieve (default: 0)", metavar="PAGE")
    args = parser.parse_args()
    try:
        servers = get_servers(name=args.name, address=args.address, branch=args.branch,
                              official=args.official, platform=args.platform, page=args.page)
        print(format_serverdata(servers["data"]))
        print(colored("INFO: Wait 5-9 seconds until your next query.", "cyan"))
    except ValueError as e:
        print(colored(f"ERROR: {e}", "red"))