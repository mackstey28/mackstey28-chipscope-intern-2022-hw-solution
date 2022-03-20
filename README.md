/mnt/c/users/maxwe/onedrive/documents/chipscope-intern-2022-hw-assignment

Creating tree solution:

Recursive function for creating a tree from dirs_and_files.
We check if the current dir is empty. If it is, we add "Empty" to it and return.
Next, we check if the current dir is a list. If it is, we call the function on it, with tmp_tree as our tree.
If it is not a list, it is a directory name or file name. We just add it to the current tree in our function, and set tmp_tree equal to this add, because tree.add returns the tree that was added.

Filtered tree solution:

Essentially the same solution as above, but whenever we encounter a directory, we perform checks:
Check if it has a "." in it, because we don't want to exclude directory names
Check if it has the filtered file extension type using the has_file_extension() function I wrote, which uses the regex expression to determine whether it is a filtered file type or not. If it is filtered, then we add it. If it isn't, then we don't add it.
We also need to make a boolean has_file, which is initially set to False. If we don't encounter any of the file types we want, then has_file will remain False, so we will need to add "Empty" to the current directory. However, if we do come across a file type we want, then we set has_file to True so that we don't add "Empty" to the current directory.