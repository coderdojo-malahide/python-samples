import random

titles = ['sir', 'lady', 'dame', 'duke', 'master', 'countess']
first_names = ['slime', 'grit', 'egg', 'fire', 'bone', 'worm']
last_names = ['skull', 'heart', 'hammer', 'maggot', 'snake']

def print_evil_name():
    random.shuffle(titles)
    random.shuffle(first_names)
    random.shuffle(last_names)

    my_title = titles[0]
    my_first_name = first_names[0]
    my_last_name = last_names[0]

    print("%s %s %s" % (my_title, my_first_name, my_last_name))

for i in range(1,10):
    print_evil_name()