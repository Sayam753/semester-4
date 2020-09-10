# Learning prolog

```prolog
halt.
[db].
consult('db.pl').
<!-- importing -->
listing.
write('Hello World'), nl, write('Let\' Program').

male(bhagat).  - no
listing(male).  - all entires of male

female(shivani).  - yes
listing(female).  - all entries of female

male(X), female(Y). - Cycle through all combinations

parent(X, bob).

parent(X, bob), dances(X).  --parent of bob who dances

parent(Y, carl), parent(X, Y). --carl grand parents
parent(albert, X), parent(X, Y).  --grandchildren of albert

parent(X, carl), parent(X, charlie). --share a parent

owns(albert, pet(cat, X)).

customer(sally, _, B).

vertical(line(point(3, 1), point(3, 12))).

alice = alice.
'alice' = 'alice'.

\+ ('alice' = 'alice'). -- not equal
3>=15.
3=<15.
```

```bash
[db].
common_genus(red_wolf, dog).
common_genus(red_wolf, A).

common_species(dog, A).
common_species(gray_wolf, A).
common_species(dog, fennec_fox).

relation_path(gray_wolf, dog, Z).
relation_path(african_wild_dog, dog, Z).
relation_path(african_wild_dog, fennec_fox, Z).
```
