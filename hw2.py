def get_cats_info(path):
    cats_info_list = []
    try:
        with open(path, 'r', encoding='utf-8') as cats_info_file:
            lines = cats_info_file.readlines()
            for line in lines:
                cat_data = line.strip().split(',')
                cat_info = {'id': cat_data[0], 'name': cat_data[1], 'age': cat_data[2]}
                cats_info_list.append(cat_info)
    except Exception as e:
                print(f'Error: {e}')
    return cats_info_list


print(get_cats_info('cats_info_file.txt'))

