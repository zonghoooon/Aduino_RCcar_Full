import pickle

a = [10,[1,2,3],'abc']
sample = []

with open("testp.p",'rb' )  as f:
    data = pickle.load(f)
sample.append(a)
with open("testp.p",'wb') as f:
    pickle.dump(data + sample,f)

result = pickle.load( open( "testp.p", "rb" ), encoding="latin" )
# with open("testp.p",'rb' )  as f:
#   result = pickle.load(f)
print(result)
print(1)