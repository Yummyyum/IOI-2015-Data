import json
import urllib2
from multiprocessing import Pool

def fetch_flag(team):
    headers = { 'Accept' : 'image/png' }
    url = 'http://scoreboard.ioinformatics.org/flags/' + team
    req = urllib2.Request(url, headers=headers)
    resp = urllib2.urlopen(req)
    flag = resp.read()
    with open('flags/' + team, 'w') as f:
        f.write(flag)

def fetch_sublist(user):
    headers = { 'Accept' : 'application/json' }
    url = 'http://scoreboard.ioinformatics.org/sublist/' + user
    req = urllib2.Request(url, headers=headers)
    resp = urllib2.urlopen(req)
    submissions = resp.read()
    with open('sublist/' + user + '.json', 'w') as f:
        f.write(submissions)

def fetch_face(user):
    headers = { 'Accept' : 'image/jpeg' }
    url = 'http://scoreboard.ioinformatics.org/faces/' + user
    req = urllib2.Request(url, headers=headers)
    resp = urllib2.urlopen(req)
    submissions = resp.read()
    with open('faces/' + user + '.jpeg', 'w') as f:
        f.write(submissions)

def get_flags():
    with open('teams.json') as f:
        teams = json.load(f)
    p = Pool(400)
    p.map(fetch_flag, teams)
    p.close()

def get_sublists():
    with open('users.json') as f:
        users = json.load(f)
    p = Pool(400)
    p.map(fetch_sublist, users)
    p.close()

def get_faces():
    with open('users.json') as f:
        users = json.load(f)
    p = Pool(400)
    p.map(fetch_face, users)
    p.close()

get_flags()
print 'flags DONE'
get_sublists()
print 'sublists DONE'
get_faces()
print 'faces DONE'
