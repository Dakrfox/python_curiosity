#make a dictionary where the first 100 keys are 1-100 and their respective values (1-100)^2 and i%3
def run():
    my_dicts ={}

    for i in range(1,101):
        if i %3==0:
            my_dicts[i] = i**3

    print(my_dicts)

#now a with DICTIONARY COMPREHENION 
    my_dicts2 = {i: i**3 for i in range(1,101) if i%3!=0} 



if __name__ == '__main__':
    run()