import uuid


class Utils:
    @staticmethod
    def generate_order_id():
        return uuid.uuid1()
