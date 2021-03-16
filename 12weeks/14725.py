## trie structer

class Node():
    def __init__(self , key):
        self.key = key
        self.children = dict()
    
class Trie():

    def __init__(self):
        self.head =Node(None)
    
    def insert(self , string):
        cur_node = self.head
        for char in string:
            if char not in cur_node.children:
                cur_node.children[char] = Node(char)
            cur_node = cur_node.children[char]
    
    def printTrie(self , length , cur_node):
        if length == 0:
            cur_node = self.head
        
        for child in sorted(cur_node.children.keys()):
            print("--" * length , child , sep="")
            self.printTrie(length+1 , cur_node.children[child])

trie = Trie()
 
N = int(input())


for _ in range(N):
    temp = list(input().split())
    trie.insert(temp[1:])
 
trie.printTrie(0, None)