preorder(leaf(Root), [Root]).

preorder(tree(Root, Left, Right), [Root | Traversal]) :-
    preorder(Left, LeftTraversal),
    preorder(Right, RightTraversal),
    append(LeftTraversal, RightTraversal, Traversal).
