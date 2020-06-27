# Программирование (Python)
# 6 семестр, тема 1

# Лабораторная работа 1

"""
Используя обучающий набор данных о пассажирах Титаника, находящийся в проекте (оригинал: https://www.kaggle.com/c/titanic/data), найдите ответы на следующие вопросы: 

1. Какое количество мужчин и женщин ехало на параходе? Приведите два числа через пробел.

2. Подсчитайте сколько пассажиров загрузилось на борт в различных портах? Приведите три числа через пробел.

3. Посчитайте долю погибших на параходе (число и процент)?

4. Какие доли составляли пассажиры первого, второго, третьего класса?

5. Вычислите коэффициент корреляции Пирсона между количеством супругов (SibSp) и количеством детей (Parch).

6. Выясните есть ли корреляция (вычислите коэффициент корреляции Пирсона) между:
1) возрастом и параметром survival;
2) полом человека и параметром survival;
3) классом, в котором пассажир ехал, и параметром survival.

7. Посчитайте средний возраст пассажиров и медиану.
8. Посчитайте среднюю цену за билет и медиану.

9. Какое самое популярное мужское имя на корабле?
10. Какие самые популярные мужское и женские имена людей, старше 15 лет на корабле?

"""

import numpy as np
import pandas  # импортирование библиотеки для считывания данных

# считаем данных из файла, в качестве столбца индексов используем PassengerId
data = pandas.read_csv('train.csv', index_col="PassengerId")


# TODO #1
def get_sex_distrib(data):
    """
    1. Какое количество мужчин и женщин ехало на параходе? Приведите два числа через пробел.
    """
    # count how many males, females
    res = data['Sex'].value_counts()
    n_male, n_female = res['male'], res['female']
    return n_male, n_female


# TODO #2
def get_port_distrib(data):
    """  
    2. Подсчитайте сколько пассажиров загрузилось на борт в различных портах? Приведите три числа через пробел.
    """
    ports = data['Embarked'].value_counts()
    port_S, port_C, port_Q = ports['S'], ports['C'], ports['Q']
    return port_S, port_C, port_Q


# TODO #3
def get_surv_percent(data):
    """
    3. Посчитайте долю погибших на параходе (число и процент)?
    """
    res = data['Survived'].value_counts()
    n_died, perc_died = res[0], res[0] / (res[1] + res[0])

    return n_died, perc_died


# TODO #4
def get_class_distrib(data):
    """
    4. Какие доли составляли пассажиры первого, второго, третьего класса?    
    """
    res = data['Pclass'].value_counts()
    n_pas_f_cl, n_pas_s_cl, n_pas_t_cl = res[1], res[2], res[3]

    return n_pas_f_cl, n_pas_s_cl, n_pas_t_cl


# TODO #5
def find_corr_sibsp_parch(data):
    """
    5. Вычислите коэффициент корреляции Пирсона между количеством супругов (SibSp) и количеством детей (Parch).
    """
    SibSp = data['SibSp']
    Parch = data['Parch']

    corr_val = -1

    corr_val = SibSp.corr(Parch, method='pearson')
    return corr_val

# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.corr.html 
# DataFrame.corr(self, method='pearson', min_periods=1)  
# s1.corr(s2, method=histogram_intersection)   
# method{‘pearson’, ‘kendall’, ‘spearman’} or callable

# https://www.kaggle.com/c/titanic/data
# https://moodle.herzen.spb.ru/course/view.php?id=3731 

# TODO #6-1
def find_corr_age_survival(data):
    """
    6. Выясните есть ли корреляция (вычислите коэффициент корреляции Пирсона) между:
    
    - возрастом и параметром survival;

    """
    Age = data['Age']
    Survived = data['Survived']

    corr_val = -1

    corr_val = Age.corr(Survived, method='pearson')
    return corr_val


# TODO #6-2
def find_corr_sex_survival(data):
    """
    6. Выясните есть ли корреляция (вычислите коэффициент корреляции Пирсона) между:
    
    - полом человека и параметром survival;

    Корреляция невозможна - разные типы данных
    """

    corr_val = -1
    print(corr_val)
    return corr_val


# TODO #6-3
def find_corr_class_survival(data):
    """
    6. Выясните есть ли корреляция (вычислите коэффициент корреляции Пирсона) между:

    - классом, в котором пассажир ехал, и параметром survival.
    """
    pclass = data['Pclass']
    surv = data['Survived']

    corr_val = -1
    corr_val = pclass.corr(surv, method='pearson')

    return corr_val

