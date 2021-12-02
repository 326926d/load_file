# расчет груза при заданных параметрах
def load_params(l: int, w: int, h: int, m: int):
    total_mass = 0
    number_load = 0
    total_height = 0
    while True:
        load_l = float(input('введите длину : '))
        load_w = float(input('введите ширину : '))
        load_h = float(input('введите высоту груза : '))
        load_m = float(input('введите массу : '))
        load_params = load_l * load_w
        total_mass += load_m
        print('общая масса : ', total_mass)
        total_height += load_h
        if total_mass > m:
            print('превышена масса груза')
        elif load_params > (l * w):
            print('превышены габариты груза')
            break
        elif total_height > h:
            print('превышена погрузочная высота')
            break
        else:
            number_load += 1
        
    return total_mass, number_load


if __name__ == '__main__':
    print(load_params(400, 300, 150, 500))