import itertools
from random import randint
from math import log

# QUESTION 2.12.1

def new_leaf():
    return {
        'l': {},
        'r': {},
        'v': None,
        'isnode': True
    }

def make_tree(n):
    root = new_leaf()

    leaves = [root]

    for i in range(1, n+1):
        leaf = leaves.pop(randint(1,i) - 1)
        l, r = new_leaf(), new_leaf()
        leaf['l'], leaf['r'] = l, r
        leaves.append(l)
        leaves.append(r)

    return root

def tag_tree(tree):
    gen = itertools.islice(itertools.count(start=1), None)
    def tag_tree_rec(treerec, gen=gen):
        if treerec.get('isnode'):
            tag_tree_rec(treerec['l'])
            treerec['v'] = next(gen)
            tag_tree_rec(treerec['r'])
        return tree
    return tag_tree_rec(tree)

def dump_values(tree):
    acc = []
    def dump_values_rec(tree, acc=acc):
        if tree.get('isnode'):
            dump_values_rec(tree['l'])
            acc.append(tree['v'])
            dump_values_rec(tree['r'])
    dump_values_rec(tree)
    return acc

def disp_tree(tree, acc_space=''):
    if tree.get('isnode'):
        nodestr = acc_space + 'Node'
        if tree.get('v'):
            nodestr += ' %s' % tree['v']
        print(nodestr)
        print(acc_space + 'L:')
        disp_tree(tree['l'], acc_space + '  ')
        print(acc_space + 'R:')
        disp_tree(tree['r'], acc_space + '  ')
    else:
        print(acc_space + 'Leaf')

def average_leaf_depth(tree):
    acc = []
    def ald_rec(tree, depth=0, acc=acc):
        if tree.get('isnode'):
            ald_rec(tree['l'], depth=depth+1)
            ald_rec(tree['r'], depth=depth+1)
        else:
            acc.append(depth)
    ald_rec(tree)
    return sum(acc)/len(acc)


def demonstrate_trees():
    tree = make_tree(2)
    tag_tree(tree)
    disp_tree(tree)
    print('Valeurs récupérées en parcours infixe')
    print(dump_values(tree))
    print("Profondeur moyenne d'une feuille:")
    print(average_leaf_depth(tree))


def collect_data(nbtrees, treesize):
    res = []
    for i in range(nbtrees):
        print('\r Instance %s/%s' % (i+1, nbtrees), end='')
        tree = make_tree(treesize)
        tag_tree(tree)
        res.append(average_leaf_depth(tree))
    av_depth = sum(res)/len(res)
    print('\r Average node depth for trees of size %s (log n = %s): %s' % (treesize, log(treesize, 2), av_depth))


if __name__ == '__main__':
    for i in [10, 25, 50, 75, 100, 250, 500, 750, 1000]:
        collect_data(i, i)
