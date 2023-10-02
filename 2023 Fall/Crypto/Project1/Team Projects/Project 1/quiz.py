def readable (temp):
    readable = []
    for t in temp:
        readable.append(alphabet[t])
    return (f'C Letters: {"".join(readable)}')

def encrypt(num, ans):
    e = ((ans[0]*num) + ans[1] ) % 26
    return e
s = "IFYOUBOWATALLBOWLOW"
alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", 
            "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", ]
k = [11,6]
m = 26

ciphertext = []

for i in range(len(s)):
    temp = alphabet.index(s[i])
    ciphertext.append(encrypt(temp,k))
y = readable(ciphertext)

x='QJKESREOGHGXXREOXEO'
print(y)