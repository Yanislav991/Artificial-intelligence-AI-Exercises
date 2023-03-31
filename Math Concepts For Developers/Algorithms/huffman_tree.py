class Node():
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

    def children(self):
        return (self.left, self.right)

    def nodes(self):
        return (self.left, self.right)

    def __str__(self):
        return '%s_%s' % (self.left, self.right)


text = input()
freq ={}

for c in text:
    if c in freq:
        freq[c] +=1
    else:
        freq[c] = 1

freq = sorted(freq.items(), key=lambda item: item[1])
nodes = []

while len(freq) != 0:
    newNode = Node()
    if(freq[0] is not None):
        first_min = freq[0]
        newNode.left = first_min
        if(2<len(freq)):
            second_min = freq[1]
            newNode.right = second_min
            freq.remove(freq[1])    
        freq.remove(freq[0])
    value = newNode.left[1]
    if newNode.right is not None:
        value += newNode.right[1]
    nodes.append((newNode, value))

print(nodes)