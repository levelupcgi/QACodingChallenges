from collections import OrderedDict


# option 1
def remove_duplicates1(some_list):
    result = []
    for elem in some_list:
        if elem not in result:
            result.append(elem)
    return result

def remove_duplicates_with_set(some_list):
    """
    order of elements is lost
    :param some_list:
    :return:
    """

    unique_some_list = list(set(some_list))


def remove_duplicates_with_hash(some_list):
    result = list(OrderedDict.fromkeys(some_list))
    # printing list after removal

    print("The list after removing duplicates: " + str(result))

