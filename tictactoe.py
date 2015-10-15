game = [
    [1,0,1],
    [0,1,0],
    [0,0,1],
]

def check_victory(game):
    results = [
        True, #diag right
        True, #diag left
        True, #rows
        True  #columns
    ]

    # for x in xrange(1, len(game)):
    #     if results[0] and game[x][x] != game[x-1][x-1]:
    #         results[0] = False
    #     if results[1] and game[len(game)-1-x][x] != game[len(game)-2-x][x-1]:
    #         results[1] = False
    #     if results[2] and game[x-1][0] != row_results[x][0]:
    #         results[2] = False
    #     if results[3] and row_results[x-1] != row_results[x]:
    #         results[3] = False
    #
    # return reduce(lambda x,y: x or y, results)

print check_victory(game)
