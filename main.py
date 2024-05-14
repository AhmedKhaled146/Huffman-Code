import heapq
from collections import defaultdict

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(freq_table):
    priority_queue = [Node(char, freq) for char, freq in freq_table.items()]
    heapq.heapify(priority_queue)

    while len(priority_queue) > 1:
        left = heapq.heappop(priority_queue)
        right = heapq.heappop(priority_queue)

        internal_node = Node(None, left.freq + right.freq)
        internal_node.left = left
        internal_node.right = right

        heapq.heappush(priority_queue, internal_node)

    return priority_queue[0]

def build_frequency_table(text):
    freq_table = defaultdict(int)
    for char in text:
        freq_table[char] += 1
    return freq_table

def build_huffman_codes(node, current_code="", codes=None):
    if codes is None:
        codes = {}

    if node is not None:
        if node.char is not None:
            codes[node.char] = current_code
        build_huffman_codes(node.left, current_code + "0", codes)
        build_huffman_codes(node.right, current_code + "1", codes)

    return codes

def encode(text, codes):
    encoded_text = ""
    for char in text:
        encoded_text += codes[char]
    return encoded_text

def decode(encoded_text, root):
    decoded_text = ""
    current_node = root

    for bit in encoded_text:
        if bit == "0":
            current_node = current_node.left
        else:
            current_node = current_node.right

        if current_node.char is not None:
            decoded_text += current_node.char
            current_node = root

    return decoded_text

# Example usage:
text = "hello world"
freq_table = build_frequency_table(text)
huffman_tree_root = build_huffman_tree(freq_table)
huffman_codes = build_huffman_codes(huffman_tree_root)
encoded_text = encode(text, huffman_codes)
decoded_text = decode(encoded_text, huffman_tree_root)

print(f"Original Text: {text}")
print(f"Encoded Text: {encoded_text}")
print(f"Decoded Text: {decoded_text}")


# Output
# Original Text: hello world
# Encoded Text: 11100001010110111101111001010001
# Decoded Text: hello world