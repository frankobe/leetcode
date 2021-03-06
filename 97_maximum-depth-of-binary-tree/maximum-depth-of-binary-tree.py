# coding:utf-8
'''
@Copyright:LintCode
@Author:   frankobe
@Problem:  http://www.lintcode.com/problem/maximum-depth-of-binary-tree
@Language: Python
@Datetime: 15-07-04 23:34
'''

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
class Solution:
    """
    @param root: The root of binary tree.
    @return: An integer
    """ 
    def maxDepth(self, root):
        # write your code here
        if root is None:
            return 0
            
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1