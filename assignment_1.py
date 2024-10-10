def total_salary(path):
    try:
        with open(path, "r", encoding="utf-8") as file:
            all_salary = 0
            count = 0
            for el in file:
                person, money = el.strip().split(",")
                if money == "":
                    break
                all_salary += int(money)
                count += 1
            average_salary = all_salary // count
            return (all_salary, average_salary)
    except FileNotFoundError:
        print(f"File {path} is not found")
    except ValueError:
        print("Value error")

path = "info_for_salary.txt"
print(total_salary(path))