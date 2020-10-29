# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 00:35:47 2020

@author: norhther
"""
class Node(object):
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

  def __repr__(self):
    # string representation
    return self.val

#O(|V|) -> linear
def deep_aux(root, n, root_prev):
    if root == None:
        return (root_prev, n)
    else:
        left = deep_aux(root.left, n+1, root)
        right = deep_aux(root.right, n+1, root)
        if left[1] > right[1]:
            return left
        else:
            return right

def deepest(node):
  return deep_aux(node, 0, None)

root = Node('a')
root.left = Node('b')
root.left.left = Node('d')
root.right = Node('c')

print (deepest(root))
# (d, 3)