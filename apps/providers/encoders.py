import decimal
import json


class DecimalEncoder(json.JSONEncoder):

    def default(self, obj):
        if isinstance(obj, decimal.Decimal):
            return '%.2f' % obj
        return json.JSONEncoder.default(self, obj)
