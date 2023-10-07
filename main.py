import customtkinter, tkinter
import webscrape
import time

imgs_list = ['''
      +---+
          |
          |
          |
          |
          |
    =========''', '''
      +---+
      |   |
          |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========''']


word = ''
tries = 0
tile_list = []
user_guess = []
guess_word_label = ''
correct=0
hints=3
def game():
    #window creation
    window = customtkinter.CTk()
    window.geometry('540x500')
    window.configure(fg_color='white')
    window.resizable(False,False)
    normal_font = customtkinter.CTkFont(weight="bold", size=15, family='Comic Sans MS')
    canvas = customtkinter.CTkLabel(window, text=imgs_list[tries], text_color='black', width=540, height=400)
    canvas.grid(column=0, row=0, columnspan=9)
    def game_setup():
        global  word, tries, user_guess, guess_word_label, hints
        hints=3
        word = webscrape.get_word()
        print(word)
        tries = 0
        user_guess = []
        for letter in range(len(word)):
            user_guess.append('__')
        #
        guess_word_label = ''
        for letter in user_guess:
            guess_word_label += letter + '  '

        x = 0
        y = 1

        canvas.configure(text = imgs_list[tries])

        if len(tile_list)>0:
            for item in tile_list:
                item.en()

        else:

            all = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ⌫'
            all = list(all)
            for i in range(3):
                for v in range(9):
                    tile_list.append(letters(all[0], y, x))
                    all.pop(0)
                    x += 1
                x = 0
                y += 1
        word_label.configure(text=f'{guess_word_label}')


        entry_box.configure(text='')



    # widgets creation


    top_banner = customtkinter.CTkLabel(window, text_color='black', fg_color='#FEF71B', text='', corner_radius=5)
    top_banner.place(relx=0.5, rely=0.03, relwidth=0.95, relheight=0.05, anchor=tkinter.CENTER)

    score_label = customtkinter.CTkLabel(window, text_color='black', fg_color='#FEF71B', text='WORDS GUESSED: 0 ',
                                         bg_color='#FEF71B', corner_radius=5)
    score_label.place(relx=0.2, rely=0.03, relwidth=0.25, relheight=0.05, anchor=tkinter.CENTER)

    # home_btn = customtkinter.CTkButton(window, text_color='black', fg_color='#FEF71B', text='HOME',
    #                                    hover_color='#AC9C1D', corner_radius=5, bg_color='#FEF71B', border_color='black',
    #                                    border_width=1.5)
    # home_btn.place(relx=0.9, rely=0.03, relwidth=0.08, relheight=0.04, anchor=tkinter.CENTER)





    tries_label=customtkinter.CTkLabel(window, text=F'TRIES - {5-tries}', corner_radius=5, fg_color='#ECF5D2',
    text_color='black',width=40,height=30)
    tries_label.place(relx=0.85,rely=0.73)

    word_label=customtkinter.CTkLabel(window, text=f'{guess_word_label}', corner_radius=5, fg_color='#ECF5D2',text_color='black',width=270,height=30)
    word_label.place(relx=0.5,rely=0.68,anchor=tkinter.CENTER)

    entry_box=customtkinter.CTkLabel(window, text='', corner_radius=5, fg_color='#ECF5D2',text_color='black',width=270,height=30)
    entry_box.place(relx=0.01,rely=0.73)


    #submition
    def update_label(letter):

        global user_guess, guess_word_label
        for i in range(len(word)):
            if word[i]==letter:

                user_guess[i]=letter

        guess_word_label = ''
        for letter in user_guess:
            guess_word_label += letter + '  '

        word_label.configure(text=f'{guess_word_label}')

    def submit():

        global tries, guess_word_label,user_guess,correct
        if len(entry_box.cget('text'))==0:
            return
        if len(entry_box.cget('text'))==1:
            if entry_box.cget('text') in word:
                update_label(entry_box.cget('text'))
                entry_box.configure(text='')

            else:
                tries+=1
                canvas.configure(text=imgs_list[tries])
                tries_label .configure(text=F'TRIES - {5 - tries}')
                for item in tile_list:
                    if item.getname().cget('text')==entry_box.cget('text'):
                        item.getname().configure(state=tkinter.DISABLED)
                        break

                entry_box.configure(text='')

                if tries==5:
                    print('game_over')
        else:
            if word != entry_box.cget('text'):
                tries += 1
                canvas.configure(text=imgs_list[tries])
                tries_label.configure(text=F'TRIES - {5 - tries}')
            if word == entry_box.cget('text'):
                correct+=1
                score_label.configure(text=f'WORDS GUESSED: {correct} ')

                game_setup()


        if '__' not in word_label.cget('text'):
            correct += 1
            score_label.configure(text=f'WORDS GUESSED: {correct} ')
            game_setup()

        if tries==5:
            correct=0
            score_label.configure(text=f'WORDS GUESSED: {correct} ')
            game_setup()


    submit_btn=customtkinter.CTkButton(window, text='SUBMIT', corner_radius=5, fg_color='#ECF5D2',hover_color='#D9E3BA',
    text_color='black',width=120,height=30,command=submit)
    submit_btn.place(relx=0.52,rely=0.73)



    #letters and class---------------------------

    class letters():
        def click(self):
            if self.tile_name.cget('text') == '⌫':
                entry_box.configure(text=entry_box.cget('text')[:len(entry_box.cget('text')) - 1])
            else:
                entry_box.configure(text=entry_box.cget('text') + self.tile_name.cget('text'))

        def __init__(self, letter, grid_x, grid_y):
            self.tile_name = customtkinter.CTkButton(window, text=letter, corner_radius=7, fg_color='#DBC416',
                                                     font=normal_font,
                                                     hover_color='#AC9C1D', text_color='black', width=60, height=30,
                                                     command=self.click)

            self.tile_name.grid(column=grid_y, row=grid_x)

        def getname(self):
            return self.tile_name

        def en(self):
            self.tile_name.configure(state=tkinter.ACTIVE)


    def hint():
        global hints, correct
        if hints==0:
            return

        for letter in word:
            if letter not in user_guess:
                update_label(letter)
                entry_box.configure(text='')
                break

        if '__' not in word_label.cget('text'):
            correct += 1
            score_label.configure(text=f'WORDS GUESSED: {correct} ')
            game_setup()

        hints-=1
        if hints==2:
            hint_btn.configure(text='🔍₂')
        elif hints==1:
            hint_btn.configure(text='🔍₁')
        elif hints==0:
            hint_btn.configure(text='🔍₀')







    hint_btn = customtkinter.CTkButton(window, text='🔍₃', corner_radius=5, fg_color='#ECF5D2', hover_color='#D9E3BA',
                                       text_color='black', width=40, height=30,command=hint)
    hint_btn.place(relx=0.75, rely=0.73)

    game_setup()
    window.mainloop()








    window.mainloop()







while True:
    game()