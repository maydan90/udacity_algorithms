from collections import defaultdict


# Represents a single node in the Trie
class TrieNode:
    # Initialize this node in the Trie
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.is_word = False

    # Add a child node in this Trie
    def insert(self, char):
        return self.children[char]

    def suffixes(self, suffix=''):
        # Recursive function that collects the suffix for
        # all complete words below this point
        suffixes = []
        if suffix != '' and self.is_word:
            suffixes.append(suffix)
        for char, node in self.children.items():
            suffixes.extend(node.suffixes(suffix + char))
        return suffixes


# The Trie itself containing the root node and insert/find functions
class Trie:
    # Initialize this Trie (add a root node)
    def __init__(self):
        self.root = TrieNode()

    # Add a word to the Trie
    def insert(self, word):
        # start from the root node
        current_node = self.root
        # insert every letter in the word one by one into the Trie
        for char in word:
            current_node = current_node.insert(char)
        # the end of the word is reached
        current_node.is_word = True

    # Find the Trie node that represents this prefix
    def find(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return TrieNode()
            node = node.children[char]
        return node


MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym",
    "fun", "function", "factory",
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.insert(word)

print(MyTrie.find('tr').suffixes())
print(MyTrie.find('trght').suffixes())
print(MyTrie.find('').suffixes())
print(MyTrie.find('f').suffixes())

MyTrie1 = Trie()
wordList = []
for word in wordList:
    MyTrie1.insert(word)

print(MyTrie1.find('tr').suffixes())
print(MyTrie1.find('').suffixes())
print(MyTrie1.find('f').suffixes())
