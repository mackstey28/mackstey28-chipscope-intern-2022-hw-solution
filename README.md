/mnt/c/users/maxwe/onedrive/documents/chipscope-intern-2022-hw-assignment

Creating tree solution:

Recursive function for creating a tree from dirs_and_files.
We check if the current dir is empty. If it is, we add "Empty" to it and return.
Next, we check if the current dir is a list. If it is, we call the function on it, with tmp_tree as our tree.
If it is not a list, it is a directory name or file name. We just add it to the current tree in our function, and set tmp_tree equal to this add, because tree.add returns the tree that was added.

Filtered tree solution:

IN PROGRESS