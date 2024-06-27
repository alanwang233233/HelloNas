import json
import os
from datetime import datetime
import uuid


class AppCore:

    def json_load_data(self, jsonfile):
        try:
            with open('./data/' + jsonfile, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            try:
                os.mknod('./data/' + jsonfile)
                with open('./data/' + jsonfile, 'r', encoding='utf-8') as f:
                    json.dump({}, f)
            except Exception as e:
                self.new_log('Error', e)
                return {}
            self.new_log('Warning', 'file not found' + jsonfile + ',now created')
            return {}
        except Exception as e:
            self.new_log('Error', e)
            return {}

    def json_write_data(self, jsonfile, content):
        try:
            with open('./data/' + jsonfile, 'w', encoding='utf-8') as f:
                json.dump(content, f, indent=4, ensure_ascii=False)
                return True
        except FileNotFoundError:
            try:
                os.mknod('./data/' + jsonfile)
                with open('./data/' + jsonfile, 'w', encoding='utf-8') as f:
                    json.dump({}, f)
            except Exception as e:
                self.new_log('Error', e)
                return False
            self.new_log('Warning', 'file not found' + jsonfile + ',now created')
            return False
        except Exception as e:
            self.new_log('Error', e)
            return False

    @staticmethod
    def today():
        today = datetime.now()
        formatted_date = today.strftime('%Y.%m.%d')
        return formatted_date

    def new_log(self, sign, msg):
        uuid1 = 114514
        content = self.json_load_data('log.json')
        active = True
        while active:
            uuid1 = str(uuid.uuid4())
            if uuid1 in content:
                active = True
            else:
                if not self.today() in content:
                    content[self.today()] = {}
                content[self.today()][uuid1] = {}
                active = False
        content[self.today()][uuid1]['sign'] = sign
        content[self.today()][uuid1]['msg'] = msg
        if self.json_write_data('log.json', content):
            return uuid1
        else:
            return False

    def get_log_info(self, logid, date):
        return self.json_load_data('log.json')[date][logid]
