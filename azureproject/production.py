import os
from azure.identity import DefaultAzureCredential
import psycopg2

cred = DefaultAzureCredential()

accessToken = cred.get_token('https://ossrdbms-aad.database.windows.net/.default')

conn_string = os.environ['AZURE_POSTGRESQL_CONNECTIONSTRING']
conn_str = psycopg2.connect(conn_string + ' password=' + accessToken.token) 

# Configure Postgres database based on connection string of the libpq Keyword/Value form
# https://www.postgresql.org/docs/current/libpq-connect.html#LIBPQ-CONNSTRING
# Uncomment the following lines for App Service
#conn_str = os.environ['AZURE_POSTGRESQL_CONNECTIONSTRING']
conn_str_params = {pair.split('=')[0]: pair.split('=')[1] for pair in conn_str.split(' ')}
DATABASE_URI = 'postgresql+psycopg2://{dbuser}:{dbpass}@{dbhost}/{dbname}'.format(
     dbuser=conn_str_params['user'],
     dbpass=conn_str_params['password'],
     dbhost=conn_str_params['host'],
     dbname=conn_str_params['dbname']
 )