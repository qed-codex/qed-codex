---
{
  "module": "Paper/Tree.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Paper/Tree.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/vp-vnp/Paper/Tree.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```


# The paper, section "Networks are sums of thin trees": Theorem thm:tree

A network is given by numbers of units between pairs of nodes and, at every node, a table of the bits of the units at
it. The moves of the tower plan rewrite its value as a sum, over good outcomes, of values of networks on trees.


### `NetUnit`

 The units of a network with n a c units from a to c. 

### `NodeTable`

 A table of the node a, with values in R, of the contents of the units at a. 

### `netValue`

 The value of a network: the sum over all contents of the units of the product of the tables. 

### `lawMap`

 A law over A is a law over every A-algebra. 

### `flagMap`

 The laws at the vertices of a tower, over an A-algebra. 

### `startTab`

 The tables with which the moves start: every node of the network has its table, applied to the units at it, and
every other node the table 1. 

### `posVal_start`

 The position with which the moves start has the value of the network. 

### `ThinTrees`

 The networks on trees of Theorem thm:tree, for networks on AA nodes with units of ℓ bits, at most N units at a
node and at most M nodes, over R, with the exponent C, the gain γ and the integer G₁ of the test for good outcomes.
The nodes are the parties 0, ..., AA + A' − 1. For numbers n of units and outcomes o the units of the tree are those
that are current at the end, plan.cur. A unit from a node to itself is allowed; it stays at its node, whose value sums
over it. 

### `ThinTrees.A'`

 the number of further nodes 

### `ThinTrees.E`

 the number of moves 

### `ThinTrees.U1`

 a bound for outcomes 

### `ThinTrees.sys`

 the moves 

### `ThinTrees.plan`

 the units given in the moves, their numbers, and the good outcomes 

### `ThinTrees.cap`

 a bound for the units of one move 

### `ThinTrees.ok`

 the plan is causal and gives only current units between the ends of their slots 

### `ThinTrees.stage`

 the stage of a node 

### `ThinTrees.depth`

 the depth of the tree 

### `ThinTrees.root`

 the root 

### `ThinTrees.par`

 the parent of a node 

### `ThinTrees.up`

 the number of units between a node and its parent, as the program bounds it: the load at the node 

### `ThinTrees.dead`

 the dead units 

### `ThinTrees.isLaw`

 is the move a law move? 

### `ThinTrees.good_iff`

 what good means 

### `ThinTrees.poss_good`

 every possible outcome is good 

### `ThinTrees.copies_le`

 copies: what a node ever holds, with the zeros in slots and the counts of the moves, against the units that it
  has in the end 

### `goodBound`

 The integer of the test for good outcomes: "the test for good outcomes compare[s] integers, as C₀ is an integer". 

### `cutUnits_id_cur`

 Without units from a node to itself every current unit joins two nodes: thin trees give the printed formula. 

### `thm_tree_good`

 **Paper: the paragraph before Theorem thm:tree.** "An outcome is good if ‖o‖_* ≤ √C₁a₁t and o_e ≥ t for all e":
at a law move the integer test of the trees of thm_tree implies this, and is equivalent to it when 2C₁a₁² is an
integer, as it is for C₁ = 4C₀ with the integer C₀ of the laws. 

### `ndStage`

 The stage of a node of the tree. 

### `ndPar`

 The parent of a node of the tree. 

### `treePar`

 The parent of a party. 

### `treeUp`

 The load at a party: the number of units between it and its parent. 

### `cur_tree`

 Every unit of the end is dead or lies between a chamber and its parent. 

### `layers_le_seen`

 The law moves at a node have no more layers than the node has units. 

### `thm_tree_poss_good`

 "Every possible outcome is good, by Theorem thm:laws(b), the triangle inequality over the tℓ layers, and λ ≥ 1." 

### `tree_slp`

 The program of the tower plan, with the parents and the loads. 

### `par_computed`

 Parents are computed: the indicator of "q is the parent of p". 

### `const_mul_pow_le`

 A constant times a power is a higher power. 

### `cKap`

 The constant in front of the bounds for loads. 

### `gain_rpow`

 The gain, as a power of M. 

### `const_pow_le`

 Powers of a constant times Z are powers of Z. 

### `tree_nums`

 Units are few: the bounds in numbers. 

### `card_treeChildren`

 The children of a node are few. 

### `tree_node_le`

 The units at one node. 

### `tree_total_le`

 All units of the tree. 

### `tree_between`

 The units between a party and its parent are at most the load at it. 

### `tree_up_node`

 The loads at one node. 

### `tree_up_total`

 All loads. 

### `onN_le_up`

 The loads at a chamber and below its children are those at the party and its children. 

### `thm_tree_copies`

 **Paper: proof of Theorem thm:tree, Bounds.** The Lean form of "At no time does a node hold more than a constant times
the units that it has in the end ...": relays leave copies here, so what a node ever holds, zeros in slots included, is at
most a constant times the loads at it and its children, plus (1+8m)N at a given node (m bounds the words) and twice the
dead units at it. 

### `tree_value`

 The network is the sum of the networks on trees. 

### `tree_computed`

 The program that computes the trees. 

### `thm_tree_start_units`

 **Paper: Theorem thm:tree, Start.** "Hence every edge gets at most n₀ = 4L(N+M²) units." 

### `_root_.Nc.Tow.Routes.mono`

 More generous routes. 

### `tree_towers`

 "Take the least n ≥ 1 with M ≤ |G_n|; so |G_n| = O(M)": towers of all sizes from Proposition prop:tower, whose
parts (c) and (d) give the size, the bottom and the words of the routes. 

### `cTree`

 The exponent of the trees of a tower with the constant c. 

### `exists_thinTrees`

 The thin trees of one tower. 

### `thm_tree`

 **Paper: Theorem thm:tree.** "There is a constant C with the following property. Let M ≥ 2, let ℓ, N ≥ 1, and let a
network over an A-algebra have at most M nodes, no unit from a node to itself, and at most N units at each node. Its
value is the sum, over a set of choices o (sequences of good outcomes), of values of networks with the following
properties. Put Λ = (lg M)^C, where lg M = ⌊log M⌋+1, and γ = 1/log b. (a) The nodes form a rooted tree of depth at most
Λ, by stages: the given nodes are of stage 0, every node but the root has its parent in the next stage and at most b
children, and the root has at most C. (b) A set of at most M^C dead units may join any two nodes. All others join a node
and its parent; their number is at most ΛM^(1−γ)(N+M²) for one node, its children included, and ΛM(N+M²) in all. (c)
The table of a node is the given one (or 1) times the tables of the moves at it, summed over the units that they have
used up. At stage 0 these are tests only; elsewhere they are tests and table entries of laws, and the numbers of
layers of the law moves at a node add up to at most the number of bits of all units that it ever holds. (d) The parents,
the units present, the units and numbers of the moves, and which outcomes are good are computed from o and the given
numbers of units by a straight-line program with at most (MN)^C steps on numbers below (MN)^C. A step is an input, a
constant, or an arbitrary function of two earlier results, given by its table (a binary operation). The program does not
depend on the numbers of units, the outcomes or the tables." The tests are relays, and the laws are the fixed list, mapped to R. A move of num
units uses num·ℓ layers, so (c) is stated as num summed over the law moves at a node against the units ever seen at it
(seenAt). Units from a node to itself are also allowed: they stay, and their node sums over them (the printed formula is
the case without them, cutUnits_id_cur). The operations of (d) are those of a straight-line program that may depend on M, N and ℓ. 
