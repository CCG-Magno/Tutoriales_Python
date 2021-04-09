import csv,math,os,re,typing

from typing import Generator,List

import easy_plot
from easy_plot import plot_fn



def is_csv_format(text_file:str)->bool:
    '''
        Verifies that the provided text_file contains the .csv format in its string name.

        Parameters:
            text_file : str
                The str representation of the filename we wish to verify

        Returns:
             bool

        Raises:
            AssertionException - In case where text_file isn't of type str
    '''
    assert(isinstance(text_file,str))

    pattern = r"^.?[\w]+.csv$"

    compiled = re.compile(pattern)
    result = re.match(compiled, text_file)

    return None != result

def write_dic_to_csv(filename:str , dic:Dict[str, Generator[int]]):

    with open(filename , 'w') as csv_file:
        fields = dic.keys()
        writer = csv.DictWriter(csv_file, fields)

        writer.writerow(dic)
    return

def write_csv(name:str, data:List[List[int]]):
    '''
        Verifies that the provided text_file contains the .csv format in its string name.

        Parameters:
            text_file : str
                The str representation of the filename we wish to verify

        Returns:
             bool

        Raises:
            AssertionException - In case where text_file isn't of type str, isnt a valid csv or is empty
    '''
    assert(is_csv_format(name))
    assert(len(name)> 0 and name != None)

    with open(name, 'w') as file:

        csv_writer = csv.writer(name)

        for line in data:
            csv_writer.write(line)

    return

def constant(inp=gen_input()):

    for i in inp:
        yield 1

def linear(inp=gen_input()):

    for i in inp:
        yield i

def quadratic(inp=gen_input()):

    for i in inp:
        yield i * i

def logarithmic(inp=gen_input()):

    for i in inp:
        if i > 0:
            yield math.log10(i)
        else:
            yield 0

def n_logarithmic(inp=gen_input()):

    for i in inp:
        if i > 0:
            yield i * math.log10(i)
        else:
            yield 0

def exponential(inp=gen_input()):
    for i in inp:
        yield i ** 2

def gen_input(num_points:int=100)->Generator[int]:
    '''
        Generates a range of numbers uptil but not including num_points.

        Parameters:
            num_points : int
                The int representation of the amount of data points  we wish to use.

        Returns:
             Generator object yielding the int 's in linearly increasing fashion.

        Raises:
            AssertionException - In case where num_points isn't of type int.
    '''
    assert(isinstance(num_points, int))

    for i in range(num_points):
        yield i

def plot_graphs(data:tuple(Any,Any)):
    # plt.plot(data)
    # plt.ylabel('Time')
    # plt.xlabel('Input Size')
    # plt.title('Big O Notation')
    # plt.show()
    plot_fn(data=data,labels=('Input Size','Time'),title='Big O Notation')
    return

def data_dict(data)->Dict[str, Generator[int]]:

    di={}
    di['Time'] = data[0]
    di['Constant'] = data[1]
    di['Linear'] = data[2]
    di['Quadratic'] = data[3]
    di['Exponential'] =  data[4]
    return di

def main():
    num_points = 10,000,000
    in_data = gen_input(num_points)

    #keep the data as generators
    data = in_data, constant(gen_input(num_points)), linear(gen_input(num_points)), quadratic(gen_input(num_points)),exponential(gen_input(num_points))
    dic = data_dict(data)

    #write the csv file we want
    write_dic_to_csv(filename='sample.csv',dic=dic)

if __name__ == "__main__":
    main()