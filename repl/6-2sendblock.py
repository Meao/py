"""

На основе кода, размещенного в файле b_chain.py, реализовать корутину (генератор), позволяющий с помощью метода send(), возвращать новый блок. Кроме механизма возврата нового блока требуется создать механизм, позволяющий вернуть историю сгенерированных блоков. 

"""

import random
from hashlib import sha3_512
import binascii

genesis_block = bytearray([0 for i in range(0, 64)])
baseblock = genesis_block

def b_history(b_chain, limit):
  for i in range(limit):
    tosend = next(random_b)
    block = senddata.send(tosend)
    print("link=" + binascii.hexlify(block[0:64]).decode("iso-8859-1"))
    print("data=" + block[64:192].decode("iso-8859-1"))
    print("digest=" + binascii.hexlify(block[192:256]).decode("iso-8859-1"))
    print("======================")

def randomblock():
  while True:
    ml = sha3_512()
    ml.update(str(random.randint(0, 1e18)).encode("iso-8859-1"))
    yield bytearray(ml.hexdigest().encode("iso-8859-1"))


def signedblock(baseblock):
  block = yield
  while True:
    block_data = baseblock + block
    digest = sha3_512()
    digest.update(block_data)
    baseblock = digest.digest()
    yield block_data + digest.digest()


limit = 3


# def chain(limit):
#   b_chain = []
#   random_b = randomblock()
#   senddata = signedblock(genesis_block)
#   next(senddata)
#   for i in range(limit):
#     tosend = next(random_b)
#     result = senddata.send(tosend)
#     b_chain += result 
#   return b_chain

# b_chain = chain(limit)

random_b = randomblock()
senddata = signedblock(genesis_block)
next(senddata)
limit = 3
b_chain = []
for i in range(limit):
  tosend = next(random_b)
  result = senddata.send(tosend)
  b_chain += result 


b_history(b_chain, limit) 
