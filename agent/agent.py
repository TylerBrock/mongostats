#!/usr/bin/env python
import sys
import platform
import json
import datetime
import pymongo

connection = pymongo.Connection()
admin_db = connection['admin']

info = {}

info['serverStatus'] = admin_db.command("serverStatus")
info['isMaster'] = admin_db.command("isMaster")
info['connPoolStats'] = admin_db.command("connPoolStats")
info['cursorInfo'] = admin_db.command("cursorInfo")
info['dbStats'] = admin_db.command("dbStats")
info['whatsmyuri'] = admin_db.command("whatsmyuri")
info['getCmdLineOpts'] = admin_db.command("getCmdLineOpts")

if 'members' in info['isMaster']:
    info['replSetGetStatus'] = admin_db.command("replSetGetStatus")

dthandler = lambda obj: obj.isoformat() if isinstance(obj, datetime.datetime) else None

print json.dumps(info, sort_keys=True, indent=2, default=dthandler)

print sys.platform
print platform.machine()
print platform.node()
print platform.processor()
print platform.system()
print platform.uname()

# Platform specific
print platform.win32_ver()
print platform.mac_ver()
print platform.linux_distribution()


