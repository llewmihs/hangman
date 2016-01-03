#!/usr/bin/python
import random

#def remove_replace(index):
    


#a list of words that might be selected as the secret word
hangman_words = ["hat"] #, "hat", "gift"]

#work out how many possible words there are
no_of_words = len(hangman_words)

#choose a random number 
random_word = random.randrange(0, no_of_words)

#select the random secret word

secret_word = str(hangman_words[random_word])

secret_word_lst = []

for i in secret_word:
    secret_word_lst.append(i)

guess_word = []

for i in range(len(secret_word)):
    
    guess_word.append("-")
    
#guess_word = ["-" * len(secret_word)]

print "Ready to play hangman. Your %s letter word is:" % (str(len(secret_word)))


#print str(guess_word)
print ''.join(guess_word)

#print secret_word_lst

#set number of guesses
guesses_left = 10

guesses_so_far = []

while guesses_left > 0:
    
    guess = str(raw_input("%s guesses left. Guess a letter:" % (guesses_left)))
    guess = guess.lower()
    
    
    
    if guess in guesses_so_far:
        print "You've guessed %s already!" % (guess)
        #guesses_left = guesses_left - 1
        
    elif guess in secret_word_lst:
        guesses_so_far.append(guess)
        
        print "%s is correct" %(guess)
        index = []
        
        for i in range(len(secret_word_lst)):
            if guess == secret_word_lst[i]:
                index.append(i)
        
        for i in range(len(index)):
            guess_word.remove("-")
        
        for i in index:
            guess_word.insert(i, guess)
        
        print ''.join(guess_word)
    else:
        print "%s is incorrect" %(guess)
        print ''.join(guess_word)
        guesses_so_far.append(guess)
    
    if "-" in guess_word:
    	guesses_left = guesses_left - 1
    else:
        guesses_left = 0

if guess_word == secret_word_lst:
    print "Congrats!, you win"
else:
    print "Sorry loser, the word was"
    print ''.join(secret_word_lst)
