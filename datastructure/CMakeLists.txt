cmake_minimum_required(VERSION 3.19)
project(datastructure)

set(CMAKE_CXX_STANDARD 14)

include_directories(.)

add_executable(datastructure
        binary_search.c
        BST_pre-in_to_post.c
        bubble_sort.c
        circulardoublyLinkedlist.c
        circularLinkedlist.c
        circularqueue.c
        doubleendedqueue.c
        four-linkedlist.c
        heap_sort.c
        infixtopostfix.c
        insertion_sort.c
        linkedlist.c
        main.cpp
        merge_sort.c
        phone_book.c
        polynomials.c
        priorityqueue.c
        quick_sort.c
        recursion.c
        selection_sort.c
        simplequeue.c
        spanningTree.c
        stack.c
        Untitled1.c)
