import copy
import timeit


class CountTrees:
    def __init__(self, tree_lst, number_of_days):
        self.trees = tree_lst
        self.days = number_of_days

    def count_trees_loop(self):
        if self.days > 120:
            print("This might take a while.. Please consider commenting out this function for faster results.")

        number_of_new_trees = 0
        tree_list = copy.deepcopy(self.trees)

        for day in range(self.days):
            for tree_number in range(len(tree_list)):
                tree_list[tree_number] += 1

                if tree_list[tree_number] == 8:
                    tree_list[tree_number] = 2
                    number_of_new_trees += 1
                if number_of_new_trees > 0:
                    for new_tree in range(number_of_new_trees):
                        tree_list.append(0)
                        number_of_new_trees = 0
        print(len(tree_list))

    def count_trees_dict(self):
        leaf_count = {i: self.trees.count(i) for i in range(9)}
        last_key = sorted(leaf_count.keys())[-1]

        prev = 0

        for day in range(self.days):
            for i in range(len(leaf_count)):
                temp = prev
                prev = leaf_count[i]
                leaf_count[i] = temp
                if i == last_key:
                    leaf_count[0] += leaf_count[8]
                    leaf_count[2] += leaf_count[8]
                    leaf_count[last_key] = 0
        print(sum(leaf_count.values()))


days = 121
trees = [3, 1, 1, 5, 2]

counter = CountTrees(trees, days)

print(timeit.timeit(counter.count_trees_dict, number=1))
print(timeit.timeit(counter.count_trees_loop, number=1))
