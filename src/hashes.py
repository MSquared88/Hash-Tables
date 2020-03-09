import hashlib

n = 10
key = b'string'
key2 = 'string'.encode()
print(key2)

for i in range (n):
    print(hashlib.sha256(key).hexdigest() % 2)

for i in range (n):
    print(hash(key2))
