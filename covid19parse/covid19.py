from covid19parse import ENDDATE, STARTDATE
from datetime import date, timedelta, time

class Covid19():
    def __init__(self):
        self.data = {}
        self.data['dates'] = {}
        self.data['countries'] = {}

    def add_date(self, date, confirmed=None, deaths=None, recovered=None, override=False,
        country=None, state=None, place=None):
        dates = None
        if country == None:
            dates = self.data['dates']
        elif state == None:
            if not country in self.data['countries']:
                raise Exception('covid19.add_date can not find country: %s' % country)
            dates = self.data['countries'][country]['dates']
        elif place == None:
            if not state in self.data['countries'][country]['states']:
                raise Exception('covid19.add_date can not find state: %s in country: %s' % (state, country))
            dates = self.data['countries'][country]['states'][state]['dates']
        else:
            if not place in self.data['countries'][country]['states'][state]['places']:
                raise Exception('covid19.add_date can not find place: %s in state: %s in country: %s' % (place, state, country))
            dates = self.data['countries'][country]['states'][state]['places'][place]['dates']
        if not date in dates:
            dates[date] = {}
            dates[date]['confirmed'] = 0
            dates[date]['deaths'] = 0
            dates[date]['recovered'] = 0
        if not override:
            if confirmed != None:
                dates[date]['confirmed'] += confirmed
            if deaths != None:
                dates[date]['deaths'] += deaths
            if recovered != None:
                dates[date]['recovered'] += recovered
        else:
            if confirmed != None:
                dates[date]['confirmed'] = confirmed
            if deaths != None:
                dates[date]['deaths'] = deaths
            if recovered != None:
                dates[date]['recovered'] = recovered

    def add_country(self, country,
        date=None, confirmed=None, deaths=None, recovered=None, override=False):
        countries = self.data['countries']
        if not country in countries:
            countries[country] = {}
            countries[country]['states'] = {}
            countries[country]['dates'] = {}
        if date == None: return
        self.add_date(date, country=country,
            confirmed=confirmed,
            deaths=deaths,
            recovered=recovered,
            override=override)

    def add_state(self, country, state,
        date=None, confirmed=None, deaths=None, recovered=None, override=False):
        if not country in self.data['countries']:
            print('Could not add state: %s to non existing country: %s' % (state, country))
            return
        states = self.data['countries'][country]['states']
        if not state in states:
            states[state] = {}
            states[state]['places'] = {}
            states[state]['dates'] = {}
        if date == None: return
        self.add_date(date, country=country, state=state,
            confirmed=confirmed,
            deaths=deaths,
            recovered=recovered,
            override=override)

    def add_place(self, country, state, place,
        date=None, confirmed=None, deaths=None, recovered=None, override=False):
        if not country in self.data['countries']:
            print('Could not add state: %s to non existing country: %s' % (state, country))
            return
        if not state in self.data['countries'][country]['states']:
            print('Could not add place: %s to non existing state: %s' % (place, state))
            return
        places = self.data['countries'][country]['states'][state]['places']
        if not place in places:
            places[place] = {}
            places[place]['dates'] = {}
        if date == None: return
        self.add_date(date, country=country, state=state, place=place,
            confirmed=confirmed,
            deaths=deaths,
            recovered=recovered,
            override=override)

    def get_children(self, country=None, state=None):
        if country == None:
            return list(self.data['countries'])
        elif state == None:
            if not country in self.data['countries']:
                raise Exception('covid19.get_children can not find country: %s' % country)
            return self.data['countries'][country]['states']
        else:
            if not state in self.data['countries'][country]['states']:
                raise Exception('covid19.get_children can not find state: %s in country: %s' % (state, country))
            return self.data['countries'][country]['states'][state]['places']

    def fill_blank_dates(self):
        delta = ENDDATE - STARTDATE
        dates = [(STARTDATE + timedelta(days=i)).strftime('%m-%d-%Y') for i in range(delta.days + 1)]
        for date in dates:
            self.add_date(date)
            for country in self.get_children():
                self.add_date(date, country=country)
                for state in self.get_children(country=country):
                    self.add_date(date, country=country, state=state)
                    for place in self.get_children(country=country, state=state):
                        self.add_date(date, country=country, state=state, place=place)

    def get_dates(self, country=None, state=None, place=None):
        if country == None:
            return self.data['dates']
        elif state == None:
            if not country in self.data['countries']:
                raise Exception('covid19.get_dates can not get dates for country: %s' % country)
            return self.data['countries'][country]['dates']
        elif place == None:
            if not state in self.data['countries'][country]['states']:
                raise Exception('covid19.get_dates can not get dates for state: %s in country: %s' % (state, country))
            return self.data['countries'][country]['states'][state]['dates']
        else:
            if not place in self.data['countries'][country]['states'][state]['places']:
                raise Exception('covid19.get_dates can not get dates for place: %s in state: %s in country: %s' % (place, state, country))
            return self.data['countries'][country]['states'][state]['places'][place]['dates']

    def get_confirmed(self, country=None, state=None, place=None):
        dates = self.get_dates(country=country, state=state, place=place)
        sortedDates = list(dates)
        sortedDates.sort()
        confirmed = []
        for date in sortedDates:
            confirmed.append(dates[date]['confirmed'])
        return confirmed

    def get_deaths(self, country=None, state=None, place=None):
        dates = self.get_dates(country=country, state=state, place=place)
        sortedDates = list(dates)
        sortedDates.sort()
        deaths = []
        for date in sortedDates:
            deaths.append(dates[date]['deaths'])
        return deaths
    
    def get_recovered(self, country=None, state=None, place=None):
        dates = self.get_dates(country=country, state=state, place=place)
        sortedDates = list(dates)
        sortedDates.sort()
        recovered = []
        for date in sortedDates:
            recovered.append(dates[date]['recovered'])
        return recovered

    def upgrade_dates(self, fromCovid19,
        country=None, state=None, place=None):
        fromDates = fromCovid19.get_dates(country=country, state=state, place=place)
        toDates = self.get_dates(country=country, state=state, place=place)
        for date in fromDates:
            self.add_date(date, country=country, state=state, place=place)
            if toDates[date]['confirmed'] < fromDates[date]['confirmed']:
                toDates[date]['confirmed'] = fromDates[date]['confirmed']
            if toDates[date]['deaths'] < fromDates[date]['deaths']:
                toDates[date]['deaths'] = fromDates[date]['deaths']
            if toDates[date]['recovered'] < fromDates[date]['recovered']:
                toDates[date]['recovered'] = fromDates[date]['recovered']

    def update_with(self, fromCovid19):
        for country in fromCovid19.get_children():
            self.add_country(country)
            self.upgrade_dates( fromCovid19,
                country=country)
            for state in fromCovid19.get_children(country=country):
                self.add_state(country, state)
                self.upgrade_dates( fromCovid19,
                    country=country,
                    state=state)
                for place in fromCovid19.get_children(country=country, state=state):
                    self.add_place(country, state, place)
                    self.upgrade_dates( fromCovid19,
                        country=country,
                        state=state,
                        place=place)
    

