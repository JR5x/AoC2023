import time
start = time.time()


def parse_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    seeds = []
    seed_to_soil = []
    soil_to_fertilizer = []
    fertilizer_to_water = []
    water_to_light = []
    light_to_temperature = []
    temperature_to_humidity = []
    humidity_to_location = []

    current_section = None

    for line in lines:
        line = line.strip()
        if line.startswith('seeds:'):
            seed_values = list(map(int, line.split(':')[1].split()))
            seeds = [seed_values[i:i+2] for i in range(0, len(seed_values), 2)]
        elif line.startswith('seed-to-soil map'):
            current_section = 'seed-to-soil'
        elif line.startswith('soil-to-fertilizer map'):
            current_section = 'soil-to-fertilizer'
        elif line.startswith('fertilizer-to-water map'):
            current_section = 'fertilizer-to-water'
        elif line.startswith('water-to-light map'):
            current_section = 'water-to-light'
        elif line.startswith('light-to-temperature map'):
            current_section = 'light-to-temperature'
        elif line.startswith('temperature-to-humidity map'):
            current_section = 'temperature-to-humidity'
        elif line.startswith('humidity-to-location map'):
            current_section = 'humidity-to-location'
        elif line:
            values = list(map(int, line.split()))
            if current_section == 'seed-to-soil':
                seed_to_soil.append(values)
            elif current_section == 'soil-to-fertilizer':
                soil_to_fertilizer.append(values)
            elif current_section == 'fertilizer-to-water':
                fertilizer_to_water.append(values)
            elif current_section == 'water-to-light':
                water_to_light.append(values)
            elif current_section == 'light-to-temperature':
                light_to_temperature.append(values)
            elif current_section == 'temperature-to-humidity':
                temperature_to_humidity.append(values)
            elif current_section == 'humidity-to-location':
                humidity_to_location.append(values)

    return (seeds, seed_to_soil, soil_to_fertilizer, fertilizer_to_water,
            water_to_light, light_to_temperature, temperature_to_humidity,
            humidity_to_location)


def destination_to_source(map, given):
    for triple in map:
        if given >= triple[0] and given < triple[0] + triple[2]:
            given += triple[1] - triple[0]
            return given
    return given


def seed_to_location(i):
    humidity = destination_to_source(humidity_to_location, i)
    temperature = destination_to_source(temperature_to_humidity, humidity)
    light = destination_to_source(light_to_temperature, temperature)
    water = destination_to_source(water_to_light, light)
    fertilizer = destination_to_source(fertilizer_to_water, water)
    soil = destination_to_source(soil_to_fertilizer, fertilizer)
    seed = destination_to_source(seed_to_soil, soil)
    return seed


def speedy_lookup(i, j, n):
    while n >= 0:
        seed_diff_i = seed_to_location(i) - i
        seed_diff_j = seed_to_location(j) - j
        if (j - i) < 10:
            return j
        elif seed_diff_i == seed_diff_j:
            i += 10 ** n
            j += 10 ** n
        else:
            n -= 1
            j = i + 10 ** n


file_path = 'input5.txt'

(seeds, seed_to_soil, soil_to_fertilizer, fertilizer_to_water,
 water_to_light, light_to_temperature, temperature_to_humidity,
 humidity_to_location) = parse_file(file_path)

a = 1
b = 10 ** 8
c = 7

if any(pair[0] <= seed_to_location(1) < (pair[0] + pair[1]) for pair in seeds):
    print("1 is the answer.")
else:
    done = False
    while done == False:
        count = 1
        while count < 10:
            loc = speedy_lookup(a, b, c)
            seed = seed_to_location(loc)
            if any(pair[0] <= seed < (pair[0] + pair[1]) for pair in seeds):
                print(f"{loc} is the answer")
                done = True
                break
            loc += count
            count += 1
        a = loc - 9

end = time.time()
print(f'Time taken: {end - start} seconds')
