#include "lists.h"

/**
 * reverse_list - reverses a linked list
 * @head: pointer to the first node in the list
 * Return: pointer to the first node in the new list
 */
void reverse_list(listint_t **head)
{
	listint_t *prev = NULL;
	listint_t *current = *head;
	listint_t *next = NULL;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}
	*head = prev;
}
/**
 * is_palindrome - checks if a linked list is a palindrome
 * @head: double pointer to the linked list
 *
 * Return: 1 if it is, 0 if not
 */
int is_palindrome(listint_t **head)
{
	listint_t *temp = *head;
	listint_t *dup = NULL;

	if (temp == NULL)
		return (1);
	while (temp != NULL)
	{
		add_nodeint_end(&dup, temp->n);
		temp = temp->next;
	}
	reverse_list(&dup);
	temp = *head;

	while (dup != NULL && temp != NULL)
	{
		if (dup->n != temp->n)
			return (0);
		dup = dup->next;
		temp = temp->next;
	}
	free_listint(dup);
	return (1);
}
