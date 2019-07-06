#!/usr/bin/env python3

import base64
import binascii
import hashlib
import concurrent.futures
import multiprocessing

base64ver = "GXU7y+PcmpkcjmggtiG+VeGy2Ye6KcCHbIy2GTYJfSDxHNYu" # give me the hash here!
# and don't forget the fill the 'passwords.txt' file!



print("\nCreated this script when doing pentest without a GPU; anyway I had to try just a small list, not much.")
print("\n\tBut, wanted to share it on github and it is here!")
print("\nFor now, it is only cracking rabbit_password_hashing_sha256 type hashes but, if you change few places it is gonna work well :)\n\n")
print("\tIf you have questions: @sercansayitoglu \n\n")

global finishTheJob
finishTheJob = False

def deleteLineFeed(line):
    hexValue = binascii.hexlify(bytes(line, encoding="utf-8"))
    hexValue = str(hexValue, "ascii")
    hexValue = hexValue.replace("0a", "")
    hexValue = binascii.unhexlify(hexValue)
    stringValue = str(hexValue, "ascii")
    stringValue = stringValue.replace("\n", "")
    stringValue = stringValue.replace("\r", "")
    return stringValue


def calculateHash(line, a):
	line = deleteLineFeed(line)
	utf8 = line.encode('utf-8').hex()
	prepare = salt + utf8
	prepare = bytes.fromhex(prepare)
	newSha256 = str(hashlib.sha256(prepare).hexdigest())
	if newSha256 == sha256:
		print("\nFOUND THE PASSWORD!\nPassword is: " + line + "\n\nTurning off the engine slowly..")
		global finishTheJob
		finishTheJob = True
		exit()
	print("Attempt: " + str(a) + " : " + line + "                ", end="\r")


decoded = base64.standard_b64decode(base64ver).hex()
salt = base64.standard_b64decode(base64ver).hex()[0:8]
sha256 = base64.standard_b64decode(base64ver).hex()[8:]
print("Core number: " + str(multiprocessing.cpu_count()))
print("DECODED: " + decoded)
print("SALT: " + salt)
print("SHA256: " + sha256)


file = open("passwords.txt", "r", encoding="utf-8")
linebyline = file.readlines()
file.close()

a = 1
with concurrent.futures.ThreadPoolExecutor(max_workers=multiprocessing.cpu_count()) as threadPoolCalculate:
	for line in linebyline:
		if finishTheJob:
			exit()
		threadPoolCalculate.submit(calculateHash, line, a)
		a = a + 1
	try:
		concurrent.futures.wait(threadPoolCalculate, return_when=concurrent.futures.ALL_COMPLETED)
	except:
		pass