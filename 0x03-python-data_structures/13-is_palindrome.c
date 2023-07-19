#include "lists.h"
/**
 * reverse_list - reverses
 * @hd: head
 * Return: nth
 */
void reverse_list(listint_t **hd)
{
	listint_t *pv;
	listint_t cu;
	listint_t nxt;

	pv = NULL;
	cu = *hd;

	while (cu != NULL)
	{
		nxt = cu->next;
		cu->next = pv;
		pv = cu;
		cu = nxt;
	}

	*hd = pv;
}
/**
 * compare_list - compares
 * @hd1: head
 * @hd2: head of remaining half
 * Return: 1 or 0
 */
int compare_list(listint_t *hd1, listint_t *hd2)
{
	listint_t *tp1;
	listint_t *tp2;

	tp1 = hd1;
	tp2 = hd2;

	while (tp1 != NULL && tp2 != NULL)
	{
		if (tp1->n == tp2->n)
		{
			tp1 = tp1->next;
			tp2 = tp2->next;
		}
		else
		{
			return (0);
		}
	}
	if (tp1 == NULL && tp2 == NULL)
	{
		return (1);
	}
}
/**
 * is_palindrome - checks for palindrome
 * @head: head
 * Return: 0 or 1
 */
int is_palindrome(listint_t **head)
{
	listint_t *sl, *fst, *prev_sl;
	listint_t *half, *mid;
	int i;

	sl = fst = prev_sl = *head;
	mid = NULL;
	i = 1;

	if (*head != NULL && (*head)->next != NULL)
	{
		while (fst != NULL && fst->next != NULL)
		{
			fst = fst->next->next;
			prev_sl = sl;
			sl = sl->next;
		}

		if (fst != NULL)
		{
			mid = sl;
			sl = sl->next;
		}

		half = sl;
		prev_sl->next = NULL;
		reverse_list(&half);
		i = compare_list(*head, half);

		if (mid != NULL)
		{
			prev_sl->next = mid;
			mid->next = half;
		}
		else
		{
			prev_sl->next = half;
		}
	}
	return (i);
}

