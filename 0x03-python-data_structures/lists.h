#ifndef LISTS_H
#define LISTS_H

#include <Python.h>

typedef struct listint_s {
    int n;
    struct listint_s *next;
} listint_t;

void print_list_integer(listint_t *my_list);
int element_at(listint_t *my_list, int idx);
void replace_in_list(listint_t **my_list, int idx, int element);
void print_reversed_list_integer(listint_t *my_list);
int new_in_list(listint_t **my_list, int idx, int element);
int no_c(char *my_string);
void print_matrix_integer(int **matrix);
PyObject *add_tuple(PyObject *tuple_a, PyObject *tuple_b);
PyObject *multiple_returns(char *sentence);
int max_integer(listint_t *my_list);
int divisible_by_2(listint_t *my_list);
int delete_at(listint_t **my_list, unsigned int idx);

int is_palindrome(listint_t **head);
void print_python_list_info(PyObject *p);

#endif /* LISTS_H */
