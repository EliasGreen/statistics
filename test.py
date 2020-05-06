import random
from numpy import sqrt, cos, pi
from scipy.special import erf
import scipy.integrate as integrate
Phi = lambda x: erf(x/2**0.5)/2


def task18():
    task = ''
    solving = ''
    answer = ''
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

    task += 'Дана таблица распределения вероятностей двумерной случайной величины (e, n):\n'
    task += "{:<5} {:<5} {:<5} {:<5}\n".format('e/n', column_values[0], column_values[1], column_values[2])
    task += "{:<5} {:<5} {:<5} {:<5}\n".format(row_values[0], matrix[0][0], matrix[0][1], matrix[0][2])
    task += "{:<5} {:<5} {:<5} {:<5}\n".format(row_values[1], matrix[1][0], matrix[1][1], matrix[1][2])
    task += 'Найти M(e), M(n), M(en), D(e), D(n), D(en)\n'

    M_e = round(row_values[0]*sum(matrix[0]) + row_values[1]*sum(matrix[1]), 2)
    solving += 'M(e) = {0}*{1} + {2}*{3} = {4}\n'.format(row_values[0], round(sum(matrix[0]), 2), row_values[1], round(sum(matrix[1]), 2), M_e)
    answer += 'M(e) = {0}\n'.format(M_e)
    M_n = round(column_values[0]*(matrix[0][0] + matrix[1][0]) + column_values[1]*(matrix[0][1] + matrix[1][1]) + column_values[2]*(matrix[0][2] + matrix[1][2]), 2)
    solving += 'M(n) = {0}*{1} + {2}*{3} + {4}*{5}= {6} \n'.format(column_values[0],
        round(matrix[0][0] + matrix[1][0], 2),
        column_values[1],
        round(matrix[0][1] + matrix[1][1], 2),
        column_values[2],
        round(matrix[0][2] + matrix[1][2], 2),
                  M_n)
    answer += 'M(n) = {0}\n'.format(M_n)

    M_e_n_1 = row_values[0]*column_values[0]*matrix[0][0] + row_values[0]*column_values[1]*matrix[0][1] + row_values[0]*column_values[2]*matrix[0][2]
    M_e_n_2 = row_values[1]*column_values[0]*matrix[0][0] + row_values[1]*column_values[1]*matrix[0][1] + row_values[1]*column_values[2]*matrix[0][2]

    M_e_n = round(M_e_n_1 + M_e_n_2, 2)
    answer += 'M(en) = {0}\n'.format(M_e_n)
    solving += 'M(en) = {0}*{1}*{2} + {3}*{4}*{5} + {6}*{7}*{8} + {9}*{10}*{11} + {12}*{13}*{14} + {15}*{16}*{17} = {18}\n'.format(row_values[0],column_values[0],matrix[0][0],
        row_values[0],column_values[1],matrix[0][1],
    row_values[0],column_values[2],matrix[0][2],
    row_values[1],column_values[0],matrix[0][0],
        row_values[1],column_values[1],matrix[0][1],
    row_values[1],column_values[2],matrix[0][2],
                  M_e_n)

    M_e_2 = round(row_values[0]*row_values[0]*sum(matrix[0]) + row_values[1]*row_values[1]*sum(matrix[1]), 2)
    M_n_2 = round(column_values[0]*column_values[0]*(matrix[0][0] + matrix[1][0]) + column_values[1]*column_values[1]*(matrix[0][1] + matrix[1][1]) + column_values[2]*column_values[2]*(matrix[0][2] + matrix[1][2]), 2)

    M_e_n_in_1 = pow(row_values[0]*column_values[0], 2)*matrix[0][0] + pow(row_values[0]*column_values[1], 2)*matrix[0][1] + pow(row_values[0]*column_values[2], 2)*matrix[0][2]
    M_e_n_in_2 = pow(row_values[1]*column_values[0], 2)*matrix[0][0] + pow(row_values[1]*column_values[1], 2)*matrix[0][1] + pow(row_values[1]*column_values[2], 2)*matrix[0][2]
    M_e_n_in_final = round(M_e_n_in_1 + M_e_n_in_2, 2)

    solving += 'M(e^2) = {0}\n'.format(M_e_2)
    solving += 'M(n^2) = {0}\n'.format(M_n_2)
    solving += 'M((en)^2) = {0}\n'.format(M_e_n_in_final)

    D_e = round(M_e_2 - M_e*M_e, 2)
    solving += 'D(e) = {0} - {1} = {2}\n'.format(M_e_2, round(M_e*M_e, 2), D_e)
    answer += 'D(e) = {0}\n'.format(D_e)
    D_n = round(M_n_2 - M_n*M_n, 2)
    solving += 'D(n) = {0} - {1} = {2}\n'.format(M_n_2,round( M_n*M_n, 2), D_n)
    answer += 'D(n) = {0}\n'.format(D_n)
    D_e_n = round(M_e_n_in_final - M_e_n*M_e_n, 2)
    solving += 'D(en) = {0} - {1} = {2}\n'.format(M_e_n_in_final, round(M_e_n*M_e_n, 2), D_e_n)
    answer += 'D(en) = {0}\n'.format(D_e_n)

    return task, solving, answer


