import random

players = [[2, "Keeeru", 600], [0, "GhostofTheWest", 900], [3, "GoldExcellence", 400], [1, "Loki", 500],
           [1, "Pac", 1000],
           [0, "Macklin", 900], [2, "Drako", 650], [4, "Dhopamine", 550], [4, "Kite", 450], [1, "Zeburgerking", 800],
           [3, "Chime", 600], [0, "Strangle", 900], [1, "cash money", 100], [2, "0mnikron", 600], [3, "Architech", 700],
           [4, "Don Lino", 100]]

queue = []
blue = []
red = []
top = []
jg = []
mid = []
adc = []
sup = []
match = []
top_num = 0
jg_num = 0
mid_num = 0
adc_num = 0
sup_num = 0


def top_make(top_list):
    mmr_diff_threshold = 100
    count = 0
    balanced = False
    while not balanced:
        toppers = random.sample(top_list, 2)
        diff1 = toppers[0][2] - toppers[1][2]
        diff2 = toppers[1][2] - toppers[0][2]
        if diff1 < mmr_diff_threshold and diff2 < mmr_diff_threshold:
            blue.append(toppers[1])
            red.append(toppers[0])
            balanced = True
        count += 1
        if count >= 15:
            mmr_diff_threshold += 10
            count = 0


def jg_make(jg_list):
    mmr_diff_threshold = 100
    balanced = False
    count = 0
    while not balanced:
        junglers = random.sample(jg_list, 2)
        diff1 = junglers[0][2] - junglers[1][2]
        diff2 = junglers[1][2] - junglers[0][2]
        if diff1 < mmr_diff_threshold and diff2 < mmr_diff_threshold:
            blue.append(junglers[1])
            red.append(junglers[0])
            balanced = True
        count += 1
        if count >= 15:
            mmr_diff_threshold += 10
            count = 0


def mid_make(mid_list):
    mmr_diff_threshold = 100
    count = 0
    balanced = False
    while not balanced:
        midders = random.sample(mid_list, 2)
        diff1 = midders[0][2] - midders[1][2]
        diff2 = midders[1][2] - midders[0][2]
        if diff1 < mmr_diff_threshold and diff2 < mmr_diff_threshold:
            blue.append(midders[1])
            red.append(midders[0])
            balanced = True
        count += 1
        if count >= 15:
            mmr_diff_threshold += 10


def adc_make(adc_list):
    mmr_diff_threshold = 100
    count = 0
    balanced = False
    while not balanced:
        adcers = random.sample(adc_list, 2)
        diff1 = adcers[0][2] - adcers[1][2]
        diff2 = adcers[1][2] - adcers[0][2]
        if diff1 < mmr_diff_threshold and diff2 < mmr_diff_threshold:
            blue.append(adcers[1])
            red.append(adcers[0])
            balanced = True
        count += 1
        if count >= 15:
            mmr_diff_threshold += 10
            count = 0


def sup_make(sup_list):
    mmr_diff_threshold = 100
    count = 0
    balanced = False
    while not balanced:
        suppers = random.sample(sup_list, 2)
        diff1 = suppers[0][2] - suppers[1][2]
        diff2 = suppers[1][2] - suppers[0][2]
        if diff1 < mmr_diff_threshold and diff2 < mmr_diff_threshold:
            blue.append(suppers[1])
            red.append(suppers[0])
            balanced = True
        count += 1
        if count >= 15:
            mmr_diff_threshold += 10
            count = 0


def matchmake():
    global match
    for player in players:
        if player[0] == 0:
            top.append(player)
        elif player[0] == 1:
            jg.append(player)
        elif player[0] == 2:
            mid.append(player)
        elif player[0] == 3:
            adc.append(player)
        elif player[0] == 4:
            sup.append(player)

    top_make(top)
    jg_make(jg)
    mid_make(mid)
    adc_make(adc)
    sup_make(sup)

    print("Blue Team")
    for blues in blue:
        print(blues[1])
    print("\n")
    print("Red Team")
    for reds in red:
        print(reds[1])


def clear_teams():
    global blue
    global red

    tempmatch = [blue, red]
    match.append(tempmatch)
    blue.clear()
    red.clear()


def queue_up(player, role, mmr):
    global top_num
    global jg_num
    global mid_num
    global adc_num
    global sup_num
    player = []

    for player in players:
        if player[0] == 0:
            top_num += 1
        elif player[0] == 1:
            jg_num += 1
        elif player[0] == 2:
            mid_num += 1
        elif player[0] == 3:
            adc_num += 1
        elif player[0] == 4:
            sup_num += 1

    if top_num >= 3 and jg_num >= 3 and mid_num >= 3 and adc_num >= 3 and sup_num >= 3:
        matchmake()


