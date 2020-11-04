# fscc
_Fast Sonar Consult CLI_

## Install

Cone repository and execulte:

```
git clone https://github.com/phor3nsic/fscc.git
cd fscc
python3 fscc.py -h


=====================
Fast Sonar Consult CLI
=====================
usage: fscc.py [-h] -d DOMAIN [-i] [-s]

optional arguments:
  -h, --help            show this help message and exit
  -d DOMAIN, --domain DOMAIN
                        Domain for osint
  -i, --ip              Show Ip of Targets
  -s, --subdomains      Show Subdomains of Targets

```

## Usage

Get All Infos:

```
python3 fscc.py -d hackerone.com

[+] [name] hackerone.msk.ru
[-] [domain] hackerone
[i] [subdomain] 
[i] [value] xxx.xxx.xxx.xxx
[i] [type] a

[+] [name] hackerone.me
[-] [domain] hackerone
[i] [subdomain] 
[i] [value] xxx.xxx.xxx.xxx
[i] [type] a

...
```

Get Subdomains and Ip's:

```
python3 fscc.py -d hackerone.com -i -s

[+] [subdomain::value] a.ns.hackerone.com::xxx.xxx.xxx.xxx
[+] [subdomain::value] api.hackerone.com::xxx.xxx.xxx.xxx
[+] [subdomain::value] api.hackerone.com::xxx.xxx.xxx.xxx
[+] [subdomain::value] api.hackerone.pro::xxx.xxx.xxx.xxx
[+] [subdomain::value] b.ns.hackerone.com::xxx.xxx.xxx.xxx
[+] [subdomain::value] docs.hackerone.com::hacker0x01.github.io
[+] [subdomain::value] email.hackerone.cf::hackerone.cf

...
```

Get Subdomains:
```
python3 fscc.py -d hackerone.com -s

[+] [subdomain] a.ns.hackerone.com
[+] [subdomain] api.hackerone.com
[+] [subdomain] api.hackerone.com
[+] [subdomain] api.hackerone.pro
[+] [subdomain] b.ns.hackerone.com
[+] [subdomain] docs.hackerone.com

...
```

Get Ip's:
```
python3 fscc.py -d hackerone.com -s

[+] [value] xxx.xxx.xxx.xxx
[+] [value] xxx.xxx.xxx.xxx
[+] [value] xxx.xxx.xxx.xxx
[+] [value] xxx.xxx.xxx.xxx
[+] [value] xxx.xxx.xxx.xxx
[+] [value] hacker0x01.github.io

```

###### tags: `sonar cli` `sonar project` `subdomains` `enum` `osint` `ips`