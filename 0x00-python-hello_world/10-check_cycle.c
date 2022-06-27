#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - checks if there is cycle in linked list
 * @list: pointer to start of linked list
 * Return: 0 or 1
 */

int check_cycle(listint_t *list)
{
	listint_t *current = list, *previous = list;

	while (current && current->next)
	{
		previous = previous->next;
		current = current->next->next;
		if (current == previous)
			return (1);
	}

	return (0);
}
