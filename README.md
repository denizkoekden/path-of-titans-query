# Path of Titans - Query Helper
This Project aims to generate an Query for the Game "Path of Titans".
So you can check, if the given Servers is online and check if all Settings and Mods have been set correctly.


## Usage/Examples

### Python Usage:

Needs python3 installed.

#### Lookup Server "MyServer":

```shell
python3 query.py -n MyServer
```
#### Lookup Server with IP-Address "127.0.0.1":
```shell
python3 query.py -ip 127.0.0.1
```

### PHP Usage:

Put .php-File on Webserver and use as follow

#### Lookup Server with IP-Address "127.0.0.1":

```shell
https://myserver.tld/potquery/potquery.php?addr=127.0.0.1
```
#### Lookup Server with Name "MyServer":

```shell
https://myserver.tld/potquery/potquery.php?name=MyServer
```



## Roadmap

- Beautify Results

- Add more filters and params

