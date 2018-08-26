# https://leetcode.com/articles/the-maze/
# Dynamic Programming
import numpy as np

class Solution():
    def moveNext(self, maze, ball, dest, stopped, nextLevelPos, new_pos):
        m = len(maze)
        n = len(maze[0])
        move = ball.copy()
        run = True
        while run:
            move_copy = move
            move = new_pos(move)
            if move[0] >= m or move[0] <0 or move[1] >= n or move[1]<0 or maze[move[0]][move[1]] == 1:
                move = move_copy
                run = False
        if move[0] != ball[0] or move[1] != ball[1]:
            if stopped[move[0]][move[1]] == 0:
                stopped[move[0]][move[1]] = 1
                nextLevelPos.append(move)
                print(move[0], move[1])
                if dest[0] == move[0] and dest[1] == move[1]:
                    print('hit dest')
                    return True        
        return False

    def findShortestWay(self, maze, ball, dest):
        """
        :type maze: List[List[int]]
        :type ball: List[int]
        :type dest: List[int]
        :rtype: bool
        """
        m = len(maze)
        n = len(maze[0])
        stopped = np.zeros((m,n)).tolist() 

        currentLevelPos = []
        currentLevelPos.append(ball)
        nextLevelPos = [] # [[x,y], [x,y]...]

        while len(currentLevelPos)>0:
            # print('loop1')
            for pos in currentLevelPos:
                if self.moveNext(maze, pos, dest, stopped, nextLevelPos, lambda move: [move[0]+1, move[1]]):
                    return True
                if self.moveNext(maze, pos, dest, stopped, nextLevelPos, lambda move: [move[0]-1, move[1]]):
                    return True
                if self.moveNext(maze, pos, dest, stopped, nextLevelPos, lambda move: [move[0], move[1]+1]):
                    return True
                if self.moveNext(maze, pos, dest, stopped, nextLevelPos, lambda move: [move[0], move[1]-1]):
                    return True
            currentLevelPos = nextLevelPos
            nextLevelPos = []
            # print('loop2')
        print('not hit dest')
        return False
def test_func():
    test = Solution()
    a = np.array([[0, 0, 1, 0, 0],
                  [0, 0, 0, 0, 0],
                  [0, 0, 0, 1, 0],
                  [1, 1, 0, 1, 1],
                  [0, 0, 0, 0, 0]])
    b = a.tolist()
    assert test.findShortestWay(b, [0,4], [4,4]) == True    
    assert test.findShortestWay(b, [0,4], [3,2]) == False
