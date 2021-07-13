import keyboard
import pyperclip
import subprocess
import time



while True:
    try:
        if keyboard.is_pressed('t+e'):
            print('Working')
            time.sleep(10)

        if keyboard.is_pressed('p+e'):
            Program = pyperclip.paste()
            ProgramFile = open("Program.py", "w")
            ProgramFile.write(Program)
            ProgramFile.close()
            ProgramExecution = subprocess.run(["python", "-m", "Program"], shell=True, universal_newlines=True, stdout=subprocess.PIPE)
            Output = ProgramExecution.stdout
            Errors = ProgramExecution.stderr
            if Errors == None:
                Errors = 'None'
            Data = "<p>Result: " + Output + "<br>" + "Error: " + Errors + "</p>"
            IndexFile = open('templates\index.html','w')
            IndexFile.write(repr(Data))
            IndexFile.close()
            print("Result: ", Output, "\nError: ", Errors)
            time.sleep(10)

        if keyboard.is_pressed('c+e'):
            Program = pyperclip.paste()
            ProgramFile = open("Program.c", "w")
            ProgramFile.write(Program)
            ProgramFile.close()
            ProgramExecution = subprocess.run([".\\tcc\\tcc.exe", "-run", "Program.c"], shell=True, universal_newlines=True, stdout=subprocess.PIPE)
            Output = ProgramExecution.stdout
            Errors = ProgramExecution.stderr
            if Errors == None:
                Errors = 'None'
            Data = "<p>Result: " + Output + "<br>" + "Error: " + Errors + "</p>"
            IndexFile = open('templates\index.html','w')
            IndexFile.write(repr(Data))
            IndexFile.close()
            print("Result: ", Output, "\nError: ", Errors)
            time.sleep(10)

        if keyboard.is_pressed('d+e'):
            subprocess.run(["del", "Program.py", "Program.c"], shell=True)
            IndexFile = open('templates\index.html','w')
            InstructionFile = open('templates\instructions.txt','r')
            Instructions = InstructionFile.readlines()
            Data = ''
            for i in Instructions:
                Data = Data + ' <br> ' + i
            Data = '<p>' + Data + '</p>'    
            IndexFile.write(Data)
            IndexFile.close()
            time.sleep(10)



    except:
        continue
