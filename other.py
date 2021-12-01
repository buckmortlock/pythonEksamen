#01.12.2021
def draw(river1,river2,river3):
    river1_draw = "#"*10*river1
    river2_draw = "#"*10*river2
    river3_draw = "#"*10*river3
    spacer_len = 120-((river1*10)+(river2*10)+(river3*10))

    return river1_draw, river2_draw, river3_draw, spacer_len

river1_draw, river2_draw, river3_draw, spacer_len = draw(1,2,2)

for i in range(4):
    print("#"*120)
spacer = int(spacer_len/2)

for i in range(4):
    print(river1_draw + spacer*" " + river2_draw + spacer*" " + river3_draw)

