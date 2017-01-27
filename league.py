import requests

def retrieveSummoner(name):
	URL = "https://na.api.pvp.net/api/lol/na/v1.4/summoner/by-name/" + NAME + "?api_key=c07d4fd5-82c1-4816-a45c-605b8291daff"
	me = requests.get(URL).json()
	USERNAME = me[NAME]['name']
	LEVEL = me[NAME]['summonerLevel']
	ID = me[NAME]['id']

	print "Username:", USERNAME
	print "Level:", LEVEL
	print "Identification Code:", ID

	URL3 = "https://na.api.pvp.net/api/lol/na/v2.5/league/by-summoner/" + str(ID) + "/entry?api_key=c07d4fd5-82c1-4816-a45c-605b8291daff"
	rank = requests.get(URL3).json()

	ID = str(ID)

	# print "Length of list:", len(rank[ID])

	# if len(rank[ID] != 1):
	# 	return

	# print len(rank)

	if rank.has_key(ID) is True:
		tier = rank[ID][0]['tier']
		division = rank[ID][0]['entries'][0]['division']
		leaguePoints = rank[ID][0]['entries'][0]['leaguePoints']

		print "Tier:", tier
		print "Division:", division
		print "LP:", leaguePoints
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

def retrieveChampion(list, count):

	if len(list) == 0:
		print "Sorry you haven't earned any mastery points on any champions yet"
		return
	elif count > len(list):
		print "Sorry you haven't played", count, "champions yet"
		print "You have only earned mastery for", len(list), "champions"
		count = len(list)
	print "Your top", count, "champions are:"

	x = 0

	masteries=[]
	mIndex = []

	while x < count:
		placed = False
		index = 0
		while placed == False:
			# print "My index is", index
			# if len(masteries) > 0:
				# print "Top champ is", masteries[0]
			if len(masteries) < index + 1:
				masteries.append(list[x]['championId'])
				mIndex.append(x)
				# print "Champion", x, "is placed here"
				placed = True
			elif list[x]['championLevel'] > list[mIndex[index]]['championLevel'] or list[x]['championPoints'] > list[mIndex[index]]['championPoints']:
				# print "Champion", x, "Mastery Level:", list[x]['championLevel']
				# print "Index", index, "Champion Mastery Level:", list[index]['championLevel']
				# print "Champion", x, "Champion Mastery Level at index", index, "is", list[x]['championLevel'] > list[index]['championLevel']
				# print "Champion", x, "Champion Mastery Points at index", index, "is", list[x]['championPoints'] > list[index]['championPoints']
				dec = len(masteries)
				masteries.append(masteries[dec - 1])
				mIndex.append(mIndex[dec - 1])
				dec -= 1
				while dec > index:
					masteries[dec] = masteries[dec - 1]
					mIndex[dec] = mIndex[dec - 1]
					dec -= 1
				masteries[index] = list[x]['championId']
				mIndex[index] = x
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


	x = 0
	while x < count:
		id = masteries[x]
		# id = list[x]['championId']
		champion = requests.get("https://global.api.pvp.net/api/lol/static-data/na/v1.2/champion/" + str(id) + "?api_key=c07d4fd5-82c1-4816-a45c-605b8291daff")
		# champ = champion.json()
		print champion.json()['name'], "Mastery Lvl:", list[mIndex[x]]['championLevel'], "Champion Pts:", list[mIndex[x]]['championPoints']
		# print x+1
		x += 1
	# print "all done!"
	
	# return champion.json()['name']

# def main():

NAME = (str)(raw_input("What is your summoners name?\n"))
NUMBER = (int)(raw_input("How many of your top champions would you like to view?\n"))
# print str(NUMBER)

# NAME = "ktdesk"

id = retrieveSummoner(NAME)

# print me[NAME]


# NUMBER = 5
URL2 = "https://na.api.pvp.net/championmastery/location/NA1/player/" + id + "/topchampions?count=" + str(NUMBER) + "&api_key=c07d4fd5-82c1-4816-a45c-605b8291daff"
mastery = requests.get(URL2).json()

# CHAMPIONS = [mastery[0][championId], mastery[1][championId], mastery[2][championId], []]

retrieveChampion(mastery, NUMBER)
# print mastery[0]
# print retrieveChampion(mastery[0]['championId'])
# print retrieveChampion(mastery[1]['championId'])
# print retrieveChampion(mastery[2]['championId'])
# print retrieveChampion(mastery[3]['championId'])
# print retrieveChampion(mastery[4]['championId'])