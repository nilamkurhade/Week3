import json


class StockReport:
    def __init__(self):
        total_shares = total_Price = amount = 0
        with open("/home/user/PycharmProjects/Python/OOPs/StockInformation.json") as file:
            data = json.load(file)
            for i in data:
                print("********", i, "************")
                for j in data[i]:
                    total_shares = total_shares + int(j["No_of_Share"])
                    total_Price = int(j["price"]) * int(j["No_of_Share"])
                    amount = amount + total_Price
                print("Total Shares", total_shares)
                print("Total Price", amount)


if __name__ == "__main__":
    obj = StockReport()




































