#include "list.h"

/**
  * check_cycle - checks if a singly linked list has a cycle
  * @list: param
  *
  * Return: 0 if there is no cycle, 1 if there is a cycle
  */
int check_cycle(listint_t *list)
{
	listint_t *n1 = list, *n2 = list;

	while (n1 && n1->next)
	{
		n2 = n2->next;
		n1 = n1->next->next;
		if (n1 == n2)
			return (1);
	}
	return (0);
}
