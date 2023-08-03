class Operation:
    def __init__(self, the_date, descr, from_, to_, amount, currency):
        '''
        Иициаоизация класса
        :param the_date: дата операции
        :param descr: описание операции
        :param from_: откуда перевод
        :param to_: куда перевод
        :param amount: баланс карты/счета
        :param currency: валюта
        '''
        self.the_date = the_date
        self.descr = descr
        self.from_ = from_ if from_ else ""
        self.to_ = to_
        self.amount = amount
        self.currency = currency

    def __repr__(self):
        return f'Operation("{self.the_date}", "{self.descr}", \
"{self.from_}", "{self.to_}", "{self.amount}", "{self.currency}")'

    def print_1st_line(self):
        '''
        Выводит на экран первую строку с датой и описанием операции
        '''
        the_date = self.the_date.strftime('%d.%m.%Y')
        return f'{the_date} {self.descr}'

    def print_to(self):
        '''
        Выводит на экран информацию, куда перевод
        '''
        account_list = self.to_.split()

        account_num = account_list[-1]
        account_num_hid = '**' + account_num[-4:]

        new_account_list = account_list[:-1]
        new_account_list.append(account_num_hid)
        return ' '.join(new_account_list)

    def print_from(self):
        '''
        Выводит на экран информацию, откуда перевод
        '''
        list_from = self.from_.split()
        num_from = list_from[-1]
        if len(num_from) == 16:
            card_name = ' '.join(list_from[:-1])
            card_num = f'{num_from[:4]} {num_from[4:6]}** **** {num_from[12:]}'
            return f'{card_name} {card_num}'
        else:
            account_num_hid = '**' + num_from[-4:]
            new_account_list = list_from[:-1]
            new_account_list.append(account_num_hid)
            return ' '.join(new_account_list)
