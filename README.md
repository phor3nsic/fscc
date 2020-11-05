# fscc
**_Fast Sonar Consult CLI_**

<p align="center">
  <img width="15%" height="15%" src="icon/icon.jpg">
</p>

_References for project: [Crobat](https://github.com/cgboal/sonarsearch)_

## Install

Clone the repository and execulte:

```
git clone https://github.com/phor3nsic/fscc.git
cd fscc
python3 fscc.py -h


=====================
Fast Sonar Consult CLI
=====================
usage: fscc.py [-h] -d DOMAIN [-r REVERSE] [-i] [-s]

optional arguments:
  -h, --help            show this help message and exit
  -d DOMAIN, --domain DOMAIN
                        Domain for osint
  -r REVERSE, --reverse REVERSE
                        Reverse IP
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
python3 fscc.py -d hackerone.com -i

[+] [value] xxx.xxx.xxx.xxx
[+] [value] xxx.xxx.xxx.xxx
[+] [value] xxx.xxx.xxx.xxx
[+] [value] xxx.xxx.xxx.xxx
[+] [value] xxx.xxx.xxx.xxx
[+] [value] hacker0x01.github.io

```

Reverse Ip:

```
python3 fscc.py -d hackerone.com -r xxx.xxx.xxx

[?] by1.recoms.net
[?] by4.recoms.pro
[?] dns.abcd.domains
[?] dns.abcd.support
[?] dns2.wfolio.ru
[?] kz1.recoms.net
[?] kz4.recoms.pro
[?] ns-sel4.axelname.ru
[?] ns2.mediaweb.ru

...
```

###### tags: `sonar cli` `sonar project` `subdomains` `enum` `osint` `ips` `bugbounty` `enumeration` `pentest` `dns` `sonar-api` `osint-tool` 