# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        cnt=[0]
        ans=[0]
        def ino(node):
            if not node:
                return
            ino(node.left)
            cnt[0]=cnt[0]+1
            if cnt[0]==k:
                ans[0]=node.val
            ino(node.right)
        ino(root)
        return ans[0]

