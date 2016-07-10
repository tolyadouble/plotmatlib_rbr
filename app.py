import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np

def get_average(numbers):
    step = 0
    race = 0
    while step != len(numbers) + 1:
        if step == 0:
            x = numbers[step]
            step += 2
            race += 1
            yield x
        if numbers[step-1] != 0:
            race += 1
        x = sum(numbers[:step]) / race
        step += 1
        yield x

home_name = [
    #2015
    'AUS','MAL','CHN','BHR','ESP','MON','CAN','AUT','GBR',
    'HUN','BEL','ITA','SIN','JPN','RUS','USA','MEX','BRA','ABU',
    #2016
    'AUS','BHR','CHN','RUS','ESP','MON','CAN','EUR','AUT','GBR'
]

home_ticks = [x for x in range(1, len(home_name) + 1)]
plt.xticks(home_ticks, home_name)

riccardo = [
    [6,4,7,7,10,4,9,18,10,4,5,19,2,7,10,3,5,19,5,8,5,2,5,3,1,4,2,5,4],
    [6,10,9,6,7,5,13,10,0,3,0,8,2,15,0,10,5,11,6,4,4,4,11,4,2,7,7,5,4]
]

verstappen = [
    [12,6,13,15,11,9,19,7,13,9,18,20,8,15,9,8,8,9,11,4,10,9,9,4,21,5,9,8,3],
    # DNF - AUS 2015
    [7,0,18,11,0,15,8,0,4,8,12,8,9,10,4,9,9,16,10,6,8,0,1,0,4,8,2,3]
]

sainz = [
    [8,15,14,9,9,20,11,12,8,12,19,17,14,12,20,20,11,19,10,7,11,8,11,8,6,15,18,15,7],
    [9,8,14,19,9,10,12,0,14,0,0,11,9,10,0,7,13,0,11,9,0,9,12,6,8,9,0,8,8]
]

kvyat = [
    [13,5,12,17,19,5,8,15,7,7,12,18,4,10,11,4,4,7,9,18,15,6,8,13,8,16,6,22,14],
    # DNF - AUS 2015
    [9,0,9,10,4,9,12,6,2,4,10,6,13,5,0,4,7,10,0,7,3,15,10,0,12,0,0,10]
]

#race
plt.plot(home_ticks, np.array([x for x in get_average(riccardo[1])]), color='red')
plt.plot(home_ticks[1:], np.array([x for x in get_average(verstappen[1])]), color='orange')
plt.plot(home_ticks, np.array([x for x in get_average(sainz[1])]), color='green')
plt.plot(home_ticks[1:], np.array([x for x in get_average(kvyat[1])]), color='purple')

#quali
plt.plot(home_ticks, np.array([x for x in get_average(riccardo[0])]), color='red', linestyle='dashed')
plt.plot(home_ticks, np.array([x for x in get_average(verstappen[0])]), color='orange', linestyle='dashed')
plt.plot(home_ticks, np.array([x for x in get_average(sainz[0])]), color='green', linestyle='dashed')
plt.plot(home_ticks, np.array([x for x in get_average(kvyat[0])]), color='purple', linestyle='dashed')


plt.axvline(x=1, color='gray', linestyle='dashed',
            label='pre-industrial', lw=1.5)
plt.text(1.1,0.5,'2015')
plt.axvline(x=20, color='gray', linestyle='dashed',
            label='pre-industrial', lw=1.5)
plt.text(20.1,0.5,'2016')

plt.axvline(x=24, color='gray', linestyle='dotted',
            label='pre-industrial', lw=1.5)
plt.text(24.1,0.5,'KVY<->VES')

plt.title('RedBull Racing drivers average position per clean race/qualification', fontsize=18)
plt.legend(['Daniel Ricciardo', 'Max Verstappen', 'Carlos Sainz', 'Daniil Kvyat', 'Qualification'], loc='upper left')
plt.xlabel('GP HOME')
plt.ylabel('Average Position')
plt.gca().invert_yaxis()

plt.show()