def players_as_dictionaries(squads_list):
  playalist = []
  for _ in range(len(squads_list)):
    playalist.append({})
  for i in range(len(squads_list)):
    playalist[i]['number']=squads_list[i][0]
    playalist[i]['position']=squads_list[i][1]
    playalist[i]['name']=squads_list[i][2]
    playalist[i]['date_of_birth']=squads_list[i][3]
    playalist[i]['caps']=squads_list[i][4]
    playalist[i]['club']=squads_list[i][5]
    playalist[i]['country']=squads_list[i][6]
    playalist[i]['club_country']=squads_list[i][7]
    playalist[i]['year']=squads_list[i][8]
  return playalist
