Complexity of this algorithm consists of two parts: adding words and finding suffixes. 
Time complexity: adding - O(n*k) where n is the number of paths to add, k - average length of each path (separation by slashes).
find - O(k)
Space complexity: O(n*k) worst case that all parts in paths are different.