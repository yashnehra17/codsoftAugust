import secrets
import string
import random

lower = string.ascii_lowercase  
upper = string.ascii_uppercase
digits = string.digits
special = string.punctuation
allChars = lower + upper + digits + special
password = ""

pwLen = int(input("How long should the password be? "))
minUpper = int(input("Minimum Upper Case: "))
minLower = int(input("Minimum Lower Case: "))  # Corrected typo
minDigits = int(input("Minimum Numbers: "))    # Corrected typo
minSpec = int(input("Minimum Special: "))      # Corrected typo

for i in range(minUpper):
    password += random.choice(upper)

for i in range(minLower):
    password += random.choice(lower)

for i in range(minDigits):
    password += random.choice(digits)

for i in range(minSpec):
    password += random.choice(special)

remaining = pwLen - minLower - minUpper - minDigits - minSpec  # Corrected typo

for i in range(remaining):
    password += random.choice(allChars)

password = list(password)
random.shuffle(password)
print("".join(password))

