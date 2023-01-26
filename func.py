list = ["Семен", "Ян", "Олег", "Tom"]
result_list = []
for i in range(len(list)):
    if len(list[i]) <= 3:
        result_list.append(list[i])
print(result_list)

