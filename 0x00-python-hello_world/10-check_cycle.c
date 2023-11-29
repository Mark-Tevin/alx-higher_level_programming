#include <stdlib.h>
#include "lists.h"

/**
 * return: 0 if no cycle or 1 if cycle
 * list:singly list
 * check_cycle : checks if a singly list has a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *fast, *slow;

	if (list == NULL || list->next == NULL)
		return (0);

	fast = list->next->next;
	slow = list->next;

	while (slow && fast && fast->next)
	{
		if (fast == slow)
			return (1);

		fast = fast->next->next;
		slow = slow->next;
	}
	return (0);
}
