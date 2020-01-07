import pygame  # The main module!
import time  # To delay the execution of a certain code, as will be explained wherever used!
import random  # To generate a random number, substituting the actual dice!
import pygame.mixer  # For sound effects
import ast

import sqlite3

conn = sqlite3.connect('NounsMissionsFeelings.db')
c = conn.cursor()  # The database will be saved in the location where your 'py' file is saved

# Create table - NOUNS
c.execute('''CREATE TABLE IF NOT EXISTS NOUNS
             ([generated_id] INTEGER PRIMARY KEY,[Noun_Name] text)''')

# Create table - FEELINFS
c.execute('''CREATE TABLE IF NOT EXISTS FEELINGS
             ([generated_id] INTEGER PRIMARY KEY,[Feeling_Name] text)''')

# Create table - MISSIONS
c.execute('''CREATE TABLE IF NOT EXISTS MISSIONS
             ([generated_id] INTEGER PRIMARY KEY,[Mission_Name] text)''')

conn.commit()

conn1 = sqlite3.connect('Users.db')
c = conn1.cursor()  # The database will be saved in the location where your 'py' file is saved

# Create table - PLAYERS
c.execute('''CREATE TABLE IF NOT EXISTS PLAYERS
             ([Player_Name] text,[Player_Age] INTEGER)''')

# Create table - ADMINS
c.execute('''CREATE TABLE IF NOT EXISTS ADMINS
             ([generated_id] INTEGER PRIMARY KEY,[Admin_Password] text)''')

# Create table - GUIDERS
c.execute('''CREATE TABLE IF NOT EXISTS GUIDERS
             ([generated_id] INTEGER PRIMARY KEY,[Guider_Password] text)''')

conn1.commit()
conn2 = sqlite3.connect('Tokens.db')
c = conn2.cursor()  # The database will be saved in the location where your 'py' file is saved

# Create table - TOKENS
c.execute('''CREATE TABLE IF NOT EXISTS TOKENS
             ([generated_id] INTEGER PRIMARY KEY,[Color_Name] text,[RED] INTEGER,[GREEN] INTEGER,[BLUE] INTEGER)''')


conn2.commit()

pygame.init()  # pygame initialisation
pygame.font.init()  # font initialisation
pygame.mixer.init()  # sounds initialisation

# Colors according to RGB conventions, which is compatible with pygame
white = (255, 255, 255)
red = (255, 0, 0)
lightred = (100, 0, 0)
blue = (0, 50, 100)
darkblue = (0, 0, 255)
green = (0, 255, 0)
yellow = (250, 150, 0)
lightyellow = (200, 150, 0)
black = (0, 0, 0)
lightgreen = (34, 177, 76)
lightblue = (205, 230, 208)
violet = (0, 0, 128)
cream = (255, 228, 181)

# Dimensions, and title of the main screen.
display_width = 1300
display_height = 710
gamedisplay = pygame.display.set_mode((display_width, display_height))  # Screen Dimension
pygame.display.set_caption('MONOFEEL')  # Title

# --- ADD TOOLS FOR PLAYERS
# Dimensions of marbles for both the players
x1 = 1050
y1 = 585
x2 = 1030
y2 = 585

# Fonts initialisation
font = pygame.font.Font(None, 25)
verysmallfont = pygame.font.SysFont("comicsansms", 15)
smallfont = pygame.font.SysFont("comicsansms", 25)
medfont = pygame.font.SysFont("comicsansms", 50)
largefont = pygame.font.SysFont("comicsansms", 80)


# Function which helps to print message on the screen
def message_to_screen(msg, color):
    screen_text = font.render(msg, True, color)
    gamedisplay.blit(screen_text, [display_width / 2, display_height / 2])


# Dice function which generates a random number between 1 to 6
a = 0


def dice():
    b = 0
    global a
    a = random.randint(1, 6)
    b = b + a
    if (b > 22):
        b = b - 22  # Since 22 blocks in our board, one lap completion will result in a decrease of 22
    # print b
    return b


# Used in the main game loop, helps to switch between chances of different players
def alternate():
    global alt
    alt = not alt
    return alt


alt = True  # The first call to alternate will return False (0)

initial_cost1 = 5  # number of nouns


def onFeeling1(db_file):
    conn = sqlite3.connect(db_file)
    cur = conn.cursor()
    cur.execute("SELECT * FROM FEELINGS")
    rows = cur.fetchall()
    feelingRow = random.choice(rows)
    feeling = feelingRow[1]
    display_surface = pygame.display.set_mode((200, 200))
    text = font.render("feeling:    " + feeling, True, black, white)
    textRect = text.get_rect()
    textRect.center = (100, 100)
    flag = True
    while flag:
        display_surface.fill(white)
        display_surface.blit(text, textRect)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

                # Draws the surface object to the screen.
            pygame.display.update()

def fiveNounsStart(db_file):
    nouns=[]
    for i in range(5):
        conn = sqlite3.connect(db_file)
        cur = conn.cursor()
        cur.execute("SELECT * FROM NOUNS")
        rows = cur.fetchall()
        nounRow = random.choice(rows)
        nouns.append(nounRow[1])
    assert (len(nouns) == 5)
    return nouns

