#Each shopping cart has a collection of products. It should also have the following functionality:

#add an product to the cart
#remove an product from the cart
#add up the total cost of all products in the cart before tax
#add up the total cost of all products in the cart after tax


from Products import Product


class shoppingcart:
	"""docstring for shopping_cart"""
	def __init__(self):
		self.products = []
			

	def put_in_cart(self,product):
		self.products.append(product)



	def remove_from_cart(self, product):
		self.Products.pop(product)
	
	

	def subtotal(self):
		result = 0
		for product in self.products:
			result += product.base_price
		return result	
		


	def Total(self):
		result = 0
		for product in self.products:
			result += product.base_price + product.base_price * product.tax_rate
		return result	



shopping_cart = shoppingcart()

shopping_cart.put_in_cart(Product('Bananas', 0.25))
shopping_cart.put_in_cart(Product('hot sauce', 4.99, 0.13))
shopping_cart.put_in_cart(Product('whiskey', 25.00, 0.25))


print(shopping_cart.subtotal())
print(shopping_cart.Total())