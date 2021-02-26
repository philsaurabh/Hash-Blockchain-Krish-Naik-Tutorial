import hashlib

str1="test string 123"
hashedval1 = hashlib.sha256(str1.encode()) 
print("Using SHA 256")
print(hashedval1)

print(hashedval1.hexdigest())


hashedval2=hashlib.sha384(str1.encode()) 
print("Using SHA 384")
print(hashedval2)
print(hashedval2.hexdigest())


hashedval3=hashlib.sha224(str1.encode())
print("Using SHA 224")
print(hashedval3) 
print(hashedval3.hexdigest())


hashedval4=hashlib.sha512(str1.encode())
print("Using SHA 512")
print(hashedval4) 
print(hashedval4.hexdigest())

hashedval5=hashlib.sha1(str1.encode()) 
print("Using SHA 1")
print(hashedval5)
print(hashedval5.hexdigest())

