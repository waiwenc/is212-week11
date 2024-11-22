class OrderProcessor:
    def process_order(self, order):
        self.validate_details(order)
        total_price = self.calculate_price(order)
        total_price = total_price * self.get_discount_rate(order)
        self.update_inventory(order)
        receipt = self.generate_receipt(order, total_price)
        self.send_email(order, receipt)
        return receipt


    # Step 1: Validate order details
    def validate_details(self, order):
        if not order.get("customer_id"):
            raise ValueError("Customer ID is required.")
        if not order.get("items"):
            raise ValueError("Order must contain items.")

    # Step 2: Calculate total price
    def calculate_price(self, order):
        total_price = 0
        for item in order["items"]:
            total_price += item["price"] * item["quantity"]
        return total_price

    # Step 3: Apply discounts if applicable
    def get_discount_rate(self, order):
        rate = 1
        if order.get("discount_code") == "SUMMER20":
            rate = 0.8  # 20% discount
        elif order.get("discount_code") == "WELCOME10":
            rate = 0.9  # 10% discount
        return rate
        
    # Step 4: Update inventory
    def update_inventory(self, order):
        for item in order["items"]:
            item_id = item["id"]
            quantity = item["quantity"]
            # Code to update inventory for each item
            # (for simplicity, let's assume a simple print statement here)
            print(f"Updating inventory for item {item_id}, reducing stock by {quantity}.")

    # Step 5: Generate receipt
    def generate_receipt(self, order, total_price):
        receipt = f"Customer ID: {order['customer_id']}\n"
        receipt += "Items:\n"
        for item in order["items"]:
            receipt += f"- {item['name']}: {item['quantity']} x ${item['price']}\n"
        receipt += f"Total: ${total_price:.2f}\n"
        return receipt

    # Step 6: Send confirmation email
    def send_email(self, order, receipt):
        print(f"Sending email to customer {order['customer_id']} with receipt:\n{receipt}")

