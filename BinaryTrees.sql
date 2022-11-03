-- BST ( N = Node, P = Parent)

CREATE TABLE BST (
  N Integer,
  P Integer
)

-- Write a query to find the node type of Binary Tree ordered by the value of the node. Output one of the following for each node:

-- Root: If node is root node.
-- Leaf: If node is leaf node.
-- Inner: If node is neither root nor leaf node.

SELECT 
  N,
    CASE WHEN N = Null THEN 'Root'
         WHEN N IN (SELECT P FROM BST) THEN 'Inner'
         ELSE 'Leaf'
    END AS Node_Type
FROM BST;