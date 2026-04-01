votes = {} 
candidates = ["A", "B", "A", "C", "B", "A"] 
for c in candidates: 
  votes[c] = votes.get(c, 0) + 1 
print(votes)
