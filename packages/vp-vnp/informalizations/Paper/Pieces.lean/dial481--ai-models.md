---
{
  "module": "Paper/Pieces.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Paper/Pieces.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Paper/Pieces.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# The paper, Proposition prop:pieces


### `yOf`

 The contents of the units at a node, as copies of all units. 

### `runTab`

 The tables of the blocks and parts, as tables of the units at them. 

### `prop_pieces_identity`

 "Then apply Theorem thm:tree ... The units between different pieces are the cut units, and the value of a piece sums
over its inner units. Every assignment of units and letters is counted once": the value of one network of Lemma
lem:runnet, by the value of its thin trees and a regrouping of their nodes. 

### `PieceCut`

 The pieces of Proposition prop:pieces for the scale v, K blocks of T steps and the parameter k, with the exponent
C and the list kinds of roles that may occur in moves. An input word is cut into K consecutive parts of ℓ ≤ T symbols;
ρ gives, for every node and side of a tape, the first and the last node that take the symbols of the node, n gives the
numbers of units, o the outcomes, and grp says in which piece a node is. At the beginning a node holds at most load
units. 

### `PieceCut.c`

 bits for a symbol 

### `PieceCut.cb`

 the code of symbols 

### `PieceCut.ub`

 bits of a unit 

### `PieceCut.U0`

 the bound for units between two nodes 

### `PieceCut.load`

 the bound for units at a node at the beginning 

### `PieceCut.unit_le`

 units have at most T bits, and a node starts with few of them 

### `PieceCut.A'`

 the number of further nodes 

### `PieceCut.E`

 the number of moves 

### `PieceCut.U1`

 a bound for outcomes 

### `PieceCut.num`

 the number of pieces 

### `PieceCut.D`

 the digits of the program 

### `PieceCut.steps`

 the steps of the program 

### `PieceCut.sys`

 the moves 

### `PieceCut.plan`

 the plan 

### `PieceCut.cap`

 a bound for the units of one move 

### `PieceCut.ok`

 the plan is causal and gives only current units between the ends of their slots 

### `PieceCut.isLaw`

 is the move a law move? 

### `PieceCut.good_iff`

 what good means 

### `PieceCut.poss_good`

 every possible outcome is good 

### `PieceCut.grp`

 the piece of a node 

### `PieceCut.tab`

 the program that computes units, moves, good outcomes and pieces from n and o 

### `PieceCut.tab_valid`

 it checks that no node has more than load units 

### `PieceCut.digits`

 its numbers have room for the units, the outcomes and the pieces 

### `PieceCut.kinds_mem`

 every role at a move is from the fixed list, so its numbers of channels and slots are bounded 

### `treeAt`

 The tree of the numbers of units and outcomes x. 

### `given`

 The given nodes: blocks and parts. 

### `yhat`

 The bound Ŷ for the total of Theorem thm:tree(b). 

### `pieceAt`

 The piece of a node. 

### `pieceNum`

 The number of pieces. 

### `pieceFin`

 The piece of a node, as a number below the number of pieces. 

### `piece_given`

 "A subtree has at most 4M/k given nodes and a single node has fewer still." 

### `piece_cut`

 "By (b) of the theorem a piece has at most ΛM^(1−γ)Nℓ bits in cut units, besides the dead ones." 

### `piece_all`

 "Units used up and zeros in slots change this by a constant factor only": the bits in all. 

### `slp_inputs`

 The inputs are added to a program. 

### `prop_pieces_program`

 "The units, the pieces and what each table does are computed from the numbers of units and the outcomes": the
program of Theorem thm:tree(d), extended by the pieces and by the check of the numbers. 

### `prop_pieces_dead`

 **Paper: proof of Proposition prop:pieces.** "All M^C dead units together have at most T/v^300 bits." 

### `pieces_numbers`

 The numbers of Proposition prop:pieces: "units of ⌊T/v^a'⌋ bits, so that all M^C dead units together have at most
T/v^300 bits", and N, a bound for the units at a node. 

### `pieces_gain`

 The gain: units at one node against all units. 

### `prop_pieces`

 **Paper: Proposition prop:pieces.** "For every tape automaton over A there are constants a, e, C (a and e do not
depend on the automaton) such that for all large v there is K with v^e ≤ K ≤ Cv^e and the following holds for all
T ≥ v^a with lg T ≤ (lg v)² and all 2 ≤ k ≤ v^64. Cut an input word of at most KT′ symbols, T′ ≤ T, into K consecutive
parts. The value of the automaton in KT steps is the sum, over boundary states, valid data ρ as in Lemma lem:runnet,
numbers of units, good outcomes, and the contents of cut units, of products of the values of at most kΛ pieces. A piece
has at most CK/k blocks and parts, at most KTΛ/v^300 bits in cut units, and at most KTΛ/k bits in all. The units, the
pieces and what each table does are computed from the numbers of units and the outcomes by v^C binary operations on
numbers below v^C."
Here Λ = (lg v)^C, e ≥ 300 (as chosen in the printed proof) and the bound on lg T is not needed; bits in all count every copy that the nodes of the piece ever
hold and the zeros in slots. What a table does is given by the units and the number of each move (cons and num),
because the kind of each role is one of the fixed list of roles of the relay and the laws. A step is one binary
operation on numbers below v^C, in a program that may depend on v, T and k. The proof applies Lemma lem:runnet, then
Theorem thm:tree, and calls the nodes heavy as printed. 
