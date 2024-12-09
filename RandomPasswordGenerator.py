import random
import string


password_len = 8
charvalues = string.ascii_letters + string.digits + string.punctuation

password = ""
for i in range (password_len):
    password += random.choice(charvalues)



print ("your random password is",password)

