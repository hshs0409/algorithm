import sys
n = int(input())
tree = {}
for _ in range(n):
    a, b, c = sys.stdin.readline().split()
    tree[a] = [b, c]


def pre(node='A'):
    if node != '.':
        print(node, end='')
        pre(tree[node][0])
        pre(tree[node][1])


def inorder(node='A'):
    if node != '.':
        inorder(tree[node][0])
        print(node, end='')
        inorder(tree[node][1])


def post(node='A'):
    if node != '.':
        post(tree[node][0])
        post(tree[node][1])
        print(node, end='')


pre(), print(), inorder(), print(), post()
