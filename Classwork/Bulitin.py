'''import platform
print(platform.system(),platform.release(),platform.processor())

import sys
print(sys.argv)
print(sys.path)
print(sys.version)
print(sys.exit())'''

import math
print(math.sqrt(6))
print(math.pow(4,6))
print(math.ceil(19.8))
print(math.floor(87.9))
print(math.fabs(7))
print(math.factorial(8))
print(math.gcd(7,9))
print(math.log(7,8))
print(math.sin(30))
print(math.cos(60))
print(math.tan(90))
print(math.degrees(30))
print(math.radians(60))

import random
print(random.random())
print(random.randint(1,7))
print(random.uniform(1,9))
names=['vikash','hemanth','manikanta','sheshu','adithya']
print(random.choice(names))
print(random.choices(names,k=4))
print(random.shuffle(names))
print(random.seed(19))