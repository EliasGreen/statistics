import random
from scipy.special import erf
Phi = lambda x: erf(x/2**0.5)/2


def task18():
    column_values = [random.randint(-3, 3) for i in range(3)]
    row_values = [random.randint(-3, 3) for i in range(2)]
    matrix = []
    for i in range(2):
        row = []
        while len(row) < 3:
            if len(row) == 2:
                if i == 1:
                    row.append(round(1 - sum(row) - sum(matrix[0]), 1))
                    break
            random_num = round(random.random(), 1)
            if random_num >= 0.5:
                random_num = 0.1
            if i == 1 and sum(matrix[0]) + sum(row) + random_num <= 1:
                row.append(random_num)
            elif i == 0 and sum(row) + random_num <= 1:
                row.append(random_num)

        matrix.append(row)

    print('Условие:')
    print('Дана таблица распределения вероятностей двумерной случайной величины (e, n):')
    print ("{:<5} {:<5} {:<5} {:<5}".format('e/n', column_values[0], column_values[1], column_values[2]))
    print("{:<5} {:<5} {:<5} {:<5}".format(row_values[0], matrix[0][0], matrix[0][1], matrix[0][2]))
    print("{:<5} {:<5} {:<5} {:<5}".format(row_values[1], matrix[1][0], matrix[1][1], matrix[1][2]))

    print('\nРешение:')
    M_e = row_values[0]*sum(matrix[0]) + row_values[1]*sum(matrix[1])
    print('M(e) = {0}*{1} + {2}*{3} = {4}'.format(row_values[0], sum(matrix[0]), row_values[1], sum(matrix[1]), M_e))

    M_n = column_values[0]*(matrix[0][0] + matrix[1][0]) + column_values[1]*(matrix[0][1] + matrix[1][1]) + column_values[2]*(matrix[0][2] + matrix[1][2])
    print('M(n) = {0}*{1} + {2}*{3} + {4}*{5}= {6}'
          .format(column_values[0],
        (matrix[0][0] + matrix[1][0]),
        column_values[1],
        (matrix[0][1] + matrix[1][1]),
        column_values[2],
        (matrix[0][2] + matrix[1][2]),
                  M_n))

    M_e_n_1 = row_values[0]*column_values[0]*matrix[0][0] + row_values[0]*column_values[1]*matrix[0][1] + row_values[0]*column_values[2]*matrix[0][2]
    M_e_n_2 = row_values[1]*column_values[0]*matrix[0][0] + row_values[1]*column_values[1]*matrix[0][1] + row_values[1]*column_values[2]*matrix[0][2]

    M_e_n = M_e_n_1 + M_e_n_2

    print('M(en) = {0}*{1}*{2} + {3}*{4}*{5} + {6}*{7}*{8} + {9}*{10}*{11} + {12}*{13}*{14} + {15}*{16}*{17} = {18}'
          .format(row_values[0],column_values[0],matrix[0][0],
        row_values[0],column_values[1],matrix[0][1],
    row_values[0],column_values[2],matrix[0][2],
    row_values[1],column_values[0],matrix[0][0],
        row_values[1],column_values[1],matrix[0][1],
    row_values[1],column_values[2],matrix[0][2],
                  M_e_n))

    M_e_2 = row_values[0]*row_values[0]*sum(matrix[0]) + row_values[1]*row_values[1]*sum(matrix[1])
    M_n_2 = column_values[0]*column_values[0]*(matrix[0][0] + matrix[1][0]) + column_values[1]*column_values[1]*(matrix[0][1] + matrix[1][1]) + column_values[2]*column_values[2]*(matrix[0][2] + matrix[1][2])

    M_e_n_in_1 = pow(row_values[0]*column_values[0], 2)*matrix[0][0] + pow(row_values[0]*column_values[1], 2)*matrix[0][1] + pow(row_values[0]*column_values[2], 2)*matrix[0][2]
    M_e_n_in_2 = pow(row_values[1]*column_values[0], 2)*matrix[0][0] + pow(row_values[1]*column_values[1], 2)*matrix[0][1] + pow(row_values[1]*column_values[2], 2)*matrix[0][2]
    M_e_n_in_final = M_e_n_in_1 + M_e_n_in_2

    print('M(e^2) =', M_e_2)
    print('M(n^2) =', M_n_2)
    print('M((en)^2) =', M_e_n_in_final)

    D_e = M_e_2 - M_e*M_e
    print('D(e) = {0} - {1} = {2}'.format(M_e_2, M_e*M_e, D_e))

    D_n = M_n_2 - M_n*M_n
    print('D(n) = {0} - {1} = {2}'.format(M_n_2, M_n*M_n, D_n))

    D_e_n = M_e_n_in_final - M_e_n*M_e_n
    print('D(en) = {0} - {1} = {2}'.format(M_e_n_in_final, M_e_n*M_e_n, D_e_n))


def task16():
    all_a_values_list = [0.1, 0.3, 0.5, 1, 1.5, 1.8, 2, 2.2, 2.6, 3]
    a_value = random.choice(all_a_values_list)

    all_b_values_list = [0.1, 0.2, 0.3, 0.5, 0.6, 0.7, 0.8, 1]
    b_value = random.choice(all_b_values_list)

    all_low_values_list = [1, 2, 3]
    low_value = random.choice(all_low_values_list)

    all_sum_values_list = [1, 2, 3]
    high_value = low_value + random.choice(all_sum_values_list)

    print('Условие:')
    print('Пусть E - нормально распределенная случайная величина')
    print(f'с параметрами a = {a_value}, б = {b_value}')
    print(f'Найти P({low_value} < E < {high_value})')

    print('Решение')
    print(f'P({low_value} < E < {high_value}) =')
    print(f'F({high_value}) - F({low_value}) =')
    print(f'Ф(({high_value} - {a_value})/{b_value}) - Ф(({low_value} - {a_value})/{b_value}) =')
    print(f'Ф({(high_value - a_value)/b_value}) - Ф({(low_value - a_value)/b_value}) =')
    print(f'{Phi((high_value - a_value) / b_value)} - {Phi((low_value - a_value) / b_value)} =')
    print(f'{Phi((high_value - a_value) / b_value) - Phi((low_value - a_value) / b_value)}')


def task17():
    all_a_values_list = [0.1, 0.3, 0.5, 1, 1.5, 1.8, 2, 2.2, 2.6, 3]
    a_value = random.choice(all_a_values_list)

    all_b_values_list = [0.1, 0.2, 0.3, 0.5, 0.6, 0.7, 0.8, 1]
    b_value = random.choice(all_b_values_list)

    all_shift_values_list = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]
    shift_value = random.choice(all_shift_values_list)

    print('Условие:')
    print('Пусть E - нормально распределенная случайная величина')
    print(f'с параметрами a = {a_value}, б = {b_value}')
    print(f'Найти P(|E - {a_value}| < {shift_value})')

    print('\nРешение:')
    print(f'P(|E - {a_value}| < {shift_value}) =')
    print('(Поскольку из нормально распределенной случайной величины вычитается ее математическое '
          'ожидание, можем воспользоваться следующей формулой)')
    print(f'2Ф({shift_value}/{b_value}) = ')
    print(2*Phi(shift_value/b_value))
