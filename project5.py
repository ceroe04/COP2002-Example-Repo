#Ceroe04, Carmen Roe COP2002 0M1 3-15-24
#Project 5 Part 2:Use functions to write rest of the program, Uses functions to ask the user a question selected by them to answer which port or number belongs to which port or number. Along with an exit cue.
import random as rnd

#sets up the questions asked and the arrays that include the question data.
def getInput() :
    numArray=["20","21","22","23","25","53","67","68","80","110","137","139","143","161","162","389","443","445","3389"]
    nameArray=["FTP", "FTP","SSH","Telnet","SMTP","DNS","DHCP", "DHCP","HTTP","POP3","NetBIOS","NetBIOS","IMAP","SNMP","SNMP","LDAP","HTTPS","SMB","RDP"]
    print("    Main Menu:")
    print("1.  Given a port number, identify the PROTOCOL (use abbreviation).")
    print("2.  Given a port protocol, identify a port NUMBER.")
    print("3.  Exit")
    choiceSelected = input("Choice: ")
    choiceSelected = choiceSelected.rstrip()
    if choiceSelected == "1" :
        randomChoice = rnd.randint(0,18)
        numToName(numArray,nameArray,randomChoice)     
    elif choiceSelected == "2" :
        randomChoice = rnd.randint(0,18)
        nameToNum(numArray,nameArray,randomChoice)
    elif choiceSelected == "3" :
        SystemExit
    else :
        getInput()
    
#sets up the function for asking and answering the number for protocols
def numToName(portNumArray,portNameArray,portNumber) :
    answer = input("What is the number for protocol "+ portNameArray[portNumber] +" (m=Main Menu)?")
    answer = answer.rstrip()
    if answer == "m":
        getInput()
    for x in range(0,18):
        if portNumArray[x] == answer and portNameArray[x] == portNameArray[portNumber]:
            print("Correct answer!")
            numToName(portNumArray,portNameArray,rnd.randint(0,18))
    print("Incorrect. The correct answer is", portNumArray[portNumber])
    numToName(portNumArray,portNameArray,rnd.randint(0,18))    
    
#sets up the function for asking and answering the number for protocols
def nameToNum(portNumArray,portNameArray,portName) :
    answer = input("What is the protocol for port "+ portNumArray[portName] +" (m=Main Menu)?")
    answer = answer.rstrip()
    if answer == "m":
        getInput()
    elif answer == portNameArray[portName]:
        print("Correct answer!")
        nameToNum(portNumArray,portNameArray,rnd.randint(0,18))
    else:
        print("Incorrect. The correct answer is", portNameArray[portName])
        nameToNum(portNumArray,portNameArray,rnd.randint(0,18))

def main():
    getInput()

if(__name__=="__main__"):
    main()