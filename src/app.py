import os
import sys
import time
from trie import Trie

def load_data(trie, filepath):
    """Loads words from a file into the Trie."""
    if not os.path.exists(filepath):
        print(f"Error: File {filepath} not found.")
        return 0
    
    count = 0
    with open(filepath, 'r') as f:
        for line in f:
            word = line.strip().lower()
            if word:
                trie.insert(word)
                count += 1
    return count

def main():
    trie = Trie()
    print("------------------------------------------------")
    print("🌲  Welcome to the Trie Autocomplete System  🌲")
    print("------------------------------------------------")
    
    # 1. Load Data

    data_path = os.path.join(os.path.dirname(__file__), '../data/words.txt')
    print(f"Loading dictionary from {data_path}...")
    start_time = time.time()
    count = load_data(trie, data_path)
    end_time = time.time()
    print(f"Successfully loaded {count} words in {end_time - start_time:.4f} seconds.")

    # 2. Interactive Loop

    while True:
        print("\nOptions:")
        print("  1. Check Word (Search)")
        print("  2. Autocomplete (Suggestions)")
        print("  3. Add New Word")
        print("  4. Exit")
        
        choice = input("\nEnter choice (1-4): ").strip()

        if choice == '1':
            word = input("Enter word to check: ").strip().lower()
            found = trie.search(word)
            if found:
                print(f"✅ '{word}' is in the dictionary.")
            else:
                print(f"❌ '{word}' was NOT found.")

        elif choice == '2':
            prefix = input("Enter prefix to complete: ").strip().lower()
            if not prefix:
                print("Please enter a prefix.")
                continue
            
            # Demonstrate performance
            s_time = time.time_ns()
            suggestions = trie.get_suggestions(prefix)
            e_time = time.time_ns()
            
            duration_ms = (e_time - s_time) / 1_000_000
            
            if suggestions:
                print(f"\nFound {len(suggestions)} matches in {duration_ms:.3f}ms:")
                for s in suggestions[:10]: # Limit output to 10
                    print(f"  -> {s}")
                if len(suggestions) > 10:
                    print(f"  ...and {len(suggestions)-10} more.")
            else:
                print("No suggestions found.")

        elif choice == '3':
            word = input("Enter new word to add: ").strip().lower()
            trie.insert(word)
            print(f"Saved '{word}' to memory.")

        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()