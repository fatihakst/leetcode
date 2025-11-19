class Solution(object):
    def matchPlayersAndTrainers(self, players, trainers):
        """
        :type players: List[int]
        :type trainers: List[int]
        :rtype: int
        """
        players.sort()
        trainers.sort()
        j=0
        i=0
        count=0
        while i<len(players) and j<len(trainers):
            if players[i]<=trainers[j]:
                count+=1
                i+=1
                del trainers[j]
                j=0
            else:
                j+=1
        return count

        