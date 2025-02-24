"""
    implementation of a trie data structure. (prefix trie)
"""
import string

class Node:
    def __init__(self, stores_key=False):
        """
            Constructing a Node in trie.
            for each letter we have a children which is initialized
            with None, the edges specify the word and Nodes just 
            hold a tiny piece of information, just True or False
            to detemine that the path is a key (word) or not.
        """
        # Using Hash table for mapping
        # for constant time lookup on each edge.
        self._children = {} # chr: Node
        for ch in list(string.ascii_letters):
            self._children[ch] = None
        self.key_node = stores_key


class Trie:
    def __init__(self):
        """
            Constructing a Trie with a single Node named root.
        """
        self.root = Node(False)

    
    def _search(self, node: Node, s): 
        """
            Method search is a standalone recursive function that takes a Trie
            node and a string that should be searched, it return True
            if the string is stored in the Trie and False otherwise.

            We Assume that node is never None.
        """
        if s == "":
            return node.key_node
        #! PERFORMANCE BOTTLENECK!
        #! can we pass a reference to the string?
        #! and an index to the start of the next string.
        c, tail = s[0], s[1:] 
        if node._children[c] == None:
            return False
        return self._search(node._children[c], tail)

    def search(self, s):
        if self.root == None:
            return False
        return self._search(self.root, s)

    def _search_node(self, node: Node, s):
        """
            Method search_node is basically a variant of Method _search
            but instead of just returning True or False, it'll return the
            node itself. 
        """
        if s == "":
            return node #
        c, tail = s[0], s[1:]
        if node._children[c] == None: 
            return None
        return self._search(node._children[c], tail)

    def _insert(self, node: Node, s):
        """
            Method _insert a an internal insert method used in public insert.
            doesn't return but has side effect, making the node a key_node node.

            It Assumes that the node is not None
        """
        if s == "":
            node.key_node = True
            return
        c, tail = s[0], s[1:]
        if node._children[c] != None:
            return self._insert(node._children[c], tail)
        else:
            return self._add_new_branch(node, s)

    def _add_new_branch(self, node: Node, s):
        """
            Method _add_new_branch takes a trie node and the string key s
            for the new branch.

            It Assumes that the node is never None.
        """
        if s == "":
            node.key_node = True
            return
        c, tail = s[0], s[1:]
        node._children[c] = Node(False) # add an emtpy node.
        return self._add_new_branch(node._children[c], tail)

    def insert(self, s):
        if self.root == None:
            return False
        return self._insert(self.root, s)
    
    def _ordinary_remove(self, s):
        """
            Method remove simply search for the node containing
            string 's' and set it's key_node to False and makes
            it intermediate node.

            Warning: this method may leave dangling branches
            and leak memory.
        """
        node = self._search_node(self.root, s)
        if node == None or node.key_node == False:
            return False
        node.key_node = False
        return True

    def _remove_with_pruning(self, node: Node, s):
        """
            Method remove_with_pruning is the preferred remove method of Trie.
            it's implementing a pruning method that will remove
            dangling nodes while backtracking the path traversed
            during search.
            it returns a couple of Booleans, the first one tells the caller
            that the key has been successfully deleted, the second one is
            True if the last link followed becomes a dangling empty branch
            and should be pruned.
            Good for dynamic arrays with many calls to remove,
            it'll remove dangling branches and free up unneccesary
            memory for dangling branches.
        """
        if s == "":
            deleted = node.key_node
            node.key_node = False
            # return that the operation was successful and
            # if this node is to be pruned.
            return (deleted, len(node._children) == 0)
        c, tail = s[0], s[1:]
        if node._children[c] is not None:
            (deleted, should_prune) = self._remove_with_pruning(node._children[c], tail)
            if deleted and should_prune:
                node._children[c] = None
                if node.key_node is not None or len(node._children) > 0:
                    should_prune = False
                    return (deleted, should_prune)
        return (False, False) # at this point the search was unsuccessful and we return.

    def remove(self, s):
        if self.root == None:
            return (False, False)
        return self._remove_with_pruning(self.root, s)

    def _insert_using_longest_prefix(self, s):
        """
            rewriting _insert by leveraging the Method longest_common_prefix

            Method _insert_using_longest_prefix is a two step operation:
            1. finding the longest prefix already in the trie.
            2. create a new branch and add the string.
        """
        # we need to tune _longest_prefix method to also return the last node.
        def _longest_prefix_with_node(node: Node, s, prefix):
            if s == "":
                if node.key_node:
                    return prefix
                else:
                    return None
            c, tail = s[0], s[1:]
            if node._children[c] == None:
                return prefix if node.key_node else None
            else:
                result = _longest_prefix_with_node(node._children[c], tail, prefix+c)
                if result != None:
                    return result
                elif node.key_node:
                    return prefix
                else:
                    return None
        
        p, last_node = _longest_prefix_with_node(self.root, s, "")
        new_branch = s.removeprefix(p)
        return self._add_new_branch(last_node, new_branch)

    def _longest_prefix(self, node: Node, s, prefix):
        """
            Method _longest_prefix takes a trie node, the string key
            to be searched, and a string with the path from root to node.
            it returns the longest prefix of s stored in the trie.
        """
        if s == "":
            if node.key_node:
                return prefix
            else:
                return None

        c, tail = s[0], s[1:]
        if node._children[c] == None:
            return prefix if node.key_node else None
        else:
            result = self._longest_prefix(node._children[c], tail, prefix+c)
            if result != None:
                return result
            elif node.key_node:
                return prefix
            else:
                return None

    def longest_prefix(self, s):
        return self._longest_prefix(self.root, s, "")

    def key_starting_with(self, prefix: str):
        """
            Method key_starting_with takes a prefix string and
            returns all the keys stored in the trie which starts
            with that specific prefix.
        """
        node = self._search_node(self.root, prefix)
        if node == None:
            return []
        return self._all_keys(self.node)

    def _all_keys(self, node: Node, prefix):
        """
            Method _all_keys takes a trie node and the string
            prefix corresponding to the path from the trie's root
            to node. 
            It returns the list of strings s(k)=prefix+suffix(k),
            where suffix(k) is the k-th string contained in this subtree.
        """
        keys = []
        if node.key_node:
            keys.append(prefix)
        for c in node._children.keys():
            keys = keys + self._all_keys(node._children[c], prefix+c)
        return keys