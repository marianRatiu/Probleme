from abc import ABC, abstractmethod


class AbstractPayment(ABC):
    @abstractmethod
    def authorize_payment(self, user_id, amount, currency):
        pass

    @abstractmethod
    def charge_payment(self, user_id, amount, currency, merchant_id):
        pass

    @abstractmethod
    def reverse_payment(self, user_id, amount, currency, merchant_id):
        pass


try:
    ap = AbstractPayment()
except TypeError as e:
    print(e)


class CreditCardPayment(AbstractPayment):
    def authorize_payment(self, user_id, amount, currency):
        print(f"Authorizing credit card payment for user {user_id}: {amount} {currency}")
        return True

    def charge_payment(self, user_id, amount, currency, merchant_id):
        print(f"Charging credit card payment for user {user_id}: {amount} {currency} to merchant {merchant_id}")
        return "transaction_id_12345"

    def reverse_payment(self, user_id, amount, currency, merchant_id):
        print(f"Reversing credit card payment for user {user_id}: {amount} {currency} from merchant {merchant_id}")
        return "transaction_id_54321"


cc_payment = CreditCardPayment()
print(cc_payment.authorize_payment(1, 100.0, 'USD'))
print(cc_payment.charge_payment(1, 100.0, 'USD', 'merchant_001'))
print(cc_payment.reverse_payment(1, 100.0, 'USD', 'merchant_001'))
