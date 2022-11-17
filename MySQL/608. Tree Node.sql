# Write your
MySQL query statement below
    SELECT id, "Root" AS type
    FROM Tree
    WHERE p_id iS NULL

UNION

    SELECT id, "Inner" AS type
    FROM Tree
    WHERE id IN 
(
    SELECT p_id
    FROM Tree
    WHERE p_id NOT IN 
    (
        SELECT id
    FROM TREE
    WHERE p_id is NULL
    
    )
    
)

UNION

    SELECT id, "Leaf" AS type
    FROM Tree
    WHERE id NOT IN 
(
    #
the first
condition:
it is not the parent of any nodes
    SELECT p_id
    FROM Tree
    WHERE p_id IS NOT NULL

UNION

    SELECT id
    FROM Tree
    WHERE p_id IS NULL
# the second
condition:
it is not the root node 
    

)
