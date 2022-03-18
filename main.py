import re
import generator
from rich import print
from rich.tree import Tree

dirs_and_files = generator.get_mock_dirs()
print(dirs_and_files)

tree = Tree("Regular tree")

tmp_tree = Tree("")

def create_tree(curr_tree, dir) -> None:
	if len(dir) == 0:
		curr_tree.add("<Empty>")
		return
	for x in dir:
		if type(x) is list: # directory
			create_tree(tmp_tree, x)
		else: # directory/file name
			tmp_tree = curr_tree.add(x)

create_tree(tree, dirs_and_files)

print(tree)

# ----------------- Bonus section ----------------------

filter = re.compile(r"(.py|.txt|.csv)\b") # remove whichever file extension we don't want
									      # filter = re.compile(r"(.py|.txt|.csv)\b")

filtered_tree = Tree("Filtered tree")

def has_file_extension(n) -> bool:
	res = filter.findall(n)
	if len(res) > 0:
		return True
	return False

tmp_tree = Tree("")
hjb = False;

def create_filtered_tree(curr_tree, dir) -> None:
	if len(dir) == 0:
		curr_tree.add("<Empty>")
		return
	for x in dir:
		if type(x) is list: # directory
			create_tree(tmp_tree, x)
		else: # directory/file name
			if "." in x:
				if has_file_extension(x):
					curr_tree.add(x)
			else:
				tmp_tree = curr_tree.add(x)

create_filtered_tree(filtered_tree, dirs_and_files)

print(filtered_tree)