def toral_salary(path):
    try:
        with open(path, 'r', encoding='utf-8') as salary_info:
            file = salary_info.readlines()
            line = [int(line.split(',')[1]) for line in file]
            total_salary = sum(line)
            average_salary = total_salary // len(line)
            print(f"Загальна сума заробітної плати: {total_salary}, Середня заробітна плата: {average_salary}")
    except FileNotFoundError:
        print('File not found')
sal = toral_salary('salary_info.txt')
print(sal)