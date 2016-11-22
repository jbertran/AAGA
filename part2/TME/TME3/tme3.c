#include <stdlib.h>
#include <stdio.h>
#include <time.h>
#include "tme3.h"

#define STACK_INIT_COUNT 32
#define TRUE 1
#define FALSE 0

#ifdef DEBUG
#define debug(i) fprintf(stderr, "%s\n", i);
#else
#define debug(i) ;
#endif

stack * make_stack(){
  debug("make stack");
  stack * res = malloc(sizeof(stack));
  res->nodearr = malloc(STACK_INIT_COUNT * sizeof(node *));
  res->nodecount = 0;
  res->maxcount = STACK_INIT_COUNT;
}

void push_leaf(stack * st, node * leaf){
  debug("push leaf");
  if (st->nodecount >= st->maxcount) {
    node ** newarr = malloc(st->maxcount * 2 * sizeof(node *));
    for (int i=0; i<st->maxcount; i++)
      newarr[i] = st->nodearr[i];
    free(st->nodearr);
    st->nodearr = newarr;
    st->maxcount *= 2;
  }
  st->nodearr[st->nodecount++] = leaf;
}

node * get_leaf(stack * st, int i) {
  debug("get leaf");
  return st->nodearr[i];
}

void destroy_stack(stack * st){
  debug("destroy stack");
  free(st->nodearr);
  free(st);
}

node * make_leaf() {
  debug("make leaf");
  node * res = malloc(sizeof(node));
  res->left = NULL;
  res->right = NULL;
  res->isLeaf = TRUE;
  res->value = -1;

  return res;
}

node * make_tree(int size) {
  debug("make tree");
  srand(time(NULL));

  stack * stack = make_stack();
  node ** leaves = malloc(size * sizeof(node *));
  node * root = make_leaf();

  push_leaf(stack, root);

  for (int i=1; i<size+1; i++) {
    int random = rand() % (stack->nodecount); // TODO better random gen
    node * leaf = get_leaf(stack, random);
    leaf->isLeaf = FALSE;
    node * l = make_leaf();
    node * r = make_leaf();
    leaf->left = l;
    leaf->right = r;
    push_leaf(stack, l);
    push_leaf(stack, r);
  }

  destroy_stack(stack);
  return root;
}

void destroy_tree(node * tree) {
  debug("destroy tree");
  if (!tree->isLeaf) {
    destroy_tree(tree->left);
    destroy_tree(tree->right);
  }
  free(tree);
}

void tag_tree_rec(node * tree, int * value) {
  debug("tag tree rec");
  if (!tree->isLeaf) {
    tag_tree_rec(tree->left, value);
    tree->value = *value++;
    tag_tree_rec(tree->right, value);
  }
}

void tag_tree(node * tree) {
  debug("tag tree");
  int i = 0;
  tag_tree_rec(tree, &i);
}

void ald_rec(node * tree, float * count, float * acc, float depth) {
  debug("ald rec");
  if (tree->isLeaf) {
    *count++;
    *acc += depth;
  }
  else {
    ald_rec(tree->left, count, acc, depth + 1);
    ald_rec(tree->right, count, acc, depth + 1);
  }
}

float ald (node * tree) {
  debug("ald");
  float count = 0;
  float acc = 0;
  ald_rec(tree, &count, &acc, 0);
  return acc / count;
}

int main() {
  float depth = 0;
  for (int i=0; i<10000; i++) {
    node * tree = make_tree(10000);
    tag_tree(tree);
    depth += ald(tree);
    destroy_tree(tree);
    fprintf(stdout, "%d / %d\n", i, 10000);
  }
  fprintf(stdout, "Average: %d\n", depth / 10000);
}
