def load_params(l: int, w: int, m: int):
    total_mass = 0
    number_load = 0
    while True:
        load_l = int(input('введите длину : '))
        load_w = int(input('введите ширину : '))
        load_m = int(input('введите массу : '))
        load_params = load_l * load_w
        total_mass += load_m
        if load_params < (l * w) and total_mass < m:
            print('общая масса : ', total_mass)
            number_load += 1
            print('количество мест : ', number_load)
        else:
            print('превышение габаритов и массы')
            break
    return total_mass - load_m, number_load


if __name__ == '__main__':
    print(load_params(400, 300, 500))