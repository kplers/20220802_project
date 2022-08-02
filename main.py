# This is a bulls and cows game program.
# 숫자야구 게임 프로그램
from random import randint

# setting a random number
def setRand(digits):
    return_list=[]
    for i in range(digits):
        while True:
            r=randint(1,9)
            if r not in return_list:
                return_list.append(r)
                break
    return return_list
# game
def game(try_count,trials,ans,digits):
    print("Trial #"+str(try_count))
    if try_count==trials:
        print("Last Try!")
    while True:
        try:
            input_number=int(input("Type a valid number: "))
            if not 10**(digits-1)<=input_number<10**digits:
                print("Wrong digits!")
                continue
            input_number_list=[int(x) for x in str(input_number)]
            if 0 in input_number_list:
                print("'0' is not allowed. Try another one.")
                continue
            if len(set(input_number_list))!=digits:
                print("Each number should be different")
                continue
            break
        except:
            print("Wrong input!")
            continue
        
    if input_number_list==ans:
        print("Great!",str(digits),"Strikes! You got it right!")
        print("You got it in",str(try_count),"out of",str(trials))
        return True
    
    strike=0
    ball=0
    out=False
    for i in range(digits):
        if input_number_list[i]==ans[i]:
            strike+=1
        elif input_number_list[i] in ans:
            ball+=1
    if strike==0 and ball==0: 
        print("OUT!!!")
        return False
    print(str(strike)+"S "+str(ball)+"B")
    return False
    
    
if __name__=='__main__':
    print("===================================")
    print("WELCOME TO THE BULLS AND COWS GAME!")
    print("===================================")

    while True:
        # how many digits?
        while True:
            try:
                digits=int(input("How many digits? (type 3, 4 or 5) "))
                if digits<3 or digits>5:
                    print("Wrong input!")
                    continue
            except:
                print("Wrong input!")
                continue
            break
        # set trials
        while True:
            try:
                trials=int(input("How many trials will you have? If you want infinite, type 0: "))
                if trials<0:
                    print("Wrong input!")
                    continue
                if trials==0:
                    trials=1000000
                    print("You will have ALMOST INFINITE trials this game.")
                break
            except:
                print("Wrong input!")
                continue
        # set ans
        ans=setRand(digits)
        print("Let's begin the game!!")
        print("===================================")
        tryCount=0
        while True:
            tryCount+=1
            if trials<tryCount:
                print("YOU LOSE!! YOU RAN OUT OF TRIALS!")
                break
            result=game(tryCount,trials,ans,digits)
            if result:
                break

        if input("To continue, press Y: ")!='Y':
            break
        print("===================================")
        print("New Game!")
        print("===================================")



        