def passwordsAdmin(db_file):
    conn = sqlite3.connect(db_file)
    cur = conn.cursor()
    cur.execute("SELECT distinct Admin_Password FROM ADMINS")
    rows = cur.fetchall()
    return rows

def passwordsOb(db_file):
    conn = sqlite3.connect(db_file)
    cur = conn.cursor()
    cur.execute("SELECT distinct Guider_Password FROM GUIDERS")
    rows = cur.fetchall()
    return rows

def drawFive(nouns,x,y):
    all_rects = []
    for noun in nouns:
        rect=Rect(noun,white,x,y)
        all_rects.append(rect)
        rect.Draw()
        nounText = font.render(noun, 1, black)
        gamedisplay.blit(nounText, [x,y])
        y+=60



def onMission1(db_file):
    conn = sqlite3.connect(db_file)
    cur = conn.cursor()
    cur.execute("SELECT * FROM MISSIONS")
    rows = cur.fetchall()
    missionRow = random.choice(rows)
    mission = missionRow[1]
    display_surface = pygame.display.set_mode((400, 400))
    text = font.render("mission:    " + mission, True, black, white)
    textRect = text.get_rect()
    textRect.center = (200, 200)
    for i in range(0, 1):
        display_surface.fill(white)
        display_surface.blit(text, textRect)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

                # Draws the surface object to the screen.
            pygame.display.update()
        time.sleep(1)
    gamedisplay = pygame.display.set_mode((display_width, display_height))  # Screen Dimension
    gameloop()


def amountp1():
    global x1
    global y1
    global initial_cost1
    """if (x1 < 341 and y1 < 610 and y1 > 500):
        initial_cost1 -= 0  # Start
    elif (x1 < 341 and y1 < 500 and y1 > 415):
        initial_cost1 -= 250
    elif (x1 < 341 and y1 < 415 and y1 > 321):
        initial_cost1 -= 500
    elif (x1 < 341 and y1 < 321 and y1 > 240):
        initial_cost1 += 700  # Chance
    elif (x1 < 341 and y1 < 240 and y1 > 159):
        initial_cost1 -= 2250
    elif (x1 < 341 and y1 < 159 and y1 > 53):
        initial_cost1 -= 1000  # Jail

    elif (y1 < 159 and x1 < 487 and x1 > 341):
        initial_cost1 -= 1250
    elif (y1 < 159 and x1 < 621 and x1 > 487):
        initial_cost1 -= 500
    elif (y1 < 159 and x1 < 725 and x1 > 621):
        initial_cost1 -= 1000  # Community chest!
    elif (y1 < 159 and x1 < 852 and x1 > 725):
        initial_cost1 -= 1750
    elif (y1 < 159 and x1 < 972 and x1 > 852):
        initial_cost1 -= 750
    elif (y1 < 159 and x1 < 1095 and x1 > 972):
        initial_cost1 -= 0  # Free ride!

    elif (x1 > 972 and y1 < 253 and y1 > 159):
        initial_cost1 -= 750
    elif (x1 > 972 and y1 < 327 and y1 > 253):
        initial_cost1 -= 500  # Community chest
    elif (x1 > 972 and y1 < 423 and y1 > 327):
        initial_cost1 -= 250
    elif (x1 > 972 and y1 < 500 and y1 > 423):
        initial_cost1 -= 1250
    elif (x1 > 972 and y1 < 610 and y1 > 500):
        initial_cost1 -= 1000  # Go to jail

    elif (y1 > 500 and x1 < 972 and y1 > 854):
        initial_cost1 -= 2500
    elif (y1 > 500 and x1 < 854 and y1 > 729):
        initial_cost1 += 1500  # Chance
    elif (y1 > 500 and x1 < 729 and y1 > 621):
        initial_cost1 -= 1500
    elif (y1 > 500 and x1 < 621 and y1 > 486):
        initial_cost1 -= 750
    elif (y1 > 500 and x1 < 486 and y1 > 341):
        initial_cost1 -= 500"""
    return initial_cost1


# Same for player 2
initial_cost2 = 5


