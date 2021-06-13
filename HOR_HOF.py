from functools import reduce

def run():
    #filter
    my_list = [1,4,5,6,9,14,19,21]
    dd = list(filter(lambda x: x%2 !=0, my_list))
    print(dd)
    #map
    my_s_list = [1,2,3,4,5]
    dd2 = list(map(lambda x: x**2, my_s_list))
    print(dd2)
    #reduce
    #import reduce
    my_3_list = [2,2,2,2,2]
    multi = reduce(lambda a,b: a * b, my_3_list)
    print(multi)

if __name__ =='__main__':
    run()