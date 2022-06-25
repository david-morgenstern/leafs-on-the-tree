# leaves-on-the-tree
Every 8th leaf on a tree spawns a new tree with zero leafs, and goes back to having two leafs itself.

## count_trees_loop
Keeps every tree as a list element, thier value marks the number of leaves on the tree. When a tree reaches 8 leaves, it will drop 6 of them and spawn a new tree with 0 leaves.

## count_trees_dict
Our keys are the number of leaves and the values mark how many trees have that many leaves. We keep "pushing them to the righ" until they would reach 8 leaves. When that happens we add the number of the would-have-8-leaves-trees to the keys that mark trees with 0 and 2 leaves.