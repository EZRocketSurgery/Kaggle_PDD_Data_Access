def dataset_paths():
    with open("dataset_list.txt", "r") as file:
        lines = file.readlines()
    lines = [line.strip() for line in lines]
    return lines