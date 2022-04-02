class Bank:

    def __init__(self, balance: List[int]):

        self.arr=balance

    def transfer(self, account1: int, account2: int, money: int) -> bool:

        if account1 <= len(self.arr) and account2 <= len(self.arr):
            if self.arr[account1-1]>=money:
                self.arr[account1-1]=self.arr[account1-1]-money
                self.arr[account2-1]=self.arr[account2-1]+money

                return True
            else:
                return False
        else:
            return False


    def deposit(self, account: int, money: int) -> bool:
        if account <= len(self.arr):
            self.arr[account-1]=self.arr[account-1]+money
            return True
        else:
            return False

    def withdraw(self, account: int, money: int) -> bool:
        if account <= len(self.arr):
            if self.arr[account-1]>=money:
                self.arr[account-1]=self.arr[account-1]-money
                return True
            else:
                return False
        else:
            return False