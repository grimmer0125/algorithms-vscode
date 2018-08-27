class TreeNode:
    def __init__(self, x):
        self.val = x
        self.end = False
        # OR List(key)+BFS (<-but slow)
        self.dict = {} # key: "a", value: node (fast but extra space)

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TreeNode("")

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        node = self.root
        total = len(word)
        for i in range(0, total):
            char = word[i]
            if char in node.dict:
                node = node.dict[char]
            else:
                # insert char
                tmp_node =  TreeNode(char)
                node.dict[char] = tmp_node
                node = tmp_node
            if i == total - 1:
                node.end = True
    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        node = self.root
        for char in word:
            if char in node.dict:
                node = node.dict[char]
            else:
                return False
        if node.end:
            return True
        return False

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        node = self.root
        for char in prefix:
            if char in node.dict:
                node = node.dict[char]
            else:
                return False
        return True
def test_func():
    trie = Trie()
    trie.insert("apple")
    assert trie.search("apple") == True
    assert trie.search("app") == False
    assert trie.startsWith("app") == True
    trie.insert("app")
    assert trie.search("app") == True
