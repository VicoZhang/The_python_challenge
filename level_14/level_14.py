import xmlrpc.client
with xmlrpc.client.ServerProxy("http://www.pythonchallenge.com/pc/phonebook.php") as pb:
    print(pb.system.listMethods())
    print(pb.system.methodHelp('phone'))
    print(pb.phone('evil'))

with open('evil4.jpg') as f:
    de = f.read()
    print(de)

print(pb.phone('Bert'))
