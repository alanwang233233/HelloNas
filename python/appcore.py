import json
import os


class AppCore:
    @staticmethod
    def json_load_data(jsonfile):
        try:
            with open('./data/' + jsonfile, 'w', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            os.mknod('./data/' + jsonfile)
            try:
                with open('./data/' + jsonfile, 'w', encoding='utf-8') as f:
                    json.dump({}, f)
            except:
                # self.new_log('Error',e)
                return {}
            # self.new_log('Warning','file not found'+jsonfile+',now created')
            return {}
        except Exception as e:
            # self.new_log('Error',e)
            return {}

    @staticmethod
    def json_write_data(jsonfile):
        pass
