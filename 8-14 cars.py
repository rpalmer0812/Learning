def make_car(manu, model, **more_info):
    more_info['manufacturer'] = manu
    more_info['model'] = model
    return more_info

car_profile = make_car('subi', 'impreza', location = 'blah', rate = 'high')

print(car_profile)


make_profile = make_car('subaru', 'outback', color='blue', tow_package=True)

print(make_profile)

from hello import *

hellomate()
