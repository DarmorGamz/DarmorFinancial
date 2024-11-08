from flask import Flask, request, jsonify
import time
import json
import inspect

import os
from dotenv import load_dotenv
# Load environment variables from the .env file in the root directory
load_dotenv()
DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PWD = os.getenv("DB_PWD")

from common.errorcodes import ERROR_CMD_NOT_SUPPORT

app = Flask(__name__)


class ApiAccess():
    def __init__(self):
        self.resp = {}
        self.resp['DateMsUtc'] = int(time.time())
        self.resp['Errors'] = []

    def ProcCmd(self, cmd):
        # TODO Validatation
        self.resp['Cmd'] = cmd

        match cmd:
            case 'User.Get' | 'User.Set' | 'User.Add' | 'User.Del':
                self.__Cmd__UserGsad(cmd)

            case _:
                self.resp['Errors'].append(ERROR_CMD_NOT_SUPPORT)

    def __Cmd__UserGsad(self, cmd):
        from user.user import User
        oUser = User()

        match cmd:
            case 'User.Get':
                if not oUser.UserGsad('Get'):
                    self.resp['Errors'].append(inspect.currentframe().f_lineno)

            case 'User.Set':
                if not oUser.UserGsad('Set'):
                    self.resp['Errors'].append(inspect.currentframe().f_lineno)

            case 'User.Add':
                if not oUser.UserGsad('Add'):
                    self.resp['Errors'].append(inspect.currentframe().f_lineno)

            case 'User.Del':
                if not oUser.UserGsad('Del'):
                    self.resp['Errors'].append(inspect.currentframe().f_lineno)

            case _:
                self.resp['Errors'].append(ERROR_CMD_NOT_SUPPORT)

@app.route('/api', methods=['POST', 'GET'])
def api():
    oAPI = ApiAccess()
    cmd = request.args.get('Cmd')
    oAPI.ProcCmd(cmd)

    # return jsonify(resp), 200
    return json.dumps(oAPI.resp), 200

if __name__ == "__main__":
    app.run(debug=True)