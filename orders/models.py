from django.db import models


class Order(models.Model):
    user = models.ForeignKey(
        'users.User',
        on_delete=models.CASCADE,
        related_name='orders',
    )
    offer = models.ForeignKey(
        'offers.Offer',
        on_delete=models.CASCADE,
        related_name='orders'
    )
    order_date = models.DateTimeField(
        auto_now_add=True,
    )

    @property
    def total(self) -> int:
        return sum([
            product.product.price * product.qty for product in self.products.all()
        ])
