def get_cats_info(path):
    try:
        with open(path, "r", encoding="utf-8") as file:
            list_cats = []
            items = file.readlines()
            for cat in items:
                cat = cat.strip().split(",")
                list_cats.append({"id": cat[0], "name": cat[1], "age": cat[2]})
        return list_cats
    except FileNotFoundError:
        print(f"File {path} is not found.")
    except IndexError:
        print("Error")

path = "info_for_assign_2.txt"
print(get_cats_info(path))

"""ertyuio"""