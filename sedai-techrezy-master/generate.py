import yaml
from yaml.loader import SafeLoader


def generatefn(url_list, to_list, newfun):
    f=open('app.py', 'a')
    f.write('\n\ndef ' + newfun + '(data, **kwargs):\n')
    for i in range(len(url_list)):
        f.write('   if \'' + url_list[i] + '\' in data: \n')
        f.write('       ' + to_list[i] + '(**kwargs)\n')
        #f.write('       return redirect(url_for("home"))\n')

y='.'
url_list=[]
to_list=[]
li1=[]
li2=[]
with open('output.txt') as f:
    for i in range(2):
        next(f)
       

    for line in f:

        
        aux=''.join(c for c in line if c not in y)
        aux=aux.split()
    
        url_list.append(aux[2])
        li1.append(aux[2])
        li2.append(aux[0])
        to_list.append(aux[0])
        
    
    
    #loading yaml file
    with open("file.yaml", "r") as f:
        yaml_dict = yaml.load(f,Loader=SafeLoader)
    print(yaml_dict)

    print(yaml_dict['task'])
   
    #print(li1)
    #print(li2)
c=0
for i in url_list:
    s=i.split('/<',1)
    a=s[0]
    url_list[c]=a
    c=c+1
#print(url_list)
c=0
for i in to_list:
    s=i.split('/<',1)
    a=s[0]
    to_list[c]=a
    c=c+1

#converting to dictionary
url_dict = dict(zip(url_list, to_list))
print(url_dict)


for i in yaml_dict:
    #yaml_list=[]
    yaml_list=yaml_dict[i]
    print('\n\n\n')
    print(yaml_list)
    print('\n\n\n')
    do_list=[]
    for j in yaml_list:

        do_list.append(url_dict[j])
    print(do_list)
    generatefn(yaml_list, do_list, i)
    
    
    #print(do_list)
#print(to_list)
#url_list = ['/add', '/update', '/delete']
#to_list = ['addpage', 'updatepage', 'deletepage']

