import boto3

class Config(object):

    client = boto3.client('ssm')
    endpoint = client.get_parameter(Name='PoolPartyAPI')['Parameter']['Value']
    username = client.get_parameter(Name='PoolPartyUsername')['Parameter']['Value']
    password = client.get_parameter(Name='PoolPartyPassword')['Parameter']['Value']
    cache_key = client.get_parameter(Name='metadata_cache_key')['Parameter']['Value']
    cache_servers = [client.get_parameter(Name='ElastiCacheServer')['Parameter']['Value']]

    # PoolParty and Linked Data
    project_id = '1E14CCD7-4805-0001-A3F9-198214D8AD30'

    available_languages = {
        'en': 'English',
        'fr': 'French',
        'es': 'Spanish'
    }

class ProductionConfig(Config):
    DEBUG = False
    
class DevelopmentConfig(Config):
    # Provide overrides for production settings here.
    DEBUG = True
