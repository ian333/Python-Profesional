def remove_duplicates(some_list:list) -> list:

    return list(set(some_list))



if __name__ == "__main__":
    print(remove_duplicates([1,2,3,6,5,6,3,2,1,4,5,8,6,5,8,5]))
    