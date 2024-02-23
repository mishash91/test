import random
import uuid
from datetime import datetime
import pandas as pd
import numpy as np
import warnings


class Func:
    def __init__(self):
        self._info_client: dict = {'fio': None, 'number': 0, 'cash': 0,
                                   'currency': 'RUR', 'date_open': None}  # информация по текущему состоянию счета
        self._history_operation: pd.DataFrame = pd.DataFrame(columns={'date', 'type', 'is_success', 'summ',
                                                                      'balance'})  # история операций,is_success - изменение баланса
        self._cash = 0
        self._currency = 'RUR'

    @staticmethod
    def get_bill():  # уникальный номер счета
        return uuid.uuid4().int

    def _check_num(self):  # проверка открытия счета
        if self._info_client['number'] == 0:
            raise ValueError('Не открыт счет')
        elif self._info_client['fio'] is None:
            raise ValueError('Не указан ФИО клиента')
        else:
            return True

    @staticmethod
    def check_sum(cash, balance, currency):  # проверка суммы
        if balance + cash < 0:
            warn_str = f'Операция не выполнена, недостаточно средств для списания {cash} {currency}'
            warnings.warn(warn_str, DeprecationWarning, stacklevel=5)
            return False
        else:
            return True

    def __decorator(arg1):  # декоратор для сохранения истории операций
        def save_history(func):
            def wrapper(self, *args, **kwargs):
                now = self._info_client['cash']
                ready_func = func(self, *args, **kwargs)
                after = self._info_client['cash']
                cash = 0 if arg1 not in ('зачисление средств', 'списание средств') else after - now
                is_success = False if now == after and arg1 in ('зачисление средств', 'списание средств') else True
                operation = self.history(cash=cash, balance=now,
                                         types_operations=arg1, is_success=is_success)
                self._history_operation = pd.concat([self._history_operation, operation])
                return ready_func
            return wrapper
        return save_history

    @staticmethod
    def history(cash=0, balance=0, types_operations=None, is_success=None):  # создание истории
        if types_operations is None:
            if cash > 0:
                types_operations = 'Зачисление средств'
            elif cash < 0:
                types_operations = 'Списание средств'
            else:
                types_operations = 'Просмотр баланса'
        return pd.DataFrame(columns=['date', 'type', 'is_success', 'summ', 'balance'],
                            data=[[datetime.today(), types_operations, is_success, cash, balance]])

    @__decorator('открытие счета')
    def _open_bill(self):  # открыть счет
        self._info_client['fio'] = self.name_client
        self._info_client['number'] = self.get_bill()
        self._info_client['currency'] = self._currency
        return self._check_num()

    @__decorator('зачисление средств')
    def _deposit_money(self, cash=0):
        now = self._info_client['cash']
        check_sum = self.check_sum(cash=cash, balance=now, currency=self._currency)
        self._info_client['cash'] = now + cash if check_sum else self._info_client['cash']

    @__decorator('списание средств')
    def _withdraw_money(self, cash=0):
        now = self._info_client['cash']
        check_sum = self.check_sum(cash=cash, balance=now, currency=self._currency)
        self._info_client['cash'] = now + cash if check_sum else self._info_client['cash']

    @__decorator('запрос информации по счету')
    def _info_balance(self, type_history=None) -> pd.DataFrame:
        if type_history == 'state_balance':
            return pd.DataFrame(columns=['Дата запроса', 'Текущий баланс по счету'],
                                data=[[datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
                                       self._info_client['cash']]])
        else:
            results = self._history_operation.copy()
            results['change_sum'] = np.where(results['summ'] == 0, False, True)
            results['balance_after'] = results['summ'] + results['balance']
            results['is_success'] = np.where(results['is_success'], "Успешно", "Операция отменена")
            results['date'] = pd.to_datetime(results['date']).dt.strftime("%d-%m-%Y %H:%M:%S")
            if type_history == 'history_operations':
                return results[['date', 'type', 'is_success', 'summ', 'balance',
                                'balance_after']].rename(
                    dict(date='Дата операции', type='Тип операции', is_success='Успешность выполнения',
                         summ='Сумма операции',
                         balance='Баланс до', balance_after='Баланс после'), axis=1)
            elif type_history == 'history_balance':
                results = results[results['change_sum'].isin([True])]
                results = results[['date', 'balance_after']].rename(
                    dict(date='Дата', balance_after='Баланс на конец дня'), axis=1)
                return results.groupby("Дата").last().reset_index()
            else:
                return pd.DataFrame()


class Bills(Func):
    def __init__(self, name=None, cash=0, currency='RUR'):
        super().__init__()
        self.name_client = name
        self._cash = cash
        self._currency = currency

        if self.name_client is not None and super()._open_bill():
            print(f"Для {self.name_client} открыт счет в {self._currency}")
            self.balance = cash
        else:
            print("Ошибка. Счет не открыт")

    @property
    def history_operations(self):
        return super()._info_balance('history_operations').to_string()

    @property
    def history_balance(self):
        return super()._info_balance('history_balance').to_string()

    @property
    def balance(self) -> pd.DataFrame:
        return super()._info_balance('state_balance')

    @balance.setter
    def balance(self, value):
        if value > 0:
            super()._deposit_money(cash=value)
        elif value < 0:
            super()._withdraw_money(cash=value)
        else:
            pass


client2 = Bills(cash=1, name='Петров I.I.', currency='EUR')  # открыть счет
client2.balance = 20
client2.balance = -50
client2.balance = -10
print(client2.balance)
print(client2.history_operations)
print(client2.history_balance)
print(client2.name_client)
