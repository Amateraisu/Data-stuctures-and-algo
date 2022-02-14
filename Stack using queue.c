typedef struct node{
    int item;
    struct node* next;
}QueueNode;

typedef struct queue{
    int size;
    QueueNode* head;
    QueueNode* tail;
}Queue;

typedef struct {
    Queue* queueptr;
} MyStack;


void enqueue(Queue* queue, int key)
{

    QueueNode* temp_q = (QueueNode*)malloc(sizeof(QueueNode));
    temp_q -> item = key;
    if (queue->tail == NULL)
    {
        // printf("This is ran\n");
        temp_q->next = NULL;
        queue->head = temp_q;
        queue->head->next = NULL;
        queue->tail = temp_q;
        queue->head->next = NULL;
    }
    else 
    {
        // printf("This is ran2\n");
        temp_q ->next = queue->tail;
        queue->tail = temp_q;
    }
    queue->size += 1;

}


int dequeue(Queue* queue)
{
    int key;
    QueueNode* ptr = queue->tail;
    QueueNode* prev = NULL;


    if (queue->size ==1)
    {

        key = queue->head->item;
        ptr = queue->head;
        queue->head = NULL;
        queue->tail = NULL;
        

        queue->size -= 1;

        
        return key;
    }
    else 
    {

        while (ptr->next != NULL)
        {
            prev = ptr;
            ptr = ptr->next;
            
        }

        prev->next = NULL;
        key = ptr->item;

    }
    queue->size -= 1;

    return key;
}




MyStack* myStackCreate() {
    MyStack* stack = (MyStack*)malloc(sizeof(MyStack));
    Queue* q = (Queue*)malloc(sizeof(Queue));
    stack->queueptr = q;
    stack->queueptr->size = 0;
    stack->queueptr->head = NULL;
    stack->queueptr->tail = NULL;
    return stack;
}

void myStackPush(MyStack* obj, int x) 
{
    enqueue(obj->queueptr, x);
}

int myStackPop(MyStack* obj) 
{

    int count = (obj->queueptr->size) - 1;
    int key;
    int popped = obj->queueptr->tail->item;

    if ((obj->queueptr->size) != 1)
    {
        for (int i = 0; i<count ; i++)
        {

            key = dequeue(obj->queueptr);

            enqueue(obj->queueptr, key);

        }
    }

    
    key = dequeue(obj->queueptr);


    return popped;
}

int myStackTop(MyStack* obj) 
{
    return obj->queueptr->tail->item;
}

bool myStackEmpty(MyStack* obj) 
{
    if (obj->queueptr->size == 0)
    {
        return true;
    }
    else 
    {
        return false;
    }
}

void myStackFree(MyStack* obj) 
{
    free(obj);    
}

/**
 * Your MyStack struct will be instantiated and called as such:
 * MyStack* obj = myStackCreate();
 * myStackPush(obj, x);
 
 * int param_2 = myStackPop(obj);
 
 * int param_3 = myStackTop(obj);
 
 * bool param_4 = myStackEmpty(obj);
 
 * myStackFree(obj);
*/