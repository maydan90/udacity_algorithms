from collections import defaultdict


# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self, root_handler):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root = RouteTrieNode(root_handler)

    def insert(self):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path
        pass

    def find(self):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        pass


# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self, handler=None):
        # Initialize the node with children as before, plus a handler
        self.children = defaultdict(RouteTrieNode)
        self.handler = handler

    def insert(self, handler):
        # Insert the node as before
        return self.children[handler]


# The Router class will wrap the Trie and handle
class Router:
    def __init__(self, root_handler='root handler', not_found_handler='not found handler'):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!
        self.root = RouteTrie(root_handler)
        self.not_found_handler = not_found_handler

    def add_handler(self):
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie
        pass

    def lookup(self):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler
        pass

    def split_path(self):
        # you need to split the path into parts for
        # both the add_handler and lookup functions,
        # so it should be placed in a function here
        pass