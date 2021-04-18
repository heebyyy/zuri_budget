class Budget:

    balance = 0
    expense = 0

    

    def __init__(self):
        self.category = []
        self.category_balance = {}



    def start_budget(self):
        print('WELCOME TOBUDGET APP')
        if not self.category and self.category_balance:
            print('You currently do not have a budget\nAdd a new category?')
            self.create_categories()
        else:
            self.operation()

    
    def create_categories(self):
        number_of_categories = int(input('How mny categories will you like to add?\n'))
        for num in range(1, number_of_categories+1):
            category_created = input(f'What is the category name?\n')
            self.category.append(category_created)

        for category in self.category:
            self.category_balance[category] = 0
        print(f'categories have been created successfully')
        print(f'The balance for the category is: {self.category_balance}\n')
        self.operation()
        
    
    def operation(self):
        print('''These are the opeartions that canbe performed
            1. DEPOSIT TO CATEGORY.
            2. WITHDRAWAL FROM CATEGORY.
            3. GET CATEGORY BALANCE.
            4. TRANSFER BETWEEN CATEGORIES.
            5. CREATE NEW CATEGORY.
            6. TOTAL BALANCE.
            0. EXIT
        ''')
        try:
            action = int(input('Which will you like to do?\n'))
            if action == 1:
                self.deposit()

            elif action == 2:
                self.withdraw()

            elif action == 3:
                self.category_balance()

            elif action == 4:
                self.transfer()

            elif action == 5:
                self.add_new_category()

            elif action == 6:
                self.total_balance()

            elif action == 0:
                self.exit()

            else:
                print('You have input aninvalid number')

            









    def deposit(self):
        pass

    def withdraw(self):
        pass

    def category_balance():
        pass

    def transfer():
        pass

    def add_new_category():
        pass

    def total_balance():
        pass

    def exit():
        pass