def amountp2():
    global x2
    global y2
    global initial_cost2
    """if (x2 < 341 and y2 < 610 and y2 > 500):
        initial_cost2 -= 0  # Start
    elif (x2 < 341 and y2 < 500 and y2 > 415):
        initial_cost2 -= 250
    elif (x2 < 341 and y2 < 415 and y2 > 321):
        initial_cost2 -= 500
    elif (x2 < 341 and y2 < 321 and y2 > 240):
        initial_cost2 += 700  # Chance
    elif (x2 < 341 and y2 < 240 and y2 > 159):
        initial_cost2 -= 2250
    elif (x2 < 341 and y2 < 159 and y2 > 53):
        initial_cost2 -= 1000  # Jail

    elif (y2 < 159 and x2 < 487 and x2 > 341):
        initial_cost2 -= 1250
    elif (y2 < 159 and x2 < 621 and x2 > 487):
        initial_cost2 -= 500
    elif (y2 < 159 and x2 < 725 and x2 > 621):
        initial_cost2 -= 1000  # Community chest!
    elif (y2 < 159 and x2 < 852 and x2 > 725):
        initial_cost2 -= 1750
    elif (y2 < 159 and x2 < 972 and x2 > 852):
        initial_cost2 -= 750
    elif (y2 < 159 and x2 < 1095 and x2 > 972):
        initial_cost2 -= 0  # Free ride!

    elif (x2 > 972 and y2 < 253 and y2 > 159):
        initial_cost2 -= 750
    elif (x2 > 972 and y2 < 327 and y2 > 253):
        initial_cost2 -= 500  # Community chest
    elif (x2 > 972 and y2 < 423 and y2 > 327):
        initial_cost2 -= 250
    elif (x2 > 972 and y2 < 500 and y2 > 423):
        initial_cost2 -= 1250
    elif (x2 > 972 and y2 < 610 and y2 > 500):
        initial_cost2 -= 1000  # Go to jail

    elif (y2 > 500 and x2 < 972 and y2 > 854):
        initial_cost2 -= 2500
    elif (y2 > 500 and x2 < 854 and y2 > 729):
        initial_cost2 += 1500  # Chance
    elif (y2 > 500 and x2 < 729 and y2 > 621):
        initial_cost2 -= 1500
    elif (y2 > 500 and x2 < 621 and y2 > 486):
        initial_cost2 -= 750
    elif (y2 > 500 and x2 < 486 and y2 > 341):
        initial_cost2 -= 500"""
    return initial_cost2


# The side function responsible for game controls. i.e. the INSTRUCTION button as well as the quit button!
def game_controls():
    gcont = True
    pygame.mixer.music.stop()
    while gcont:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gamedisplay.fill(cream)
        background = pygame.image.load('logo.jpg')
        gamedisplay.blit(background, (450, 0))
        # using the defined text_to_button function in order to produce text to the screen
        text_to_button("INSTRUCTIONS", blue, 630, 125, 50, 100)
        text_to_button2(
            "1. The game begins with player '1' rolling the dice. The marble moves the respective number of blocks ahead!",
            black, 628, 220, 10, 10)
        text_to_button2(
            "2. Once on a block, the player need to do what the block said - feeling, mission or drop a noun).",
            black, 628, 250, 10, 10)
        text_to_button2(
            "3. If a player lands on a feeling - he need to tell a story with 1 or 2 nouns that he has - that fit to the feeling",
            black, 628, 280, 10, 10)
        text_to_button2("4. Player who finishes all his nouns - wins.", black, 628, 310, 10, 10)
        text_to_button2(
            "   5. if a player lands on a mission - he needs to do it - or take 2 more nouns.",
            black, 628, 340, 10, 10)
        text_to_button2(
            "  6. if a player lands on drop a card - he can choose which noun he will drop .",
            black, 628, 370, 10, 10)
        text_to_button2(
            "  7. when the player tell a story, the other players need to mark if the story fits or not .",
            black, 628, 400, 10, 10)
        button("back", 300, 600, 150, 40, darkblue, blue, action="back")
        button("quit", 900, 600, 150, 40, lightgreen, green, action="quit")
        pygame.display.update()


class Rect():
    def __init__(self, name, color, x, y):
        self.rect = pygame.Rect(50, 50, 50, 50)
        self.rect.x = x
        self.rect.y = y
        self.name = name
        self.color = color

    def Draw(self):
        pygame.draw.rect(gamedisplay, (self.color), self.rect)

def login(user):
    background = pygame.image.load('logo.jpg')
    pygame.mixer.music.stop()
    input_box = pygame.Rect(570, 300, 140, 32)
    color_inactive = pygame.Color('blue')
    color_active = pygame.Color('black')
    color = color_inactive
    active = False
    text = ''
    done = False

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                # If the user clicked on the input_box rect.
                if input_box.collidepoint(event.pos):
                    # Toggle the active variable.
                    active = not active
                else:
                    active = False
                # Change the current color of the input box.
                color = color_active if active else color_inactive
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        text = ''
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode

        gamedisplay.fill(cream)
        background = pygame.image.load('logo.jpg')
        gamedisplay.blit(background, (450, 0))
        # Render the current text.
        txt_surface = font.render(text, True, color)
        # Resize the box if the text is too long.
        width = max(200, txt_surface.get_width() + 10)
        input_box.w = width
        text_to_button2("PASSWORD: ", black, 480, 310, 10, 10)
        # Blit the text.
        gamedisplay.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
        # Blit the input_box rect.
        pygame.draw.rect(gamedisplay, color, input_box, 2)

        button("back", 300, 600, 150, 40, darkblue, blue, action="back")
        button("play", 600, 600, 150, 40, lightgreen, green, action="play")
        button("quit", 900, 600, 150, 40, lightgreen, green, action="quit")
        pygame.display.update()
        if user=='a':
            pwds=passwordsAdmin('USERS.db')
            for i in range(len(pwds)):
                if(text == pwds[i][0]):
                    admin_screen()
        else:
            pwds = passwordsOb('USERS.db')
            for i in range(len(pwds)):
                if (text == pwds[i][0]):
                    ob_screen()

