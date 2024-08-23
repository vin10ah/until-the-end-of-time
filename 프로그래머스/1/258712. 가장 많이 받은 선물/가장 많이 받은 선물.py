# 두 사람이 선물 주고받은 기록o -> 더 많이 준 사람이 다음 달에 하나 get
# 선물 지수 = 준 선물 수 - 받은 선물 수
# 선물 주고받은 적 없거나 같은 수로 주고받았다면 선물 지수가 높은 사람이 하나 get
# 선물 지수가 같으면 다음 달에 선물 주고받지 않음



def solution(friends, gifts):
	answer = 0
	scores = {name:0 for name in friends}
	records = {name:{name:0 for name in friends} for name in friends}
	get = {name:0 for name in friends}
	combs = []

	# 친구들 조합 구하기
	for i in range(len(friends)-1):
		a = friends[i]
		for b in friends[i+1:]:
			combs.append((a, b))

	for name in friends:
		for record in gifts:
			give, take = record.split()
			if name == give:
				scores[name] += 1
				records[name][take] += 1
			elif name == take:
				scores[name] -= 1

	for a, b in combs:
		a_get = records[b][a]
		b_get = records[a][b]
		a_score = scores[a]
		b_score = scores[b]

		if a_get + b_get == 0 or a_get == b_get:
			if a_score > b_score:
				get[a] += 1
			elif b_score > a_score:
				get[b] += 1
		
		else:
			if a_get < b_get:
				get[a] += 1
			elif b_get < a_get:
				get[b] += 1	

	return max(get.values())