import json

from OOPs.InventoryData4 import Inventory_Stock_Management

# t1 = Inventory_Stock_Management()

"""if __name__ == "__main__":
    t1.inventory_Stock()"""


class Inventory_Prog_4:
    try:
        with open("InvData.json", "r") as file:
            new_file = file.read()
            file.close()

            item = json.loads(new_file)
            t1 = Inventory_Stock_Management(item)
            print()
            t1.inventory_Stock_Data()

    except RuntimeError:
        print("=========")
