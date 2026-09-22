def delete_node_bst(root, key):
    # base case 
    if not root:
        return root
    
    if key > root:
        root.right = delete_node_bst(root.right, key)
    if key < root:
        root.left = delete_node_bst(root.left, key)
    else:
        if not root.left:
            return root.right 
        elif not root.right:
            return root.left
        
        curr = root 
        while curr.left:
            curr = curr.left
            
        root.val = curr.val
        delete_node_bst(root.right, root.val)
    
    