# расчет груза при заданных параметрах
def load_params(l: int, w: int, m: int, h: int):
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
        total_height += load_h
        if load_params < (l * w) and total_mass < m and total_height < h:
            print('общая масса : ', total_mass)
            number_load += 1
            print('количество мест : ', number_load)
        else:
            print('превышение габаритов и массы')
            break
    return total_mass - load_m, number_load


if __name__ == '__main__':
    print(load_params(400, 300, 500, 100))