'''
Welcome to Secure Code Game Season-1/Level-1!

Follow the instructions below to get started:

1. tests.py is passing but code.py is vulnerable
2. Review the code. Can you spot the bug?
3. Fix the code but ensure that tests.py passes
4. Run hack.py and if passing then CONGRATS!
5. If stuck then read the hint
6. Compare your solution with solution.py
'''

from collections import namedtuple

MAX_ITEM_QUANTITY = 1000
MAX_ITEM_AMOUNT = 1_000_000
MAX_ALL_ITEMS_AMOUNT = 1_000_000


Order = namedtuple('Order', 'id, items')
Item = namedtuple('Item', 'type, description, amount, quantity')

def validorder(order: Order):
    all_items_amount = 0
    net = 0

    for item in order.items:
        if item.type == 'payment':
            if abs(item.amount) < MAX_ITEM_AMOUNT:
                all_items_amount = round(all_items_amount, 2) + round(item.amount, 2)
        elif item.type == 'product':
            if item.amount < MAX_ITEM_AMOUNT and item.quantity < MAX_ITEM_QUANTITY:
                net = round(net, 2) - round(item.amount, 2) * item.quantity
        else:
            return "Invalid item type: %s" % item.type
        
        if all_items_amount > MAX_ALL_ITEMS_AMOUNT:
            return 'Total amount payable for an order exceeded'

    net += round(all_items_amount, 2)

    if net != 0:
        return "Order ID: %s - Payment imbalance: $%0.2f" % (order.id, net)
    else:
        return "Order ID: %s - Full payment received!" % order.id