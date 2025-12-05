from typing import List, Optional

class TrieNode:
    """A node in the Trie structure."""
    def __init__(self):
        # Maps a character to the next TrieNode
        self.children = {}
        # True if this node represents the end of a valid word
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        Time Complexity: O(L) where L is length of word
        """
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word: str) -> bool:
        """
        Returns True if the word is in the trie.
        Time Complexity: O(L) where L is length of word
        """
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

    def starts_with(self, prefix: str) -> bool:
        """
        Returns True if there is any word in the trie that starts with the given prefix.
        Time Complexity: O(P) where P is length of prefix
        """
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

    def get_suggestions(self, prefix: str) -> List[str]:
        """
        Returns a list of all words starting with the prefix.
        Time Complexity: O(P + N) where P is prefix len and N is total chars in all matching words
        """
        node = self.root
        suggestions = []
        
        # Step 1: Navigate to the end of the prefix

        for char in prefix:
            if char not in node.children:
                return [] # Prefix not found
            node = node.children[char]
        
        # Step 2: Recursively find all words from this node
        
        self._dfs(node, prefix, suggestions)
        return suggestions

    def _dfs(self, node: TrieNode, current_word: str, suggestions: List[str]):
        """Helper DFS function to traverse tree."""
        if node.is_end_of_word:
            suggestions.append(current_word)
        
        for char, child_node in node.children.items():
            self._dfs(child_node, current_word + char, suggestions)