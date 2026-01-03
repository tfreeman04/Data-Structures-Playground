class node:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
class binary_tree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if not self.root:
            self.root = node(value)
        else:
            self._insert_rec(self.root, value)
    
    def _insert_rec(self, current_node, value):
        if value < current_node.value:
            if current_node.left is None:
                current_node.left = node(value)
            else:
                self._insert_rec(current_node.left, value)
        else:
            if current_node.right is None:
                current_node.right = node(value)
            else:
                self._insert_rec(current_node.right, value)
    
    def inorder_traversal(self):
        result = []
        self._inorder_rec(self.root, result)
        return result
     
    def _inorder_rec(self, current_node, result):
        if current_node:
            self._inorder_rec(current_node.left, result)
            result.append(current_node.value)
            self._inorder_rec(current_node.right, result)
    
    def preorder_traversal(self):
        result = []
        self._preorder_rec(self.root, result)
        return result
    
    def _preorder_rec(self, current_node, result):
        if current_node:
            result.append(current_node.value)
            self._preorder_rec(current_node.left, result)
            self._preorder_rec(current_node.right, result)
    
    def postorder_traversal(self):
        result = []
        self._postorder_rec(self.root, result)
        return result
    
    def _postorder_rec(self, current_node, result):
        if current_node:
            self._postorder_rec(current_node.left, result)
            self._postorder_rec(current_node.right, result)
            result.append(current_node.value)
    
    def __repr__(self):
        return "BinaryTree(" + ", ".join(map(str, self.inorder_traversal())) + ")"
    
    def is_empty(self):
        """Return True if the binary tree is empty"""
        return self.root is None
    
    def delete_node(self, value):
        """Delete a node with the given value from the binary tree"""
        self.root = self._delete_rec(self.root, value)
    
    def _delete_rec(self, current_node, value):
        if current_node is None:
            return current_node
        
        if value < current_node.value:
            current_node.left = self._delete_rec(current_node.left, value)
        elif value > current_node.value:
            current_node.right = self._delete_rec(current_node.right, value)
        else:
            # Node with only one child or no child
            if current_node.left is None:
                return current_node.right
            elif current_node.right is None:
                return current_node.left
            
            # Node with two children: Get the inorder successor (smallest in the right subtree)
            temp = self._min_value_node(current_node.right)
            current_node.value = temp.value
            current_node.right = self._delete_rec(current_node.right, temp.value)
        
        return current_node
    
    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current
    
    def search(self, value):
        """Search for a node with the given value in the binary tree"""
        return self._search_rec(self.root, value)
    
    def _search_rec(self, current_node, value):
        if current_node is None or current_node.value == value:
            return current_node is not None
        
        if value < current_node.value:
            return self._search_rec(current_node.left, value)
        else:
            return self._search_rec(current_node.right, value)
        
    def height(self):
        """Return the height of the binary tree"""
        return self._height_rec(self.root)
    
    def _height_rec(self, current_node):
        if current_node is None:
            return -1
        left_height = self._height_rec(current_node.left)
        right_height = self._height_rec(current_node.right)
        return 1 + max(left_height, right_height)   
    
    def size(self):
        """Return the number of nodes in the binary tree"""
        return self._size_rec(self.root)
    
    def _size_rec(self, current_node):
        if current_node is None:
            return 0
        return 1 + self._size_rec(current_node.left) + self._size_rec(current_node.right)
    
    def bfs_traversal(self):
        """Breadth-First Search (Level Order Traversal)"""
        result = []
        if not self.root:
            return result
        
        queue = [self.root]
        while queue:
            current_node = queue.pop(0)
            result.append(current_node.value)
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)
        
        return result
    
    def dfs_traversal(self):
        """Depth-First Search (Preorder Traversal)"""
        return self.preorder_traversal()
    
    def clear(self):
        """Clear the binary tree"""
        self.root = None
    
    