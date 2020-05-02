import random
from numpy import sqrt, sin, cos, pi
from scipy.special import erf
import scipy.integrate as integrate
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


def task13and14():
    # чтобы добавить вариативности 13-ому заданию - достаточно добавить новую функцию в лист
    # сначала идет функция -> потом ее собственный интеграл от нуля до x
    all_functions = [('5cos(5x)', 'sin(5x)'), ('2x', 'x^2'), ('4*x^3','x^4')]
    main_interval_points = ['PI/10', '1', '1']

    selected_item = random.randint(0, len(all_functions) - 1)

    # выводим условие задачи
    print('Условие задачи:')
    print('E - непрерывная случайная величина с плотностью распределения p(x), заданной следующим образом:')
    print(f'p(x) = {all_functions[selected_item][0]}, для любого x, который принадлежит интервалу '
          f'(0;{main_interval_points[selected_item]})')
    print(f'p(x) = 0, для любого x, который не принадлежит интервалу '
          f'(0;{main_interval_points[selected_item]})')
    print('Нати функцию распределения F(x).')

    # выводим решение
    print('Решение:')
    print('F(x) = 0, при x <= 0')
    print(f'F(x) = {all_functions[selected_item][1]}, при 0 < x <= {main_interval_points[selected_item]}')
    print(f'F(x) = 1, при x > {main_interval_points[selected_item]}')

    # Далее идет условие/решение 14-ой задачи
    print('\nУсловие задачи:')
    print('E - непрерывная случайная величина примера 13.')
    print('Найти M(E), D(E), б(E).\n')
    M_E_values = [
        integrate.quad(lambda x: x*5*cos(5*x), 0, pi/10),
        integrate.quad(lambda x: x * (x*x), 0, 1),
        integrate.quad(lambda x: x * 4 * x * x * x, 0, 1),
                  ]

    xx_F_values = [
        integrate.quad(lambda x: x*x * 5 * cos(5 * x), 0, pi / 10),
        integrate.quad(lambda x: x*x * (x*x), 0, 1),
        integrate.quad(lambda x: x*x * 4 * x * x * x, 0, 1),
    ]

    D_E_values = [xx_F_values[i][0] - (M_E_values[i][0]*M_E_values[i][0]) for i in range(len(M_E_values))]
    B_E_values = [sqrt(d_value) for d_value in D_E_values]

    print('M(E) = ', M_E_values[selected_item][0])
    print('D(E) = ', D_E_values[selected_item])
    print('б(E) = ', B_E_values[selected_item])


def task15():
    n = 1
    p = 1
    q = 1
    k = 1

    while n*p*q <= 9 or not(sqrt(n*p*q).is_integer()):
        n = random.randint(100, 10000)
        p_values = [0.1, 0.2, 0.3, 0.5, 0.6, 0.7, 0.8]
        p = random.choice(p_values)
        q = (10.0 - p*10)/10.0

        k = random.randint(45, n - 50)

    phi_result = abs((k - n*p)/sqrt(n*p*q))


    print(n, p, q)

    print('Условие задачи:')
    print(f'Вероятность наступления события А в одном опыте равна {p}.')
    print(f'Найти вероятность того, что событие А наступит {k} раз в {n} опытах.')

    print('Решение:')
    print('Так как n*p*q много больше 9, то')
    print('воспользуемся локальной теоремой лапласа')
    print('Pn(K) = Phi(x)/sqrt(n*p*q)')
    print('Где x = (k - np)/sqrt(n*p*q)')
    print('Найдем значение x:')
    print(f'x = ({k} - {n}*{p})/sqrt({(n*p*q)}) = {(k - n*p)/sqrt(n*p*q)}')
    print('Т.к. Phi(x) - четная функция, то Phi(-x) = Phi(x)')
    print(f'Phi({abs((k - n*p)/sqrt(n*p*q))}) = {Phi(abs((k - n*p)/sqrt(n*p*q)))}')
    print(f'Тогда P = {Phi(abs((k - n*p)/sqrt(n*p*q)))/sqrt(n*p*q)}')

task15()



