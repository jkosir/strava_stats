# Strava uses sequential athlete IDs, currently one of the highest is 17.6 million
# That also suggests 17.6 million users
MAX_ATHLETE_NUM = 17600000

# How many profiles to load
SAMPLE_SIZE = 1000

# Athlete profile url
PROFILE_URL = 'https://www.strava.com/athletes/{id}'

with open('raw_headers.txt', 'r') as header_file:
    HEADERS = {x.split(':')[0]: x.split(':')[1].strip('\n') for x in header_file.readlines()}

# XPath selectors for profile analysis
LAST_4_WEEKS_ACTIVITIES_XPATH = '//div[@class = "activity-count"]/*/span[@class = "count"]'