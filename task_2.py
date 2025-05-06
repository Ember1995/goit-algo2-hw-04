from trie import Trie
from typing import List

class LongestCommonWord(Trie):
    def find_longest_common_word(self, strings: List[str]) -> str:
        if not isinstance(strings, list) or not all(isinstance(s, str) for s in strings) or not strings:
            raise TypeError(f"Illegal argument: strings = {strings} must be a non-empty list of strings")

        # Додаємо всі слова до Trie
        for word in strings:
            self.put(word)

        current_node = self.root
        longest_prefix = ""

        # Проходимо по Trie зверху вниз:
        # Поки в поточному вузлі лише один нащадок
        # і вузол не є кінцем жодного слова
        while (
            current_node is not None and 
            len(current_node.children) == 1 and 
            current_node.value is None
        ):
            # Отримуємо єдиного нащадка — пару (символ, наступний вузол)
            child_item = next(iter(current_node.children.items()))
            char = child_item[0]         # символ ребра
            next_node = child_item[1]    # вузол, у який веде ребро

            # Додаємо символ до префікса
            longest_prefix += char

            # Переходимо до наступного вузла
            current_node = next_node

        return longest_prefix

if __name__ == "__main__":
    # Тести
    trie = LongestCommonWord()
    strings = ["flower", "flow", "flight"]
    print(trie.find_longest_common_word(strings) == "fl")

    trie = LongestCommonWord()
    strings = ["interspecies", "interstellar", "interstate"]
    print(trie.find_longest_common_word(strings) == "inters")

    trie = LongestCommonWord()
    strings = ["dog", "racecar", "car"]
    print(trie.find_longest_common_word(strings) == "")