class SnakesLadders():
    def __init__(self):
        self.snakein=[16,46,49,62,64,74,89,92,95,99]
        self.snakeout=[6,25,11,19,60,53,68,88,75,80]
        self.ladderin=[2,7,8,15,21,28,36,51,71,78,87]
        self.ladderout=[38,14,31,26,42,84,44,67,91,98,94]
        self.snake = { self.snakein[i]:self.snakeout[i] for i in range(len(self.snakeout))}
        self.ladder = { self.ladderin[i]:self.ladderout[i] for i in range(len(self.ladderout))}
        self.step=[0,0]
        self.player=1
        self.won=False
    def play(self, die1, die2):
        if self.won:return 'Game over!'
        die=die1+die2
        if self.step[self.player-1] +die<=100:
            self.step[self.player-1] += die
            if self.step[self.player-1] ==100:
                self.won = True    
        else:
            self.step[self.player-1] =100-self.step[self.player-1] - die+100
        
        if self.step[self.player-1] in self.snakein:
            self.step[self.player-1]=self.snake[self.step[self.player-1]]
        if self.step[self.player-1] in self.ladderin:
            self.step[self.player-1]=self.ladder[self.step[self.player-1]]
        if self.won:
            message='Player '+str(self.player)+' Wins!'
        else:
            message='Player '+str(self.player)+' is on square '+str(self.step[self.player-1])
        if die1!=die2 and self.player==1:self.player=2
        elif die1!=die2 and self.player==2:self.player=1
        return message