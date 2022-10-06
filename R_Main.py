# Risk, Good luck

import pygame, R_Grid, IM, random

Display_Width = 1500
Display_Height = 750

GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

win = pygame.display.set_mode((Display_Width, Display_Height))

pygame.display.set_caption("Aisa")
clock = pygame.time.Clock()

Pl_Col = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 192, 203), (255, 255, 0)]

pygame.init()

players = 3

Max_Units = 35 - 5 * (players - 3)

Card_Bonus = [4,6,8,10,15,20,25,30,35,40,45,50,55,60]

Card_Track = 0

class Player:
    def __init__(self, Num):
        self.Regions = []
        self.Units = 0
        self.Cards = []
        self.Num = Num
        self.attack = True
        self.defend = True
        self.capped = False

    def Gen_Card(self):
        type = random.randint(0,2)
        if type == 0:
            self.Cards.append("cavalry")
        if type == 1:
            self.Cards.append("cannon")
        else:
            self.Cards.append("infantry")
        font = pygame.font.SysFont("ariel", 40)
        text = font.render(f"New card: {self.Cards[-1]}", True, (255, 255, 255))
        win.blit(text,(1350,200))

    def Cash_Cards(self):
        c_cav = 0
        c_inf = 0
        c_can = 0
        for card in self.Cards:
            if card == "cavalry":
                c_cav += 1
            elif card == "cannon":
                c_can += 1
            elif card == "infantry":
                c_inf += 1
        if c_cav >=3:
            for a in range (3):
                self.Cards.remove("cavalry")
            return True
        elif c_inf >= 3:
            for a in range (3):
                self.Cards.remove("infantry")
            return True
        elif c_can >= 3:
            for a in range (3):
                self.Cards.remove("cannon")
            return True

        elif c_cav >=1 and c_can >=1 and c_inf >= 1:
            self.Cards.remove("cannon")
            self.Cards.remove("infantry")
            self.Cards.remove("cavalry")
            return True

PList = []
for a in range(players):
    P = Player(a + 1)
    PList.append(P)
    #P.Cards = ["cannon","cannon","cannon"]


class Button:
    def __init__(self, text, x, y, colour, action):
        self.text = text
        self.x = x
        self.y = y
        self.colour = colour
        self.width = 150
        self.height = 100
        self.action = action

    def draw(self, win):
        pygame.draw.rect(win, self.colour, (self.x, self.y, self.width, self.height))
        font = pygame.font.SysFont("ariel", 30)
        text = font.render(self.text, True, (255, 255, 255))
        win.blit(text, (self.x + round(self.width / 2) - round(text.get_width() / 2),
                        self.y + round(self.height / 2) - round(text.get_height() / 2)))

    def click(self, pos, arg=None):
        x1, y1 = pos[0], pos[1]
        if self.x <= x1 <= self.x + self.width and self.y <= y1 <= self.y + self.height:
            # print("button true",self.text)
            self.action(arg)

def Bound_Box(grid):
    win.blit(IM.Board, (0, 0))
    for row in grid:
        for Region in row:
            # pygame.draw.rect(win,GREEN,(Region.x,Region.y,Region.w,Region.h),width = 5)
            if not Region.Pl == 0:
                font = pygame.font.SysFont("ariel", 40)
                units = str(Region.units)
                text = font.render(units, True, (Pl_Col[Region.Pl - 1]))
                win.blit(text, (Region.x + round(Region.w / 2) - round(text.get_width() / 2),
                                Region.y + round(Region.h / 2) - round(text.get_height() / 2)))


def R1_Check(grid):
    for row in grid:
        for reg in row:
            if reg.Pl == 0:
                return False
    return True


def R2_Check(PList):
    for p in PList:
        if p.Units < Max_Units:
            return False
    print("Round 3")
    return True


