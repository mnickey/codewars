def rake_garden(garden):
    garden = garden.split()
    for item in range(0, len(garden)):
        if garden[item] != 'gravel' and garden[item] != 'rock':
            garden[item] = 'gravel'
    return ' '.join(garden)


def rake_garden(garden):
    knoll = garden.split(' ')
    knoll = [k.replace('slug', 'gravel') for k in knoll]
    knoll = [k.replace('spider', 'gravel') for k in knoll]
    knoll = [k.replace('ant', 'gravel') for k in knoll]
    knoll = [k.replace('snail', 'gravel') for k in knoll]
    knoll = [k.replace('moss', 'gravel') for k in knoll]
    land = ' '.join(knoll)
    return land
