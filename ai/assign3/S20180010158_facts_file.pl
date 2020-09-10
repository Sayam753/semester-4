species_name(african_wild_dog, lycaon_pictus).
species_name(common_fox, vulpes_vulpes).
species_name(arctic_fox, vulpes_lagopus).
species_name(fennec_fox, vulpes_zerda).
species_name(red_wolf, canis_rufus).
species_name(coyote, canis_latrans).
species_name(gray_wolf, canis_lupus).
species_name(dog, canis_lupus_familiaris).

sub_species(canis_lupus_familiaris, canis_lupus).

species_genus(lycaon_pictus, lycaon).
species_genus(vulpes_vulpes, vulpes).
species_genus(vulpes_lagopus, vulpes).
species_genus(vulpes_zerda, vulpes).
species_genus(canis_rufus, canis).
species_genus(canis_latrans, canis).
species_genus(canis_lupus, canis).


genus_family(lycaon, canidae).
genus_family(vulpes, canidae).
genus_family(canis, canidae).


% Question - common-genus 
% X and Y do not have sub_species
common_genus(X, Y) :-
    species_name(X, S1),
    species_genus(S1, G),
    species_name(Y, S2),
    species_genus(S2, G).

% Only X has a sub_species
common_genus(X, Y) :-
    species_name(X, Sub1),
    sub_species(Sub1, S1),
    species_genus(S1, G),
    species_name(Y, S2),
    species_genus(S2, G).

% Only Y has a sub_species
common_genus(X, Y) :-
    species_name(X, S1),
    species_genus(S1, G),
    species_name(Y, Sub2),
    sub_species(Sub2, S2),
    species_genus(S2, G).

% Both X and Y has a sub_species
common_genus(X, Y) :-
    species_name(X, Sub1),
    sub_species(Sub1, S1),
    species_genus(S1, G),
    species_name(Y, Sub2),
    sub_species(Sub2, S2),
    species_genus(S2, G).


% Question - common-species 
% X and Y do not have sub_species
common_species(X, Y) :-
    species_name(X, S),
    species_name(Y, S).

% Only X has a sub_species
common_species(X, Y) :-
    species_name(X, Sub),
    sub_species(Sub, S),
    species_name(Y, S).

% Only Y has a sub_species
common_species(X, Y) :-
    species_name(X, S),
    species_name(Y, Sub),
    sub_species(Sub, S).

% Both X and Y has a sub_species
common_species(X, Y) :-
    species_name(X, Sub1),
    sub_species(Sub1, S),
    species_name(Y, Sub2),
    sub_species(Sub2, S).



% Question - relation-path 
% utility common-family
common_family(X, Y) :- 
    species_name(X, S1),
    species_genus(S1, G1),
    genus_family(G1, Z),

    species_name(Y, S2),
    species_genus(S2, G2),
    genus_family(G2, Z).


common_family(X, Y) :- 
    species_name(X, Sub1),
    sub_species(Sub1, S1),
    species_genus(S1, G1),
    genus_family(G1, Z),

    species_name(Y, S2),
    species_genus(S2, G2),
    genus_family(G2, Z).


common_family(X, Y) :- 
    species_name(X, S1),
    species_genus(S1, G1),
    genus_family(G1, Z),

    species_name(Y, Sub2),
    sub_species(Sub2, S2),
    species_genus(S2, G2),
    genus_family(G2, Z).


% Finding by common_species
relation_path(X, Y, Z) :-
    common_species(X, Y),
    species_name(X, S1),
    species_name(Y, S2),
    sub_species(S2, Sub),
    Z = [X, S1, Sub, S2, Y].


% Finding by common_genus
relation_path(X, Y, Z) :-
    common_genus(X, Y),
    species_name(X, S1),
    species_name(Y, S2),
    species_genus(S2, G),
    Z = [X, S1, G, S2, Y].


relation_path(X, Y, Z) :-
    common_genus(X, Y),
    species_name(X, Sub1),
    sub_species(Sub1, S1),
    species_name(Y, S2),
    species_genus(S2, G),
    Z = [X, Sub1, S1, G, S2, Y].


relation_path(X, Y, Z) :-
    common_genus(X, Y),
    species_name(X, S1),
    species_name(Y, Sub2),
    sub_species(Sub2, S2),
    species_genus(S2, G),
    Z = [X, S1, G, S2, Sub2, Y].


% Finding by Family
relation_path(X, Y, Z):-
    common_family(X, Y),
    species_name(X, S1),
    species_genus(S1, G1),

    species_name(Y, S2),
    species_genus(S2, G2),
    genus_family(G2, F),
    Z = [X, S1, G1, F, G2, S2, Y].


relation_path(X, Y, Z):-
    common_family(X, Y),
    species_name(X, Sub1),
    sub_species(Sub1, S1),
    species_genus(S1, G1),

    species_name(Y, S2),
    species_genus(S2, G2),
    genus_family(G2, F),
    Z = [X, Sub1, S1, G1, F, G2, S2, Y].


relation_path(X, Y, Z):-
    common_family(X, Y),
    species_name(X, S1),
    species_genus(S1, G1),

    species_name(Y, Sub2),
    sub_species(Sub2, S2),
    species_genus(S2, G2),
    genus_family(G2, F),
    Z = [X, S1, G1, F, G2, S2, Sub2, Y].