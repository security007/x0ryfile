#!/usr/bin/python3

# File data encryptor with xor algorithm
# Coded By Security007

import random
import string
import argparse
import codecs
import sys
import hashlib
import time

banner = """
++++++++++++++++++++++++++++++++++++++++++++++++++++++++
+                   [ XoryFile ]                       +
+      (File data encryptor with xor algorithm)        +
+               Coded By Security007                   +
++++++++++++++++++++++++++++++++++++++++++++++++++++++++
"""
print(banner)
ext_type = ".x0r"
parser = argparse.ArgumentParser()
parser.add_argument("-F", "--file", help="File to encrypt/decrypt",required=True)
parser.add_argument("-E", "--encrypt", help="Encrypt file",action="store_true")
parser.add_argument("-D", "--decrypt", help="Decrypt file (required key argument)",action="store_true")
parser.add_argument("-K", "--key", help="Key to decrypt file")
parser.add_argument("-O", "--output", help="Output file",required=True)
args = parser.parse_args()

def zuper():
	alpa = "10"
	return "".join([random.choice(alpa) for x in range(70)])

class x0r_enc:
	def __init__(self,char,keyz=None):
		self.char = char
		self.keyz = keyz	
		self.alpa = string.ascii_letters+string.digits+string.ascii_uppercase
	
	def create_key(self):
		return "".join([random.choice(self.alpa) for x in range(len(self.char))])
		
	def this(self):
		try:
			if self.keyz != None:
				k3y = self.keyz
				new_char = codecs.decode(self.char,"hex").decode()
				return {"Data":"".join([chr(ord(new_char[x]) ^ ord(k3y[x])) for x in range(len(new_char))])} #dec
			else:
				k3y = self.create_key()
				return {"Data":codecs.encode("".join([chr(ord(self.char[x]) ^ ord(k3y[x])) for x in range(len(self.char))]).encode(),"hex").decode(),"Key":k3y} #enc
		except IndexError:
			return "[!] Data and key length are not same"				


def main():
	if (args.decrypt):
		if (args.key):
			try:
				op = open(args.file,"r")
				baca = op.read()
			except FileNotFoundError:
				print("[!] File not found : "+args.file)
				sys.exit()
			for x in range(100):
				sys.stdout.write("\r\r[XoryFile] %s" % str(zuper()))
				sys.stdout.flush()
				time.sleep(0.05)
			go = x0r_enc(baca,args.key)
			hasil = go.this()
			out = args.output
			buka_out = open(out,"w")
			tulis_hasil = buka_out.write(hasil['Data'])
			buka_out.close()
			print("\n[+] Saved as : "+out+" [Decrypted]")
		else:
			print("[!] Key is required")
	elif(args.encrypt):
		try:
			op = open(args.file,"r")
			baca = op.read()
		except FileNotFoundError:
			print("[!] File not found : "+args.file)
			sys.exit()
		for x in range(100):
			sys.stdout.write("\r\r[XoryFile] %s" % str(zuper()))
			sys.stdout.flush()
			time.sleep(0.05)		
		go = x0r_enc(baca)
		hasil = go.this()
		out = args.output+ext_type
		buka_out = open(out,"w")
		tulis_hasil = buka_out.write(hasil['Data'])
		buka_out.close()
		print("\n[+] Saved as : "+out+" [Encrypted]")
		print("[^] Key : "+hasil['Key']+" [You must decrypt file using this key]")
		
	else:
		print("[!] Required -e/--encrypt or -d/--decrypt argument")
		
if __name__ == "__main__":
	main()