find_corr_class_survival(data)
# TODO #7
def find_pass_mean_median(data):
    """
    7. Посчитайте средний возраст пассажиров и медиану.

    1.1. Разработка скрипта, вычисляющего статистические показатели (среднее значение, дисперсия, среднее квадратичное отклонение) для данных, считанных из CSV-файла.

1.2. Осуществить рефакторинг (модификация) скрипта, вычисляющего статистические показатели для данных, считанных из CSV, с использованием библиотеки научных вычислений numpy.
    """
    Age = data['Age']
    # среднее квадратичное отклонение
    standard_deviation = np.std(Age)
    # дисперсия
    variance = np.var(Age)
    mean_age, median = Age.mean(), Age.median()
    return mean_age, median

find_pass_mean_median(data)
# TODO #8
def find_ticket_mean_median(data):
    """
    8. Посчитайте среднюю цену за билет и медиану.
    """

    # mean_price, median = None, None
    # print(mean_age, median)
    Fare = data['Fare']

    mean_price, median = Fare.mean(), Fare.median()
    return mean_price, median


# TODO #9
def find_popular_name(data):
    """
    9. Какое самое популярное мужское имя на корабле?
    """
    men = data[data['Sex']=='male']
    name = ""
    name = men['Name'].value_counts().idxmax()
    print(name)
    return name

# find_popular_name(data)
# TODO #10
def find_popular_adult_names(data):
    """
    10. Какие самые популярные мужское и женские имена людей, старше 15 лет на корабле?
    """
    popular_male_name, popular_female_name = "", ""
    return popular_male_name, popular_female_name


# ------------------------------

# Реализуем вычисление количества пассажиров на параходе и опишем предварительные действия с данными (считывание)

# После загрузки данных с помощью метода read_csv и индексации его по первому столбцу данных (PassangerId) становится доступно выборка данных по индексу. 
# С помощью запроса ниже мы можем получить имя сотого пассажира
# print((data.iloc[100]['Name']))


def get_number_of_pass(data_file):
    """
        Подсчет количества пассажиров. 
        data_file - str
        В качестве аргумента удобнее всего использовать строковую переменную, куда будет передаваться название файла (т. к. далее, возможно, потребуется подсчитать параметры для другого набора данных test.csv)
    """
    male_int, female_int = 0, 0
    # считывание и обработка данных
    data = pandas.read_csv(data_file, index_col="PassengerId")

    # считать данных из столбца возможно с помощью метода value_counts()
    res = data['Sex'].value_counts()
    # res будет содержать ассоциативный массив, ключами в котором являются значения столбца sex, а целочисленные значениями - количества пассажиров обоих полов
    male_int, female_int = res['male'], res['female']
    return male_int, female_int


def test_get_number_of_pass():
    assert get_number_of_pass('train.csv') == (577,314), " Количество мужчин и женщин на Титанике"
    assert get_port_distrib('train.csv') == (644,168,77), " Количество - сколько пассажиров загрузилось на борт в различных портах"
    assert get_surv_percent('train.csv') == (549,0.6161616161616161), " Количество и доля погибших на параходе (число и процент)"
    assert get_class_distrib('train.csv') == (216,184,491), " Какие доли составляли пассажиры первого, второго, третьего класса"
    assert find_corr_sibsp_parch('train.csv') == (0.41483769862015557), " Коэффициент корреляции Пирсона между количеством супругов (SibSp) и количеством детей (Parch) "
    assert find_corr_age_survival('train.csv') == (-0.07722109457217768), " Коэффициент корреляции Пирсона между возрастом человека и параметром survival "
    assert find_corr_sex_survival('train.csv') == (-1), " Коэффициент корреляции Пирсона между полом человека и параметром survival "
    assert find_corr_class_survival('train.csv') == (-0.33848103596101478), " Коэффициент корреляции Пирсона между классом, в котором пассажир ехал, и параметром survival "
    assert find_pass_mean_median('train.csv') == (29.69911764705882,28.0), " средний возраст пассажиров и медиана "
    assert find_ticket_mean_median('train.csv') == (-0.07722109457217768), " средняя цена за билет и медиана "
    assert find_popular_name('train.csv') == (-0.07722109457217768), " самое популярное мужское имя на корабле "
    assert find_popular_adult_names('train.csv') == (-0.07722109457217768), " самые популярные мужское и женские имена людей старше 15 лет на корабле "

# аналогично протестировать остальные функции
