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

	# print "Length of list:", len(rank[ID])

	# if len(rank[ID] != 1):
	# 	return

	# print rank
	# print len(rank)

	# if rank.has_key(ID) is True:
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

		# tier = rank[ID][0]['tier']
		# division = rank[ID][0]['entries'][0]['division']
		# leaguePoints = rank[ID][0]['entries'][0]['leaguePoints']

		# print "Ranked Solo/Duo"
		# print "Tier:", tier
		# print "Division:", division
		# print "LP:", leaguePoints
	else:
		print "You have not played enough ranked games to be placed yet"
		print "You suck."

	# if len(rank[ID][0]['tier'] > 0):
	# 	tier = rank[ID][0]['tier']
	# 	division = rank[ID][0]['entries'][0]['division']
	# 	leaguePoints = rank[ID][0]['entries'][0]['leaguePoints']

	# 	print "Tier:", tier
	# 	print "Division:", division
	# 	print "LP:", leaguePoints
	# else:
	# 	print "You have not played enough ranked games to be placed yet"
	# 	print "You suck."
	

	return ID

def retrieveChampion(list, order, record, recordPoints, count):

	if len(list) == 0:
		# print "Sorry you haven't earned any mastery points on any champions yet"
		return
	elif count > len(list):
		# print "Sorry you haven't played", count, "champions yet"
		# print "You have only earned mastery for", len(list), "champions"
		count = len(list)

	print str(count) + "/138 played"
	print
	print "Your top champions are:"

	x = 0

	masteries=[]
	# mIndex = []
	for i in range(1,9):
		record[i] = 0
		recordPoints[i] = 0

	while x < count:
		placed = False
		index = 0
		while placed == False:
			# print "My index is", index
			# if len(masteries) > 0:
				# print "Top champ is", masteries[0]
			masteryLevel = list[x]['championLevel']
			if len(masteries) < index + 1:
				masteries.append(list[x]['championId'])
				order.append(x)
				record[masteryLevel] += 1
				recordPoints[masteryLevel] += list[x]['championPoints']
				record[8] += masteryLevel
				# print "Champion", x, "is placed here"
				placed = True
			elif masteryLevel > list[order[index]]['championLevel'] or list[x]['championPoints'] > list[order[index]]['championPoints']:
				# print "Champion", x, "Mastery Level:", list[x]['championLevel']
				# print "Index", index, "Champion Mastery Level:", list[index]['championLevel']
				# print "Champion", x, "Champion Mastery Level at index", index, "is", list[x]['championLevel'] > list[index]['championLevel']
				# print "Champion", x, "Champion Mastery Points at index", index, "is", list[x]['championPoints'] > list[index]['championPoints']
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
				# while index < len(masteries):
				# 	tempChamp = masteries[index]
				# 	masteries[index] = list[x]['championId']
				# 	masteries[index+1] = tempChamp
				# 	index += 1
				# index = tempIndex
				# print "Champion", x, "is placed there but not here"
				placed = True
			else:
				index += 1
		x += 1

		# c = 0
		# while c < len(masteries):
		# 	champion = requests.get("https://global.api.pvp.net/api/lol/static-data/na/v1.2/champion/" + str(masteries[c]) + "?api_key=c07d4fd5-82c1-4816-a45c-605b8291daff")
		# 	print champion.json()['name']
		# 	c += 1


	# list = masteries

	x = 0
	# while x < count:
	# 	id = masteries[x]
	# 	# id = list[x]['championId']
	# 	# list[x]['championId'] is equivalent to masteries[x]

	# 	champion = requests.get("https://global.api.pvp.net/api/lol/static-data/na/v1.2/champion/" + str(id) + "?api_key=c07d4fd5-82c1-4816-a45c-605b8291daff")
	# 	# champ = champion.json()
	# 	# print champion.json()['name'], "Mastery Lvl:", list[mIndex[x]]['championLevel'], "Champion Pts:", list[mIndex[x]]['championPoints']
	# 	# print x+1
	# 	x += 1
	# print "all done!"
	
	# order = mIndex

	# return champion.json()['name']

def printTopChampions(list, order, record, recordPoints):
	champList = requests.get("https://na1.api.riotgames.com/lol/static-data/v3/champions?dataById=true&api_key=" + key).json()
	# print champList
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
			# print i
			# id = list[i]['championId']
			# champion = requests.get("https://global.api.pvp.net/api/lol/static-data/na/v1.2/champion/" + str(id) + "?api_key=c07d4fd5-82c1-4816-a45c-605b8291daff")
			# print champion.json()['name'], x
			if list[order[i]]['championLevel'] == x:
				# print "yay"
				id = list[order[i]]['championId']
				# champion = requests.get("https://na1.api.riotgames.com/lol/static-data/v3/champions/" + str(id) + "?api_key=c07d4fd5-82c1-4816-a45c-605b8291daff")
				# print id
				# if champion.json().has_key('name'):
				print "\t", champList['data'][str(id)]['name'], list[order[i]]['championPoints']
				i += 1
			else:
				x -= 1
				if x >= lowestMastery:
					print
					print "Mastery", x, "(" + (str)(record[x]) + ")"

# def main():

if not len(sys.argv) == 2:
	print "RuntimeError: Username is required"
else:

	# print len(sys.argv)

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

		# print "Mastery Length:", len(mastery)

		order = []
		record = {}
		recordPoints = {}

		count = 138

		retrieveChampion(mastery, order, record, recordPoints, count)

		printTopChampions(mastery, order, record, recordPoints)

	# NAME = (str)(raw_input("What is your summoners name?\n"))
	# NUMBER = (int)(raw_input("How many of your top champions would you like to view?\n"))

	











