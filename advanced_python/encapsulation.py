import type_safe


@type_safe
class Bill:
    cost = float
    card = bool
    name = str

    def __init__(self, cost, card):
        self.cost = cost
        self.card = card


class Account:

    def __init__(self, username: str, password: str, bio: str, pro: bool):

        # (check types of inputted values)
        self.bill = Bill(False, True)
        self.__username = username
        self.__password = password
        self.__bio = bio
        self.__pro = pro

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, new_username):
        if type(new_username) == str:
            self.__username = new_username
        else:
            print("Wrong type provided for field Username")


account = Account("user", "pass", "I'm me", False)
print(account.username)

account.username = "bob"

print(account.username)


print(f"Account bill state: {account.bill.cost}")

account.bill.cost = "Nope"

print(f"Account bill state: {account.bill.cost}")