def task16():
    task = ''
    solving = ''
    answer = ''
    all_a_values_list = [0.1, 0.3, 0.5, 1, 1.5, 1.8, 2, 2.2, 2.6, 3]
    a_value = random.choice(all_a_values_list)

    all_b_values_list = [0.1, 0.2, 0.3, 0.5, 0.6, 0.7, 0.8, 1]
    b_value = random.choice(all_b_values_list)

    all_low_values_list = [1, 2, 3]
    low_value = random.choice(all_low_values_list)

    all_sum_values_list = [1, 2, 3]
    high_value = low_value + random.choice(all_sum_values_list)

    task += 'Пусть E - нормально распределенная случайная величина\n'
    task += f'с параметрами a = {a_value}, б = {b_value}\n'
    task += f'Найти P({low_value} < E < {high_value})\n'

    solving += f'P({low_value} < E < {high_value}) =\n'
    solving += f'F({high_value}) - F({low_value}) =\n'
    solving += f'Ф(({high_value} - {a_value})/{b_value}) - Ф(({low_value} - {a_value})/{b_value}) =\n'
    solving += f'Ф({(high_value - a_value)/b_value}) - Ф({(low_value - a_value)/b_value}) =\n'
    solving += f'{Phi((high_value - a_value) / b_value)} - {Phi((low_value - a_value) / b_value)} =\n'
    solving += f'{Phi((high_value - a_value) / b_value) - Phi((low_value - a_value) / b_value)}\n'

    answer += f'P({low_value} < E < {high_value}) = '
    answer += f'{Phi((high_value - a_value) / b_value) - Phi((low_value - a_value) / b_value)}\n'

    return task, solving, answer


def task17():
    task = ''
    solving = ''
    answer = ''

    all_a_values_list = [0.1, 0.3, 0.5, 1, 1.5, 1.8, 2, 2.2, 2.6, 3]
    a_value = random.choice(all_a_values_list)

    all_b_values_list = [0.1, 0.2, 0.3, 0.5, 0.6, 0.7, 0.8, 1]
    b_value = random.choice(all_b_values_list)

    all_shift_values_list = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]
    shift_value = random.choice(all_shift_values_list)

    task += 'Пусть E - нормально распределенная случайная величина\n'
    task += f'с параметрами a = {a_value}, б = {b_value}\n'
    task += f'Найти P(|E - {a_value}| < {shift_value})\n'

    solving += f'P(|E - {a_value}| < {shift_value}) =\n'
    solving += '(Поскольку из нормально распределенной случайной величины вычитается ее математическое ожидание, можем воспользоваться следующей формулой)\n'
    solving += f'2Ф({shift_value}/{b_value}) =\n'
    solving += str(2*Phi(shift_value/b_value)) + '\n'

    answer += f'P(|E - {a_value}| < {shift_value}) = '
    answer += str(2*Phi(shift_value/b_value)) + '\n'

    return task, solving, answer


