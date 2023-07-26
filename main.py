footballers_goals = {'Eusebio': 120, 'Cruyff': 104, 'Pele': 150, 'Ronaldo': 132, 'Messi': None}


def convert_none_to_str(my_dict):
    for key, value in my_dict.items():
        my_dict[key] = str(value)
    return my_dict


def convert_str_back_to_int(my_dict):
    for key, value in my_dict.items():
        my_dict[key] = int(value) if value != 'None' else None
    return my_dict


def aggregate_function_sort_by_dict_value(initial_dict):
    initial_dict_none_as_str = convert_none_to_str(initial_dict)
    dict_sorted_by_values = sorted(initial_dict_none_as_str.items(), key=lambda x: x[1])
    sorted_dict = dict(dict_sorted_by_values)
    return convert_str_back_to_int(sorted_dict)


print(aggregate_function_sort_by_dict_value(footballers_goals))
