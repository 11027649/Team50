# # # # # # # # # # # # # # # # #
# A breadth first search algorithm.
# Input = A search problem. A search-problem abstracts out the
# problem specific requirements from the actual search algorithm.
#
# Output = An ordered list of actions to be followed to reach from start to
# the goal state.
# # # # # # # # # # # # # # # # #

def main(problem):
	""" BFS algorithm. """

	# a first in first out open set
	open_set = Queue()

	# an empty set to maintain visited nodes
	closed_set = set()

	# initialize
	start = problem.get_start_state()
	open_set.enqueue(start)

	while not open_set.length == 0:
		parent_state = open_set.dequeue()

		for (child_state, action) in problem.get_successors(parent_state):
			if child_state in closed_set:
				continue
			if child_state not in closed_set:
				open_set.enqueue(child_state)

		closed_set.add(parent_state)




if __name__ == '__main__':
	main()

