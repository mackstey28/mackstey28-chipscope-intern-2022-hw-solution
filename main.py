import re
import generator
from rich import print
from rich.tree import Tree

dirs_and_files = generator.get_mock_dirs()
print(dirs_and_files)

tree = Tree("Regular tree")

tmp_tree = None

def create_tree(curr_tree, dir_and_file_list) -> None:
	if len(dir_and_file_list) == 0:
		curr_tree.add("<Empty>")
		return
	for x in dir_and_file_list:
		if type(x) is list: # directory
			create_tree(tmp_tree, x)
		else: # a directory or file name
			tmp_tree = curr_tree.add(x)

create_tree(tree, dirs_and_files)

print(tree)

# ----------------- Bonus section ----------------------

filter = re.compile(r"(.*\.py|.*\.txt|.*\.csv)\b") # remove whichever file extension we don't want
									      		   # filter = re.compile(r"(.*\.py|.*\.txt|.*\.csv)\b")

filtered_tree = Tree("Filtered tree")

def has_file_extension(n) -> bool:
	res = filter.findall(n)
	if len(res) > 0:
		return True
	return False

tmp_tree = None

def create_filtered_tree(curr_tree, dir_and_file_list) -> None:
	if len(dir_and_file_list) == 0:
		curr_tree.add("<Empty>")
		return
	has_file = False
	for x in dir_and_file_list:
		if type(x) is list: # directory
			create_filtered_tree(tmp_tree, x)
		else: # directory/file name
			if "." in x:
				if has_file_extension(x): # if it is a file extension we want
					tmp_tree = curr_tree.add(x)
					has_file = True
				else:
					continue
			else:
				tmp_tree = curr_tree.add(x)
	if has_file == False: # no file extension we wanted were added
		curr_tree.add("<Empty>")

create_filtered_tree(filtered_tree, dirs_and_files)

print(filtered_tree)