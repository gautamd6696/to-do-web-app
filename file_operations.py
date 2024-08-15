
def get_list(filename="to_dos.txt"):
    with open(filename, "r") as file:
        to_do_list_local = file.readlines()
    return to_do_list_local


def write(to_do_arg, filename="to_dos.txt"):
    with open(filename, "w") as file:
        file.writelines(to_do_arg)
