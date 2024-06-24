# Diberikan jaringan distribusi yang berbentuk pohon, tulis sebuah fungsi untuk menemukan rute pengiriman dari
# gudang pusat ke cabang tertentu dan menghitung total biaya berdasarkan jumlah jalur yang dilalui.
#         Gudang Pusat
#        /     |      \
#   Cabang1  Cabang2  Cabang3
#   /   \       |
# C1-1 C1-2    C2-1
class Node:
    def __init__(self, name):
        self.name = name
        self.children = []

def findRouteAndCost(root: Node, target: str, cost_per_route: int):
    def dfs(node: Node, path: list, cost: int):
        if node.name == target:
            return path + [node.name], cost
        for child in node.children:
            result_path, result_cost = dfs(child, path + [node.name], cost + cost_per_route)
            if result_path:
                return result_path, result_cost
        return [], 0

    return dfs(root, [], 0)

# Contoh jaringan distribusi
warehouse = Node('Gudang Pusat')
branch1 = Node('Cabang1')
branch2 = Node('Cabang2')
branch3 = Node('Cabang3')
c1_1 = Node('C1-1')
c1_2 = Node('C1-2')
c2_1 = Node('C2-1')

warehouse.children = [branch1, branch2, branch3]
branch1.children = [c1_1, c1_2]
branch2.children = [c2_1]

# Menemukan rute pengiriman dan biaya ke C2-1
target_branch = 'C2-1'
cost_per_route = 100
route, total_cost = findRouteAndCost(warehouse, target_branch, cost_per_route)
print(f"Rute pengiriman dari Gudang Pusat ke {target_branch}: {' -> '.join(route)}")
print(f"Total biaya pengiriman: {total_cost}")


