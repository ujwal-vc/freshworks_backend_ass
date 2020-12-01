
import os
import json

class sad:
    #class for the crd operations

    def __init__(self):
        #1.path constraint
        try:
            path=input('Please enter the path you want to store the data : \n')
            os.mkdir(os.path.join(path,'data_store'))
            path=path+'\data_store'
            os.chdir(path)
            print(path)
        except:
            os.mkdir('data_store')
            
    def create(self):
        dic={}

        key=input('Enter the key : ')
        #2.constraint
        if len(key)>32:
            raise Exception('!!!key should contain only 32 characters')
        #3.constraint
        if (os.path.isfile('key_list')):
            raise Exception('!!!The key is already used try different one')

        value=input('Enter the value : ')
        y=json.dumps(value)
        if y.__sizeof__()>(16000):
            raise Exception("!!!The size of the value is more")
        with open(key,'w') as f:
            dic[key]=value
            f.write(json.dumps(dic))
    
    
    def read(self):
        key=input('Enter the key to search : ')
        if not(os.path.isfile(key)):
            raise Exception("!!!File not found")
        else:
            with open(key,'r') as f:
                print(json.loads(f.readline()))


    def delete(self):
        key=input('Enter the key to delete : ')
        if not(os.path.isfile(key)):
            raise Exception("!!!File not found")    
        else:
            os.remove(key)
        