def ob_screen():
    print ("ob_screen")

def admin_screen():
    pygame.mixer.music.stop()
    cur=(0,0)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                cur = pygame.mouse.get_pos()
        gamedisplay.fill(cream)
        background = pygame.image.load('logo.jpg')
        gamedisplay.blit(background, (450, 0))
        # using the defined text_to_button function in order to produce text to the screen
        button("Nouns", 600, 190, 100, 40,white,lightyellow,action="nouns")
        button("Feelings",  600, 250, 100, 40,white,lightyellow, action="feelings")
        button("Missions",  600, 310, 100, 40,white,lightyellow, action="missions")
        button("Players",  600, 370, 100, 40,white,lightyellow, action="players")
        button("Tokens", 600, 430, 100, 40,white,lightyellow, action="tokens")
        button("back", 300, 600, 150, 40, darkblue, blue, action="back")
        button("play", 600, 600, 150, 40, lightgreen, green, action="play")
        button("quit", 900, 600, 150, 40, lightgreen, green, action="quit")
        pygame.display.update()

def wordsAdmin(db_file,com,str1,str2):
    input_box = pygame.Rect(600, 600, 140, 32)
    color_inactive = pygame.Color('blue')
    color_active = pygame.Color('black')
    color = color_inactive
    active = False
    text = ''
    word=''
    gcont = True
    pygame.mixer.music.stop()
    while gcont:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos):
                    # Toggle the active variable.
                    active = not active
                else:
                    active = False
            color = color_active if active else color_inactive
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    elif (event.key!=pygame.K_RETURN):
                        text += event.unicode
                    else:
                        word = text
                        text=''
        gamedisplay.fill(cream)
        background = pygame.image.load('logo.jpg')
        gamedisplay.blit(background, (450, 0))
        txt_surface = font.render(text, True, color)
        # Resize the box if the text is too long.
        width = max(200, txt_surface.get_width() + 10)
        input_box.w = width
        # Blit the text.
        gamedisplay.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
        # Blit the input_box rect.
        pygame.draw.rect(gamedisplay, color, input_box, 2)
        conn = sqlite3.connect(db_file)
        cur = conn.cursor()
        cur.execute(com)
        rows = cur.fetchall()
        all_nouns=[]
        x, y = 400, 180
        for i in rows:
            all_nouns.append(i[0])
        for noun in all_nouns:
            text_to_button2(noun, black, x, y, 50, 10)
            y += 40
            if (y>500):
                x = x+220
                y=180
        if word in all_nouns:
            cur.execute(str1 + word + "'")
            word=''
        else:
            cur.execute(str2+word+"')")
            word=''
        conn.commit()
        button("back", 300, 600, 150, 40, darkblue, blue, action="backAd")
        button("quit", 900, 600, 150, 40, lightgreen, green, action="quit")
        pygame.display.update()

