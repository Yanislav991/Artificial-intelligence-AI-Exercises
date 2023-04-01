class Node():
    def __init__(self, freq, char=None,  left=None, right=None):
        self.left = left
        self.right = right
        self.char = char
        self.freq = freq

    def children(self):
        return (self.left, self.right)

    def __str__(self):
        return '%s_%s' % (self.left, self.right)

def create_node(t):
    return Node(t[1], t[0])

def create_huffman_tree(nodes):
    while len(nodes) >= 1:
        left_node = nodes.pop(0)
        if (len(nodes) == 0):
            return left_node
        right_node = nodes.pop(0)
        nodes.append(Node(left_node.freq + right_node.freq,
                     left=left_node, right=right_node))
        nodes = sorted(nodes, key=lambda item: item.freq)

def huffman_code_tree(node, left=True, binString=''):
    if node.char is not None:
        return {node.char: (node.freq, binString)}
    (l, r) = node.children()
    d = dict()
    d.update(huffman_code_tree(l, True, binString + '0'))
    d.update(huffman_code_tree(r, False, binString + '1'))
    return d

def calc_tree_size(dict):
    values = dict.values()
    result = 0
    for v in values:
        result += v[0]*len(v[1])
        result += v[0]
    result += len(values)*8
    return result



text = 'BCAADDDCCACACAC'
freq = {}

for c in text:
    if c in freq:
        freq[c] += 1
    else:
        freq[c] = 1

freq = sorted(freq.items(), key=lambda item: item[1])
nodes = list(map(create_node, freq))
huffman_tree = create_huffman_tree(nodes)

encoded_values = huffman_code_tree(huffman_tree)
totalSize = 0
initial_size = len(text) * 8
tree_size = calc_tree_size(encoded_values)

print(' Char | Huffman code ')
print('----------------------')
for (char, frequency) in freq:
    print(' %-4r |%12s' % (char, encoded_values[char]))

print(f"Intial Size -> {initial_size}")
print(f"Tree Size -> {tree_size}")
