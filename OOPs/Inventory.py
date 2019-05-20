import json


class InventoryData:

    def __init__(self):
        price1 = weight1 = 0
        # JSON file path
        with open("/home/user/PycharmProjects/Python/OOPs/InventoryDataMgmt.json") as file:
            data = json.load(file)
        for i in data:
            print("***********", i, "*************")
            for j in data[i]:
                price1 = price1 + int(j["price"])
                weight1 = weight1 + int(j["weight"])
            print("Price : ", price1)
            print("Weight : ", weight1)


if __name__ == "__main__":
    obj = InventoryData()
