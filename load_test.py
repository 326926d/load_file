# расчет груза при заданных параметрах
def load_params(l: int, w: int, h: int, m: int):
    total_mass = 0
    number_load = 0
    total_height = 0
    l_1 = []
    while True:
        load_l = float(input('введите длину : '))
        load_w = float(input('введите ширину : '))
        load_h = float(input('введите высоту груза : '))
        load_m = float(input('введите массу : '))
        total_mass += load_m
        print('общая масса : ', total_mass)
        total_height += load_h
        if load_l < l and load_w < w and load_h < total_height:
            number_load += 1
            l_1.append([load_l, load_w, load_h])
            print('количество мест', number_load, 'список', l_1)
        else:
            print(" превышение параметров")
            break
    return l_1, number_load


if __name__ == '__main__':
    print(load_params(400, 300, 150, 500))