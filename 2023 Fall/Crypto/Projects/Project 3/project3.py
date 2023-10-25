from typing import List
import binascii
from random import randrange


def problem3():
	'''
	Author: Payge Winfield
	Assignment: 3
	Problem: 3
	Date: 10/23/2023

	Purpose: To encrypt 10 hardcoded messages with a randomly generated key. Export messages, key, and ciphertext to .txt file
	'''
	# 10 hardcoded messages
	message = [
			'Because I am happy', 
			'Why is six afraid of sever', 
			'because sever eight nine',
			'sometimes computer programmers like to to drink tea',
			'speaking of tea',
			'My FAVORITE tea is pistachio ice cream team',
			'I believe the children are our future teach them well and let them lead the way',
			'Happy BIRTHDAY',
			'What is your favorite food',
			'mine is popcorn at the moment'
			]
	
	ciphertext = []
	
	# Random Key
	key = ''

	max_len = 0
	for m in message:
		if len(m) > max_len:
			max_len = len(m)
	
	i = 0
	while i < max_len+10:
		r = randrange(32, 122)
		if((r == 32) or (r in range(65,91)) or (r in range(97,122))):
			key += chr(r)
			i+=1
	
	print(key)
	hex_key = key.encode("utf-8").hex()
	ord_key = []
	print(hex_key)

	for i in key:
		ord_key.append(ord(i))
	print(ord_key)

	# Now it's time to encrypt!
	
	for m in message:
		cipher = []
		temp = []
		for i in range(len(m)):
			c = hex(ord_key[i]^ord(m[i]))
			c = c.replace('0x', "")
			if len(c) <2:
				c = '0' + c
			temp.append(c)
		ciphertext.append(temp)

	print(ciphertext)
	
	# File to store data
	file = 'myResults.txt'

	with open('myResults.txt', 'w') as f:
		f.write('Plain text in hex: \n\n')
		for p in message:
			f.write(f'{p}\n')
		f.write(f'\nKey: {hex_key} \n')
		f.write('\nCiphertexts: \n')
		for c in ciphertext:
			cipher = "".join(c)
			f.write(f'{cipher}\n\n')




