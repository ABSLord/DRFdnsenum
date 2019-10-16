
def find_index_in_list(lst, pattern):
    indexes = [i for i, s in enumerate(lst) if pattern in s]
    if not indexes:
        return -1
    else:
        return indexes[-1]


def parse_dnsenum_output(output):
    result = dict()
    lst = output.split("\n\n")

    index = find_index_in_list(lst, "Host\'s addresses:")
    result["Host\'s addresses:"] = lst[index + 1].split("\n") if index != -1 else [""]

    index = find_index_in_list(lst, "Name Servers")
    result["Name Servers"] = lst[index + 1].split("\n") if index != -1 else [""]

    index = find_index_in_list(lst, "Mail (MX) Servers")
    result["Mail (MX) Servers"] = lst[index + 1].split("\n") if index != -1 else [""]

    return result
