from Base.read_data import Op_Data



data = Op_Data("data.yml").read_yaml().get('Login_data')
data_list = []
print(data)
for i in data:
    print(i)
        # for o in i.keys():
        #     data_list.append((o,))