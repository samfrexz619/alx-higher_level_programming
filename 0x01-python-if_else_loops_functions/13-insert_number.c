#include "lists.h"
/**
 * insert_node - inserts
 * @head: head
 * @number: index
 * Return: address of the new node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *nw;
	listint_t *hd;
	listint_t *hd_pv;

	hd = *head;
	nw = malloc(sizeof(listint_t));

	if (nw == NULL)
		return (NULL);

	while (hd != NULL)
	{
		if (hd->n > number)
			break;
		hd_pv = hd;
		hd = hd->next;
	}

	nw->n = number;

	if (*head == NULL)
	{
		nw->next = NULL;
		*head = nw;
	}
	else
	{
		nw->next = hd;
		if (hd == *head)
			*head = nw;
		else
			hd_pv->next = nw;
	}
	return (nw);
}
