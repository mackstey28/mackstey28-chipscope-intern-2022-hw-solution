Creating tree solution:

Iterated over the dirs_and_files list. If the value is not a list, then it is a directory.
Otherwise, it is a list, and we iterate over that list, and add it to the most recent directory we encountered.
If we encounter another list in this list, then we have to iterate over this next list, adding it to the most recent directory.
It is important we take advantage of the fact that the tree add() function returns a tree, so we can add branches to it.

Can probably solve this using a recursive function as well. It would be much better, since we can have an infinitely deep tree.
We do not need to be limited to 3 layers deep, as the dirs_and_files list is restricted to.