def playersAdmin(db_file):
    input_boxName = pygame.Rect(600, 550, 140, 32)
    input_boxAge = pygame.Rect(600, 600, 140, 32)
    color_inactive = pygame.Color('blue')
    color_active = pygame.Color('black')
    colorName = color_inactive
    colorAge = color_inactive
    activeName = False
    activeAge = False
    age=''
    textName = ''
    textAge=''
    word=''
    gcont = True
    pygame.mixer.music.stop()
    while gcont:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_boxName.collidepoint(event.pos):
                    # Toggle the active variable.
                    activeName = not activeName
                else:
                    activeName = False
                if input_boxAge.collidepoint(event.pos):
                     # Toggle the active variable.
                    activeAge = not activeAge
                else:
                    activeAge = False
            colorName = color_active if activeName else color_inactive
            colorAge = color_active if activeAge else color_inactive
            if event.type == pygame.KEYDOWN:
                if activeName:
                    if event.key == pygame.K_BACKSPACE:
                        textName = textName[:-1]
                    elif (event.key==pygame.K_RETURN):
                        textName = textName
                    else:
                        textName += event.unicode

                if activeAge:
                    if event.key == pygame.K_BACKSPACE:
                        textAge = textAge[:-1]
                    elif (event.key!=pygame.K_RETURN):
                        textAge += event.unicode
                    else:
                        age = textAge
                        textAge=''
                        word = textName
                        textName = ''
        gamedisplay.fill(cream)
        background = pygame.image.load('logo.jpg')
        gamedisplay.blit(background, (450, 0))
        txt_surfaceName = font.render(textName, True, colorName)
        txt_surfaceAge = font.render(textAge, True, colorAge)
        # Resize the box if the text is too long.
        width = max(200, txt_surfaceAge.get_width() + 10)
        input_boxName.w = width
        input_boxAge.w = width
        # Blit the text.
        gamedisplay.blit(txt_surfaceName, (input_boxName.x + 5, input_boxName.y + 5))
        gamedisplay.blit(txt_surfaceAge, (input_boxAge.x + 5, input_boxAge.y + 5))
        # Blit the input_box rect.
        text_to_button2("Username: ", black, 540, 560, 10, 10)
        text_to_button2("Age: ", black, 550, 610, 10, 10)
        pygame.draw.rect(gamedisplay, colorName, input_boxName, 2)
        pygame.draw.rect(gamedisplay, colorAge, input_boxAge, 2)
        conn = sqlite3.connect(db_file)
        cur = conn.cursor()
        cur.execute("SELECT distinct Player_Name FROM PLAYERS")
        rowsNames = cur.fetchall()
        cur.execute("SELECT Player_Age FROM PLAYERS")
        rowsAges = cur.fetchall()
        all_names=[]
        all_ages=[]
        text_to_button2("Username", black, 400, 170, 50, 10)
        text_to_button2("Age", black, 500, 170, 50, 10)
        x, y = 400, 210
        xa, ya = 500,210
        for i in rowsNames:
            all_names.append(i[0])
        for j in rowsAges:
            all_ages.append(j[0])
        for name in all_names:
            text_to_button2(name, black, x, y, 50, 10)
            y += 40
            if (y>500):
                x = x+220
                y=180
        for dbage in all_ages:
            text_to_button2(str(dbage), black, xa, ya, 50, 10)
            ya += 40
            if (ya>500):
                xa = xa+270
                ya=180
        if word in all_names:
            cur.execute("DELETE FROM PLAYERS WHERE Player_Name='" + word + "' AND Player_Age="+str(age))
            conn.commit()
            word=''
            age=''
        elif (word != ''):
            cur.execute("INSERT INTO PLAYERS (Player_Name, Player_Age) VALUES ('"+word+"','"+str(age)+"')")
            conn.commit()
            word=''
            age=''
        button("back", 300, 600, 150, 40, darkblue, blue, action="backAd")
        button("quit", 900, 600, 150, 40, lightgreen, green, action="quit")
        pygame.display.update()

