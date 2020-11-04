import requests
import argparse
import sys
import json

banner = """
=====================
Fast Sonar Consult CLI
====================="""
print(banner)

parser = argparse.ArgumentParser(add_help=True)
parser.add_argument("-d", "--domain", help="Domain for osint", required=True)
parser.add_argument("-i", "--ip", help="Show Ip of Targets", action="store_true")
parser.add_argument("-s", "--subdomains", help="Show Subdomains of Targets", action="store_true")
args = parser.parse_args()

SONAR = "https://sonar.omnisint.io/all/"

def getinfo(domain):
	print(f"[!] [target] {domain}\n")
	req = requests.get(SONAR+domain)
	return req.text

def beautifulResponse(response):
	response = json.loads(response)
	for data in response:
		if args.ip == True and args.subdomains == True:
			print(f"[+] [subdomain::value] {data['name']}::{data['value']}")
		elif args.subdomains == True:
			print(f"[+] [subdomain] {data['name']}")
		elif args.ip == True:
			print(f"[+] [value] {data['value']}")
		else:
			print(f"[+] [name] {data['name']}")
			print(f"[-] [domain] {data['domain']}")
			print(f"[i] [subdomain] {data['subdomain']}")
			print(f"[i] [value] {data['value']}")
			print(f"[i] [type] {data['type']}")
			print("")

def main():
	beautifulResponse(getinfo(args.domain))

if __name__ == '__main__':
	main()
