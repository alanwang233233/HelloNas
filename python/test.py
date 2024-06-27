from appcore import AppCore

ac = AppCore()

print(ac.json_write_data('test.json', {}))
print(ac.json_load_data('test.json'))
print(ac.json_write_data('test.json', {
    "date": "2024.1.2"
}))
print(ac.json_load_data('test.json'))
print(ac.new_log('E','MSG'))