In the previous steps, you learned about tuples and `NamedTuples`. Now we're
going to tie those two concepts together, making a complex data structure that
uses both.

For this example, pretend we're writing software for an electronic register in
a coffee shop. We'll have to record the full list of someone's purchases, and
support the ability to add coupons.

First, let's create a class to represent one purchase. For that, you need the
name, ID, and price of the purchased item:

```
class Item(NamedTuple):
    id: int
    name: str
    price: int  # price in cents
```{{execute windows}}

While we're at it, let's make some examples for later:

```
coffee = Item(1, "Coffee", 400)
latte = Item(2, "Latte", 550)
biscotti = Item(3, "Biscotti", 275)
```{{execute windows}}

Now that we can represent items, we'll need to represent a series of them:

```
from typing import Tuple

class Order(NamedTuple):
    order_id: int
    items: Tuple[Item]
```{{execute windows}}

And again, an example:

```
order = Order(1, (coffee, biscotti))
```{{execute windows}}

Now we have built a complex, immutable data structure. We can add some methods
to it, like `total_price`:

```
class Order(NamedTuple):
    order_id: int
    items: Tuple[Item]
    def total_price(self):
        return sum(item.price for item in self.items)

assert Order(2, (coffee, biscotti)).total_price() == 675
```{{execute windows}}

There you have it. A fully functional data structure representing orders, and
completely immutable.