def tokensAdmin(db_file):
    input_boxName = pygame.Rect(600, 550, 140, 32)
    input_boxR = pygame.Rect(605, 600, 20, 20)
    input_boxG = pygame.Rect(675, 600, 20, 20)
    input_boxB = pygame.Rect(745, 600, 20, 20)
    color_inactive = pygame.Color('blue')
    color_active = pygame.Color('black')
    colorName = color_inactive
    colorR = color_inactive
    colorG = color_inactive
    colorB = color_inactive
    activeName = False
    activeR = False
    activeG = False
    activeB = False
    r=''
    g=''
    b=''
    textName = ''
    textR=''
    textG = ''
    textB = ''
    word=''
    gcont = True
    pygame.mixer.music.stop()
    while gcont:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_boxName.collidepoint(event.pos):
                    # Toggle the active variable.
                    activeName = not activeName
                else:
                    activeName = False
                if input_boxR.collidepoint(event.pos):
                     # Toggle the active variable.
                    activeR = not activeR
                else:
                    activeR = False
                if input_boxB.collidepoint(event.pos):
                     # Toggle the active variable.
                    activeB = not activeB
                else:
                    activeB = False
                if input_boxG.collidepoint(event.pos):
                     # Toggle the active variable.
                    activeG = not activeG
                else:
                    activeG = False
            colorName = color_active if activeName else color_inactive
            colorR = color_active if activeR else color_inactive
            colorG = color_active if activeG else color_inactive
            colorB = color_active if activeB else color_inactive
            if event.type == pygame.KEYDOWN:
                if activeName:
                    if event.key == pygame.K_BACKSPACE:
                        textName = textName[:-1]
                    elif (event.key==pygame.K_RETURN):
                        textName = textName
                    else:
                        textName += event.unicode

                if activeR:
                    if event.key == pygame.K_BACKSPACE:
                        textR = textR[:-1]
                    elif (event.key == pygame.K_RETURN):
                        textR = textR
                    else:
                        textR += event.unicode
                if activeG:
                    if event.key == pygame.K_BACKSPACE:
                        textG = textG[:-1]
                    elif (event.key == pygame.K_RETURN):
                        textG = textG
                    else:
                        textG += event.unicode
                if activeB:
                    if event.key == pygame.K_BACKSPACE:
                        textB = textB[:-1]
                    elif (event.key!=pygame.K_RETURN):
                        textB += event.unicode
                    else:
                        r=textR
                        g=textG
                        b = textB
                        textR = ''
                        textG = ''
                        textB=''
                        word = textName
                        textName = ''
        gamedisplay.fill(cream)
        background = pygame.image.load('logo.jpg')
        gamedisplay.blit(background, (450, 0))
        txt_surfaceName = font.render(textName, True, colorName)
        txt_surfaceR = font.render(textR, True, colorR)
        txt_surfaceG = font.render(textG, True, colorG)
        txt_surfaceB = font.render(textB, True, colorB)
        # Resize the box if the text is too long.
        widthName = max(200, txt_surfaceName.get_width() + 10)
        widthColor = max(50, txt_surfaceR.get_width() + 10)
        input_boxName.w = widthName
        input_boxR.w = widthColor
        input_boxG.w = widthColor
        input_boxB.w = widthColor
        # Blit the text.
        gamedisplay.blit(txt_surfaceName, (input_boxName.x + 5, input_boxName.y + 5))
        gamedisplay.blit(txt_surfaceR, (input_boxR.x + 5, input_boxR.y + 5))
        gamedisplay.blit(txt_surfaceG, (input_boxG.x + 5, input_boxG.y + 5))
        gamedisplay.blit(txt_surfaceB, (input_boxB.x + 5, input_boxB.y + 5))
        # Blit the input_box rect.
        text_to_button2("Color Name: ", black, 540, 560, 10, 10)
        text_to_button2("R: ", black, 590, 600, 10, 10)
        text_to_button2("G: ", black, 662, 600, 10, 10)
        text_to_button2("B: ", black, 732, 600, 10, 10)
        pygame.draw.rect(gamedisplay, colorName, input_boxName, 2)
        pygame.draw.rect(gamedisplay, colorR, input_boxR, 2)
        pygame.draw.rect(gamedisplay, colorG, input_boxG, 2)
        pygame.draw.rect(gamedisplay, colorB, input_boxB, 2)
        conn = sqlite3.connect(db_file)
        cur = conn.cursor()
        cur.execute("SELECT distinct Color_Name FROM TOKENS")
        rowsNames = cur.fetchall()
        cur.execute("SELECT RED FROM TOKENS")
        rowsRed = cur.fetchall()
        cur.execute("SELECT GREEN FROM TOKENS")
        rowsGreen = cur.fetchall()
        cur.execute("SELECT BLUE FROM TOKENS")
        rowsBlue = cur.fetchall()
        all_names=[]
        all_red=[]
        all_green = []
        all_blue = []
        text_to_button2("Color", black, 400, 170, 50, 10)
        text_to_button2("RGB", black, 500, 170, 50, 10)
        x, y = 400, 210
        xa, ya = 500,210
        for i in rowsNames:
            all_names.append(i[0])
        for j in rowsRed:
            all_red.append(j[0])
        for k in rowsBlue:
            all_blue.append(k[0])
        for t in rowsGreen:
            all_green.append(t[0])
        for name in all_names:
            text_to_button2(name, black, x, y, 50, 10)
            y += 40
            if (y>500):
                x = x+220
                y=180
        for dbrgb in range (len(all_red)):
            text_to_button2('('+str(all_red[dbrgb])+','+str(all_green[dbrgb])+','+str(all_blue[dbrgb])+')', black, xa, ya, 50, 10)
            ya += 40
            if (ya>500):
                xa = xa+270
                ya=180
        if word in all_names:
            cur.execute("DELETE FROM TOKENS WHERE Color_Name='" + word + "' AND RED="+str(r)+ " AND GREEN="+str(g)+ " AND BLUE="+str(b))
            conn.commit()
            word=''
            r = ''
            g = ''
            b = ''
        elif (word != ''):
            cur.execute("INSERT INTO TOKENS (Color_Name, RED, GREEN, BLUE) VALUES ('"+word+"','"+str(r)+"','"+str(g)+"','"+str(b)+"')")
            conn.commit()
            word=''
            age=''
        button("back", 300, 600, 150, 40, darkblue, blue, action="backAd")
        button("quit", 900, 600, 150, 40, lightgreen, green, action="quit")
        pygame.display.update()

