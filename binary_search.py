# encoding: utf-8
def solve(root, n):

    def traverse(node, nr_seen):
        '''Trả về (số đỉnh đã qua, và kết quả).'''
        if node is None:
            return nr_seen, None

        # Tìm trong nhánh trái
        nr_seen, answer = traverse(node.left, nr_seen)
        if answer is not None:
            # Tìm thấy kết quả bên nhánh trái.
            return nr_seen, answer

        nr_seen += 1
        if nr_seen == n:
            # Đỉnh hiện tại chính là đỉnh cần tìm.
            return nr_seen, node.value

        # Tìm trong nhánh phải
        nr_seen, answer = traverse(node.right, nr_seen)
        return nr_seen, answer

    nr_seen, answer = traverse(root, 0)
    return answer


class Node(object):

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


root = Node(7, Node(5, Node(3), Node(6)), Node(9, None, Node(10)))
assert(solve(root, 1) == 3)
assert(solve(root, 2) == 5)
assert(solve(root, 3) == 6)
assert(solve(root, 4) == 7)
assert(solve(root, 5) == 9)
assert(solve(root, 6) == 10)