#A stack that will always have a value in it
class Stack:
	def __init__(self, initial_item = None):
		self.stack = [initial_item]

	def push(self, item):
		self.stack.append(item)

	def top(self):
		return self.stack[-1]

	def pop(self):
		return_val = self.stack.pop()
		if not self.stack:
			self.stack = [None]
		return return_val