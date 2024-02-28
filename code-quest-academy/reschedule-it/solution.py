# Incomplete?
import datetime

cases = int(input())

for _ in range(cases):
    orders_count, shipments_count = map(
        int, input().split())

    orders = []
    for _ in range(orders_count):
        date, order_count = input().split()
        date = datetime.datetime.strptime(date, "%Y-%m-%d")
        order_count = int(order_count)

        for _ in range(order_count):
            orders.append(date)

    shipments = []
    for _ in range(shipments_count):
        date, shipment_count = input().split()
        date = datetime.datetime.strptime(date, "%Y-%m-%d")
        shipment_count = int(shipment_count)

        for _ in range(shipment_count):
            shipments.append(date)

    # Longer than 28 days
    flag = False
    for s in shipments:
        o = orders.pop(0)
        while (o - s).days == 0:
            a = o
            o = orders.pop(0)
            orders.insert(0, a)
        if (o - s).days > 28:
            flag = True

    # Extra orders
    if len(orders) > 0:
        flag = True

    if flag:
        print("NOT OK")
    else:
        print("OK")
