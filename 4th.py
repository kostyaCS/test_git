from typing import List
import urllib.request


def read_input_file(url: str, number: int) -> List[List[str]]:
    """
    (str, int) -> (list(list))
    Preconditions: 0 <= number <= 77
    Return list of strings lists from url
    >>> read_input_file('https://raw.githubusercontent.com/anrom7/\
Test_Olya/master/New%20folder/total.txt',1)
    [['1', 'Мацюк М. І.', '+', '197.859', '10.80']]
    >>> read_input_file('https://raw.githubusercontent.com/anrom7/\
Test_Olya/master/New%20folder/total.txt',3)
    [['1', 'Мацюк М. І.', '+', '197.859', '10.80'], ['2', 'Проць О. В.', '+', '197.152', '11.60'],\
 ['3', 'Лесько В. О.', '+', '195.385', '10.60']]
    """
    output_text = []
    with urllib.request.urlopen(url) as webpage:
        for line in webpage:
            line = line.decode('utf-8').strip()
            tab_line = line.split('\t')
            if tab_line[0].isdigit():
                if number == 0:
                    break
                tab_line[2] = '+'
                output_text.append(tab_line[:4])
            if tab_line[0].startswith('Середній'):
                output_text[-1].append(tab_line[0].split()[-1])
                number -=1
    return output_text


def write_csv_file(url: str):
    """
    Writes info from read_input_file in file 'total.csv'
    >>> write_csv_file('https://raw.githubusercontent.com/\
anrom7/Test_Olya/master/New%20folder/total.txt')
    """
    with open('total.csv', 'w', encoding='utf-8') as new_file:
        new_file.write('№,ПІБ,Д,Заг.бал,С.б.док.осв.\n')
        for line in read_input_file(url, 78):
            new_file.write(','.join(line) + '\n')
