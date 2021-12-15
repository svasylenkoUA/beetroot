class Product:
    def __init__(self, ptype, pname, or_price):
        self.ptype = ptype
        self.pname = pname
        self.price = or_price
        self.full_price = 0

class Margin:
    def __init__(self):
        self.rules = {
            "Sport": 20,
            "Food": 10
        }

    def calc_full_price(self, prod: Product):
        return prod.price*(1 + self.rules[prod.ptype]/100)



class ProductsInShop(Product):
    def __init__(self, prod: Product):
        self.product = prod
        m = Margin()
        prod.full_price = m.calc_full_price(prod)
        self.quantity = 0


class ProductStore:
    MARGIN = 10

    def __init__(self):
        self.items_in_store = []

    def add(self, product, quantity):
        p = ProductsInShop(product)
        p.quantity = quantity
        self.items_in_store.append(p)

    def sell(self, product, quantity):
        for i in self.items_in_store:
            if i.product.pname == product:
                i.quantity -= quantity
            else:
                continue


    def get_income(self):
        income = 0
        for p in self.items_in_store:
            income += (p.product.full_price - p.product.price)*p.quantity
        return income

    def get_all_items(self):
        return [p.product.pname+str(p.quantity) for p in self.items_in_store]


p1 = Product('Sport', 'Football T-Shirt', 100)
p2 = Product('Food', 'Chicken', 80)

ps1 = ProductStore()

ps1.add(p1, 20)
ps1.add(p2, 10)
print(ps1.get_all_items())
print(ps1.get_income())
ps1.sell("Chicken", 5)
print(ps1.get_all_items())
print(ps1.get_income())
