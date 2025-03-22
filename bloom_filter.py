import base64
import hashlib

class BloomFilter:
    def __init__(self, size=1000):
        self.size = size
        self.bit_array = [0] * size

    def _hash(self, item):
        """Use SHA256 for stable hashing"""
        return int(hashlib.sha256(item.encode()).hexdigest(), 16) % self.size

    def add(self, item):
        index = self._hash(item)
        self.bit_array[index] = 1

    def __contains__(self, item):
        index = self._hash(item)
        return self.bit_array[index] == 1

    def get_state(self):
        return base64.b64encode(bytes(self.bit_array)).decode("utf-8")

    def load_state(self, state):
        self.bit_array = list(base64.b64decode(state))
