from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from MinimaxSearch import MinimaxSearch
from AlphaBetaSearch import AlphaBetaSearch
from State import State
from Move import Move
import Config
import time


class TicTacToe(App):

    def build(self):

        self.currentState = State()
        self.winner = Config.running
        self.buttons = []
        self.winnerLabel = None

        layout = FloatLayout(size=(300,300))
        colWidth = 0.75 / Config.nSquares
        rowHeight = 1.0 / Config.nSquares

        for i in range(Config.nSquares):
            for j in range(Config.nSquares):
                button = Button(text=str('-'), size_hint=(colWidth, rowHeight),
                pos_hint={'x':colWidth * i, 'y':rowHeight * j}, font_size = 60)

                button.bind(on_press = self.selectBox)
                layout.add_widget(button)
                self.buttons.append(button)

        labelText = 'The human starts'
        if Config.startPlayer == Config.computerPlayer:
            labelText = 'Skynet starts the game'

        self.winnerLabel = Label(text = labelText, size_hint=(0.25,1), 
        pos_hint={'x':0.75, 'y':0.0}, font_size=20)
        layout.add_widget(self.winnerLabel)

        if Config.startPlayer == Config.computerPlayer:
            self.callComputerPlayer()

        return layout

    def selectBox(self, instance):
        if self.winner != Config.running:
            return
        
        if instance.text == '-':
            instance.text = Config.moveTexts[Config.humanPlayer]

            for i in range(Config.nSquares):
                for j in range(Config.nSquares):
                    index = j * Config.nSquares + 2 - i
                    if self.buttons[index] == instance:
                        humanMove = Move(i, j, Config.humanPlayer)
                        self.currentState = self.currentState.createChildState(humanMove)

        if self.checkWinner():
            return

        self.callComputerPlayer()

        self.checkWinner()

    def checkWinner(self):
        endFlag, self.winner = self.currentState.checkGoalState()

        if endFlag:
            print("Game has ended")
            self.changeWinnerText()
            return True
        
        return False

    def callComputerPlayer(self):
        if(Config.withMinimax):
            kindOfSearch = MinimaxSearch(self.currentState, Config.maximumDepth, False)
        else:
            kindOfSearch = AlphaBetaSearch(self.currentState, Config.maximumDepth)

        bestMove = kindOfSearch.search()
        if bestMove != None:
            buttonIndex = bestMove.col * Config.nSquares + 2 - bestMove.row
            self.buttons[buttonIndex].text = Config.moveTexts[Config.computerPlayer]
            self.currentState = self.currentState.createChildState(bestMove)
    
    def changeWinnerText(self):
        if self.winner == Config.computerPlayer:
            self.winnerLabel.text = 'You lose'
        elif self.winner == Config.humanPlayer:
            self.winnerLabel.text = 'You win'
        else:
            self.winnerLabel.text = 'Try again'


TicTacToe().run()