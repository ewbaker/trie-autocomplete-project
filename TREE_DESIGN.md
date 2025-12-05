# Tree Design: Trie (Prefix Tree)

## 1. Tree Selection

I have chosen to implement a **Trie (Prefix Tree)**.

**Why:** Tries are specialized tree structures used for searching strings. unlike a Binary Search Tree, nodes in a Trie do not store keys associated with the node; instead, the node's position in the tree defines the key. This makes them exceptionally fast for prefix-based operations.

## 2. Use Cases

1. **Autocomplete Systems:** Predicting the rest of a word based on a typed prefix.

2. **Spell Checkers:** Rapidly verifying if a word exists in a dictionary.

3. **IP Routing:** Longest prefix matching in network routers.

## 3. Properties & Performance

*   **Unique Property:** All descendants of a node have a common prefix of the string associated with that node. The root is the empty string.

*   **Performance:** Lookup time depends on the length of the word ($L$), not the number of items in the database ($N$). This is usually O($L$), which is faster than O(log $N$) in BSTs for large datasets.

## 4. Interface Design

### `TrieNode` Class

*   **Attributes:**
    *   `children`: Dictionary mapping characters to child nodes.

    *   `is_end_of_word`: Boolean indicating if this path completes a valid word.

### `Trie` Class Interface

#### `insert(word: str) -> None`

Inserts a word into the trie.

*   **Time Complexity:** O($L$) where $L$ is word length.

*   **Space Complexity:** O($L$) in worst case (creating new nodes).

#### `search(word: str) -> bool`

Checks if a specific word exists in the trie.

*   **Time Complexity:** O($L$).

*   **Space Complexity:** O(1).

#### `starts_with(prefix: str) -> bool`

Checks if there is any word in the trie that starts with the given prefix.

*   **Time Complexity:** O($P$) where $P$ is prefix length.

*   **Space Complexity:** O(1).

#### `get_suggestions(prefix: str) -> List[str]`

Returns a list of all words in the trie that start with the given prefix.

*   **Time Complexity:** O($P + N \cdot K$) where $P$ is prefix length, $N$ is number of matches, $K$ is avg word length of matches.

*   **Space Complexity:** O($N \cdot K$) to store results.

## 5. Implementation Notes

I will use a Python Dictionary (Hash Map) for the `children` attribute in nodes. This allows for O(1) access to specific child characters, keeping the overall traversal linear relative to the word length.