import math
import matplotlib.pyplot as plt
# Universal stuff
def readable (temp):
    readable = []
    for t in temp:
        readable.append(alphabet[t])
    return (f'C Letters: {"".join(readable)}')

alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", 
            "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", ]
'''
Part 1:

a. Define affine cipher in more detial

b. What is the size of the keyspace for a fixed integer n?

c. Encrypt "CRYPTOISFUN" where:
    n=26
    function: c=5p + 9 mod 26

d.

e. Ans: c=ap + b mod 53

'''


def cryptoisfun():
    n = 26
    p = "CRYPTOISFUN"
    c = []
    p1 = []
    for letter in p:
        val = find_index(letter)
        p1.append(val)
        c.append((((5*val) + 9) % n))
    print("Problem 1\n\n")
    print("1c.")
    print(f"Plaintext: {p}")
    print(f'Plaintext Numerical: {p1}')
    print(f"Ciphertext Numerical: {c}")
    print(f"Ciphertext Readable: {readable(c)}\n")



def affine():
    ciphertext = "QJKESREOGHGXXREOXEO"

    m = 26
    p2 = 19
    c2 = 7

    p1 = 14
    c1 = 4

    nums = find_a_b(p1, c1, p2, c2,m)
    plaintext1 = []
    ciphertextNumerical = []
    for letter in ciphertext:
        i = find_index(letter)
        ciphertextNumerical.append(i)
        d = decrypt(i,nums)
        plaintext1.append(d)

    
    print("1d.")
    print(f'(a = {nums[0]}, b={nums[1]})')
    print(f"Ciphertext: {ciphertext}")
    print(f"Ciphertext Numerical: {ciphertextNumerical}")
    print(f"Plaintext Numerical: {plaintext1}")
    print(f"Plaintext: {readable(plaintext1)}")

def find_relatives():
    ans = []
    for i in range(26):
        if math.gcd(i,26) == 1:
            ans.append(i)
    return ans

def find_index(letter):
    i = 0
    for i in range(0,26):
        if alphabet[i] == letter:
            return i
        
def find_a_b(p1, c1, p2, c2,m):
    nums = find_relatives()
    for i in nums: #a
        for j in range(m): #b
            ans = ((i*p1) + j) % m
            if(ans==c1):
                ans2 = ((i*p2) + j) % m
                if(ans2==c2):
                    return [i,j]
                
                
def decrypt(num,ans):
    i = 0
    for i in range(0,26):
        if (((ans[0]*i) + ans[1]) % 26) == num:
            return i
        
def encrypt(num, ans):
    e = ((ans[0]*num) + ans[1] ) % 26
    return e

#cryptoisfun()
#affine()
'''

for t in temp:
    e = encrypt(t, ans)
    c.append(e)
print(c)
'''
'''
Part 2:

a. Describe Substiution Cipher

b. What is the size of key space?

c. 

'''
def combine(ans, ciphertext):
    res = []
    print(ans)
    for c in ciphertext:
        res.append(ans[c])
    return res

def attempt_to_decrypt(bd, md, ciphertext):
    hint = "LIBERTY"
    p = 0
    new_assignment = {}
    used =[]
    ans = ""

    for key,value in md.items():
        temp = 100
        ktemp=""
        if hint in "".join(ans):
            return ''.join(ans)

        for k,v in bd.items():
            if k in used:
                continue
            elif k == key:
                continue
            else:
                t = abs(value[1] - v)
                if((t < 2.3) and (k not in used)):
                    if abs(t) < abs(temp):
                        temp  = t
                        ktemp = k 
        used.append(ktemp)
        new_assignment[key] = ktemp

    ans = combine(new_assignment, ciphertext)

    return "NO"
                


def create_dictionary(letters, numbers):
    d = {}
    for i in range(len(letters)):
        temp = letters[i]
        d[temp] = numbers[i]
    return d

def substitution(cipher = "TNFOSFOZSWPZLOCGQAOZWAGQRPJZPNABCZPQDOGRAMTHARAXTBAGZJOGMTHARAVAPZW"):
    cipherList = []
    hint = "LIBERTY"
    A = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", 
            "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", ]
    
    freq = [8.2, 1.5, 2.8, 4.2, 12.7, 2.2, 2.0, 6.1, 7.0, 0.1, 0.8, 4.0, 2.4, 6.7,
                 7.5, 1.9, 0.1, 6.0, 6.3, 9.0, 2.8, 1.0, 2.4, 0.1, 2.0, 0.1]

    base_dictionary = create_dictionary(A, freq)

    cipher_frequency = {}
    for c in cipher:
        cipherList.append(c)

    for i in range(len(cipherList)):
        f = cipherList.count(cipherList[i])
        cipher_frequency[cipherList[i]] = [f, (f/len(cipherList)*100)]

    #print(base_dictionary)
    #print(f'\n{cipher_frequency }')

    print(attempt_to_decrypt(base_dictionary, cipher_frequency, cipherList))
    exit()
    keys = []
    value_count = []
    value_percent = []
    for key, value in cipher_frequency.items():
        keys.append(key)
        value_count.append(value[0])
        value_percent.append(value[1])

    subKey = {
        "A": "E",
        "B": "",
        "C": "",
        "D": "",
        "E": "",
        "F": "",
        "G": "",
        "H": "",
        "I": "",
        "J": "",
        "K": "",
        "L": "",
        "M": "",
        "N": "",
        "O": "",
        "P": "",
        "Q": "",
        "R": "",
        "S": "",
        "T": "",
        "U": "",
        "V": "",
        "W": "",
        "X": "",
        "Y": "",
        "Z": "",
    }
    temp = []
    for i in range(len(cipherList)):
        if subKey[cipherList[i]] != "":
            temp.append(subKey[cipherList[i]])
        else:
            temp.append(cipherList[i])

    print(cipher)
    print(f"\n{temp}")

    for i in range(len(temp)):
        if temp[i] == "E":
            t = temp[i-3:i+4]
            if t.count("E") == 1:
                print(t)
    
    
    graph(keys, value_count, value_percent)




def graph(keys, value_count, value_percent):
    plt.bar(
        keys,value_count
    )
    plt.xlabel('Letters')
    plt.ylabel('Counts')
    plt.title("Test")
    plt.show()

    plt.bar(
        keys,value_percent
    )
    plt.xlabel('Letters')
    plt.ylabel('Percent')
    plt.title("Test")
    plt.show()

#substitution()
