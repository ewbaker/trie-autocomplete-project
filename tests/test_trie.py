import unittest
import sys
import os

# Add the src directory to the python path so we can import the Trie
sys.path.append(os.path.join(os.path.dirname(__file__), '../src'))

from trie import Trie

class TestTrie(unittest.TestCase):
    def setUp(self):
        """Runs before every test method."""
        self.trie = Trie()

    def test_insert_and_search(self):
        """Test that words can be inserted and found."""
        self.trie.insert("apple")
        self.assertTrue(self.trie.search("apple"))
        self.assertFalse(self.trie.search("app"))  # "app" is a prefix, not a word yet
        self.assertFalse(self.trie.search("orange"))

    def test_starts_with(self):
        """Test the prefix checking capability."""
        self.trie.insert("banana")
        self.assertTrue(self.trie.starts_with("ban"))
        self.assertTrue(self.trie.starts_with("banana"))
        self.assertFalse(self.trie.starts_with("band"))

    def test_get_suggestions_basic(self):
        """Test if autocomplete returns correct suggestions."""
        words = ["cat", "caterpillar", "catacombs", "dog"]
        for w in words:
            self.trie.insert(w)
        
        suggestions = self.trie.get_suggestions("cat")
        
        # Should contain 3 words
        self.assertEqual(len(suggestions), 3)
        self.assertIn("cat", suggestions)
        self.assertIn("caterpillar", suggestions)
        self.assertIn("catacombs", suggestions)
        self.assertNotIn("dog", suggestions)

    def test_get_suggestions_empty_prefix(self):
        """Test suggestions for a prefix that doesn't exist."""
        self.trie.insert("hello")
        suggestions = self.trie.get_suggestions("xyz")
        self.assertEqual(suggestions, [])

    def test_case_sensitivity_handling(self):
        """Ensure the Trie handles strings exactly as given (case sensitivity depends on usage)."""
        # Our implementation is case-sensitive by default, app.py handles the lowercasing.
        self.trie.insert("Apple")
        self.assertTrue(self.trie.search("Apple"))
        self.assertFalse(self.trie.search("apple")) 

if __name__ == '__main__':
    unittest.main()