class DeliveryPartner:
    def __init__(self, name, partner_id, deliveries):
        self.name = name
        self.partner_id = partner_id
        self.deliveries = deliveries

    def total_earning(self):
        pass

    def display(self):
        print(f"Name: {self.name}")
        print(f"Partner ID: {self.partner_id}")
        print(f"Deliveries: {self.deliveries}")
        print(f"Total Earning: NPR {self.total_earning()}")
        print("-" * 30)


class BikeRider(DeliveryPartner):
    def __init__(self, name, partner_id, deliveries, km_travelled):
        super().__init__(name, partner_id, deliveries)
        self.km_travelled = km_travelled

    def total_earning(self):
        return (80 * self.deliveries) + (5 * self.km_travelled)


class Walker(DeliveryPartner):
    def __init__(self, name, partner_id, deliveries, rainy_deliveries):
        super().__init__(name, partner_id, deliveries)
        self.rainy_deliveries = rainy_deliveries

    def total_earning(self):
        return (60 * self.deliveries) + (50 * self.rainy_deliveries)


class CarDriver(DeliveryPartner):
    def __init__(self, name, partner_id, deliveries, fuel_cost):
        super().__init__(name, partner_id, deliveries)
        self.fuel_cost = fuel_cost

    def total_earning(self):
        return (120 * self.deliveries) - self.fuel_cost


partners = [
    BikeRider("Santosh Rai", "B-01", 15, 42),
    Walker("Kabita Maharjan", "W-01", 18, 5),
    CarDriver("Roshan KC", "C-01", 20, 850)
]

print("Delivery Partner Details:")
for partner in partners:
    partner.display()

highest_earner = partners[0]

for partner in partners:
    if partner.total_earning() > highest_earner.total_earning():
        highest_earner = partner

print(f"Highest Earning Partner: {highest_earner.name}")
print(f"Total Earning: NPR {highest_earner.total_earning()}")