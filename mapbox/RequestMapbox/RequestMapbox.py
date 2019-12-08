from ..Country import Country
import requests

class RequestMapbox(Country):
    '''
    exp
    '''

    def __init__(self,country_name):
        super().__init__(country_name)

    def __repr__(self):
        ''' Representation of the class'''
        return f'{self.__class__.__name__} at 0x{id(self)}({self.__dict__.keys()})'

    def get_features(self):
        '''

        :return:
        '''
        self.features = requests.get(self.url).json()['features']
        self.lat = self.features[0]['bbox'][1::2]
        self.long = self.features[0]['bbox'][0::2]
        self.country_id = self.features[0]['id']
        self.id = self.conn.execute(''' SELECT id 
                                        FROM Country
                         WHERE name = "{}";'''.format(self.country_name)).fetchone()[0]

    def drop_table(self,table):
        '''
        explain
        :param table: str
        :return:
        '''
        if table != 'latlong':
            warn = str(input('Drop a table != than `latlong` could be dangerous!!' +
                  'Are you sure you want to proceed? [y/n]: '))
            if warn == 'y':
                self.conn.execute('DROP TABLE IF EXISTS {};'.format(table))
            else:
                print('Drop table ignored')
        else:
            self.conn.execute('DROP TABLE IF EXISTS {};'.format(table))

    def insert_value(self, table):
        '''

        :param table:
        :return:
        '''
        values = '("{}","{}","{}","{}","{}")'.format(self.id, self.country_id, self.country_name, self.lat, self.long)
        self.conn.execute('INSERT INTO {} (id, country_id, country_name, lat, long) VALUES {};'.format(table, values))

    def create_table(self,table):
        '''
        Hardcoded schema
        :param table:  str
        :return:
        '''
        self.conn.execute('''
                            create table {} (
                                id TEXT PRIMARY KEY,
                                country_id TEXT,  
                                country_name TEXT, 
                                lat TEXT,
                                long TEXT); '''.format(table))
