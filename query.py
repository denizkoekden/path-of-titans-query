import urllib.request
import json
from argparse import ArgumentParser


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
            if "data" in serverdata:
                serverdata = {"data": serverdata["data"]}
            else:
                serverdata = {"data": []}
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
        print(json.dumps(servers, indent=4))
        print("INFO: Wait 5-9 seconds until your next query.")
    except ValueError as e:
        print(f"ERROR: {e}")
