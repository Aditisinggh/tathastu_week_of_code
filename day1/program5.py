player1 = int(input( " Runs of Player 1 : "))
player2 = int(input( " Runs of Player 2 : "))
player3 = int(input( " Runs of Player 3 : "))

sr1 = player1/60
sr2 = player2/60
sr3 = player3/60

print('*'*28 , 'Strike rates of Players' , '*'*27)
print(sr1 , sr2 , sr3 , sep='\t\t\t\t')

score1 = player1 + sr1*60
score2 = player2 + sr2*60
score3 = player3 + sr3*60

print('*'*25 , 'New Scores of Players (120 balls)' , '*'*25)
print(score1 , score2 , score3 , sep='\t\t\t\t')

six1 = player1//6
six2 = player2//6
six3 = player3//6

print('*'*28 , 'Number of sixes ' , '*'*28)
print(six1 , six2 , six3 , sep='\t\t\t\t')

print('*'*70)
