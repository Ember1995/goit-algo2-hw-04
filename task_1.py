from trie import Trie

class Homework(Trie):
    def count_words_with_suffix(self, suffix) -> int:
        if not isinstance(suffix, str):
            raise TypeError(f"Illegal argument for countWordsWithPrefix: suffix = {suffix} must be a string")
        
        all_words = self._get_all_words()
        return sum(1 for word in all_words if word.endswith(suffix))
    
    def _get_all_words(self):
        result = []
        self._dfs(self.root, "", result)
        return result
    
    def _dfs(self, node, path, result):
        if node.value is not None:
            result.append(path)
        for char, child in node.children.items():
            self._dfs(child, path + char, result)

    def has_prefix(self, prefix) -> bool:
        if not isinstance(prefix, str):
            raise TypeError(f"Illegal argument for countWordsWithPrefix: prefix = {prefix} must be a string")

        current = self.root
        for char in prefix:
            if char not in current.children:
                return False
            current = current.children[char]
        return True

if __name__ == "__main__":
    trie = Homework()
    words = ["apple", "application", "banana", "cat"]
    for i, word in enumerate(words):
        trie.put(word, i)

    # Перевірка кількості слів, що закінчуються на заданий суфікс
    print(trie.count_words_with_suffix("e") == 1)  # apple
    print(trie.count_words_with_suffix("ion") == 1)  # application
    print(trie.count_words_with_suffix("a") == 1)  # banana
    print(trie.count_words_with_suffix("at") == 1)  # cat

    # Перевірка наявності префікса
    print(trie.has_prefix("app") == True)  # apple, application
    print(trie.has_prefix("bat") == False)
    print(trie.has_prefix("ban") == True)  # banana
    print(trie.has_prefix("ca") == True)  # cat
