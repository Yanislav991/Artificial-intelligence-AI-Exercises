class Node():
    def __init__(self, freq, char=None,  left=None, right=None):
        self.left = left
        self.right = right
        self.char = char
        self.freq = freq

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


text = input()
freq = {}

for c in text:
    if c in freq:
        freq[c] += 1
    else:
        freq[c] = 1

freq = sorted(freq.items(), key=lambda item: item[1])

nodes = list(map(create_node, freq))

huffman_tree = create_huffman_tree(nodes)

print(huffman_tree)