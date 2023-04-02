#!/usr/bin/env python3

import base64
import hashlib


base64ver = "GXU7y+PcmpkcjmggtiG+VeGy2Ye6KcCHbIy2GTYJfSDxHNYu" # give me the hash here!
# and don't forget the fill the 'passwords.txt' file!


print("\nCreated this script while doing pentest without a GPU; anyway I had to try just a small list, not much.")
print("\nBut, wanted to share it on github and it is here!")
print("\nFor now, it is only cracking rabbit_password_hashing_sha256 type hashes but, if you change few places it is gonna work well :)\n\n")
print("If you have questions: @sercansayitoglu \n\n")


def calculateHash(line):
	print(line + "                ", end="\r")
	utf8 = line.encode('utf-8').hex()
	prepare = salt + utf8
	prepare = bytes.fromhex(prepare)
	newSha256 = str(hashlib.sha256(prepare).hexdigest())
	if newSha256 == sha256:
		print("\nFOUND THE PASSWORD!\nPassword is: " + line + "\n")


decoded = base64.standard_b64decode(base64ver).hex()
salt = base64.standard_b64decode(base64ver).hex()[0:8]
sha256 = base64.standard_b64decode(base64ver).hex()[8:]


print("THE HASH: " + base64ver)
print("DECODED: " + decoded)
print("SALT: " + salt)
print("SHA256: " + sha256)
print("\n")


file = open("passwords.txt", "r", encoding="iso-8859-1")
linebyline = file.readlines()
file.close()


for line in linebyline:
	line = line.strip()
	if calculateHash(line):
		exit()

print("Finished...            ")
