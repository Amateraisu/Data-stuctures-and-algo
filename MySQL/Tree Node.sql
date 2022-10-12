# Write your MySQL query statement below
# so every node has a id and a parent id 

# a root node has no parent id 

# an inner node has a child node == it is the parent of some node 

# a leaf node has no child == it has a parent , while it isnt the parent of any node 

    # SELECT DISTINCT p_id FROM Tree
    # WHERE p_id IS NOT NULL
    
 # so this is all the nodes who have a parent = leaf + ineer 
# to get all the parents of nodes who have a parent, do this 



# 


SELECT id, "Root" as "type"
FROM Tree
WHERE p_id IS NULL

UNION 

SELECT id, "Inner" as "type"
FROM Tree
WHERE id IN (
    SELECT p_id FROM Tree
) AND p_id IS NOT NULL

UNION 

# for the nodes whose parent id is not null, select their parents 
# that means I dont want their parents 

SELECT id, "Leaf" as "type"
FROM Tree
WHERE id NOT IN (
    SELECT p_id FROM Tree # select all the nodes who have a parent, = inner + leaf 
    # but leaf nodes arent the parent of any 
    # so select from this subset , 
    # 
    
    WHERE p_id IS NOT NULL
) AND p_id IS NOT NULL


ORDER BY id;