import re


class RegularExpression:
    def __init__(self, string):
        self.string = string

    def regular_expression(self):

        pattName = re.search("<+.{4}>+", self.string)
        pattFullName = re.search("<+.{9}>+", self.string)
        pattMobNo = re.search("x{10}", self.string)
        pattDate = re.search("xx\Wxx\Wx{4}", self.string)

        try:
            name = input("Enter name : ").strip()
            full_name = input("Enter full name : ").strip()
            mobile_number = input("Enter mobile number : ").strip()
            date = input("Enter date : ").strip()

            if not name.isalpha() or not mobile_number.isnumeric():  # validation for Mobile No and name
                raise ValueError
        except ValueError:
            print("You have enter wrong data.")
            self.regular_expression()
        else:
            self.replace_string(pattName .group(), name)
            self.replace_string(pattFullName.group(), full_name)
            self.replace_string(pattMobNo.group(), mobile_number)
            self.replace_string(pattDate.group(), date)
            print(self.string)
        return

    def replace_string(self, patt, word):

        self.string = self.string.replace(patt, word)


    # Main method
if __name__ == '__main__':
    string = "Hello <<name>>, We have your full" \
    + " name as <<full name>> in our system. your contact number is 91­xxxxxxxxxx." \
    + " Please,let us know in case of any clarification Thank you BridgeLabz xx/xx/xxxx."
    regular_exp = RegularExpression(string)
    regular_exp.regular_expression()


