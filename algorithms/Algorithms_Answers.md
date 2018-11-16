Add your answers to the Algorithms exercises here.

**Exercise I**:

1. a = 0 is O(1)
   while (a < n * n * n) is O(n) because we are looping for n times
    a = a + n * n is O(1)

   So, *O(n)* because O(n) could be greater than O(1). If the while loop was constant it could have been different, but since we are looping *n* times and n keeps changing, it becomes O(n)

2. sum = 0 is O(1)
    for (i = 0; i < n; i++) is O(n)
      for (j = i + 1; j < n; j++) is O(n)
        for (k = j + 1; k < n; k++) is O(n)
          for (l = k + 1; l < 10 + k; l++) is O(n)
            sum++ is O(1)
    so we have O(1) + O(n) * 4 + O(1) = O(n) * 4 = O(4n) = O(n)
    so the answer would be *O(n^4)* because the first two are constant while the 4 for loops are O(n) but changing the value making more operations

3. bunnyEars = function(bunnies) {
      if (bunnies == 0) return 0
      return 2 + bunnyEars(bunnies-1)
    }

    *O(n)* because the recursion is calling n times before reaching the base case

**Exercise II**:
n = # of floors
f = floor
e = eggs
eg = # of eggs dropped

// psuedocode

class n():
    top_floor = t
    bottom_floor = b
    floors = x

def breaking_eggs(n, f):
    f = n.floors // 2
    f.drop_egg()

    if e.didn't_break:
        f = (n.top_floor - n.floors) // 2

    if e.did_break:
        f = (n.floors - n.bottom_floor) // 2

    breaking_eggs(n, f)

// strategy

So basically, get the base floor, which which is half of the total floors
and then drop an egg. If it didn't break, set the floor to the top floor - 
total floors divided by two, half of the section we dropped it in. And then 
recursivly call the function again with the # of floors and the current floor
until the lowest # of eggs are dropped and return that value.

The code may not work, but I believe the strategy is in the right direction