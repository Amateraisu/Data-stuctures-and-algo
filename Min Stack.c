

typedef struct stack
{
    int val;
    int min;
    struct stack *next;
} MinStack;

MinStack *Top = NULL; // Declare top node to be a Global variable pointing to NULL;
MinStack *minStackCreate()
{

    return Top;
}

void minStackPush(MinStack *obj, int val)
{
    MinStack *new_layer = (MinStack *)malloc(sizeof(MinStack)); // FIRST PUSH TO THE TOP OF THE STACK
    new_layer->next = Top;
    Top = new_layer;
    Top->val = val;
    if (Top->next == NULL) // check against the next node for the lowest value of min, and assign accordingly.
    {
        Top->min = val;
    }
    else
    {
        if (Top->next->min > val)
        {
            Top->min = val;
        }
        else
        {
            Top->min = Top->next->min;
        }
    }
}

void minStackPop(MinStack *obj)
{
    MinStack *Temp = Top;
    Top = Top->next;
    free(Temp);
}

int minStackTop(MinStack *obj)
{
    return Top->val;
}

int minStackGetMin(MinStack *obj)
{
    return Top->min;
}

void minStackFree(MinStack *obj)
{
    MinStack *Temp = Top;
    while (Top != NULL)
    {
        Temp = Top;
        Top = Top->next;
        free(Temp);
    }
}

/**
 * Your MinStack struct will be instantiated and called as such:
 * MinStack* obj = minStackCreate();
 * minStackPush(obj, val);

 * minStackPop(obj);

 * int param_3 = minStackTop(obj);

 * int param_4 = minStackGetMin(obj);

 * minStackFree(obj);
*/