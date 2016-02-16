import json
import os


class AccountManager(object):

    def __init__(self):
        self.accounts = []

    def add_account(self, name, _id, password, _type):
        if os.path.exists('../files/accounts.json'):
            with open('../files/accounts.json') as f:
                self.accounts = json.load(f)
            f.close()

        account = dict(name=name,
                       id=_id,
                       password=password,
                       type=_type)
        self.accounts.append(account)
        with open('../files/accounts.json', 'w+') as f:
            json.dump(self.accounts, f, indent=4)
        f.close()

    def delete_account(self, _id):
        if os.path.exists('../files/accounts.json'):
            with open('../files/accounts.json') as f:
                self.accounts = json.load(f)
            f.close()

        for account in self.accounts:
            if account['id'] == _id:
                self.accounts.remove(account)

        with open('../files/accounts.json', 'w+') as f:
            json.dump(self.accounts, f, indent=4)
        f.close()

    def view_account(self, _id):
        if os.path.exists('../files/accounts.json'):
            with open('../files/accounts.json') as f:
                self.accounts = json.load(f)
            f.close()

        if len(self.accounts) == 0:
            pass  # popup empty accounts
        else:
            for account in self.accounts:
                if account['id'] == _id:
                    pass  # popup view account

    def view_all(self):
        if os.path.exists('../files/accounts.json'):
            with open('../files/accounts.json') as f:
                self.accounts = json.load(f)
            f.close()

        if len(self.accounts) == 0:
            pass  # popup empty accounts
        else:
            for account in self.accounts:
                pass  # popup all accounts
