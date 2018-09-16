from jsonpickle import encode


class Sum:

    def __init__(self, value_and_currency : str):
        self._value_and_currency = value_and_currency
        self._value = self._parse_value()
        self._currency = self._parse_currency()

    def _parse_value(self):
        return float(self._value_and_currency[:-1].replace(",", "."))

    def _parse_currency(self):
        return self._value_and_currency[-1]

    def __str__(self):
        return encode(self)