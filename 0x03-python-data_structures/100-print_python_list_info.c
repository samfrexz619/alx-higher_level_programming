#include <stdio.h>
#include <Python.h>

/**
 * print_python_list_info- prints py list
 * @p: pyobject
 * Return: nth
 */
void print_python_list_info(PyObject *p)
{
	long int sz, idx;
	PyListObject *lst;
	PyObject *itm;

	sz = Py_SIZE(p);
	printf("[*] Size of the Python List = %ld\n", sz);

	lst = (PyListObject *)p;
	printf("[*] Allocated = %ld\n", lst->allocated);

	for (idx = 0; idx < sz; idx++)
	{
		itm = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", idx, Py_TYPE(itm)->tp_name);
	}
}
