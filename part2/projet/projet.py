import math
import random

def g (n) :
    n -= 1
    if n <= 0 :
        return 1
    product = 1
    for k in range(1, n+1):
        product *= (0.5 - k)
    product *= (-2)**n
    return int(product)

def composition(n):
    a = [0 for i in range(n + 1)]
    k = 1
    a[0] = 0
    a[1] = n
    while k != 0:
        x = a[k - 1] + 1
        y = a[k] - 1
        k -= 1
        while 1 <= y:
            a[k] = x
            x = 1
            y -= x
            k += 1
        a[k] = x + y
        yield a[:k + 1]

def multinomial(n, coeffs):
    nfac = math.factorial(n)
    product = 1
    for i in coeffs:
        product *= math.factorial(i)
    return nfac/product

def compo_product(compo, n):
    total = multinomial(n, compo)
    for i in compo:
        total *= g(i)
    return total

def inner_sum(n, k):
    total = 0
    for c in composition(n):
        if (len(c) == k):
            total += compo_product(c, n)
    return total

def tree_gen_rec(size):
    if size == 0:
        return { 'leaf': True, 'tag': -1 }
    if size == 1:
        return { 'terminal': True, 'tag': -1 }
    if size == 2:
        return { 'children': [{'terminal': True, 'tag': -1 }], 'tag': -1}

    rand = random.randrange(g(size) - 1)

    k = 1
    while k < size:
        tmp = inner_sum(size-1, k)
        if (rand - tmp > 0):
            rand -= tmp
        else:
            break
        k += 1

    # on a trouvé le k
    # on doit trouver la bonne composition
    compos = []
    for comp in composition(size - 1):
        if len(comp) == k:
            compos.append(comp)

    i = 0
    while i < len(compos):
        tmp = compo_product(compos[i], size-1)
        if (rand - tmp > 0):
            rand -= tmp
        else:
            break
        i += 1

    # On a trouvé la composition: compo[i]
    children = [tree_gen_rec(x) for x in compos[i]]
    return {'children': children, 'tag': -1}

def tree_gen(size):
    tree = tree_gen_rec(size)
    print(tree_size(tree))
    tag_tree(tree)
    return tree

def traverse_side_effect(side_effect, tree):
    """Infix tree traversal for functions with side-effects.
    """
    side_effect(tree)
    if 'children' in tree:
        for node in tree['children']:
            traverse_side_effect(side_effect, node)

def gen_dot(tree, fname):
    """Generate the .dot file corresponding to the generated tree using the
    previously defined name generator.
    """
    with open(fname, 'w') as f:
        def output_dot_node(node, out=f):
            if 'children' in node:
                for child in node['children']:
                    out.write(str(node['tag']) + ' -> ' + str(child['tag']) + ';\n')

        f.write('digraph tree {\n')
        traverse_side_effect(output_dot_node, tree)
        f.write('}\n')

def tag_tree(tree):
    """Tag a general tree to make it an increasingly tagged general tree
    """

    print(tree)

    root_stack = [tree]
    end_stack = []
    i = 0
    while root_stack:
        e = root_stack[random.randrange(len(root_stack))]
        root_stack.remove(e)
        end_stack.append(e)
        i += 1
        if 'children' in e:
            root_stack += e['children']

    print("Number of elements visited: " + str(i))
    i = 1
    for e in end_stack:
        e['tag'] = i
        i+= 1

    print(tree)

def tree_size(tree):
    if not tree:
        return 0
    if 'terminal' in tree:
        return 1
    if 'children' in tree:
        return 1 + sum([tree_size(x) for x in tree['children']])

if __name__ == '__main__':
    tree = tree_gen(15)
    gen_dot(tree, 'tree.dot')



{'children': [
    {'tag': -1, 'children': [
        {'terminal': True, 'tag': -1}]}, 
    {'children': [
        {'terminal': True, 'tag': -1}, 
        {'terminal': True, 'tag': -1}, 
        {'terminal': True, 'tag': -1}, 
        {'terminal': True, 'tag': -1}, 
        {'terminal': True, 'tag': -1}, 
        {'terminal': True, 'tag': -1}, 
        {'tag': -1, 'children': [
            {'terminal': True, 'tag': -1}]}, 
        {'terminal': True, 'tag': -1}]}, 
    {'terminal': True, 'tag': -1}, 
    {'terminal': True, 'tag': -1}]}



{'tag': 1, 'children': [
    {'tag': 3, 'children': [
        {'terminal': True, 'tag': 4}]}, 
    {'tag': 5, 'children': [
        {'terminal': True, 'tag': -1}, 
        {'terminal': True, 'tag': -1}, 
        {'terminal': True, 'tag': 9}, 
        {'terminal': True, 'tag': -1}, 
        {'terminal': True, 'tag': 8}, 
        {'terminal': True, 'tag': 13}, 
        {'tag': 10, 'children': [
            {'terminal': True, 'tag': 15}]}, 
        {'terminal': True, 'tag': 14}]}, 
    {'terminal': True, 'tag': 2}, 
    {'terminal': True, 'tag': -1}]}
