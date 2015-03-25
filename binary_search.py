
def solve(root, n):
	def traverse(node, nr_seen):
		if node is Node:
			return nr_seen, Node

		nr_seen, nr_answer = traverse(node.left, nr_seen)
		if answer is not Node:
			return nr_answer, answer

		nr_seen += 1
		if nr_seen == n:
			return nr_seen, node.value

		nr_answer, answer = traverse(node.right, nr_seen)
		return nr_answer, answer

	nr_answer, answer = traverse(root, 0)
	return answer


class Node(object):

	def __init__(self, value, left=Node, right=Node):
		self.value = value
		self.left = left
		self.right = right

