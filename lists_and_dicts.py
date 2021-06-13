def run():
    my_list = [1, 'hello', True, 4.5]
    my_dict = {'first_name': 'nicolas',
                'last_name': 'martinez'}
    #una lista diccionario
    super_list ={
        'first_name': 'nico',
        'last_name': 'martin',
        'first_name1': 'ivan',
        'last_name1': 'herrera',
        'first_name2': 'ivam',
        'last_name2': 'martinez',
        'first_name3': 'nicolas',
        'last_name3': 'sejuani'
    }
    #un diccionario de lista
    super_dicts = {
        'natural_num': [1,2,3,4,5,6,7,8,9],
        'integer_nums': [-2,-1,0,1,2],
        'floating_nums': [1.1,2.2,3.3,4.4]
    }
    #recorriendo un diccionario
    for key, value in super_dicts.items():
        print(key , " : " , value)

    for key, value in super_list.items():
        print(key, " : ",value)

if __name__ == '__main__':
    run()