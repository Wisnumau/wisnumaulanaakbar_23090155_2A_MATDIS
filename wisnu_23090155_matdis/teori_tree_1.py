# Diberikan sebuah pohon biner, tulis sebuah fungsi untuk menemukan kedalaman maksimum pohon tersebut.
# Kedalaman sebuah pohon adalah jumlah maksimum simpul dari akar hingga daun terjauh.
#      3
#     / \
#    9  20
#       /  \
#      15   7
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def maxDepth(root: TreeNode) -> int:
    if not root:
        return 0
    left_depth = maxDepth(root.left)
    right_depth = maxDepth(root.right)
    return max(left_depth, right_depth) + 1

# Contoh pohon biner
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20, TreeNode(15), TreeNode(7))

# Mencari kedalaman maksimum
depth = maxDepth(root)
print(f"Kedalaman maksimum pohon biner adalah {depth}")
