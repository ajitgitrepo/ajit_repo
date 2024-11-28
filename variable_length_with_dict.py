def person(name,*data):
    print(name)
    print(data)

person('ajit',33,'kuligan',9841149863,'balasore')

def person_with_dict(name, **data):
    print(name)
    for i,j in data.items():
        print(i,j)

        
person_with_dict('ajit',age=33, city='kuligan', mob=9841149863,Dist='Balasore')
