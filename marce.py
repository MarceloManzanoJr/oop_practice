class Customer(Book):
    def __init__(self, customer_json,customer_id, customer_name, customer_address):
        super().__init__(self, customer_json,customer_id, customer_name, customer_address, cart)
        self.customer_id = customer_id
        self.customer_name = customer_name
        self.customer_address = customer_address
        self.customer_jason = customer_json
        self.cart = []

    def custommer_info(self):
        print(f"Your ID: {self.customer_id}")
        print("----------------------------")
        print(f"Welcome: {self.customer_name}")
        print("----------------------------")
        print(f"home Address: {self.customer_address}")
        print("----------------------------")

    def add_cart(book_title):
        self.cart.append(book_title)
        print(f"You add {book_title} in your cart")
        print("----------------------------")

    def sava_customer(self):
        customer_data ={
            "id": self.customer_id,
            "Nmae": self.customer_address,
            "Address": self.customer_address,
        }
        with open(self.customer_jason, 'w') as file:
            json.dump(customer_data,file, indent=4)

    def view_cart(self):
        print("Shopping List")
        for item in self.cart:
            print(item)
            print("----------------------------")
