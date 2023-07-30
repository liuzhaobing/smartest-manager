# -*- coding:utf-8 -*-
from pymongo import MongoClient

from smartest.settings import DATABASES

mongo = DATABASES.get("mongo_smartest")
info = mongo["CLIENT"]
uri = f"mongodb://{info['username']}:{info['password']}@{info['host']}:{info['port']}/{info['authSource']}"
mongo_smartest_client = MongoClient(uri)
mongo_smartest_database = mongo_smartest_client[mongo["NAME"]]
