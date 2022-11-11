import urllib.request, json
from argparse import ArgumentParser


def getbyname(name, branch="production", version="22351", official="0", platform="mac", page="0"):
  with urllib.request.urlopen("https://servers.alderongames.com/pathOfTitans?filter[name]=" +name+ "&filter[branch]=" +branch+ "&filter[version]=" +version+ "&filter[official]="+official+"&filter[platform]="+platform+"&page="+page) as url:
    serverdata = json.load(url)
  return serverdata

def getbyaddr(addr, branch="production", version="22351", official="0", platform="mac", page="0"):
  with urllib.request.urlopen("https://servers.alderongames.com/pathOfTitans?filter[ip_address]=" +addr+ "&filter[branch]=" +branch+ "&filter[version]=" +version+ "&filter[official]="+official+"&filter[platform]="+platform+"&page="+page) as url:
    serverdata = json.load(url)
  return serverdata

parser = ArgumentParser()
parser.add_argument("-n", "--name", dest="name",
                    help="Get Serers by Name", metavar="NAME")
parser.add_argument("-ip", "--address", dest="address",
                    help="Get Servers by IP-Address", metavar="ADDRESS")
  
args = parser.parse_args()

name = ((vars(args)['name']))
address = ((vars(args)['address']))

if name and address:
  print ("Only one Argument per query is support ATM")
  exit()

if name:
  parsed = getbyname(name)
  print(json.dumps(parsed, indent=4)+"\t\n")
  print ("INFO: wait 5-9 Secs till your next query...")

if address:
  parsed = getbyaddr(address)
  print(json.dumps(parsed, indent=4)+"\t\n")
  print ("INFO: wait 5-9 Secs till your next query...")



