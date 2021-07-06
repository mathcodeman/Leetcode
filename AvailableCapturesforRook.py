class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        
        def findRook(Board):
            for i in range(len(Board)):
                for j in range(len(Board)):
                    if Board[i][j] == "R":
                        return (i,j)
                
        def findRow(Board):
            count = 0
            l,r = col-1 , col+1
            #Search left of the row
            while l >= 0:
                if Board[row][l] == ".":
                    l-=1
                elif Board[row][l] == "p":
                    count+=1
                    break
                elif Board[row][l] == "B":
                    break
            while r <= len(Board)-1:
                if Board[row][r] == ".":
                    r+=1
                elif Board[row][r] == "p":
                    count+=1
                    break
                elif Board[row][r] == "B":
                    break
            return count


        def findCol(Board):
            count = 0
            u,d = row-1,row+1
            while u >= 0:

                if Board[u][col] == ".":
                    u-=1
                elif Board[u][col] == "p":
                    count+=1
                    break
                elif Board[u][col] == "B":
                    break
            while d <= len(Board)-1:
                if Board[d][col] == ".":
                    d+=1
                elif Board[d][col] == "p":
                    count+=1
                    break
                elif Board[d][col] == "B":
                    break
            return count

        
        rc = findRook(board)
        row = rc[0]
        col = rc[1]

        return findRow(board)+findCol(board)