# The side function responsible for game controls. i.e. the INSTRUCTION button as well as the quit button!
def choose_color(db_file):
    global firstc, firstrgb
    global secc, secrgb
    all_rects = []
    gcont = True
    currp = 1
    firstc = "NONE"
    secc = "NONE"
    firstrgb = "NONE"
    secrgb = "NONE"
    pygame.mixer.music.stop()
    while gcont:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                cur = pygame.mouse.get_pos()
                for rect in all_rects:
                    if rect.rect.collidepoint(cur):
                        if (currp == 1):
                            firstc = rect.name
                            firstrgb=rect.color
                            currp = 2
                            break
                        if (currp == 2):
                            secc = rect.name
                            secrgb = rect.color
                            currp = 1
                            break
        gamedisplay.fill(cream)
        background = pygame.image.load('logo.jpg')
        gamedisplay.blit(background, (450, 0))
        # using the defined text_to_button function in order to produce text to the screen
        conn = sqlite3.connect(db_file)
        cur = conn.cursor()
        cur.execute("SELECT distinct Color_Name FROM TOKENS")
        rowsNames = cur.fetchall()
        cur.execute("SELECT RED FROM TOKENS")
        rowsRed = cur.fetchall()
        cur.execute("SELECT GREEN FROM TOKENS")
        rowsGreen = cur.fetchall()
        cur.execute("SELECT BLUE FROM TOKENS")
        rowsBlue = cur.fetchall()
        all_names = []
        all_red = []
        all_green = []
        all_blue = []
        NAME_TO_RGBA = {}

        for i in rowsNames:
            all_names.append(i[0])
        for j in rowsRed:
            all_red.append(j[0])
        for k in rowsBlue:
            all_blue.append(k[0])
        for t in rowsGreen:
            all_green.append(t[0])

        for dbrgb in range(len(all_red)):
            NAME_TO_RGBA[all_names[dbrgb]] = ast.literal_eval("("+str(all_red[dbrgb]) + ',' + str(all_green[dbrgb]) + ',' + str(all_blue[dbrgb])+")")
        x, y = 428, 220
        xn,yn = 390,245
        i = 0
        text_to_button2("First player color:" + firstc, black, 600, 180, 10, 10)
        text_to_button2("Second player color:" + secc, black, 600, 200, 10, 10)
        for name in NAME_TO_RGBA.keys():
            text_to_button2(name, black, xn, yn, 10, 10)
            rgba = (NAME_TO_RGBA[name])
            rect = Rect(name, rgba, x, y)
            all_rects.append(rect)
            rect.Draw()
            y += 100
            yn+=100
            if (y>500):
                x = x+220
                xn = xn +220
                y=220
                yn = 245
        button("back", 300, 600, 150, 40, darkblue, blue, action="back")
        button("play", 600, 600, 150, 40, lightgreen, green, action="play")
        button("quit", 900, 600, 150, 40, lightgreen, green, action="quit")
        pygame.display.update()


global nouns1
global nouns2
nouns1 =  fiveNounsStart('NounsMissionsFeelings.db')
nouns2 =  fiveNounsStart('NounsMissionsFeelings.db')
# The main function responsible for the game-play.Everything after clicking the play button is hard-coded in the given fubction
def gameloop():
    global x1
    global y1
    global x2
    global y2
    pygame.mixer.music.stop()
    gloop = True
    while gloop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                cur = pygame.mouse.get_pos()
                if ((765 > cur[0] > 50) and (690 > cur[1] > 10)):
                    if (alternate() == 0):  # condition for alternate turn using the 'alternate' function
                        for i in range(dice()):
                            pygame.mixer.music.stop()
                            pygame.mixer.music.load('dice.mp3')
                            pygame.mixer.music.play(0)
                            if (y1 >= 120 and x1 <= 267):  # Conditions for moving the marbles..
                                y1 -= 85
                            elif (y1 < 120 and x1 < 1015 and x1 >= 267):
                                x1 += 125
                            elif (y1 > 110 and x1 > 1015 and y1 < 500):
                                y1 += 85
                            elif (y1 > 500 and x1 < 1040 and x1 >= 267):
                                x1 -= 125
                        print
                        amountp1()
                    else:  # Same for other player
                        for i in range(dice()):
                            pygame.mixer.music.stop()
                            pygame.mixer.music.load('dice.mp3')
                            pygame.mixer.music.play(0)
                            if (y2 >= 150 and x2 <= 267):
                                y2 -= 85
                            elif (y2 < 150 and x2 < 1015 and x2 >= 267):
                                x2 += 125
                            elif (y2 > 140 and x2 > 1015 and y2 < 500):
                                y2 += 85
                            elif (y2 > 500 and x2 < 1040 and x2 >= 267):
                                x2 -= 125
                        print
                        amountp2()
            elif event.type == pygame.MOUSEBUTTONUP:
                pass
            if (initial_cost1 <= 0 or initial_cost2 <= 0):  # THe winning condition
                gameover = font.render("Gameover", 1, green)
                gamedisplay.blit(gameover, [660, 640])
                pygame.quit()
                quit()

        gamedisplay.fill(cream)
        background1 = pygame.image.load('board1.jpg')
        gamedisplay.blit(background1, (220, 50))
        button("ROLL THE DICE", 565, 650, 200, 40, darkblue, green, action="roll")

        pygame.draw.circle(gamedisplay, firstrgb, [x1, y1],10)  # Cordinates are in form of variables, for their movement!
        pygame.draw.circle(gamedisplay, secrgb, [x2, y2], 10)  # Cordinates are in form of variables, for their movement!

        # printing all player related information on the screen
        drawFive(nouns1,1170,300)
        drawFive(nouns2,70,300)
        if (firstc=="red"):
            player1_heading = font.render("Player 1", 1, red)
        elif (firstc=="blue"):
            player1_heading = font.render("Player 1", 1, blue)
        elif (firstc=="white"):
            player1_heading = font.render("Player 1", 1, white)
        else:
            player1_heading = font.render("Player 1", 1, green)
        player1_subheading = font.render('Num Of Nouns:' + str(initial_cost1), 1, black)
        gamedisplay.blit(player1_heading, [70, 186])
        gamedisplay.blit(player1_subheading, [40, 220])
        if (secc == "red"):
            player2_heading = font.render("Player 2", 1, red)
        elif (secc == "blue"):
            player2_heading = font.render("Player 2", 1, blue)
        elif (secc == "white"):
            player2_heading = font.render("Player 2", 1, white)
        else:
            player2_heading = font.render("Player 2", 1, green)
        player1_subheading = font.render('Num Of Nouns:' + str(initial_cost2), 1, black)
        gamedisplay.blit(player2_heading, [1165, 186])
        gamedisplay.blit(player1_subheading, [1120, 220])
        dicenumber = pygame.font.Font(None, 75)
        text1 = dicenumber.render(str(a), 1, black)
        gamedisplay.blit(text1, [642, 290])
        pygame.display.update()


