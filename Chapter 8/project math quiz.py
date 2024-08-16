import pyinputplus as pyip
import random, time

numberofQuestions = 10
correcAnsers = 0
for questionNumber in range(numberOfQuestions):
    ## pick two random numbers:
    num1 = random.randint(0,9)
    num2 = random.randint(0,9)

    prompt = '#%s: %s X %s = ' % (questionNumber, num1, num2)

    try:
        #right answers are handled by allow Regexes
        # Wrong answers are handles by blockRegexes, with a custom message.
        pyip.inputStr(promp, allowRegexes=['^%$' % (num1 * num2)],
                      blockRegexes=[('.*', 'Incorrect!')],
                      timeout=8, limit=3)
    except pyip.TimeoutException:
        print('Out of time')
    except pyip.RetryLimitException:
        print('Out of Tries.')
    else:
        #This block runs if no exceptions were raised in the try block
        print('Correct!')
        correctAnswers +=1

        time.sleep(1) #Brief pause to let user see the result.
    print('Score: %s / %s' % (correctAnswers, numberofQuestions))