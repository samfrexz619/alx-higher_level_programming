#include "lists.h"
/**
 * check_cycle - checks a singly list
 * @list: pointer
 * Return: 0 or 1
 */
int check_cycle(listint_t *list)
{
	listint_t *r2;
	listint_t *pv;

	r2 = list;
	pv = list;
	while (list && r2 && r2->next)
	{
		list = list->next;
		r2 = r2->next->next;

		if (list == p2)
		{
			list = pv;
			pv = r2;
			while (1)
			{
				r2 = pv;
				while (r2->next != list && r2->next != pv)
				{
					r2 = r2->next;
				}
				if (r2->next == list)
					break;

				list = list->next;
			}
			return (1);
		}
	}
	return (0);
}
