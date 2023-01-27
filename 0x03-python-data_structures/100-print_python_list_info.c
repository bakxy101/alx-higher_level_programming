#include "lists.h"

/**
 * print_python_list_info - Prints information about python lists
 * @p: Pointer to a list object defined in python
 *
 * Return: void
 */
void print_python_list_info(PyObject *p)
{
	int i, length;
	PyListObject *list;

	list = (PyListObject *) p;
	length = list->ob_base.ob_size;
	printf("[*] Size of the Python List = %ld\n", list->ob_base.ob_size);
	printf("[*] Allocated = %ld\n", list->allocated);

	for (i = 0; i < length; ++i)
		printf(
			"Element %d: %s\n",
			i,
			list->ob_base.ob_base.ob_type->tp_name
		);
}
