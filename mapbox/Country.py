import sqlalchemy
import os

class Country:
    '''
    Some definition of this class
    '''

    def __init__(self, country_name):
        '''

        :param country_name:
        '''
        self.country_name = country_name
        self.id = None
        self.private_token = os.environ['MAPBOX_PRIVATE_TOKEN']
        self.url = "https://api.mapbox.com/geocoding/v5/mapbox.places/{}.json?types=country,region&access_token=".format(self.country_name) + self.private_token
        self.lat = None
        self.long = None
        self.country_id = None


    def database (self, db):
        '''

        :param db:
        :return:
        '''
        self.db = 'sqlite:///' + db
        self.engine = sqlalchemy.create_engine(self.db)
        self.conn = self.engine.connect()

    def query (self):
        '''

        :return:
        '''
        self.id = self.conn.execute(''' SELECT id 
                                        FROM Country
                         WHERE name = "{}";'''.format(self.country_name)).fetchone()[0]
