import math
import random
import functools

def id_generator():
    """Simple ID generator to differentiate node dictionaries,
    since they need to be unique in order for list.remove() to
    behave correctly
    """
    id = 0
    while True:
        yield id
        id += 1

@functools.lru_cache()
def g (n) :
    n -= 1
    if n <= 0 :
        return 1
    product = 1
    for k in range(1, n+1):
        product *= (0.5 - k)
    product *= (-2)**n
    return int(product)

@functools.lru_cache()
def composition(n):
    """Return a list of potential compositions with lowest value 1
    totalling n
    """
    result = []
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
        result.append(a[:k + 1])
    return result

def multinomial(n, coeffs):
    """Multinomial coefficient - n choose coeffs
    n! divided by the product of e! for e in coeffs
    """
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

@functools.lru_cache()
def inner_sum(n, k):
    total = 0
    for c in composition(n):
        if (len(c) == k):
            total += compo_product(c, n)
    return total

def tree_gen_rec(size, id_gen):
    """Recursively form a silhouette of a general tree of given size
    Use generator id_gen to differentiate nodes amongst themselves
    """
    if size == 0:
        raise Exception('You asked for a zero-size general tree.')
    if size == 1:
        return { 'terminal': True, 'tag': -1, 'id': next(id_gen) }
    if size == 2:
        return { 'children': [{'terminal': True, 'tag': -1, 'id': next(id_gen) }], 'tag': -1, 'id': next(id_gen)}

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
    compos = [x for x in composition(size-1) if len(x) == k]

    i = 0
    while i < len(compos):
        tmp = compo_product(compos[i], size-1)
        if (rand - tmp > 0):
            rand -= tmp
        else:
            break
        i += 1

    # On a trouvé la composition: compo[i]
    children = [tree_gen_rec(x, id_gen) for x in compos[i]]
    return {'children': children, 'tag': -1, 'id': next(id_gen)}

def tree_gen(size):
    """Handle calls to the recursive silhouette generator, and tag the resulting
    tree silhouette for and increasingly tagged general tree
    """
    id_gen = id_generator()
    tree = tree_gen_rec(size, id_gen)
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
    A.k.a. your basic prefix run, with a random twist
    """
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
    i = 1
    for e in end_stack:
        e['tag'] = i
        i+= 1

def tree_size(tree):
    """The size of given general tree, which may only contain terminal nodes
    and inner nodes with children
    """
    if not tree:
        return 0
    if 'terminal' in tree:
        return 1
    if 'children' in tree:
        return 1 + sum([tree_size(x) for x in tree['children']])

if __name__ == '__main__':
    tree = tree_gen(15)
    gen_dot(tree, 'tree.dot')
