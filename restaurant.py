class Dish():
    def __init__(self, name, price, category, description):
        self._name = name
        self._price = price
        self._category = category
        self._description = description
        
    def get_name(self):
        return self._name
    
    def get_category(self):
        return self._category
    
    def get_description(self):
        return self._description
    
    def get_price(self):
        return self._price
    
    def set_name(self, new_name):
        self._name = new_name
    
    def set_price(self, new_price):
        previous_price = self._price
        self._price = new_price
        print(f"{self.get_name()} price updated from ${previous_price} to ${new_price}")
        
    def set_category(self, new_category):
        previous_category = self._category
        self._category = new_category
        print(f"{self.get_name()} category updated from \"{previous_category}\" to \"{new_category}\"!")
    
    def set_description(self, new_description):
        previous_description = self._description
        self._description = new_description
        print(f"{self.get_name()} description updated from \"{previous_description}\" to \"{new_description}\"!")
    
    def __repr__(self):
        dish_repr = f"\t{self.get_name()} \n\t- {self.get_description()} \n\t- ${self.get_price()}"
        return dish_repr


class Restaurant():
    restaurant_new_id = 1
    menu_item_new_id = 1
    
    def __init__(self, name, owner, address, phone):
        self._id = self.restaurant_new_id
        self._name = name
        self._owner = owner
        self._address = address
        self._phone = phone
        self._menu = {}
        self._categories = []
        self._sales = {}
        self._sales_by_day = {}
        self._total_sales = 0
        Restaurant.restaurant_new_id += 1
        
    # Getters
        
    def get_id(self):
        return self._id
    
    def get_name(self):
        return self._name
    
    def get_owner(self):
        return self._owner
    
    def get_address(self):
        return self._address
    
    def get_phone(self):
        return self._phone

    def get_menu(self):
        if self._menu == {}:
            print("Menu has no items!")
        else:
            return self._menu
        
    def get_categories(self):
        if self._categories == []:
            print("No categories yet!")
        else:
            return self._categories
    
    def get_all_sales(self):
        if self._sales == {}:
            print("No recorded sales!")
        else:
            return self._sales
           
    def get_sales_by_day(self):
        if self._sales == {}:
            print("No recorded sales!")
        else:
            self.calculate_sales_by_day()
            return self._sales_by_day
    
    def get_total_sales(self):
        if self._sales == {}:
            print("No recorded sales!")
        else:
            self.calculate_total_sales()
            return self._total_sales
    
    # Methods for Operation
    
    # This method adds dishes to the menu dictionary. 
    # It takes an object of Dish class and verifies if the name is not already in the menu.
    # Then, it takes the current menu_item_id and assigns it to the new dish for identification.
    # The menu dictionary has dishes id's as keys and the dish object as value.
    def add_to_menu(self, dish):
        dish_name = dish.get_name()
        dish_names = [self._menu[dish_id].get_name() for dish_id in self._menu.keys()]
        if dish_name not in dish_names:
            self._menu[self.menu_item_new_id] = dish
            print(f"Dish \"{dish_name}\" with id {self.menu_item_new_id} added to menu!")
        else:
            print(f"Dish \"{dish_name}\" with id {self.menu_item_new_id} already in the menu!")
        self.menu_item_new_id += 1
        self.define_categories()
    
    # This method adds sales to a dictionary that uses dates as keys 
    # and has a list of the dishes id's as values. 
    # It verifies if the dish id already exists before adding it to the dictionary.
    def add_to_sales(self, date, dish_id):
        if dish_id not in self._menu.keys():
            print(f"Dish with id {dish_id} is not in the menu!")
        else:
            if date not in self._sales.keys():
                self._sales[date] = [dish_id]
            else:
                self._sales[date].append(dish_id)
                
                
    # This is an auxiliary method for showing the meny using categories.
    def define_categories(self):
        for dish in self.get_menu().keys():
            category = self._menu[dish].get_category()
            if category not in self._categories:
                self._categories.append(category)

    def show_menu(self):
        self.define_categories()
        print(f"\n{'-'*30} \n{self._name} Menú: ")
        for category in self._categories:
            print(f"> {category}")
            for dish in self._menu.keys():
                if self._menu[dish].get_category() == category:
                    print(f"Item No. {dish}: \n{self._menu[dish]}")            
        print('-'*30)
    
    def show_all_sales(self):
        print(f"Sales of Restaruant: {self._name}")
        for date in self._sales.keys():
            sales_date = 0
            print(f"{'-'*30} \nDate: {date}")
            for dish_id in self._sales[date]:
                print(f"- {self._menu[dish_id].get_name()}... ${self._menu[dish_id].get_price()}")
                sales_date += self._menu[dish_id].get_price()
            print(f"Total day: ${sales_date}")
    
    def calculate_sales_by_day(self):
        for date in self._sales.keys():
            self._sales_by_day[date] = 0
            for dish_id in self._sales[date]:
                self._sales_by_day[date] += self._menu[dish_id].get_price()
    
    def calculate_total_sales(self):
        self._total_sales = 0
        self.calculate_sales_by_day()
        for date in self._sales_by_day.keys():
            self._total_sales += self._sales_by_day[date]
    
    def show_total_sales(self):
        self.calculate_total_sales()
        print(f"{'-'*30} \nTotal sales: \n${self.get_total_sales()} \n{'-'*30}")
    
    def __repr__(self):
        restaurant_info = f"""        
{self._name}
{self._address}
{self._phone}
{self._owner}
        """
        return restaurant_info