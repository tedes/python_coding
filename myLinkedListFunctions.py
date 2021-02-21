import collections

def fill_linked_list(linked_list):
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(3)



def main():
   my_linked_list = collections.deque()
   fill_linked_list(my_linked_list)
   print(my_linked_list)


if __name__ == "__main__":
    main()





