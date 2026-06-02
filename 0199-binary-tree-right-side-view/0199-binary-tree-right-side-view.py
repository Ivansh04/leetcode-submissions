# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue=deque([root])
        if not root:
                return []
        ans=[root.val]
        while True:
            if not queue:
                break
            
            l=len(queue)
            for i in range(l):
                node=queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if queue:
              a=queue[-1]
              ans.append(a.val)
        return ans