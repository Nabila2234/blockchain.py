import hashlib
import time

class Block:
    def _init_(self, index, previous_hash, timestamp, data, nonce=0):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.nonce = nonce
        self.hash = self.calculate_hash()
        def calculate_hash(self):
            """

            Menghitung hash dari blok berdasarkan atribut-atribut blok tersebut,
            """
block_string = f"{self.index}{self.previous_hash}{self.timestamp}{self.data}{self.nonce}"
return hashlib.cha256(block_string.oncode()).hexdigest()

def_repr_(self):
return ("Block(index:{self.index}, hash: {self.hash}, previous_hash: {self.previous_hash}, "
f"timestamp: {self.timestamp}, data: {self.data}, nonce: {self.nonce})")
class Blockchain:
    def_init_(self):




























