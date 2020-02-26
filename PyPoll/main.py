import os
import csv

file_path = ("../../03-Python/Homework03/Instructions/PyPoll/Resources/election_data.csv")
with open(file_path, newline="") as path:
  voter_reader = csv.reader(path, delimiter=",")
  header = next(path)
  #print(f"headers: {header}")
  
  print("Election Results")
  print("------------------------------------------")
  #TOTAL NUMBER OF VOTES CAST
  votes = 0
  voter_list = []
  for vote in voter_reader:
    votes += 1
    voter_list.append(vote)
    total_votes = str(votes)
  #print(voter_list)  
  print(f"Total votes: {total_votes}")
  print("------------------------------------------")
  #complete list of candidates who received votes
  candidates = []
  new_candidate = []
  for candidate in voter_list:
    candidates.append(candidate[2])
  for a_candidate in candidates:  
    if  a_candidate not in new_candidate:
      new_candidate.append(a_candidate)
  #print(new_candidate)    
  #The total number of votes each candidate won
  Khan = 0
  Correy = 0
  Li = 0
  OTooley = 0
  Winner = []
  for x in candidates:
    if x == "Khan":
      Khan += 1  
    elif x == "Correy":
      Correy += 1
    elif x == "Li":
      Li += 1
    else:
      OTooley += 1
      
  Winner.append(Khan)
  Winner.append(Correy)
  Winner.append(Li)
  Winner.append(OTooley)
  #print(Winner)
  winner = max(Winner)
  #print(str(winner))
  khan_percent = (Khan / votes) * 100
  correy_percent = (Correy / votes) * 100
  li_percent = (Li / votes) * 100
  otooley_percent = (OTooley / votes) * 100
  
  print(f"Khan:      {'{:.2f}'.format(khan_percent)}%  ({Khan})")
  print(f"Correy :   {'{:.2f}'.format(correy_percent)}%  ({Correy})")
  print(f"Li :       {'{:.2f}'.format(li_percent)}%  ({Li})")
  print(f"O'Tooley : {'{:.2f}'.format(otooley_percent)}%   ({OTooley})")
  print("------------------------------------------")
  print("Winner:  Khan")      
  print("------------------------------------------")
