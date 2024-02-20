import random
import uuid
from datetime import datetime
import pandas as pd
import numpy as np
import warnings

class Bills:
    def __init__(self):
        self.info_client: dict = {'fio': '', 'number': 0, 'cash': 0,
                                  'currency': 'RUR', 'date_open': None}  # информация по текущему состоянию счета
        self.history_operation: pd.DataFrame = pd.DataFrame(columns={'date', 'type', 'is_success', 'summ',
                                                                     'balance'})  # история операций,is_success - изменение баланса

    def check(self):  # проверка открытия счета
        if self.info_client['number'] == 0:
            raise ValueError('Не открыт счет')
        elif self.info_client['fio'] == '':
            raise ValueError('Не указан ФИО клиента')

    def check_sum(self, cash, balance):
        if balance + cash < 0:
            warn_str = f'Операция не выполнена, недостаточно средств для списания {cash} {self.info_client["currency"]}'
            warnings.warn(warn_str, DeprecationWarning, stacklevel=4)

    def decorator(arg1):  # декоратор для сохранения истории операций
        def save_history(func):
            def wrapper(self, *args, **kwargs):
                now = self.info_client['cash']
                ready_func = func(self, *args, **kwargs)
                self.check()
                after = self.info_client['cash']
                cash = 0 if arg1 not in ('зачисление средств', 'списание средств') else after - now
                is_success = False if now == after and arg1 in ('зачисление средств', 'списание средств') else True
                operation = SaveOperation(cash=cash, balance=now,
                                          types_operations=arg1, is_success=is_success).history()
                self.history_operation = pd.concat([self.history_operation, operation])
                return ready_func

            return wrapper

        return save_history

    def get_bill(self):  # уникальный номер счета
        return uuid.uuid4().int

    @decorator('открытие счета')
    def open_bill(self, name, cash=0, currency='RUR'):  # открыть счет
        self.name_client = name
        self.info_client = {'fio': name, 'number': self.get_bill(), 'currency': currency,
                            'date_open': datetime.today(), 'cash': 0}
        cash = cash if self.info_client['cash'] + cash >= 0 else self.info_client['cash']
        self.deposit_money(cash=cash)



    @decorator('зачисление средств')
    def deposit_money(self, cash=0):
        now = self.info_client['cash']
        self.check_sum(cash=cash, balance=now)
        self.info_client['cash'] = now + cash if now + cash >= 0 else self.info_client['cash']

    @decorator('списание средств')
    def withdraw_money(self, cash=0):
        now = self.info_client['cash']
        self.check_sum(cash=-abs(cash), balance=now)
        self.info_client['cash'] = now - abs(cash) if now - abs(cash) >= 0 else self.info_client['cash']

    @decorator('проверка баланса')
    def check_balance(self):
        fio = self.info_client['fio']
        now = self.info_client['cash']
        currency = self.info_client['currency']
        print(f'{datetime.today().strftime("%d-%m-%Y %H:%M")} - Баланс по счету {fio} -  {now} {currency}')

    @decorator('запрос детализации операций')
    def detail_operations(self, is_success=True):
        is_success = is_success if isinstance(is_success, list) else [is_success]
        results = self.history_operation.copy()
        results['change_sum'] = np.where(results['summ'] == 0, False, True)
        results = results[results['change_sum'].isin(is_success)]
        results['balance_after'] = results['summ'] + results['balance']
        results['is_success'] = np.where(results['is_success'], "Успешно", "Операция отменена")
        results['date'] = pd.to_datetime(results['date']).dt.strftime("%d-%m-%Y %H:%M:%S")
        results['sort'] = np.where(results['type'] == 'открытие счета', 1, 0)
        results = results.sort_values(by=['sort', 'date'], ascending=False).reset_index()
        results = results[['date', 'type', 'is_success', 'summ', 'balance',
                           'balance_after']].rename(
            dict(date='Дата операции', type='Тип операции', is_success='Успешность выполнения', summ='Сумма операции',
                 balance='Баланс до', balance_after='Баланс после'), axis=1)
        print(results.to_string())

    @decorator('запрос истории баланса')
    def history_balance(self):
        results = self.history_operation.copy()
        results['change_sum'] = np.where(results['summ'] == 0, False, True)
        results = results[results['change_sum'].isin([True])]
        results['balance_after'] = results['summ'] + results['balance']
        results['date'] = pd.to_datetime(results['date']).dt.strftime("%d-%m-%Y")
        results = results[['date', 'balance_after']].rename(
            dict(date='Дата', balance_after='Баланс на конец дня'), axis=1)
        print(results.groupby("Дата").last().reset_index().to_string())




class SaveOperation:  #
    def __init__(self, cash=0, balance=0, types_operations=None, is_success=None):
        self.cash = cash
        self.balance = balance
        self.types_operations = types_operations
        self.is_success = is_success
        if types_operations is None:
            if cash > 0:
                self.types_operations = 'Зачисление средств'
            elif cash < 0:
                self.types_operations = 'Списание средств'
            else:
                self.types_operations = 'Просмотр баланса'

    def history(self):
        balance = self.balance
        return pd.DataFrame(columns=['date', 'type', 'is_success', 'summ', 'balance'],
                            data=[[datetime.today(), self.types_operations, self.is_success, self.cash, balance]])


client2 = Bills()  # создание экземпляра
client2.open_bill(cash=1, name='Петров I.I.', currency='EUR') # открыть счет
client2.deposit_money(2)  # зачислить
client2.deposit_money(2)  # зачислить
client2.check_balance()  # проверка баланса
client2.withdraw_money(5)  # списать
client2.withdraw_money(10)  # списать сумму больше баланса
client2.deposit_money(2)  # зачислить
client2.detail_operations([True, False])  # детализация операций на экран [True, False] - показать все операции успешные и не успешные
client2.history_balance()  # история баланса по дням
print(client2.name_client)  # имя клиента
