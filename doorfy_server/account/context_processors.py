"""
Created on Jul 5, 2012

@author: HP
"""
from doorfy_server.settings import SITE_DOMAIN

def base(context):
    # return the value you want as a dictionnary. you may add multiple values in there.
    return {
            "SITE_DOMAIN" : SITE_DOMAIN,
           }
