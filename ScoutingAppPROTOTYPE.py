import tkinter as tk
from tkinter import ttk

# Prototype of possibilities with tkinter in Python
# Ideas of what to add
    # if they got on the chain or not
    # if they left starting area
    # if they got the coopertition bonus
    # laurens ideas

scoreTotal = 0
scoreAMP = 0
scoreSpeaker = 0
leaveInAuto = False

windows = tk.Tk()
windows.title("Scouting App PROTOTYPE")
windows.geometry('600x200')

def printTeamNumber():
    inp = robotInput.get(1.0, "end-1c")
    robotOutput.config(text = "Team " + inp + " Scouting Data", font = "Helvetica 12 bold")

def addAmpScore():
    global scoreTotal
    global scoreAMP

    scoreTotal = scoreTotal + 1
    scoreAMP = scoreAMP + 1
    score.configure(text = "Score Total \n" + str(scoreTotal))
    ampTotalScore.configure(text = "Amp Total: " + str(scoreAMP))

def addAutoAmpScore():
    global scoreTotal
    global scoreAMP

    scoreTotal = scoreTotal + 2
    scoreAMP = scoreAMP + 2
    score.configure(text = "Score Total \n" + str(scoreTotal))
    ampTotalScore.configure(text = "Amp Total: " + str(scoreAMP))

def addSpeakerScore():
    global scoreTotal
    global scoreSpeaker

    scoreTotal = scoreTotal + 2 
    scoreSpeaker = scoreSpeaker + 2
    score.configure(text = "Score Total \n" + str(scoreTotal))
    speakerTotalScore.configure(text = "Speaker Total: " + str(scoreSpeaker))

def addAutoSpeakerScore():
    global scoreTotal
    global scoreSpeaker

    scoreTotal = scoreTotal + 5
    scoreSpeaker = scoreSpeaker + 5
    score.configure(text = "Score Total \n" + str(scoreTotal))
    speakerTotalScore.configure(text = "Speaker Total: " + str(scoreSpeaker))

def toggleLeaveInAuto():
    global leaveInAuto
    global scoreTotal

    leaveInAuto = True
    scoreTotal = scoreTotal + 2
    score.configure(text = "Score Total \n" + str(scoreTotal))
    leaveStartYesOrNo.configure(text = "Yes")

robotName = tk.Button(windows,
                    text = "Robot Number Input ->",
                    command = printTeamNumber)
robotName.grid(column=0, row=0)
robotInput = tk.Text(windows, 
                        height = 1,
                        width = 5,)
robotInput.grid(column=1, row=0)
robotOutput = tk.Label(windows, text = "Team ____ Scouting Data", font = "Helvetica 12 bold")
robotOutput.grid(column=3, row=0)

ampScoreTELEButton = tk.Button(windows,
                               text = "TeleAMP Score",
                               command = addAmpScore)
ampScoreTELEButton.grid(column=0, row=1)
ampScoreAUTOButton = tk.Button(windows,
                               text = "AutoAMP Score",
                               command = addAutoAmpScore)
ampScoreAUTOButton.grid(column=1, row=1)
ampTotalScore = tk.Label(windows, text = "Amp Total:")
ampTotalScore.grid(column=3, row=1)

speakerScoreTELEButton = tk.Button(windows,
                                   text = "TeleSpeaker Score",
                                   command = addSpeakerScore)
speakerScoreTELEButton.grid(column=0, row=2)
speakerScoreAUTOButton = tk.Button(windows,
                               text = "AutoSpeaker Score",
                               command = addAutoSpeakerScore)
speakerScoreAUTOButton.grid(column=1, row=2)
speakerTotalScore = tk.Label(windows, text = "Speaker Total:")
speakerTotalScore.grid(column=3, row=2)

leaveStartArea = tk.Button(windows,
                           text = "Left Start-Area?",
                           command = toggleLeaveInAuto)
leaveStartArea.grid(column=1,row=3)
leaveStartYesOrNo = tk.Label(windows, text = "No")
leaveStartYesOrNo.grid(column=3,row=3)

score = tk.Label(windows, text = "Score Total \n 0", font = "Helvetica 10 bold")
score.grid(column=3, row=5)

spacer = tk.Label(windows, text = "                             ")
spacer.grid(column=2, row=0)

windows.mainloop()