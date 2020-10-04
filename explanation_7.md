Complexity of this algorithm consists of two parts: adding words and finding suffixes. 

Time complexity:
RouteTrieNode.insert - O(1)
RouteTrie.insert - O(k) k - number of parts in path
RouteTrie.find - O(b*m) m - URLs length in terms of parts separated by slashes (assuming dictionary lookup time complexity of O(n), b - average branching factor
Router.add_handler - O(k) based on RouteTrie.insert.
Router.lookup - O(k*m) based on RouteTrie.find.

Space complexity:
RouteTrieNode.insert - O(1)
RouteTrie.insert - O(k) k - number of parts in path
RouteTrie.find - O(1)
Router.add_handler - O(k) based on RouteTrie.insert.
Router.lookup - O(1) based on RouteTrie.find.

Total space needed to store all paths is O(n*k) - worst case, where n - number of paths to add. On practice much less space is required since a lot of paths share the same prefixes.