# The button fuction responsible for creating buttons throughout the code, and redirecting to the appropriate function after the mouse click
def button(text, x, y, width, height, inactive_color, active_color, action=None):
    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if (x + width > cur[0] > x) and (y + height > cur[1] > y):
        pygame.draw.rect(gamedisplay, active_color, (x, y, width, height))
        text_to_button(text, black, x, y, width, height)
        if click[0] == 1 and action != None:
            if action == "quit":  # the actions redirect to the corresponding function
                pygame.quit()
                quit()
            if action == "controls":
                game_controls()
            if action=="players":
                playersAdmin('Users.db')
            if action=="tokens":
                tokensAdmin('Tokens.db')
            if action=="nouns":
                wordsAdmin('NounsMissionsFeelings.db',"SELECT distinct Noun_Name FROM NOUNS","DELETE FROM NOUNS WHERE Noun_Name='","INSERT INTO NOUNS (Noun_Name) VALUES ('")
            if action == "missions":
                wordsAdmin('NounsMissionsFeelings.db', "SELECT distinct Mission_Name FROM MISSIONS","DELETE FROM MISSIONS WHERE Mission_Name='","INSERT INTO MISSIONS (Mission_Name) VALUES ('")
            if action=="feelings":
                wordsAdmin('NounsMissionsFeelings.db', "SELECT distinct Feeling_Name FROM FEELINGS","DELETE FROM FEELINGS WHERE Feeling_Name='","INSERT INTO FEELINGS (Feeling_Name) VALUES ('")
            if action == "play":
                gameloop()
            if action == "back":
                game_intro()
            if action == "backAd":
                admin_screen()
            if action == "ChooseColor":
                choose_color('Tokens.db')
            if action=="AdminLogin":
                login('a')
            if action == "ObserverLogin":
                login('o')
            if action == "AdminScreen":
                admin_screen()
            if action == "roll":
                pygame.display.update()

    else:
        pygame.draw.rect(gamedisplay, inactive_color, (x, y, width, height))
        text_to_button(text, black, x, y, width, height)


def text_objects(text, color, size=None):
    textsurface = verysmallfont.render(text, True, color)

    if size == "small":
        textsurface = smallfont.render(text, True, color)
    if size == "medium":
        textsurface = medfont.render(text, True, color)
    if size == "large":
        textsurface = largefont.render(text, True, color)

    return textsurface, textsurface.get_rect()


# All text_to_button functions have the same functionality, i.e. to produce text to the screen. The only difference is the font size!!
def text_to_button(msg, color, button_x, button_y, button_width, button_height, size="small"):
    textsurf, textrect = text_objects(msg, color, size)
    textrect.center = ((button_x + (button_width / 2)), button_y + (button_height / 2))
    gamedisplay.blit(textsurf, textrect)


def text_to_button2(msg, color, buttonx, buttony, buttonwidth, buttonheight, size="verysmall"):
    textsurf, textrect = text_objects(msg, color, size)
    textrect.center = ((buttonx + (buttonwidth / 2)), buttony + (buttonheight / 2))
    gamedisplay.blit(textsurf, textrect)


def text_to_button3(msg, color, buttonx, buttony, buttonwidth, buttonheight, size="large"):
    textsurf, textrect = text_objects(msg, color, size)
    textrect.center = ((buttonx + (buttonwidth / 2)), buttony + (buttonheight / 2))
    gamedisplay.blit(textsurf, textrect)


# The very first function which runs as soon as the game starts
def game_intro():
    time.sleep(0.2)
    pygame.mixer.music.load('monopoly.mp3')  # Sound in the background
    pygame.mixer.music.play(0)
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gamedisplay.fill(violet)
        background2 = pygame.image.load('start-pic.jpg')
        background = pygame.image.load('logo.jpg')  # Image in the background
        gamedisplay.blit(background2, (0, 0))
        gamedisplay.blit(background, (840, 50))  # Adding the image

        button("PLAY", 300, 500, 150, 40, darkblue, blue,
               action="ChooseColor")  # Creating buttons using the predefined function 'button'
        button("INSTRUCTIONS", 570, 500, 220, 40, lightyellow, yellow, action="controls")
        button("ADMIN", 400, 600, 220, 40, lightblue, red, action="AdminLogin")
        button("OBSERVER", 700, 600, 220, 40, lightblue, red, action="ObserverLogin")
        button("QUIT", 900, 500, 150, 40, lightgreen, green, action="quit")
        pygame.display.update()


game_intro()
gameloop()