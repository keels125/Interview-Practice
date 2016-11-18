class Node:
    def __init__(self, data):
        self.data = data
        self.children = {}

    def hasChild(self, child):
        return (child in self.children)

    def addChild(self, child):
        if not self.hasChild(child):
            n = Node(child)
            self.children[child] = n


    def getChild(self, child):
        if self.hasChild(child):
            return self.children[child]
        else:
            return None #no child exists

class Trie():
    def __init__(self):
        self.root = Node("")

    def addWord(self, word):
        temp = self.root
        for char in word:
            if (temp.hasChild(char)):
                temp = temp.getChild(char)
            else:
                temp.addChild(char)
                temp = temp.getChild(char)

        temp.addChild('*')

    def hasWord(self, word):
        temp = self.root

        for char in word:
            if (not temp.hasChild(char)):
                return False
            else:
                temp = temp.getChild(char)
        
        if (temp.hasChild('*')):
            return True
        else:
            return False



def main():
    t = Trie()
    t.addWord("keely")
    print(t.hasWord("keely"))
    print(t.hasWord("keel"))
    t.addWord("kelp")
    print(t.hasWord("kelp"))

    

main()
        