def problem4(known):
	# Source used for inspiration and understanding:
	# https://www.thecrowned.org/the-one-time-pad-and-the-many-time-pad-vulnerability

	max_len = 0
	min_len = 600
	cipher_ord = []
	ciphertext = [
		'71fe1ace4389087266117cd7c98c4182851b3acff3b086e3f83f94d6eb05c4ba85d8e1fa14f11d1c3b568ff6cff5c09c5d67ef5c9c71b7eeb3d45a5154ab17b83e071ce9d8988adb4afedf46a840',
		'71fe1ace559a1e7266117cd7ce8745d7be2e74c3f0f68eeef57e8884e607debf81dfa0f012f95819681ae7f29fe4839b5175ef5e8760bef0b9d44b504eba12b22f5404f89dd085d550a48865a14f9b15a94dabe609ca2df2cccf210cefdb1af5389719795e1f0179cb77c5c456954d88f3',
		'72fe069c51c81a20775928c7879d4fd2a93c3acff3f69fe5fe2e9493a303d9ea98c4e5b60ae40a146058e7c787fbd09a1474e25dc865b5e6af865d4a40a61bfd384e06e0cfc1ccd356ff8853ac438905fa5fe3fd41cb3bbc8ac9',
		'67e543885b9a5b2267177084cf8453ccb8633ad7fdb39de5b13f8a93a304d6bf8bc4f4ef5def110b6f56a3e186e2c68c1470ef5c9c2ffbd6a291571e40ba1afd3b4b1fe0c4cbccc15df5dc07b043da01fa6ae4fd158f37b3c0cd',
		'71fe029a148c1236320d7192878a59cfbc3a6ec5e7f68befb13196d6ea1ec4ea81d9e3fe50ea0f196d02a2f7cfe2c29c5577e35d8630baf6ea80465b01aa1abc394f57a1f4ccccda59ff8846e44b8805bb5cabe608c231f2dec8364ae7d90ab4358c5c3a421b06',
		'6ef914ce5989152b321a769ad79c42c7be6f6ad2fab19de1fc339d84f04ad3a589dfa0ff09ab0c196f13e7e780b4c097556ded57c871fbeea393464a01aa0ab1381848cfd2d6898918efc046b00b8940bb08e3f313cb23b3dfd8645cfcd80ff82489',
		'71fe1ace4389087266117cd7c4865bd2b93b7fd2b5a58ce9f4308c9ff01e97ab82cbf2ef5dfc101d6a56b3fb8ab4d08b4167ef5c9c30b8f0ab97455b45e81efd364605e49ddb83df48eedc42b60c900fb14db4b229ca74b6c4d96442e1c34df8288f5c3a450a527ecc7c82865b8e',
		'71fe029a148c1437615978d7c58854dbec2c75cde5a39be5e37e9b97ef0697a285dfa0f01cff101d764983f29bf5',
		'71fe1ace50875b31730d6ad7cb8640c7ec3c73d4e1bf81e7b13796d6e518d8a4988ceff05dff101d2415a8fe9fe1d79a4623eb5e8430bfe3b3d442514faf40fd18420be0c8cb89924cf3cd5ee448950efd5cabe500c120f2d9d26440ebc34de029811977430b01748276d79012955cc6a65aebb9054becda5c9278',
		'71fe029a1483123c76597691878459cca9363ac4faf68ceffc2e8d82e61897b98fc5e5f809e20b0c7756b2e08aab83bc5560e257',
		'71fe0680149d083b7c1e3996879a42d0a92e7780f6bf9fe8f42cd898e61cd2b8ccd9f3f35dff101d241da2eacff9cc8d5123fe5a897efbeda4974b'
    ]

	key = []
	target = '71fe0680149d083b7c1e3996879a42d0a92e7780f6bf9fe8f42cd898e61cd2b8ccd9f3f35dff101d241da2eacff9cc8d5123fe5a897efbeda4974b'
	i = 0

	

	# The for loop does the following:
	# 1. Sets max_len to equal the longest cipher len
	# 2. Creates a 2D array of ciphertext and their ords with row = ciphertext and col = ord values
	for cipher in ciphertext:
		cipher_ord.append(binascii.unhexlify(cipher))
		if len(cipher_ord[i]) > max_len:
			max_len = len(cipher_ord[i])
		i+=1

	key = bytearray(max_len)
	cleartexts = [bytearray(b'?' * len(line)) for line in ciphertext]
	space = ord(' ')

	for col in range(max_len):  # 
		pending_ciphers = [line for line in cipher_ord if len(line) > col]  # only grab the lines that have x cols
		for row in pending_ciphers: # for each unhexified-cipher in ciphertext
			if is_space(pending_ciphers, row[col], col): 
				key[col] = row[col] ^ space
				break

	print(key)
	decrypt(key, cipher_ord, known)
	   
def is_space(ciphers, current_cipher_col, col):
	for c in ciphers:
		result = c[col] ^ current_cipher_col
		if not (chr(result).isalpha() or result == 0):
		#if 0 < result < 65:
			return False 
	return True 
 
def decrypt(key, cipher_ord,known):
	store = []
	x=0
	cval = 0
	for target in cipher_ord:
		p = bytearray(b'?'* len(target))
		for i in range(len(target)):
			if key[i] != 0:
				res = key[i] ^ target[i] 
				p[i] = ord(chr(res))
			else: 
				if x ==0:
					store.append(i)
				if cval == 5:
					for arr in known:
						if arr[0] == i:
							temp = (ord(arr[1]))
							key[i] = temp^target[i]
							p[i] = temp
		x+=1

		cval+=1
		print(p)
	'''
	t = 1
	for target in cipher_ord:
		print(f'T: {t}')
		for i in store:
			if len(target) > i:
				print(target[i], i)
		print('\n\n')
		t+=1
	'''

c5 = [[1,'o'],
	  [10,'o'],
	  [11,'m'],
	  [13, 'u'],
	  [14, 't'],
	  [17, ' '], 
	  [22, 'r'],
	  [23, 'a'],
	  [36, 't'],
	  [39, 'a'],
	  [40, 'k'],
	  [41, 'e']]
#problem4([])
#problem4(c5)
problem4([])