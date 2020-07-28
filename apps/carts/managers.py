from django.db.models import Manager,F



class CartProductsManager(Manager):
    def create_or_update(self,cart,product,quantity=1):
        obj,created = self.get_or_create(cart=cart,product=product)

        if not created:
            obj.quantity = F('quantity') + quantity
            obj.save()

        return obj