from datetime import date
__version__ = '0.1'
STARTDATE = date(2020, 1, 21)   # start date
ENDDATE = date.today()   # today

CSSE_URL = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/'
NYT_URL = 'https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties.csv'

COUNTRY_FIX = {
    'US': 'United States',
    'U.S.': 'United States',#
    'UK': 'United Kingdom',
    'Bahamas, The': 'Bahamas',
    'Hong Kong SAR': 'Hong Kong',
    'Iran (Islamic Republic of)': 'Iran',
    'Gambia, The': 'Gambia',
    'Korea, South': 'South Korea',
    'Mainland China': 'China',
    'Congo (Brazzaville)': 'Congo',
    'Congo (Kinshasa)': 'Congo',
    'Republic of the Congo': 'Congo',
    'Republic of Ireland': 'Ireland',
    'Republic of Korea': 'North Korea',
    'Republic of Moldova': 'Moldova',
    'Russian Federation': 'Russia',
    'Taiwan*': 'Taiwan',
    'The Bahamas': 'Bahamas',
    'The Gambia': 'Gambia',
    'Viet Nam': 'Vietnam',
    'occupied Palestinian territory': 'Palestine'
}

US_STATES_FIX = {
    'AK': 'Alaska',
    'AL': 'Alabama',
    'AR': 'Arkansas',
    'AS': 'American Samoa',
    'AZ': 'Arizona',
    'CA': 'California',
    'CO': 'Colorado',
    'CT': 'Connecticut',
    'DC': 'District of Columbia',
    'DE': 'Delaware',
    'FL': 'Florida',
    'GA': 'Georgia',
    'GU': 'Guam',
    'HI': 'Hawaii',
    'IA': 'Iowa',
    'ID': 'Idaho',
    'IL': 'Illinois',
    'IN': 'Indiana',
    'KS': 'Kansas',
    'KY': 'Kentucky',
    'LA': 'Louisiana',
    'MA': 'Massachusetts',
    'MD': 'Maryland',
    'ME': 'Maine',
    'MI': 'Michigan',
    'MN': 'Minnesota',
    'MO': 'Missouri',
    'MP': 'Northern Mariana Islands',
    'MS': 'Mississippi',
    'MT': 'Montana',
    'NA': 'National',
    'NC': 'North Carolina',
    'ND': 'North Dakota',
    'NE': 'Nebraska',
    'NH': 'New Hampshire',
    'NJ': 'New Jersey',
    'NM': 'New Mexico',
    'NV': 'Nevada',
    'NY': 'New York',
    'OH': 'Ohio',
    'OK': 'Oklahoma',
    'OR': 'Oregon',
    'PA': 'Pennsylvania',
    'PR': 'Puerto Rico',
    'RI': 'Rhode Island',
    'SC': 'South Carolina',
    'SD': 'South Dakota',
    'TN': 'Tennessee',
    'TX': 'Texas',
    'UT': 'Utah',
    'VA': 'Virginia',
    'VI': 'Virgin Islands',
    'VT': 'Vermont',
    'WA': 'Washington',
    'WI': 'Wisconsin',
    'WV': 'West Virginia',
    'WY': 'Wyoming',
    'U.S.': 'Virgin Islands',
    'United States Virgin Islands': 'Virgin Islands'
}

US_PLACES_FIX = {
    'James city': 'James City',
    'Richmond City': 'Richmond',
    'Roanoke City': 'Roanoke',
    'Juneau City': 'Juneau',
    'Baltimore City': 'Baltimore',
    'New York City': 'New York',
    'Fairfax City': 'Fairfax',
    'Franklin City': 'Franklin',
    'Yukon-Koyukuk Census Area': 'Yukon-Koyukuk',
    'Southeast Fairbanks Census Area': 'Southeast Fairbanks',
    'Unassigned Location': 'Unassigned',
    'unassigned': 'Unassigned',
    'Unknown': 'Unassigned'
}

CANADA_PROVINCES_FIX = {
    'AB': 'Alberta',
    'BC': 'British Columbia',
    'MB': 'Manitoba',
    'NB': 'New Brunswick',
    'NL': 'Newfoundland and Labrador',
    'NT': 'Northwest Territories',
    'NS': 'Nova Scotia',
    'NU': 'Nunavut',
    'ON': 'Ontario',
    'PE': 'Prince Edward Island',
    'QC': 'Quebec',
    'SK': 'Saskatchewan',
    'YT': 'Yukon'
}