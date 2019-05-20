import json
"""===============Inventory_Management======================"""


class Inventory_Stock_Management:

    def __init__(self, data):
        self.data = data

    def inventory_Stock_Data(self):

        while True:
            try:
                count = 1
                while count > 0:
                    print()
                    print("Enter 1.Display 2.Add_item 3.exit..\n")
                    choice = int(input())
                    if choice == 1:
                        print("displaying inventory information...\n")
                        # t1.inventory_information(self.data)
                        print("***************Rice Details***************\n")
                        print("Name            weight       price")
                        print("=====================================")
                        for i in self.data['Rice']:
                            print(i['name'], end="          ")
                            print(i['weight'], end="          ")
                            print(i['price'], )
                        print()
                        print("***************Wheat Details***************\n")
                        print("Name           weight         price")
                        print("=====================================")
                        for j in self.data['Wheat']:
                            print(j['name'], end="          ")
                            print(j['weight'], end="          ")
                            print(j['price'], )
                        print()
                        print("***************Pulses Details***************\n")
                        print("Name           weight        price")
                        print("=====================================")
                        for k in self.data['Pulses']:
                            print(k['name'], end="          ")
                            print(k['weight'], end="          ")
                            print(k['price'], )
                        print()
                    elif choice == 2:
                        print("Enter Item Name(Rice,Wheat,Pulses)..\n")
                        item = input()
                        i = 0
                        """while i < len(self.data)
                            if self.data[i]["Rice"] == item.title():"""
                        while not item.isalpha():
                            print("enter valid item name(Characters Only)...\n")
                            print("Enter Item Name(Rice,Wheat,Pulses)..\n")
                            item = input()
                        print()

                        print("enter a name of given item:=> ", item)
                        name = input()
                        while not name.isalpha():  # name of a item
                            print("enter valid name for a item(Characters Only)...\n")
                            print("enter a name of given item:=> ", item)
                            name = input()
                        print()

                        print("enter a weight of given item:=> ", item, " item_name ", name)
                        weight = input()
                        while not weight.isdigit():  # weight of a item
                            print("enter weight for a item(Integer Only)...\n")
                            print("enter weight of given item:=> ", item, "item_name ", name)
                            weight = input()
                        print()

                        print("enter a price of a given item:=> ", item)
                        price = input()
                        while not price.isdigit():  # price of a item
                            print("enter price for a item(Integer Only)...\n")
                            print("enter a price of given item:=> ", item, " item_name ", name)
                            price = input()
                        print()

                        with open("InvData.json", "w") as file:
                            self.data[item].append({
                                "name": name,
                                "weight": weight,
                                "price": price
                            })
                            file.write(json.dumps(self.data, indent=2))
                            file.close()

                    elif choice == 3:
                        exit()
                    else:
                        print(" sorry,invalid entry...\n")
            except Exception as e:
                print(e)
