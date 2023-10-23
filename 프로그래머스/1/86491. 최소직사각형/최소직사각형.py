def solution(sizes):
    # For each card, make sure width is always greater than or equal to height
    for i in range(len(sizes)):
        if sizes[i][0] < sizes[i][1]:
            sizes[i][0], sizes[i][1] = sizes[i][1], sizes[i][0]
            
    # Find the maximum width and height among all cards
    max_width = max(card[0] for card in sizes)
    max_height = max(card[1] for card in sizes)
    
    return max_width * max_height