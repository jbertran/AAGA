#ifndef __tme3__
#define __tme3__

typedef struct _node {
  int isLeaf;
  int value;
  struct _node * left;
  struct _node * right;
} node;

node * make_node();
node * make_tree(int size);
void tag_tree(node * tree);
void destroy_tree(node * tree);

typedef struct {
  node ** nodearr;
  int nodecount;
  int maxcount;
} stack;

stack * make_stack();
void push_leaf(stack * st, node * leaf);
node * get_leaf(stack * st, int i);
void destroy_stack(stack * st);

#endif
