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
            seeds = list(map(int, line.split(':')[1].split()))
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


def source_to_destination(map, given):
    for triple in map:
        if given >= triple[1] and given < triple[1] + triple[2]:
            given += triple[0] - triple[1]
            return given
    return given


file_path = 'input5.txt'

(seeds, seed_to_soil, soil_to_fertilizer, fertilizer_to_water,
 water_to_light, light_to_temperature, temperature_to_humidity,
 humidity_to_location) = parse_file(file_path)

answers = []

for seed in seeds:
    soil = source_to_destination(seed_to_soil, seed)
    fertilizer = source_to_destination(soil_to_fertilizer, soil)
    water = source_to_destination(fertilizer_to_water, fertilizer)
    light = source_to_destination(water_to_light, water)
    temperature = source_to_destination(light_to_temperature, light)
    humidity = source_to_destination(temperature_to_humidity, temperature)
    location = source_to_destination(humidity_to_location, humidity)
    answers.append(location)

print(answers)
