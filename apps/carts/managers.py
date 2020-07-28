from django.db.models import Manager,F



class CartProductsManager(Manager):
    def create_or_update(self,cart,product,quantity=1):
        try:
            obj = self.get(cart=cart,product=product)
            obj.quantity = F('quantity') + quantity 
            obj.save()
            return obj
        except:
            created = self.create(cart=cart,product=product,quantity=quantity)
            return created