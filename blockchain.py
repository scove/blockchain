from hashlib import *

class Block():
    def __init__(self, index, data, previous_hash):
        self.index = index
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.hash_block()

    def hash_block(self):
        encrypt = sha1()
        try:
            encrypt.update(str(self.index).encode('utf-8') +
                           str(self.data).encode('utf-8') +
                           str(self.previous_hash).encode('utf-8'))
        except Exception as i:
            print(i)
        return encrypt.hexdigest()

    def getData(self):
        return self.data
    def getPrevious(self):
        return self.previous_hash
    def getHash(self):
        return self.hash

def firstBlock():
     return Block(0, "Hello World", "0")
def nextBlock(previous, d):
    index = previous.index + 1
    data = d
    hash_block = previous.hash
    return Block(index, data, hash_block)
 
a = firstBlock()
b = nextBlock(a, "Second Block")
print(a.getData())
print(a.getHash())
print(a.getPrevious())

print(b.getData())
print(b.getHash())
print(b.getPrevious())
