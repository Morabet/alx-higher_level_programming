#include "lists.h"

/**
 * reverse_list - reverse a linked list.
 * @head: head of the linked list.
 * Return: void.
 */
void reverse_list(listint_t **head)
{
	listint_t *current, *prev, *next;

	if (!*head)
		return;

	prev = NULL;
	current = *head;
	next = *head;

	while (current)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}

	*head = prev;
}

/**
 * size_list - get the size of the list.
 * @head: head of the list.
 * Return: integer.
 */
int size_list(listint_t *head)
{
	int size = 0;

	while (head)
	{
		size++;
		head = head->next;
	}
	return (size);
}

/**
 * is_palindrome - check if a linked list is palindrom.
 * @head: heade of the linked list.
 * Return: return 1 if it is palindrom else 0.
 */
int is_palindrome(listint_t **head)
{
	listint_t *first, *second;
	int i = 0, size, m, div;

	if (!*head)
		return (1);

	first = *head;
	second = *head;

	size = size_list(*head);
	div = size / 2;
	if (size % 2 == 0)
		m = div;
	else
		m = div + 1;

	while (second && i < m)
	{
		i++;
		second = second->next;
	}

	reverse_list(&second);

	while (second)
	{
		if (first->n != second->n)
			return (0);
		first = first->next;
		second = second->next;
	}

	return (1);
}
