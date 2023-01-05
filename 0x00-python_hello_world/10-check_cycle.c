#include "lists.h"
#include <stdio.h>

/**
 * check_cycle - Checks if linked list has a cycle
 * @list: Pointer to first node in list
 *
 * Return: 1 if there is a cycle, 0 otherwise
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list, *fast = list;

	while (slow != NULL)
	{
		if (fast == NULL || fast->next == NULL)
			return (0);

		slow = slow->next;
		fast = fast->next->next;

		if (slow == fast)
			return (1);
	}
	return (0);
}
