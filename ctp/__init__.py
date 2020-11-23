from requests import get
url = 'https://api.covidtracking.com/v1'

class error(Exception):
    pass

class BadRequestError(error):
    pass

class us():
    def __init__(self):
        self.route = '{}/us'.format(url)
    def history(self, day=False):
        if day:
            return(get('{}/{}.json'.format(self.route, str(day))).json())
        else:
            return(get('{}/daily.json'.format(self.route)).json())
    def current(self):
        return(get('{}/current.json'.format(self.route)).json())

class states():
    def __init__(self):
        self.route = '{}/states'.format(url)
    def metadata(self, state=False):
        if state:
            return(get('{}/{}/info.json'.format(self.route, state)).json())
        else:
            return(get('{}/info.json'.format(self.route)).json())
    def history(self, state=False, day=False):
        if state and not day:
            return(get('{}/{}/daily.json'.format(self.route, state)).json())
        if state and day:
            return(get('{}/{}/{}.json'.format(self.route, state, str(day))).json())
        if not state and not day:
            return(get('{}/daily.json'.format(self.route)).json())
        raise BadRequestError('Invalid parameters, a day was given but not a state')   
    def current(self, state=False):
        if state:
            return(get('{}/{}/current.json'.format(self.route, state)).json())
        else:
            return(get('{}/current.json'.format(self.route)).json())