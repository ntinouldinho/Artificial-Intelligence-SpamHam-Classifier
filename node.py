class Node:

    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data
    def __str__(self):
        return str(self.data)
    def PrintTree(self):
        if (self.left):
            self.left.PrintTree()
        print( self.data)
        if self.right:
            self.right.PrintTree()
    def find_answer(self,vec_email,vocabulary):
        if(self.data=='spam' or self.data=='ham'):
            return self.data
        index = vocabulary[self.data]
        if(int(vec_email[index])>0):#an uparxei h leksi afti phgaine sto deksi kladi
            return self.right.find_answer(vec_email,vocabulary)
        else:
            return self.left.find_answer(vec_email,vocabulary)
    def maxDepth(node): 
        if ((node.left is None) or(node.right is None)): 
            return 0 ;  
      
        else : 
            # Compute the depth of each subtree 
            lDepth = node.left.maxDepth() 
            rDepth = node.right.maxDepth() 
            if (lDepth > rDepth): 
                return lDepth+1
            else: 
                return rDepth+1

