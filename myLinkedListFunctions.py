from collections import deque

def fill_linked_list(linked_list):
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(3)

def remove_duplicates(linked_list):
    i = 0
    while i < len(linked_list) - 1:
        j = i + 1
        while j < len(linked_list):
            if linked_list[i] == linked_list[j]:
                del linked_list[j]
                j = j - 1
            j = j + 1
        i = i + 1


def main():
   my_linked_list = deque([1,2,3,4,2,3,1,2,3,21,2,1])
   print(my_linked_list)
   remove_duplicates(my_linked_list)
   print(my_linked_list)


if __name__ == "__main__":
    main()





