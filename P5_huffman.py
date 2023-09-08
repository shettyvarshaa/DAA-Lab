



import heapq
from collections import Counter

class Node:
    def __init__(self, freq, symbol, left=None, right=None):
        self.freq = freq
        self.symbol = symbol
        self.left = left
        self.right = right
        self.huff = ''
    
    def __lt__(self, other):
        return self.freq < other.freq
    
def printNodes(node, val=''):
    if not node:
        return
    newVal = val + str(node.huff)
    if not node.left and not node.right:
        print(f"{node.symbol} -> {newVal}")
    printNodes(node.left, newVal)
    printNodes(node.right, newVal)

string = input("Enter the string: ").lower()
res = Counter(string)
nodes = [Node(freq, char) for char, freq in res.items()]
heapq.heapify(nodes)

while len(nodes) > 1:
    left = heapq.heappop(nodes)
    right = heapq.heappop(nodes)
    left.huff = '0'
    right.huff = '1'
    new_node = Node(left.freq + right.freq, left.symbol + right.symbol, left, right)
    heapq.heappush(nodes, new_node)

printNodes(nodes[0])




#OR

""" import heapq
from collections import defaultdict

class HuffmanNode:
    def __init__(self, character=None, frequency=None):
        self.character = character
        self.frequency = frequency
        self.left = None
        self.right = None
    
    def __lt__(self, other):
        return self.frequency < other.frequency

def build_frequency_table(text):
    frequency_table = defaultdict(int)
    for char in text:
        frequency_table[char] += 1
    return frequency_table

def build_huffman_tree(frequency_table):
    heap = []
    for char, frequency in frequency_table.items():
        node = HuffmanNode(char, frequency)
        heapq.heappush(heap, node)
    
    while len(heap) > 1:
        left_child = heapq.heappop(heap)
        right_child = heapq.heappop(heap)
        parent = HuffmanNode(frequency=left_child.frequency + right_child.frequency)
        parent.left = left_child
        parent.right = right_child
        heapq.heappush(heap, parent)
    
    return heap[0]

def build_huffman_codes(huffman_tree):
    codes = {}
    
    def build_codes_helper(node, current_code):
        if node is None:
            return
        if node.character:
            codes[node.character] = current_code
            return
        build_codes_helper(node.left, current_code + "0")
        build_codes_helper(node.right, current_code + "1")
    
    build_codes_helper(huffman_tree, "")
    return codes

def encode_text(text, codes):
    encoded_text = ""
    for char in text:
        encoded_text += codes[char]
    return encoded_text

def decode_text(encoded_text, huffman_tree):
    decoded_text = ""
    current_node = huffman_tree
    for bit in encoded_text:
        if bit == "0":
            current_node = current_node.left
        else:
            current_node = current_node.right
        if current_node.character:
            decoded_text += current_node.character
            current_node = huffman_tree
    return decoded_text

def main():
    text = "Hello World"
    print("Original Text: ", text)
    frequency_table = build_frequency_table(text)
    huffman_tree = build_huffman_tree(frequency_table)
    codes = build_huffman_codes(huffman_tree)
    encoded_text = encode_text(text, codes)
    print("Encoded text:", encoded_text)
    decoded_text = decode_text(encoded_text, huffman_tree)
    print("Decoded text:", decoded_text)

if __name__ == "__main__":
    main()
 """