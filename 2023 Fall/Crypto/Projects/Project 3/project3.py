import binascii

def problem3():
    print('hello')

def converter(ciphertext):

    Binary = binascii.a2b_uu("x")
    return Binary

def problem4():
    binary = []
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
        '71fe029a1483123c76597691878459cca9363ac4faf68ceffc2e8d82e61897b98fc5e5f809e20b0c7756b2e08aab83bc5560e257'
    ]
    

    target = '71fe0680149d083b7c1e3996879a42d0a92e7780f6bf9fe8f42cd898e61cd2b8ccd9f3f35dff101d241da2eacff9cc8d5123fe5a897efbeda4974b'

    for c in ciphertext:
        binary.append(converter(c))
    print(binary)

#!/usr/bin/env python3

from typing import List
import binascii
import argparse

SPACE = ord(' ')


def main():
	parser = argparse.ArgumentParser(description='Many-time Pad Cracker')
	parser.add_argument(
		'--filename',
		type=str,
		help='Name of the file containing the ciphertexts (default: ciphertexts.txt)',
		default='ciphertexts.txt'
	)
	parser.add_argument(
		'-K', '--getkey',
		action='store_true',
		help='Print cracked key instead of cracked cleartexts.'
	)
	parser.add_argument(
		'-k', '--key',
		help='Encrypt messages with provided key.',
		default=''
	)
	args = parser.parse_args()
	try:
		with open(args.filename) as file:
			ciphertexts = [binascii.unhexlify(line.rstrip()) for line in file]
	except Exception as e:
		print('Cannot crack {} --- {}'.format(args.filename, e))
		raise SystemExit(-1)
	cleartexts = [bytearray(b'?' * len(line)) for line in ciphertexts]

	if args.key:
		decrypt(ciphertexts, cleartexts, args.key)
	else:
		crack(ciphertexts, cleartexts, args.getkey)


def decrypt(ciphertexts: List[bytes], cleartexts: List[bytearray], input_key: str) -> None:
	""" Decrypt ciphertexts using provided key and print cleartexts """
	key = binascii.unhexlify(input_key.rstrip())
	for row in range(len(ciphertexts)):
		for column in range(len(ciphertexts[row])):
			cleartexts[row][column] = ciphertexts[row][column] ^ key[column % len(key)]
		print(cleartexts[row].decode('ascii'))


def crack(ciphertexts: List[bytes], cleartexts: List[bytearray], getkey: bool) -> None:
	""" Try to decrypt ciphertexts and print cleartexts or key """
	max_length = max(len(line) for line in ciphertexts)
	key = bytearray(max_length)
	key_mask = [False] * max_length
	for column in range(max_length):  # go over characters from the beginning of lines
		pending_ciphers = [line for line in ciphertexts if len(line) > column]
		for cipher in pending_ciphers:
			if is_space(pending_ciphers, cipher[column], column):
				key[column] = cipher[column] ^ SPACE
				key_mask[column] = True
				i = 0
				for clear_row in range(len(cleartexts)):
					if len(cleartexts[clear_row]) != 0 and column < len(cleartexts[clear_row]):
						result = cipher[column] ^ pending_ciphers[i][column]
						if result == 0:
							cleartexts[clear_row][column] = SPACE
						elif chr(result).isupper():  # XOR with space return letter with swapped case
							cleartexts[clear_row][column] = ord(chr(result).lower())
						elif chr(result).islower():  # XOR with space return letter with swapped case
							cleartexts[clear_row][column] = ord(chr(result).upper())
						i += 1
				break
	if getkey:
		for pos in range(max_length):
			if key_mask[pos]:
				print('{0:02x}'.format(key[pos]), end='')
			else:
				print('__', end='')
		print()
	else:
		print('\n'.join(line.decode('ascii') for line in cleartexts))


def is_space(rows: List[bytes], current: int, column: int) -> bool:
	"""
	Return whether the current byte is encrypted space
	If the current byte is space, XORing with other bytes should return alpha char or zero (when space)
	"""
	for row in rows:
		result = row[column] ^ current
		if not (chr(result).isalpha() or result == 0):
			return False
	return True


if __name__ == '__main__':
	main()