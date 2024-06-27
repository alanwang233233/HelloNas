from appcore import AppCore

ac = AppCore()
'''
print(ac.json_write_data('test.json', {}))
print(ac.json_load_data('test.json'))
print(ac.json_write_data('test.json', {
    "date": "2024.1.2"
}))
print(ac.json_load_data('test.json'))
print(ac.new_log('E','MSG'))'''
print(ac.get_log_info('0f8b7804-1b44-4fef-a999-40acfd38d2ac','2024.06.27'))