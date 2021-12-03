# расчет груза при заданных параметрах
def load_params(l: int, w: int, h: int, m: int):
    total_mass = 0
    number_load = 0
    total_height = 0
    l_1 = []
    l_2 = []
    l_3 = []
    dict_1 = {}
    while True:
        load_l = float(input('введите длину : '))
        load_w = float(input('введите ширину : '))
        load_h = float(input('введите высоту груза : '))
        load_m = float(input('введите массу : '))
        total_mass += load_m
        print('общая масса : ', total_mass)
        total_height += load_h
        print('общая высота : ', total_height)
        if total_mass < m and total_height < h:
            number_load += 1
            l_1.append([load_l, load_w, load_h])
            for elems in range(len(l_1)):
                l_2.append(elems)
                l_3.append(l_1[elems])
                dict_1 = dict(zip(l_2, l_3))
        else:
            print(" превышение параметров")
            break
    return dict_1


if __name__ == '__main__':
    print(load_params(400, 300, 150, 500))