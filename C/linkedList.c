#include <stddef.h>
#include <stdio.h>
#include <stdlib.h>

struct list_node
{
    struct list_node *next;
};

struct list_node *list_get_tail(struct list_node **head)
{
    struct list_node *current_node = *head;
    struct list_node *last_node = NULL;

    while (current_node)
    {
        last_node = current_node;
        current_node = current_node->next;
    } 

    return last_node;
}

struct list_node *list_append(struct list_node **head, struct list_node *item)
{
    struct list_node *tail = list_get_tail(head);
    if (!tail)
    {
        *head = item;
    }
    else 
    {
        tail->next = item;
    }
    item->next = NULL;
    return item;
}

void *list_remove(struct list_node **head, struct list_node *item)
{
    struct list_node *tail = list_get_tail(head);

    struct list_node *current_item = tail;
    while (current_item)
    {
        // same item when they have the same next element
        if (current_item->next == item)
        {
            current_item->next = item->next;
            return 0;
        }

        current_item = current_item->next;
    }
}

struct list_node *list_pop(struct list_node **head)
{
    struct list_node *current_head = *head;
    if (!current_head)
    {
        return NULL;
    }

    *head =(*head)->next;
    current_head->next = NULL;

    return current_head;
}

struct string_item
{
    struct list_node node;
    const char *string;
};

struct string_item *string_item_new(const char *string)
{
    struct string_item *item = malloc(sizeof(struct string_item));
    if (!item) {
        return NULL;
    }

    item->string = string;
    return item;
}

#define new_string_item(string) (struct list_node*)string_item_new(string)

int main() 
{
    struct string_item *my_linked_list = NULL;
    list_append((struct list_node **)&my_linked_list, new_string_item("Hello world"));
    list_append((struct list_node **)&my_linked_list, new_string_item("test1"));
    list_append((struct list_node **)&my_linked_list, new_string_item("test2"));
    list_append((struct list_node **)&my_linked_list, new_string_item("last element"));

    struct list_node *to_remove = list_pop((struct list_node **)&my_linked_list);

    list_remove((struct list_node **)&my_linked_list, to_remove);
    
    struct string_item *string_item = my_linked_list;
    while (string_item)
    {
        printf("%s\n", string_item->string);
        string_item = (struct string_item *)string_item->node.next;
    }
    return 0;
}