def Show_Vs(current,win,type):#true is vs,false is fortify
    font = pygame.font.SysFont("ariel", 50)
    text1 = font.render(f"{current[0].name}", True, Pl_Col[current[0].Pl - 1])
    if type:
        text2 = font.render("VS", True, Pl_Col[current[0].Pl - 1])
    else:
        text2 = font.render("To", True, Pl_Col[current[0].Pl - 1])

    win.blit(text1, (40, 220))
    win.blit(text2, (40 + round(text1.get_width()) // 2, 250))
    if current[1]:
        text3 = font.render(f"{current[1].name}", True, Pl_Col[current[1].Pl - 1])
        win.blit(text3, (40, 280))


def Show_PL(player, win, grid):
    Add_Num = calc_deploy(player, grid)
    font = pygame.font.SysFont("ariel", 150)
    text = font.render(f"Player {player.Num} Deploy, {str(Add_Num)} units", True, (Pl_Col[player.Num - 1]))
    win.blit(text,
             (Display_Width // 2 - round(text.get_width() // 2), Display_Height // 2 - round(text.get_height() // 2)))
    pygame.display.update()
    print("show pl")
    pygame.time.delay(1000)
    print("end")


def Show_Fort(player, win, grid):
    font = pygame.font.SysFont("ariel", 150)
    text = font.render(f"Player {player.Num} fortify", True, (Pl_Col[player.Num - 1]))
    win.blit(text,
             (Display_Width // 2 - round(text.get_width() // 2), Display_Height // 2 - round(text.get_height() // 2)))
    pygame.display.update()
    pygame.time.delay(1000)


def calc_deploy(player, grid):
    player.capped = True
    R_Count = 0
    Bonus = [5, 2, 6, 3, 7, 2]
    for row in grid:
        for reg in row:
            if reg.Pl == player.Num:
                R_Count += 1
    A_Units = R_Count // 3
    # print(R_Count)

    for row in grid:  # From first to last arrays, NA,SA,Eur,Afr,Asia,Aus
        Cont = False
        for reg in row:
            if reg.Pl == player.Num and Cont == False:
                pass
            else:
                Cont = True
        if Cont == False:
            A_Units += Bonus[grid.index(row)]

    return A_Units

def Card_Cash(player):
    global Card_Track,Card_Bonus
    Check = player.Cash_Cards()
    if Check:
        Card_Track += 1
        font = pygame.font.SysFont("ariel", 60)
        text = font.render(f"Bonus units {str(Card_Bonus[Card_Track])}", True, Pl_Col[player.Num - 1])
        win.blit(text,(Display_Width // 2 - round(text.get_width() // 2),Display_Height // 2 - round(text.get_height() // 2)))
        pygame.display.update()
        pygame.time.delay(1000)

        return Card_Bonus[Card_Track]
    else:
        return 0

def show_cards(player):#show cards and then done, just use text
    deck = ""
    for card in player.Cards:
        deck = deck + "," + card
    font = pygame.font.SysFont("ariel", 40)
    text = font.render(f"Cards:{deck}",True, Pl_Col[player.Num - 1])
    win.blit(text,(Display_Width // 2 - round(text.get_width() // 2),Display_Height // 2 - round(text.get_height() // 2)))
    pygame.display.update()
    pygame.time.delay(1000)


def Deploy_Phase(player, grid):  # player is obj
    print("Round Deploy")
    New_Units = calc_deploy(player, grid)
    Count = 0
    run = True
    Cards = Button("Cards",1350, 200, RED,Card_Cash)
    Show_Cards = Button("Show Cards",1350,500,BLUE,show_cards)
    while run:
        pos = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if click[0]:
                Show_Cards.click(pos,player)
                if Cards.x <= pos[0] <= Cards.x + Cards.width and Cards.y <= pos[1] <= Cards.y + Cards.height:
                    New_Units += Card_Cash(player)
                for row in grid:
                    for reg in row:
                        if reg.Click_Region(pos) and reg.Pl == player.Num:
                            # print(reg.name)
                            reg.units += 1
                            Count += 1
                            if Count == New_Units:
                                run = False
        Bound_Box(grid)
        Cards.draw(win)
        Show_Cards.draw(win)
        pygame.display.update()
        clock.tick(30)


def Att_Mode_Change(player):
    if player.attack == True:
        player.attack = False
    else:
        player.attack = True


def Def_Mode_Change(player):
    if player.defend == True:
        player.defend = False
    else:
        player.defend = True
    print(player.defend)


def Show_Pl_Mode(player1, player2):
    font = pygame.font.SysFont("ariel", 40)
    if player1.attack == True:
        text1 = font.render("Max", True, RED)
    else:
        text1 = font.render("Lesser", True, RED)

    if player2.defend == True:
        text2 = font.render("MAX", True, BLUE)
    else:
        text2 = font.render("Lesser", True, BLUE)

    win.blit(text1, (115, 650))
    win.blit(text2, (265, 650))
    pygame.display.update()


def End_Attack(foo):
    print("end attack")
    foo = True
    return foo


def Fort_Phase(win, grid, player):
    print("fort phase")
    run = True
    current = [None, None]
    Show_Fort(PList[player - 1], win, grid)
    show = False

    while run:
        pos = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if click[0]:
                for row in grid:
                    for reg in row:
                        if current[0] and current[1] and reg.Click_Region(pos) and reg.name == current[1].name and current[0].units > 1:
                            current[0].units -= 1
                            current[1].units += 1

                        elif current[0] and current[1] and reg.Click_Region(pos) and reg.name != current[1].name:
                            if PList[player-1].capped == True:
                                PList[player - 1].Gen_Card()
                            run = False

                        elif reg.Click_Region(pos) and reg.Pl == player and current[0] is None:
                            current[0] = reg
                            show = True

                        elif reg.Click_Region(pos) and current[0] and reg.Pl == player:
                            current[1] = reg
                            show = True
        Bound_Box(grid)
        if show:
            Show_Vs(current,win,False)
        pygame.display.update()
        clock.tick(10)


def Attack_Phase(win, grid, current, PList):
    run = True
    Att_Change = Button("Attack Mode", 40, 500, RED, Att_Mode_Change)
    Def_Change = Button("Defence mode", 190, 500, BLUE, Def_Mode_Change)
    Att_Reg = Button("Attack", 1350, 500, RED, Attack)
    End_Atr = Button("End Attack", 1350, 200, RED, End_Attack)
    Show_Pl_Mode(PList[current[0].Pl - 1], PList[current[1].Pl - 1])
    while run:
        # print("Attack phase")
        pos = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        Att_Change.draw(win)
        Def_Change.draw(win)
        Att_Reg.draw(win)
        End_Atr.draw(win)
        if click[0]:
            Att_Change.click(pos, PList[current[0].Pl - 1])
            Def_Change.click(pos, PList[current[1].Pl - 1])
            Att_Reg.click(pos, (current, grid))
            Bound_Box(grid)
            Show_Pl_Mode(PList[current[0].Pl - 1], PList[current[1].Pl - 1])  # -

            if End_Atr.x <= pos[0] <= End_Atr.x + End_Atr.width and End_Atr.y <= pos[1] <= End_Atr.y + End_Atr.height:
                run = False
        pygame.display.update()
        clock.tick(20)


def Att_Calc(PList, current):
    if PList[current[0].Pl - 1].attack == True:
        Max_Att = current[0].units - 1
    else:
        Max_Att = current[0].units - 2

    if PList[current[0].Pl - 1].attack == True and current[1].units >= 2:
        Max_Def = 2
    else:
        Max_Def = 1
    if Max_Att > 3:
        Max_Att = 3
    return [Max_Att, Max_Def]


def Rand_Nums(num):
    arr = []
    for i in range(num):
        a = random.randint(1, 6)
        arr.append(a)
    return arr


def Attack(tup):  # dice animations and change of units between region
    current = tup[0]
    grid = tup[1]
    Wins = [0, 0]  # attacker first
    Max_Arr = Att_Calc(PList, current)
    # print(Max_Arr)
    Att_Arr = Rand_Nums(Max_Arr[0])
    Def_Arr = Rand_Nums(Max_Arr[1])
    Att_Arr.sort(reverse=True)
    Def_Arr.sort(reverse=True)

    for i in range(len(Def_Arr)):
        if Att_Arr[i] <= Def_Arr[i]:
            Wins[1] += 1
        else:
            Wins[0] += 1
    current[0].units -= Wins[1]
    current[1].units -= Wins[0]
    Show_Dice(win, Att_Arr, Def_Arr)
    if current[1].units <= 0:
        current[1].Pl = current[0].Pl
        current[1].units = 1
        Cap_deploy(current, grid)
    # print(Att_Arr)


def Cap_deploy(current, grid):
    run = True
    while run:
        pos = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if click[0]:
                for row in grid:
                    for reg in row:
                        if reg.Click_Region(pos) and reg.name == current[1].name and current[0].units > 1:
                            current[0].units -= 1
                            current[1].units += 1
                        elif reg.Click_Region(pos) and reg.name != current[1].name:
                            run = False

        Bound_Box(grid)
        pygame.display.update()
        clock.tick(30)


def Show_Dice(win, Att_Arr, Def_Arr):
    for i in range(len(Att_Arr)):
        win.blit(IM.Die_Arr[Att_Arr[i] - 1], (585, (100 + (150 * i))))

    for i in range(len(Def_Arr)):
        win.blit(IM.Die_Arr[Def_Arr[i] - 1], (715, (100 + (150 * i))))

    pygame.display.update()
    pygame.time.delay(2000)

    for i in range(len(Def_Arr)):
        if Def_Arr[i] >= Att_Arr[i]:
            win.blit(IM.Boom, (585, (100 + (150 * i))))
        else:
            win.blit(IM.Boom, (715, (100 + (150 * i))))
    pygame.display.update()
    pygame.time.delay(1000)


def Main_Game(win, grid):
    global players         # risk cards show and fix the deploy
    print("next round")
    player = 1
    run = True
    Bound_Box(grid)
    current = [None, None]
    show = False
    Deployed = False
    End_Turn = Button("End", 1350, 500, BLUE, End_Attack)
    while run:
        End_Turn.draw(win)
        pos = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if click[0]:
                for row in grid:
                    for reg in row:
                        if reg.Click_Region(pos) and reg.Pl == player and current[0] is None:
                            current[0] = reg
                            show = True
                        elif reg.Click_Region(pos) and current[0] and reg.Pl != player and current[0].name in reg.adj:
                            current[1] = reg
                            show = True
                        elif reg.Click_Region(pos) and current[0] and current[0].name not in reg.adj:
                            current = [None, None]
                            show = False
                            Bound_Box(grid)
                if End_Turn.x <= pos[0] <= End_Turn.x + End_Turn.width and End_Turn.y <= pos[
                    1] <= End_Turn.y + End_Turn.height:
                    Fort_Phase(win, grid, player)
                    if player == players:
                        player = 1
                    else:
                        player += 1
                    Deployed = False
                    Show_PL(PList[player - 1], win, grid)
        if show:
            Show_Vs(current, win,True)

        if Deployed == False:
            Deploy_Phase(PList[player - 1], grid)
            Deployed = True

        if current[0] and current[1]:
            Attack_Phase(win, grid, current, PList)
            current = [None, None]
            show = False

        pygame.display.update()
        clock.tick(30)


def Pre_Game(win, players):
    player = 1
    R2 = True  # Change back to False for finished game
    R3 = False
    run = True
    grid = R_Grid.Find_Grid()
    win.blit(IM.Board, (0, 0))
    Bound_Box(grid)

    while run:
        pos = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False
                quit()

            if click[0]:
                for row in grid:
                    for reg in row:
                        if reg.Click_Region(pos) and reg.Pl == 0:
                            reg.Pl = player
                            PList[player - 1].Units += 1
                            if player == players:
                                player = 1
                            else:
                                player += 1
                            R2 = R1_Check(grid)
                            Bound_Box(grid)

                        elif reg.Click_Region(pos) and R2 and PList[reg.Pl - 1].Units <= Max_Units:
                            # print("add units")
                            player = reg.Pl
                            reg.units += 1
                            PList[player - 1].Units += 1
                            # print(f"{player},{PList[player-1].Units}")
                            Bound_Box(grid)
                            R3 = R2_Check(PList)
                            if R3:
                                Show_PL(PList[0], win, grid)
                                run = False
                                Main_Game(win, grid)

        pygame.display.update()
        clock.tick(60)


Pre_Game(win, players)
