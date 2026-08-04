class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
def ranked_exposures_to_risk_ladder(exposures):
    '''
    Thought process
    1. pick middle node
    2. partition exposures and recurse
    3. nodeMid.left = ranked_exposures(left_side)
        nodeMid.right = ranked_exposures(right_side)
    '''   
    # base case 
    if not exposures:
        return None

    # recursive case  
    left = 0
    right = len(exposures) - 1
    mid = (left + right) // 2

    node = TreeNode(exposures[mid])

    node.left = ranked_exposures_to_risk_ladder(exposures[:mid])
    node.right = ranked_exposures_to_risk_ladder(exposures[mid + 1:])

    return node

# ranked_exposures_to_risk_ladder([1,2,3])