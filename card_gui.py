import tkinter as tk
from PIL import Image, ImageTk
import os
import random



os.chdir(r'/Users/eschmidt/Documents/pythonHELP/cards')

tk = tkinter.Tk()
root = tk

card_images = ["basquiat_card.jpg", "dali_card.jpg", "davinci_card.jpg", 
"frida_card.jpg", "Okeeffe_card.jpg", "vincent_card.jpg"]

AtoCIm = []
for image in card_images:
    AtoCIm.append(Image.open(image))

card_scores = [77, 54, 85, 88, 67, 54]

user_cards = []
user_cards_image = []
computer_cards = []
computer_cards_images = []
index = 0
while index < 3:
    user_cards_image.append(card_images[random.randint(0, 5)])
    computer_cards.append(card_images[random.randint(0, 5)]) 
    user_cards.append(card_scores[random.randint(0, 5)])
    computer_cards_images.append(card_scores[random.randint(0, 5)])
    index += 1
#for number in range(1,4):
 #   if number == 1
 #       print('The first card is: ', user_cards[0])
#      print('The second card is: ', user_cards[1])
  #      print('The third card is: ', user_cards[2])
   # elif number == 2
        #print('The first card is: ', user_cards[0])
        #print('The second card is: ', user_cards[1])
    #else:
        #print('The only card left: ', user_cards[0])
        
    #battle_card_user = int(input('What card do you want choose (0, 1, 2): '))
    #battle_card_computer = random.randint(0,2)
    #print('The computer choose: ', computer_cards[battle_card_computer])
 
    #if user_cards[battle_card_user] > computer_cards[battle_card_computer]:
       #print("user wins!")
    #elif user_cards[battle_card_user] == computer_cards[battle_card_computer]:
       #print ("draw")
    #else:
       #print("computer wins" )

    #user_cards.pop(battle_card_user)
    #computer_cards.pop(battle_card_computer)
def sayOne(event):
    blankButton.grid(row=1, column=1)
def sayTwo(event):
    blankButton.grid(row=1, column=2)
def sayThree(event):
    blankButton.grid(row=1, column=3)
def hide_me(event):
    event.widget.grid_forget()
#def _create_image(self, coord):
    #(x,y) = coord
    #self.one = ImageTk.PhotoImage(Image.open("blank.png"))
    #root.one = self.one
    #self.canvas.create_image(x-50, y-50, image=self.one,
                             #anchor='nw', tags="image")
    #self.img_ref.append(self.one)

blank = ImageTk.PhotoImage(file="blank.png")
card1 = ImageTk.PhotoImage(file=user_cards_image[0])
card2 = ImageTk.PhotoImage(file=user_cards_image[1])
card3 = ImageTk.PhotoImage(file=user_cards_image[2])

comp_card1 = ImageTk.PhotoImage(Image.open("back.jpg"))
comp_card2 = ImageTk.PhotoImage(Image.open("back.jpg"))
comp_card3 = ImageTk.PhotoImage(Image.open("back.jpg"))

button1 = tkinter.Button(root, image=card1)
button2 = tkinter.Button(root, image=card2)
button3 = tkinter.Button(root, image=card3)
blankButton = tkinter.Button(root, image=blank)

#label_comp1 = tkinter.Label(root, image=comp_card1)
#label_comp2 = tkinter.Label(root, image=comp_card2)
#label_comp3 = tkinter.Label(root, imagre=comp_card3)

button1.bind('<Button-1>', hide_me)
button2.bind('<Button-1>', hide_me)
button3.bind('<Button-1>', hide_me)

panel = tk.Label(root, image = comp_card1)
#comp_card1.anchor(x=70,y=90)
#comp_card2.anchor(x=170, y=90)
#comp_card3.anchor(x=210, y=90)

button1.grid(row=1, column=1)
button2.grid(row=1, column=2)
button3.grid(row=1, column=3)

root.mainloop()

