import requests

class VeintitresClientError(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return repr(self.message)

class VeintitresClient:
    """Allows to connect to the 23andme API."""
    url = {
        'token': 'https://api.23andme.com/token',
        'genotypes': 'https://api.23andme.com/1/genotypes',
        'demo_genotypes': 'https://api.23andme.com/1/demo/genotypes',
        'genomes': 'https://api'
    }

    def __init__(self, clientid, clientsecret, redirect, datascope):
        self.clientid = clientid
        self.clientsecret = clientsecret
        self.redirect = redirect
        self.datascope = datascope

    def request_token(self, code):
        payload = {
            'client_id': self.clientid,
            'client_secret': self.clientsecret,
            'grant_type': 'authorization_code',
            'code': code,
            'redirect_uri': self.redirect,
            'scope': self.datascope
        }
        request = requests.post(self.url.token, data=payload)

        if request.status_code == 200:
            data = request.json()
            self.accesstoken = data.access_token
            self.expires = data.expires_in
            self.refreshtoken = data.refresh_token
            return True
        else:
            data = request.json()
            raise VeintitresClientError('Cannot connect to 23andme: ' + data.error + ' - ' + data.error_description)

    def get_auth_header(self):
        if self.accesstoken:
            return {'Authorization': 'Bearer' + self.accesstoken}
        else
            return {'Authorization': False}

    def get_genotypes(self, profileid, inputdata, demomode=False):
        if not profileid:
            raise VeintitresClientError('Missing <profile_id> in inputdata')

        if not 'locations' in inputdata:
            raise VeintitresClientError('Missing <locations> in inputdata')

        auth = get_auth_header()

        if not auth.Authorization:
            raise VeintitresClientError('No authorization data detected')

        if not demomode:
            request = requests.get(self.url.genotypes + '/' + profileid, data=inputdata, headers=auth)
        else:
            request = requests.get(self.url.demo_genotypes + '/' + profileid, data=inputdata, headers=auth)

        return request.json()

    def get_genomes(self, profileid, inputdata, demomode=False):
        if not profileid:
            raise VeintitresClientError('Missing <profile_id> in inputdata')

        auth = get_auth_header()

        if not auth.Authorization:
            raise VeintitresClientError('No authorization data detected')

        if not demomode:
            request = requests.get(self.url.genomes + '/' + profileid, data=inputdata, headers=auth)
        else:
            request = requests.get(self.url.demo_genomes + '/' + profileid, data=inputdata, headers=auth)

        return request.json()
