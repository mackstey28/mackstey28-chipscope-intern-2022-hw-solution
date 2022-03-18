import re
import generator
from rich import print
from rich.tree import Tree

dirs_and_files = generator.get_mock_dirs()
print(dirs_and_files)

tree = Tree("Regular tree")

def is_file(n) -> bool:
	if (n.endswith(".py") or n.endswith(".txt") or n.endswith(".csv")):
		return True
	return False

temp_tree = Tree("")
temp_tree2 = Tree("")

for x in dirs_and_files:
	if type(x) == list:
		if len(x) == 0:
			temp_tree.add("<Empty>")
			continue
		for y in x:
			if type(y) == list:
				if len(y) == 0:
					temp_tree2.add("<Empty>")
					continue
				for z in y:
					temp_tree2.add(z)
			else: # directory in directory in root
				temp_tree2 = temp_tree.add(y)
	else: # directory in root
		temp_tree = tree.add(x)

print(tree)

# ----------------- Bonus section ----------------------

filter = re.compile("<Regex here>")

filtered_tree = Tree("Filtered tree")

"""
***************************************************
Code for the bonus task goes here...
***************************************************
"""

print(filtered_tree)