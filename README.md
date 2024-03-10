# correcto! a bingo card generator
Bingo card Generation 
`./generar_cartones.py -c <How many>`

# Context 
On 18th February 2011, I participated in Interclubes Bingo ( http://www.bingointerclubes.com.ar/ ), 
I didn't win anything, but I had a great time. More than 40,000 people participated, all with the same dream as me: 
to win one of the 21 prizes that were drawn.

One of the questions I asked myself was: How many cards can be issued without any of them being repeated?

Here is the answer, or at least an approximation. Since I don't know exactly the restrictions that a card has to meet, I guess a few things...

A bingo card consists of fifteen numbers, from 1 to 90. But not any set of 15 numbers is a valid card, for example: It is not a valid card that has the numbers: {1, 2, 3, 4, 5, 6, 7, 8, 9, 10,11,12,13,14,15}.

Each card is made up of 9 columns of 3 squares each, the first column corresponds to numbers from 1 to 9, the second from 10 to 19, the third from 20 to 29, etc., and finally the last one from 80 to 90. Each column can be filled with 1, 2, or 3 numbers.
In the following image, we see an example.

![alt text](https://github.com/pablopilotti/correcto/blob/master/bingo-card.jpg?raw=true)

After the brief introduction of what a carton is, we are going to try to count how many different cartons can be issued. 
In the first column the numbers belong to the set {1,2,3,4,5,6,7,8,9}, therefore,

    The number of different columns with a single filled box is: 9
    The number of different columns with two filled cells is: 9*8/2!=36.
    The number of different columns with three filled cells is: 9*8*7/3!=84.

The next 7 columns have a set of 10 numbers, therefore.

    The number of different columns with a single filled box is: 10
    The number of different columns with two full cells is: 10*9/2!=45.
    The number of different columns with three filled cells is: 10*9*8/3!=120.

Finally, the last column has a set of 11 valid numbers, therefore.

    The number of different columns with a single filled box is: 11
    The number of different columns with two filled cells is: 11*10/2!=55.
    The number of different columns with three filled cells is: 11*10*9/3!=165.

Now that we have the columns counted, we need to see how to combine them, since the sum of filled numbers is 15.
To count them I made a program.

The number of cartons he gave me: 6,080,082,602,343,750.