def task13and14():
    task13 = ''
    solving13 = ''
    answer13 = ''

    task14 = ''
    solving14 = ''
    answer14 = ''

    # чтобы добавить вариативности 13-ому заданию - достаточно добавить новую функцию в лист
    # сначала идет функция -> потом ее собственный интеграл от нуля до x
    all_functions = [('5cos(5x)', 'sin(5x)'), ('2x', 'x^2'), ('4*x^3','x^4')]
    main_interval_points = ['PI/10', '1', '1']

    selected_item = random.randint(0, len(all_functions) - 1)

    # выводим условие задачи
    task13 += 'E - непрерывная случайная величина с плотностью распределения p(x), заданной следующим образом:\n'
    task13 += f'p(x) = {all_functions[selected_item][0]}, для любого x, который принадлежит интервалу\n'
    task13 += f'(0;{main_interval_points[selected_item]})\n'
    task13 += f'p(x) = 0, для любого x, который не принадлежит интервалу\n'
    task13 += f'(0;{main_interval_points[selected_item]})\n'
    task13 += 'Нати функцию распределения F(x).\n'

    # выводим решение
    solving13 += 'F(x) = 0, при x <= 0\n'
    solving13 += f'F(x) = {all_functions[selected_item][1]}, при 0 < x <= {main_interval_points[selected_item]}\n'
    solving13 += f'F(x) = 1, при x > {main_interval_points[selected_item]}\n'

    answer13 += 'F(x) = 0, при x <= 0\n'
    answer13 += f'F(x) = {all_functions[selected_item][1]}, при 0 < x <= {main_interval_points[selected_item]}\n'
    answer13 += f'F(x) = 1, при x > {main_interval_points[selected_item]}\n'

    # Далее идет условие/решение 14-ой задачи
    task14 += 'E - непрерывная случайная величина примера 13.\n'
    task14 += 'Найти M(E), D(E), б(E).\n'
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

    solving14 += 'M(E) = {0}\n'.format(M_E_values[selected_item][0])
    solving14 += 'D(E) = {0}\n'.format(D_E_values[selected_item])
    solving14 += 'б(E) = {0}\n'.format(B_E_values[selected_item])

    answer14 += 'M(E) = {0}\n'.format(M_E_values[selected_item][0])
    answer14 += 'D(E) = {0}\n'.format(D_E_values[selected_item])
    answer14 += 'б(E) = {0}\n'.format(B_E_values[selected_item])

    return task13, solving13, answer13,  task14, solving14, answer14


def task15():
    task = ''
    solving = ''
    answer = ''

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

    task += f'Вероятность наступления события А в одном опыте равна {p}.\n'
    task += f'Найти вероятность того, что событие А наступит {k} раз в {n} опытах.\n'

    solving += 'Так как n*p*q много больше 9, то\n'
    solving += 'воспользуемся локальной теоремой лапласа\n'
    solving += 'Pn(K) = Phi(x)/sqrt(n*p*q)\n'
    solving += 'Где x = (k - np)/sqrt(n*p*q)\n'
    solving += 'Найдем значение x:\n'
    solving += f'x = ({k} - {n}*{p})/sqrt({(n*p*q)}) = {(k - n*p)/sqrt(n*p*q)}\n'
    solving += 'Т.к. Phi(x) - четная функция, то Phi(-x) = Phi(x)\n'
    solving += f'Phi({abs((k - n*p)/sqrt(n*p*q))}) = {Phi(abs((k - n*p)/sqrt(n*p*q)))}\n'
    solving += f'Тогда P = {Phi(abs((k - n*p)/sqrt(n*p*q)))/sqrt(n*p*q)}\n'
    answer += f'P = {Phi(abs((k - n*p)/sqrt(n*p*q)))/sqrt(n*p*q)}\n'

    return task, solving, answer



