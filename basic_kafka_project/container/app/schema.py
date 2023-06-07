from typing import List, Dict
from decimal import Decimal
from datetime import datetime


class Ride:
    def __init__(self, arr: List[str]):
        self.arr = arr
        self.date = arr[0],
        self.customer_id = str(arr[1])
        self.payment_method = str(arr[2])
        self.delivery_status = str(arr[3])
        self.duration = str(arr[4])
        self.no_of_orders = str(arr[5])
        self.amount = str(arr[6])

        
    @classmethod
    def from_dict(cls, d: Dict):
        return [
            d['date'][0],
            d['customer_id'],
            d['payment_method'],
            d['delivery_status'],
            d['duration'],
            d['no_of_orders'],
            d['amount'],
        ]
        

    def __repr__(self):
        #return f'{self.__class__.__name__}: {self.__dict__}'
        return f'{self.arr}'
