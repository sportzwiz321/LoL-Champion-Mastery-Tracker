import requests
import sys

# update key information here
# key = 

def retrieveSummoner(name):
	URL = "https://na1.api.riotgames.com/lol/summoner/v3/summoners/by-name/" + NAME + "?api_key=" + key
	me = requests.get(URL).json()

	USERNAME = me['name']
	LEVEL = me['summonerLevel']
	ID = me['id']

	print "Username:", USERNAME
	print "Level:", LEVEL
	print "Identification Code:", ID

	URL3 = "https://na1.api.riotgames.com/lol/league/v3/positions/by-summoner/" + str(ID) + "/?api_key=" + key
	rank = requests.get(URL3).json()

	ID = str(ID)

	if len(rank) > 0:
		for x in range(0,len(rank)):
			# print x
			print
			data = rank[x]
			queueType = data['queueType']
			tier = data['tier']
			division = data['rank']
			leaguePoints = data['leaguePoints']

			print "Queue Type:", queueType
			print "Tier:", tier
			print "Division:", division
			print "LP:", leaguePoints
	else:
		print "You have not played enough ranked games to be placed yet"
		print "You suck."

	return ID

def retrieveChampion(list, order, record, recordPoints, count):

	if len(list) == 0:
		return
	elif count > len(list):
		count = len(list)

	print str(count) + "/138 played"
	print
	print "Your top champions are:"

	x = 0

	masteries=[]
	for i in range(1,9):
		record[i] = 0
		recordPoints[i] = 0

	while x < count:
		placed = False
		index = 0
		while placed == False:
			masteryLevel = list[x]['championLevel']
			if len(masteries) < index + 1:
				masteries.append(list[x]['championId'])
				order.append(x)
				record[masteryLevel] += 1
				recordPoints[masteryLevel] += list[x]['championPoints']
				record[8] += masteryLevel
				placed = True
			elif masteryLevel > list[order[index]]['championLevel'] or list[x]['championPoints'] > list[order[index]]['championPoints']:
				dec = len(masteries)
				masteries.append(masteries[dec - 1])
				order.append(order[dec - 1])
				dec -= 1
				while dec > index:
					masteries[dec] = masteries[dec - 1]
					order[dec] = order[dec - 1]
					dec -= 1
				masteries[index] = list[x]['championId']
				order[index] = x
				record[masteryLevel] += 1
				record[8] += masteryLevel
				recordPoints[masteryLevel] += list[x]['championPoints']
				placed = True
			else:
				index += 1
		x += 1

	x = 0

def printTopChampions(list, order, record, recordPoints):
	champList = requests.get("https://na1.api.riotgames.com/lol/static-data/v3/champions?dataById=true&api_key=" + key).json()
	lowestMastery = 4
	if len(list) == 0:
		print "You have no mastery"
		print "Play some more games before coming back"
	else:
		print "Mastery Score:", record[8]
		x = 7
		i = 0
		print "Mastery", x, "(" + (str)(record[x]) + ")"
		while x >= lowestMastery and i < len(order):
			if list[order[i]]['championLevel'] == x:
				id = list[order[i]]['championId']
				print "\t", champList['data'][str(id)]['name'], list[order[i]]['championPoints']
				i += 1
			else:
				x -= 1
				if x >= lowestMastery:
					print
					print "Mastery", x, "(" + (str)(record[x]) + ")"

if not len(sys.argv) == 2:
	print "RuntimeError: Username is required"
else:

	NAME = sys.argv[1]

	URL = "https://na1.api.riotgames.com/lol/summoner/v3/summoners/by-name/" + NAME + "?api_key=" + key
	me = requests.get(URL).json()

	print me

	if not me.has_key('name'):
		print "Summoner:", NAME, "does not exist"
		print "Please try again"
	else:	

		print sys.argv[1]

		id = retrieveSummoner(NAME)

		URL2 = "https://na1.api.riotgames.com/lol/champion-mastery/v3/champion-masteries/by-summoner/" + id + "?api_key=" + key
		mastery = requests.get(URL2).json()

		order = []
		record = {}
		recordPoints = {}

		count = 138

		retrieveChampion(mastery, order, record, recordPoints, count)

		printTopChampions(mastery, order, record, recordPoints)

	











