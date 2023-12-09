import customtkinter
import time

class MainWindow:
     
     def __init__(self):
          
          self.window = customtkinter.CTk()
          self.window.title("Game Collection")

          self.button_1 = customtkinter.CTkButton(self.window, text="Work in Progress", width=30, height=90, command=self.start_tictactoe)
          self.button_1.grid(row=0, column=0)

          self.button_2 = customtkinter.CTkButton(self.window, text="Work in Progress", width=30, height=90, command=self.start_tictactoe)
          self.button_2.grid(row=0, column=1)


          self.button_3 = customtkinter.CTkButton(self.window, text="Work in Progress", width=30, height=90, command=self.start_tictactoe)
          self.button_3.grid(row=0, column=2)

          self.button_4 = customtkinter.CTkButton(self.window, text="Work in Progress", width=30, height=90, command=self.start_tictactoe)
          self.button_4.grid(row=0, column=3)

          self.button_5 = customtkinter.CTkButton(self.window, text="Work in Progress", width=30, height=90, command=self.start_tictactoe)
          self.button_5.grid(row=0, column=4)

          self.button_6 = customtkinter.CTkButton(self.window, text="Work in Progress", width=30, height=90, command=self.start_tictactoe)
          self.button_6.grid(row=1, column=0)


          self.button_7 = customtkinter.CTkButton(self.window, text="Work in Progress", width=30, height=90, command=self.start_tictactoe)
          self.button_7.grid(row=1, column=1)

          self.button_8 = customtkinter.CTkButton(self.window, text="Work in Progress", width=30, height=90, command=self.start_tictactoe)
          self.button_8.grid(row=1, column=2)

          self.button_9 = customtkinter.CTkButton(self.window, text="Work in Progress", width=30, height=90, command=self.start_tictactoe)
          self.button_9.grid(row=1, column=3)

          self.button_10 = customtkinter.CTkButton(self.window, text="Work in Progress", width=30, height=90, command=self.start_tictactoe)
          self.button_10.grid(row=1, column=4)


          self.window.mainloop()
     

     def start_tictactoe(self):
        pass



class TicTacToe:
    
    def __init__(self):
         pass
        
        

class Suduko:
     def __init__(self) -> None:
          pass

class Battleship:
     pass

class RockPaperScissors:
     pass

class Minesweeper:
     pass

class Quiz:
     pass
     
class Pong:
     pass
     
class Hangman:
     pass
     

class Number_guessing:
     pass
     
class Snake:
     pass


if __name__ == "__main__":
     MainWindow()