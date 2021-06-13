
DATA = [
    {
        'name': 'Nicolas',
        'age': 21,
        'organization': 'Platzi',
        'position':'Freelancer',
        'language': 'python',
    },
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'platzi',
        'position': 'Technical Coach',
        'language': 'pyton'
    },
    {
        'name': 'alejandro',
        'age': 21,
        'organization': 'universidad de la costa',
        'position':'flojo',
        'language': 'c#',
    },
    {
        'name': 'victor',
        'age': 21,
        'organization': 'universidad de la costa',
        'position':'veteriario',
        'language': 'java',
    },
    {
        'name': 'reginaldo',
        'age': 21,
        'organization': 'universidad de la costa',
        'position':'junior',
        'language': 'javascript',
    },
    {
        'name': 'Nicolas',
        'age': 21,
        'organization': 'universidad de la costa',
        'position':'Freelancer',
        'language': 'python',
    },
    {
        'name': 'sejuani',
        'age': 21,
        'organization': 'league of legends',
        'position':'jungla',
        'language': 'python',
    },

]

def run():
    # all_python_dev = [worker['name'] for worker in DATA if worker['language'] == 'python']
    # all_universidad = [worker['name'] for worker in DATA if worker['organization']== 'universidad de la costa']
    # for worker in all_universidad:
    #     print(worker)

    #challenge 

    all_python_dev = list(filter(lambda worker: worker['language'] =='python', DATA))
    just_name = list(map(lambda worker: worker['name'], all_python_dev))
    for worker in just_name:
        print(worker)

    all_u_dev = list(filter(lambda worker: worker['organization'] =='universidad de la costa', DATA))
    just_name = list(map(lambda worker: worker['name'], all_u_dev))
    print("////////////////////////////////////////")
    for worker in just_name:
        print(worker)


    #filter + lambda

    # adults= list(filter(lambda worker: worker['age']>18, DATA))
    # for aux in adults:
    #     print(aux)
    # #map + lambda

    # adults = list(map(lambda worker: worker['name'], adults))
    # for aux in adults:
    #     print(aux)

    # # "|" this simbols is used since 3.9v and the function is join multiple dictionary in one 
    # old_people =  list(map(lambda worker: worker | {'old': worker['age'] >70}, DATA))

    #challenge
    adults = [worker['name'] for worker in DATA if worker['age']>18  ]
    print("///////////////////////////////////////")
    for worker in adults:
        print(worker)

    old_people = [worker['name'] for worker in DATA if worker['age']>70]
    print("///////////////////////////////////////")
    for worker in old_people:
        print(old_people)


if __name__ == '__main__':
    run()