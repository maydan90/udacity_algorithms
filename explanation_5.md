Complexity of this algorithm consists of two parts: adding words and finding suffixes. 
Time complexity:
TrieNode.insert - O(1)
TrieNode.suffixes - O(n) n - number of words added to the Trie
Trie.insert - O(k) k - length of word to add.
Trie.find - O(k)

Space complexity:
TrieNode.insert - O(1)
TrieNode.suffixes - O(n) n - number of words added to the Trie
Trie.insert - O(k) k - length of word to add.
Trie.find - O(1)

Total space needed to store all words is O(n*k) - worst case, where n - total number of words added. On practice much less space is required since a lot of words share the same prefixes.