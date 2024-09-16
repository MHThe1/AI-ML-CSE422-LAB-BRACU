import random

def minMax(depth, node, isMaximizer, leaf, alpha, beta):
    if (depth == 5):
        return leaf[node]

    if (isMaximizer):
        maxValue = float('-inf')
        for i in range(2): 
            value = minMax(depth + 1, node * 2 + i, False, leaf, alpha, beta)
            maxValue = max(maxValue, value)
            alpha = max(alpha, value)
            if (beta <= alpha):
                break
        return maxValue

    else:
        minValue = float('inf')
        for i in range(2):  
            value = minMax(depth + 1, node * 2 + i, True, leaf, alpha, beta)
            minValue = min(minValue, value)
            beta = min(beta, value)
            if (beta <= alpha):
                break
        return minValue

def game_winner(startingPlayer):
    leaf = [random.choice([-1, 1]) for _ in range(32)]
    winner = []
    alpha = float('-inf')
    beta = float('inf')
    
    for i in range(3):
        if (startingPlayer == 0):
            isMaximizer = True
        else:
            isMaximizer = False
            
        roundWinner = minMax(0, 0, isMaximizer, leaf, alpha, beta)
        
        if (roundWinner == -1):
            winner.append("Scorpion")
        else:
            winner.append("Sub-Zero")
        
        startingPlayer += 1
        startingPlayer %= 2
    
    print(f"Game Winner: {max(winner)}")
    print("Total Rounds Played: 3")
    for i in range(3):
        print(f"Winner of Round {i+1}: {winner[i]}")

startingPlayer = int(input("Enter starting player number: "))
game_winner(startingPlayer)
