import json
import pygal.maps.world as pmw
from pygal.style import RotateStyle, LightColorizedStyle as LCS


def get_country_code(country_name):
    for code, name in pmw.COUNTRIES.items():
        if name == country_name:
            return code

    return None


filename = 'population_data.json'

with open(filename) as f:
    pop_data = json.load(f)

# create a dictionary to save the countries and their population
cc_populations = {}
for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        country = pop_dict['Country Name']
        population = int(float(pop_dict['Value']))
        code = get_country_code(country)
        if code:
            cc_populations[code] = population

# set groups of countries according to the population
cc_pop_1, cc_pop_2, cc_pop_3 = {}, {}, {}
for cc, pop in cc_populations.items():
    if pop < 10000000:
        cc_pop_1[cc] = pop
    elif pop < 1000000000:
        cc_pop_2[cc] = pop
    else:
        cc_pop_3[cc] = pop

# set styles of the world figure
wm_style = RotateStyle('#00FFFF', base_style=LCS)

wm = pmw.World(style=wm_style)
wm.title = 'Population of every country in 2010'
wm.add('0-10m', cc_pop_1)
wm.add('10m-1bn', cc_pop_2)
wm.add('>1bn', cc_pop_3)

wm.render_to_file('world_population.svg')
