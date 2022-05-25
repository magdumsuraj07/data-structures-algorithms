def canPlacePlayers(positions, nRooms, nPlayers, dist):
    playerPos = positions[0]
    playerCount = 1
    for i in range(1, nRooms):
        if positions[i] - playerPos >= dist:
            playerPos = positions[i]
            playerCount += 1
            if playerCount == nPlayers:
                return True
    return False


def chessTournament(positions, nRooms, nPlayers):
    positions.sort()
    low, high = 1, positions[nRooms - 1] - positions[0]
    res = -1
    while low <= high:
        mid = (low + high) // 2
        if canPlacePlayers(positions, nRooms, nPlayers, mid):
            low = mid + 1
            res = mid
        else:
            high = mid - 1
    return res
