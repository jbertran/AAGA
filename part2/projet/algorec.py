import operator as op
from functools import reduce
def ncr(n, r):
    r = min(r, n-r)
    if r == 0: return 1
    numer = reduce(op.mul, iter(range(n, n-r, -1)))
    denom = reduce(op.mul, iter(range(1, r+1)))
    return numer//denom

import random
import math

def cat(n):
    if n == 0:
        return 1
    return (1/(n+1)) * ncr(2*n, n)

def catlist(n):
    return [cat(i) for i in range(n)]

def decomp(n):
    cl = catlist(n)
    bn = []
    i = 0
    while i < n:
        bn.append(cl[i]*cl[n-1-i])
        i += 1
    return bn

def gen(n):

    if n == 0:
        return {}

    rand = random.randrange(cat(n))
    dec = decomp(n)
    i = 0
    while rand >= 0:
        rand -= dec[i]
        i += 1
    i -= 1

    return {'left': gen(i),
            'right': gen(n-1-i)}

def tag_gen():
    i = 0
    while True:
        yield str(i)
        i += 1

def tag_tree_rec(tree, gen):
    if tree:
        tree['tag'] = next(gen)
    else:
        tree['tag'] = 'empty_' + next(gen)
        return tree
    tree['left'] = tag_tree_rec(tree['left'], gen)
    tree['right'] = tag_tree_rec(tree['right'], gen)
    return tree

def traverse_side_effect(side_effect, tree):
    """Infix tree traversal for functions with side-effects.
    """
    if tree.get('left'):
        traverse_side_effect(side_effect, tree['left'])
    side_effect(tree)
    if tree.get('right'):
        traverse_side_effect(side_effect, tree['right'])

def gen_dot(tree, fname):
    """Generate the .dot file corresponding to the generated tree using the
    previously defined name generator.
    """
    gen = tag_gen()
    tree = tag_tree_rec(tree, gen)
    with open(fname, 'w') as f:
        def output_dot_node(node, out=f):
            if node.get('left'):
                f.write(node['tag'] + ' -> ' + node['left']['tag'] + ';\n')
            if node.get('right'):
                f.write(node['tag'] + ' -> ' + node['right']['tag'] + ';\n')
        f.write('digraph tree {\n')
        traverse_side_effect(output_dot_node, tree)
        f.write('}\n')

if __name__ == '__main__':
    tree = gen(30)
    gen_dot(tree, 'tree.dot')
