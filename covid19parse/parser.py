from covid19parse import ENDDATE, STARTDATE, CSSE_URL, NYT_URL
from covid19parse import COUNTRY_FIX, US_STATES_FIX, US_PLACES_FIX, CANADA_PROVINCES_FIX
from covid19parse.covid19 import Covid19
from datetime import date, timedelta, time
import pandas

class Covid19Parser(object):

    @classmethod
    def parse(_cls):
        covid19CSSE_obj = _cls.parseCSSECSV()
        covid19NYT_obj = _cls.parseNYTCSV()
        covid19CSSE_obj.update_with(covid19NYT_obj)
        return covid19CSSE_obj
            
    @classmethod
    def parseNYTCSV(_cls):
        confirmedField = 'cases'
        deathsField = 'deaths'
        stateField = 'state'
        placeField = 'county'

        covid19_obj = Covid19()        

        delta = ENDDATE - STARTDATE
        dates = [(STARTDATE + timedelta(days=i)).strftime('%m-%d-%Y') for i in range(delta.days + 1)]
        
        cvsFile = NYT_URL

        try:
            data = pandas.read_csv(cvsFile)
        except:
            print('file not found: %s' % cvsFile)
            return covid19_obj

        data[confirmedField].fillna(0, inplace=True)
        data[deathsField].fillna(0, inplace=True)

        country = 'United States'

        for index, row in data.iterrows():
            dateSplit = row['date'].split('-')
            date = '%s-%s-%s' % (dateSplit[1], dateSplit[2], dateSplit[0])
            
            if not date in dates: continue
            covid19_obj.add_date( date,
                confirmed=int(row[confirmedField]),
                deaths=int(row[deathsField]))
            
            covid19_obj.add_country(country,
                date=date,
                confirmed=int(row[confirmedField]),
                deaths=int(row[deathsField]))
            
            state = row[stateField]
            if not isinstance(state, str): continue
            covid19_obj.add_state(country, state,
                date=date,
                confirmed=int(row[confirmedField]),
                deaths=int(row[deathsField]))
            
            place = row[placeField]
            place = place.replace(' city', '')
            place = place.replace(' and Borough', '')
            place = place.replace(' Borough', '')
            if place in US_PLACES_FIX: place = US_PLACES_FIX[place]
            if place == 'Unassigned': continue
            covid19_obj.add_place(country, state, place,
                date=date,
                confirmed=int(row[confirmedField]),
                deaths=int(row[deathsField]))

        covid19_obj.fill_blank_dates()
        return covid19_obj

    @classmethod
    def parseCSSECSV(_cls):
        confirmedField = 'Confirmed'
        deathsField = 'Deaths'
        recoveredField = 'Recovered'

        covid19_obj = Covid19()        

        delta = ENDDATE - STARTDATE
        for i in range(delta.days + 1):
            date = (STARTDATE + timedelta(days=i)).strftime('%m-%d-%Y')
            cvsFile = '%s%s.csv' % (CSSE_URL, date)
            print('%s ... ' % date, end='')
            try:
                data = pandas.read_csv(cvsFile)
            except:
                print('file not found: %s' % cvsFile)
                continue
            
            countryField = 'Country_Region'
            if 'Country/Region' in data:
                countryField = 'Country/Region'
            stateField = 'Province_State'
            if 'Province/State' in data:
                stateField = 'Province/State'
            placeField = None
            if 'Admin2' in data:
                placeField = 'Admin2'

            data[confirmedField].fillna(0, inplace=True)
            data[deathsField].fillna(0, inplace=True)
            data[recoveredField].fillna(0, inplace=True)

            for index, row in data.iterrows():
                covid19_obj.add_date( date,
                    confirmed=int(row[confirmedField]),
                    deaths=int(row[deathsField]),
                    recovered=int(row[recoveredField]))
                
                country = row[countryField]
                if not isinstance(country, str): continue
                country = country.strip()
                if country in COUNTRY_FIX:
                    country = COUNTRY_FIX[country]
                covid19_obj.add_country(country,
                    date=date,
                    confirmed=int(row[confirmedField]),
                    deaths=int(row[deathsField]),
                    recovered=int(row[recoveredField]))
                
                state = row[stateField]
                if not isinstance(state, str): continue
                if state == 'Recovered': continue
                place = None
                if ',' in state:
                    stateSplit = state.split(',')
                    state = stateSplit[1].split()[0].strip()
                    place = stateSplit[0].strip()
                if country == 'United States' and state in US_STATES_FIX:
                    state = US_STATES_FIX[state]
                if country == 'Canada' and state in CANADA_PROVINCES_FIX:
                    state = CANADA_PROVINCES_FIX[state]
                if state == 'US': continue
                covid19_obj.add_state(country, state,
                    date=date,
                    confirmed=int(row[confirmedField]),
                    deaths=int(row[deathsField]),
                    recovered=int(row[recoveredField]))
                
                if place == None:
                    if placeField == None: continue
                    place = row[placeField]
                    if not isinstance(place, str): continue
                place = place.strip()
                if place == 'Virgin Islands': continue
                place = place.replace(' County', '')
                if country == 'United States' and place in US_PLACES_FIX:
                    place = US_PLACES_FIX[place]
                if place == 'Unassigned': continue
                covid19_obj.add_place(country, state, place,
                    date=date,
                    confirmed=int(row[confirmedField]),
                    deaths=int(row[deathsField]),
                    recovered=int(row[recoveredField]))

            print('done')

        covid19_obj.fill_blank_dates()
        return covid19_obj

