import array
from flask import Flask, request, jsonify
import time
import json
import inspect

import os
from dotenv import load_dotenv
load_dotenv()

from common.errorcodes import ERROR_CMD_NOT_SUPPORT

app = Flask(__name__)


def __LINE__():
    return inspect.currentframe().f_back.f_lineno

class ApiAccess():
    def __init__(self):
        self.resp = {}
        self.IpVars = {}
        self.resp['DateMsUtc'] = int(time.time())
        self.resp['Errors'] = []

    def ProcCmd(self, cmd):
        # TODO Validatation
        self.resp['Cmd'] = cmd

        match cmd:
            case 'User.Get' | 'User.Set' | 'User.Add' | 'User.Del':
                if not self.__Cmd__UserGsad(cmd):
                    self.ErrorLog(__LINE__())
                    return False
            
            case 'Account.Get' | 'Account.Getlist' | 'Account.Set' | 'Account.Add' | 'Account.Del':
                if not self.__Cmd__AccountGsad(cmd):
                    self.ErrorLog(__LINE__())
                    return False
            
            case 'Transaction.Get' | 'Transaction.Getlist' | 'Transaction.Set' | 'Transaction.Add' | 'Transaction.Del':
                if not self.__Cmd__TransactionGsad(cmd):
                    self.ErrorLog(__LINE__())
                    return False
                
            case 'ExchangeRate.Get':
                if not self.__Cmd__ExchangeRateGsad(cmd):
                    self.ErrorLog(__LINE__())
                    return False

            case _:
                self.resp['Errors'].append(ERROR_CMD_NOT_SUPPORT)

    def ErrorLog(self, line, txt=''):
        if txt:
            self.resp['Errors'].append({line: txt})
        else:
            self.resp['Errors'].append({line: ""})

    def __Cmd__AccountGsad(self, cmd):
        match cmd:
            case 'Account.Get':
                # Init vars.
                if not self.IpVars.get('AccountId'):
                    self.ErrorLog(__LINE__(), "IpVars missing or invalid.")
                    return False
            
                aVarsIn, aVarsOut = {}, {}
                if self.IpVars.get('AccountId'):
                    aVarsIn['AccountId'] = self.IpVars.get('AccountId')
            
            case 'Account.Getlist':
                # Init vars.
                if not self.IpVars.get('UserId'):
                    self.ErrorLog(__LINE__(), "IpVars missing or invalid.")
                    return False
                
                aVarsIn, aVarsOut = {}, {}
                if self.IpVars.get('UserId'):
                    aVarsIn['UserId'] = self.IpVars.get('UserId')

            case 'Account.Set':
                # Init vars.
                if not self.IpVars.get('AccountId'):
                    self.ErrorLog(__LINE__(), "IpVars missing or invalid.")
                    return False
            
                aVarsIn, aVarsOut = {}, {}
                if self.IpVars.get('AccountId'):
                    aVarsIn['AccountId'] = self.IpVars.get('AccountId')

            case 'Account.Add':
                # Init vars.
                if not self.IpVars.get('UserId'):
                    self.ErrorLog(__LINE__(), "IpVars missing or invalid.")
                    return False
                
                aVarsIn, aVarsOut = {}, {}
                if self.IpVars.get('UserId'):
                    aVarsIn['UserId'] = self.IpVars.get('UserId')

            case 'Account.Del':
                # Init vars.
                if not self.IpVars.get('AccountId'):
                    self.ErrorLog(__LINE__(), "IpVars missing or invalid.")
                    return False
            
                aVarsIn, aVarsOut = {}, {}
                if self.IpVars.get('AccountId'):
                    aVarsIn['AccountId'] = self.IpVars.get('AccountId')

            case _:
                self.resp['Errors'].append(ERROR_CMD_NOT_SUPPORT)
                return False
            
        # Set Response
        return True

    def __Cmd__TransactionGsad(self, cmd):
        match cmd:
            case 'Transaction.Get':
                # Init vars.
                if not self.IpVars.get('TransactionId'):
                    self.ErrorLog(__LINE__(), "IpVars missing or invalid.")
                    return False
            
                aVarsIn, aVarsOut = {}, {}
                if self.IpVars.get('TransactionId'):
                    aVarsIn['TransactionId'] = self.IpVars.get('TransactionId')
        
            case 'Transaction.Getlist':
                # Init vars.
                if not self.IpVars.get('AccountId'):
                    self.ErrorLog(__LINE__(), "IpVars missing or invalid.")
                    return False
                
                aVarsIn, aVarsOut = {}, {}
                if self.IpVars.get('AccountId'):
                    aVarsIn['AccountId'] = self.IpVars.get('AccountId')

            case 'Transaction.Set':
                # Init vars.
                if not self.IpVars.get('TransactionId'):
                    self.ErrorLog(__LINE__(), "IpVars missing or invalid.")
                    return False
            
                aVarsIn, aVarsOut = {}, {}
                if self.IpVars.get('TransactionId'):
                    aVarsIn['TransactionId'] = self.IpVars.get('TransactionId')

            case 'Transaction.Add':
                # Init vars.
                if not self.IpVars.get('AccountId'):
                    self.ErrorLog(__LINE__(), "IpVars missing or invalid.")
                    return False
                
                aVarsIn, aVarsOut = {}, {}
                if self.IpVars.get('AccountId'):
                    aVarsIn['AccountId'] = self.IpVars.get('AccountId')

            case 'Transaction.Del':
                # Init vars.
                if not self.IpVars.get('TransactionId'):
                    self.ErrorLog(__LINE__(), "IpVars missing or invalid.")
                    return False
            
                aVarsIn, aVarsOut = {}, {}
                if self.IpVars.get('TransactionId'):
                    aVarsIn['TransactionId'] = self.IpVars.get('TransactionId')

            case _:
                self.resp['Errors'].append(ERROR_CMD_NOT_SUPPORT)
                return False
            
        # Set Response
        return True

    def __Cmd__UserGsad(self, cmd):
        from user.user import User
        oUser = User()

        match cmd:
            case 'User.Get':
                # Init vars.
                if not self.IpVars.get('UserId') and not self.IpVars.get('Username'):
                    self.ErrorLog(__LINE__(), "IpVars missing or invalid.")
                    return False
                
                aVarsIn, aVarsOut = {}, {}
                if self.IpVars.get('UserId'):
                    aVarsIn['UserId'] = self.IpVars.get('UserId')
                if self.IpVars.get('Username'):
                    aVarsIn['Username'] = self.IpVars.get('Username')

                # Get User
                if not oUser.UserGsad('Get', aVarsIn, aVarsOut):
                    self.ErrorLog(__LINE__())
                    return False
                
                if not aVarsOut.get('User'):
                    self.ErrorLog(__LINE__())
                    return False
                
                self.resp['User'] = aVarsOut['User']

            case 'User.Set':
                if not oUser.UserGsad('Set'):
                    self.ErrorLog(__LINE__())

            case 'User.Add':
                if not oUser.UserGsad('Add'):
                    self.ErrorLog(__LINE__())

            case 'User.Del':
                if not oUser.UserGsad('Del'):
                    self.ErrorLog(__LINE__())

            case _:
                self.resp['Errors'].append(ERROR_CMD_NOT_SUPPORT)
                return False
            
        # Set Response
        return True

    def __Cmd__ExchangeRateGsad(self, cmd):
        from exchange_rates.exchange_rates import ExchangeRate
        oExchangeRate = ExchangeRate()
        match cmd:
            case 'ExchangeRate.Get':
                # Init vars.
                if not self.IpVars.get('FromCurrency') or not self.IpVars.get('ToCurrency'):
                    self.ErrorLog(__LINE__(), "IpVars missing or invalid.")
                    return False
                
                aVarsIn, aVarsOut = {}, {}
                aVarsIn['FromCurrency'] = self.IpVars.get('FromCurrency')
                aVarsIn['ToCurrency'] = self.IpVars.get('ToCurrency')

                # Get Rate
                if not oExchangeRate.ExchangeRateGsad('Get', aVarsIn, aVarsOut):
                    self.ErrorLog(__LINE__())
                    return False

                if not aVarsOut.get('Rate'):
                    self.ErrorLog(__LINE__())
                    return False
                
                self.resp['Rate'] = aVarsOut['Rate']

            case _:
                self.resp['Errors'].append(ERROR_CMD_NOT_SUPPORT)
                return False
            
        # Set Response
        return True

    def __Cmd__TemplateGsad(self, cmd):
        match cmd:
            case 'Template.Get':
                pass

            case 'Template.Set':
                pass

            case 'Template.Add':
                pass

            case 'Template.Del':
                pass

            case _:
                self.resp['Errors'].append(ERROR_CMD_NOT_SUPPORT)
                return False
            
        # Set Response
        return True

@app.route('/api', methods=['POST', 'GET'])
def api():
    oAPI = ApiAccess()
    cmd = request.args.get('Cmd')

    # Combine GET and POST variables into a dictionary
    oAPI.IpVars = {**request.args.to_dict(), **request.form.to_dict()}
    oAPI.ProcCmd(cmd)

    # return jsonify(resp), 200
    return json.dumps(oAPI.resp), 200

if __name__ == "__main__":
    app.run(debug=True)