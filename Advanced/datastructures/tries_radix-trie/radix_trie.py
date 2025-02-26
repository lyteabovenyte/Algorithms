"""
    The full implementation of the Radix-Tries and it's methods.
"""
class RTNode:
    def __init__(self, stores_key: bool):
        self.key_node = stores_key
        self._children = {}

class RTEdge:
    def __init__(self, destination: RTNode, key):
        self.destination = destination  # destination node from this edge
        self.label = key                  # the string stored in this edge

class Radix_trie:
    def __init__(self):
        self.root = RTNode(False)

    def _search(self, node: RTNode, s):
        """
            Method search takes an RTNode and the string key s to be
            searched. It returns True if s is stored in the trie, or False
            otherwise. We assume that node is never null; this is a
            reasonable assumption casue this method is implemented as an internal
            method, internally called by the RadixTrie's API search method.
            Remember that all edges can't have any prefix in common.
        """
        if s == "":
            return node.key_node
        (edge, common_prefix, s_suffix, edge_suffix) = self._match_edge(node, s)
        if edge is not None and edge_suffix == "":
            return self._search(node._children[common_prefix].destination, s_suffix)
        else:
            return False
        
    def _match_edge(self, node: RTNode, s):
        """
            Method _match_edge takes an RTNode and the string key s
            to be matched, It returns a tuple with the edge found, if any,
            the common prefix between s and the edge's label, and the suffix
            of those strings. We assume
            that node is never null and that s is not empty.
        """
        c = s[0]
        if c not in node._children:
            return (None, "", s, None)
        if node._children[c] == None:
            return (None, "", s, None)
        edge: RTEdge = node._children[c]
        prefix, s_suffix, suffix_edge = self._longest_common_prefix(s, edge.label)
        return (edge, prefix, s_suffix, suffix_edge)

    def _longest_common_prefix(self, s, label):
        """
            Method _longest_common_prefix takes two strings and
            return the prefix (common parts) and the rest of
            each string.
        """
        prefix, s_suffix, suffix_edge = "", "", ""
        i = 0
        while i < len(s) and i < len(label) and s[i] == label[i]:
            prefix += s[i]
            i += 1
        s_suffix += s[i:]
        suffix_edge += label[i:]
        return prefix, s_suffix, suffix_edge
    
    def _insert(self, node: RTNode, s): 
        """
            Method insert takes a RTNode and the string key s to be
            inserted. It returns nothing but has side effects on the trie.
            Again, we assume that node is never None.
        """

        if s == "":
            node.key_node = True
        edge, common_prefix, s_suffix, suffix_edge = self._match_edge(node, s)
        if edge == None:
            node._children[s[0]] = RTEdge(RTNode(True), s)
        elif suffix_edge == "":
            self._insert(edge.destination, s_suffix)
        else:
            bridge = RTNode(False)
            node._children[s[0]] = RTEdge(bridge, common_prefix)
            bridge._children[suffix_edge[0]] = RTEdge(edge.destination, suffix_edge)
            self._insert(bridge, s_suffix)
            

    def _is_pass_through(self, node: RTNode, parent: RTNode):
        """
            Method _is_pass_through checks if a node is a pass-through node.
            this only happens when a node is not a key node, it has only one
            outgoing edge and even it's parent only has one outgoing edge.
        """
        if (len(node._children > 1) 
        or node.key_node 
        or parent is None 
        or len(parent._children) > 1):
            return False
        return True
    
    def _remove(self, node: RTNode, s):
        """
            Method remove takes a node and the string to delete from the
            sub-tree rooted at node. It returns a couple of Booleans; the
            first one tells the caller if the key has been successfully deleted,
            and the second one is true if the last link followed becames a
            dangling empty branch and should be pruned.
        """
        if s == "":
            node.key_node = False
            return (True, node._children == 0)
        edge, common_prefix, s_suffix, edge_suffix = self._match_edge(node, s)
        if edge is not None and edge_suffix == "":
            dest = edge.destination
            deleted, should_prune = self._remove(dest, s_suffix)
            if deleted:
                if should_prune:
                    node._children[s[0]] = None
                elif self._is_pass_through(dest, node):
                    next_edge: RTEdge = self._get_path_through_edge(dest)
                    node._children[s[0]] = RTEdge(next_edge.destination, edge.label+next_edge.label)
            return (deleted, False)
        else:
            return (False, False)
                

    def _get_path_through_edge(self, node: RTNode):
        if len(node._children) != 1:
            return None
        return node._children[0]
    
    def _longest_prefix(self, node: RTNode, s, prefix):
        """
            Method _longest_prefix takes an RTNode, the string
            s to be searched and the string with path from root 
            to node; it returns the longest prefix of s 
            stored in the trie.
        """
        if s == "":
            if node.key_node:
                return prefix
            else: 
                return None
        edge, common_prefix, s_suffix, edge_suffix = self._match_edge(node, s)
        # Initialize this temporary variable to None. In case we can
        # traverse another edge, it will hold the result of the recursive call.
        result = None
        if edge is not None and edge_suffix == "":
            result = self._longest_prefix(edge.destination, s_suffix, prefix+common_prefix)
        if result is not None:
            return result
        elif node.key_node:
            return prefix
        else:
            return None
    
    def _search_node_with_prefix(self, node: RTNode, s): 
        """
            Method _search_node_with_prefix takes an RTNode and a
            string key s to be searched. returns the root of the subtree
            containing all the keys stored that have s as a prefix.
        """
        if s == "":
            return node
        edge, common_prefix, s_suffix, edge_suffix = self._match_edge(node, s)
        if edge is None:
            return None
        elif edge_suffix == "":
            return self._search_node_with_prefix(edge.destination, s_suffix)
        elif s_suffix == "":
            return edge.destination
        else:
            return None