import random
import tkinter

mainWindow = tkinter.Tk()

def load_images(card_image):

    suits=['club', 'diamond', 'heart', 'spade']
    face_cards=['jack', 'queen', 'king']

    for suit in suits:

        for card in range(1,11):
            name= 'cards/{}_{}.ppm'.format(str(card),suit)
            image= tkinter.PhotoImage(file=name)
            card_image.append((card, image))

        for card in face_cards:
            name = 'cards/{}_{}.ppm'.format(card,suit)
            image= tkinter.PhotoImage(file=name)
            card_image.append((10, image))

def new_game():
    global dealer_hand
    global player_hand
    global player_card_frame
    global dealer_card_frame

    player_card_frame.destroy()
    player_card_frame = tkinter.Frame(card_frame, background='green')
    player_card_frame.grid(row=2, column=1, sticky='w', rowspan=2)

    dealer_card_frame.destroy()
    dealer_card_frame = tkinter.Frame(card_frame, background='green')
    dealer_card_frame.grid(row=0, column=1, sticky='w', rowspan=2)

    result_text.set(" ")
    dealer_hand = []
    player_hand = []

    deal_player()
    dealer_hand.append(deal_card(dealer_card_frame))
    dealer_score_label.set(score_hand(dealer_hand))
    deal_player()


def deal_card(frame):
    next_card = deck.pop(0)
    deck.append(next_card)
    tkinter.Label(frame, image = next_card[1], relief= 'raised').pack(side='left')
    return next_card

def score_hand(hand):
    score= 0
    ace= False
    for next_card in hand:
        card_vale = next_card[0]
        if card_vale == 1 and not ace:
            ace = True
            card_vale = 11
        score += card_vale

        if score >21 and ace:
            score-=10
            ace = False
    return score

def deal_dealer():
    dealer_score= score_hand(dealer_hand)
    while 0< dealer_score < 17:
        dealer_hand.append(deal_card(dealer_card_frame))
        dealer_score= score_hand(dealer_hand)
        dealer_score_label.set(dealer_score)

    player_score=score_hand(player_hand)

    if player_score>21:
        result_text.set("Dealer Wins !")
    elif dealer_score>21 or dealer_score<player_score:
        result_text.set("Player Wins !")
    elif dealer_score>21:
        result_text.set("Player Wins ")
    elif dealer_score <=21 and dealer_score>player_score:
        result_text.set("Dealer Wins ")
    elif dealer_score == player_score:
        result_text.set("Draw")

def deal_player():
    player_hand.append(deal_card(player_card_frame))
    player_score = score_hand(player_hand)

    player_score_label.set(player_score)
    if player_score>21:
        result_text.set("Dealer Wins ! ")

mainWindow.title("Black Jack")
mainWindow.geometry("400x300+550+250")

mainWindow.configure(background="green")
result_text = tkinter.StringVar()
result = tkinter.Label(mainWindow, textvariable = result_text,background="green")
result.grid(row=0, column=0, columnspan=3)

card_frame = tkinter.Frame(mainWindow, relief='sunken', borderwidth=1, background="green")
card_frame.grid(row=1, column=0, sticky='ew', columnspan=3, rowspan=2)

dealer_score_label = tkinter.IntVar()
tkinter.Label(card_frame, text= "Dealer", background= "green", fg='white').grid(row=0, column=0)
tkinter.Label(card_frame, textvariable= dealer_score_label, background="green", fg="white").grid(row=1, column=0)

dealer_card_frame = tkinter.Frame(card_frame, background= 'green')
dealer_card_frame.grid(row=0, column=1, sticky= 'w', rowspan=2)

player_score_label = tkinter.IntVar()

tkinter.Label(card_frame, text="Player", background = 'green', fg = 'white').grid(row=2, column=0)
tkinter.Label(card_frame, textvariable=player_score_label, background='green', fg='white').grid(row=3, column=0)

player_card_frame = tkinter.Frame(card_frame, background= 'green')
player_card_frame.grid(row=2, column=1, sticky= 'w', rowspan=2)

button_frame = tkinter.Frame(mainWindow, background='green')
button_frame.grid(row=3, column=0, columnspan = 3, sticky = 'w')

dealer_button = tkinter.Button(button_frame, text="  Dealer  ", command=deal_dealer)
dealer_button.grid(row=0, column=0)

player_button = tkinter.Button(button_frame, text="  Player  ", command=deal_player)
player_button.grid(row=0, column=1)

new_game_button = tkinter.Button(button_frame, text= "  New Game  ", command=new_game)
new_game_button.grid(row=0, column=2)

shuffel_button = tkinter.Button(button_frame, text="  Shuffel  ")
shuffel_button.grid(row=0,column=3)

quit_button = tkinter.Button(button_frame, text= " Quit  ", command = quit)
quit_button.grid(row=0, column = 4, sticky = 'e')

button_frame['padx']= 15
card_frame['padx']=25

cards=[]
load_images(cards)

deck = list(cards)
random.shuffle(deck)
dealer_hand= []
player_hand= []


deal_player()
dealer_hand.append(deal_card(dealer_card_frame))
dealer_score_label.set(score_hand(dealer_hand))
deal_player()

mainWindow.mainloop()
