---
{
  "module": "proof/statements/PiecesCountedStatement.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/statements/PiecesCountedStatement.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/statements/PiecesCountedStatement.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Pieces with parameters (ρ, c), with «one algorithm … within 2^{cλ} operations»

Definitions and statements only (no theorem, no proof). What an operation is:
proof/machines/QueryMachines/Kernel.lean. Imports proof/machines/QueryMachines/Comb.lean (theorems
on the constructions of proof/machines/QueryMachines/; it holds no definition) and
`PiecesFromEightSquaresStatement.lean` (and through it `AppRunningTimeStatement.lean`,
`AppHalfPiecesStatement.lean`, `PiecesStatement.lean`).

## The sentences of the paper that are stated here

* Definition 7: «Pieces with parameters (ρ, c) consist, for every λ ≥ 1, of an integer d ≥ 1, a
  finite set 𝓘 of integers and functions A_i : ({0,1}^λ)⁴ → ℤ, i ∈ 𝓘, such that: (a) … (b) … (c) |𝓘|
  ≤ (2λ)^c; the number d, the elements of 𝓘 and all values of the A_i and of the functions of these
  factorizations are below
  2^{(2λ)^c} in absolute value; and one algorithm computes each of them, and 𝓘, c^row_i, c^col_i,
  from λ, i and the arguments within 2^{cλ} operations.» This is `IsPieces`, `Exist`.
* After Definition 7: «By Lemma 2, the functions A_0, …, A_t of Definition 5 are pieces with
  parameters (11/12, c) … for every integer c ≥ 8 such that 2^{cλ} exceeds the polynomial running
  times in Lemma 2 for all λ ≥ 1» (`EightSquarePieces`); «We may and do assume c^row_i, c^col_i ≤ 2λ
  … (and c by c + 2 …)» (`MayAssume`).
* Theorem B: «There are pieces with parameters (1/√2, c), for an absolute constant c»
  (`HalfPieces`).

## How to read it

* `Data`: for every λ the integer d, the finite set 𝓘 of integers, the functions A_i and the numbers
  c^row_i, c^col_i (`Pieces.Family λ` of `PiecesStatement.lean`), and the four functions of the two
  factorizations of each A_i. `Data.Is ρ c`: clauses (a), (b) and the sizes of (c).
* `Question`, `Answer`, `Data.answer`: what the one algorithm is asked and what it has to return: d;
  the list of 𝓘, in increasing order; c^row_i or c^col_i; A_i(x, y, u, v); a value of one of the
  four functions. A question about an i outside 𝓘, or with strings of the wrong length, has no
  answer, and nothing is asked of the algorithm there.
* «One algorithm»: ONE step machine `Alg` (`Groundwork.Stepped`) with polynomial-time steps, whose
  input is λ in unary and the question. «Within 2^{cλ} operations»: it halts with the answer within
  2^{cλ} steps.
* An operation is a step of a machine whose steps are polynomial-time in the size of the state, so a
  number of operations means something only with a bound on the sizes of the states (head of
  proof/machines/QueryMachines/Kernel.lean). Here the bound is `room c λ` = (2^{cλ} + (2λ)^c + 8)·((2λ)^c + 8):
  room for as many numbers as there are
  operations or elements of 𝓘, each of the size that (c) allows, with a little to spare for the
  question. This is the case «S is exponential in a parameter» of that head. The number of steps
  alone bounds little: a state can grow to this size in few steps, and one step can then do work
  polynomial in it. So the clause amounts
  to: a Turing machine answers within 2^{O(λ)} steps, where the O depends on c and on the degree of
  the certificate of Alg. This costs nothing where c is only said to exist (Theorem B, Lemma 2's
  pieces) and nothing where the pieces are an oracle; but «the same c» as for operations on words is
  not what it says.
* `Data.oracle`, `price`: the pieces as an oracle whose query (λ, question) costs 2^{cλ} + 2
  operations: those of the algorithm, and two for handing over the question and taking the answer,
  which is what the cost model of proof/machines/QueryMachines/Kernel.lean charges when a query is
  answered by running a machine. This is the form in which
  the proof of Theorem A (b) uses the pieces: its networks, to which Lemma 8 is applied, ask them.
  `OracleFromAlgorithm` is the step from the oracle to the algorithm.

## Where these statements differ from the printed sentences

* Steps of a step machine, with the bound on the sizes of its states, in place of operations of a
  word RAM; λ in unary; strings as lists of bits.
* `AppRunningTime.IsPieces` (`AppRunningTimeStatement.lean`) renders the last clause of (c) by a
  padding string, has six programs in place of one algorithm, and numbers 𝓘 from 0. `FromPadded` is
  the step from there to here; it changes c. Its algorithm writes the padding string, one unit in
  each step, and then does the work in a single
  step: the extreme case (3) of the head of proof/machines/QueryMachines/Kernel.lean. It is honest
  only because `room` is in the statement. So Theorem B in this form says of the running time what
  `AppRunningTime.ThmHalfPieces` says, in other words; the procedures of «Sizes and operations» are
  not run step by step. 

 ### The data, and clauses (a), (b) and the sizes of (c) 

### `Data`

 For every λ: d, 𝓘, the A_i, c^row_i, c^col_i (`fam λ`), and the functions of the factorizations:
`fn λ tr side i z θ`, where tr = false is the factorization as a function of (x, y) and (u, v) and
tr = true that as a function of (x, u) and (y, v); side = false is the function of the first pair
and side = true that
of the second; z is the pair of strings and θ the string of shared bits. 

### `Data.cap`

 c^row_i (tr = false) or c^col_i (tr = true). 

### `Data.Is`

 Definition 7 without its last clause. 

### `Data.Is.rho_ge`

 ½ ≤ ρ < 1 real, c ≥ 1 an integer, d ≥ 1 

### `Data.Is.sum`

 (a) Σ_{i ∈ 𝓘} A_i = d·[x = v][y = u] 

### `Data.Is.row`

 (b) A_i factors through c^row_i bits as a function of (x, y) and (u, v) 

### `Data.Is.col`

 (b) and through c^col_i bits as a function of (x, u) and (y, v) 

### `Data.Is.caps`

 (b) where c^row_i + c^col_i ≤ 4ρλ + c·log(2λ) 

### `Data.Is.card`

 (c) |𝓘| ≤ (2λ)^c 

### `Data.Is.size_d`

 (c) d, the elements of 𝓘 and all values of the A_i and of the functions of these
      factorizations are below 2^{(2λ)^c} in absolute value 

 ### The last clause of (c): one algorithm 

### `Question`

 What the algorithm is asked, beside λ: d; 𝓘; (tr, i): c^row_i or c^col_i; (i, (x, y, u, v)):
A_i(x, y, u, v); ((tr, side), i, (z₁, z₂, θ)): a value of one of the four functions. 

### `Answer`

 An answer: an integer, or (for 𝓘) a list of integers. 

### `toBits`

 A list of bits as a string of n bits. 

### `Data.answer`

 The right answer for the strings of λ bits. A question about an i outside 𝓘, or with strings of
the wrong length, has none. 

### `Data.oracle`

 The pieces as an oracle: the query is (λ in unary, question), λ ≥ 1. 

### `steps`

 The number of operations that (c) allows for strings of λ bits: 2^{cλ}. 

### `price`

 The price of a query to the pieces as an oracle: 2^{cλ} operations, and two for handing over the
question and taking the answer. 

### `room`

 The bound on the sizes of the states of the algorithm: (2^{cλ} + (2λ)^c + 8)·((2λ)^c + 8). 

### `Computes`

 «One algorithm computes each of them, and 𝓘, c^row_i, c^col_i, from λ, i and the arguments
within 2^{cλ} operations.» 

### `IsPieces`

 **Definition 7.** D, with the algorithm Alg, are pieces with parameters (ρ, c). 

### `Exist`

 «There are pieces with parameters (ρ, c).» 

### `ToPure`

 Clauses (a), (b) and the sizes of (c) as pure mathematics (`Pieces.Family.Is`) follow. 

### `GrowWithTheParameters`

 The bound of (b) only weakens when ρ or c grows, and so do the sizes and the number of
operations: pieces with parameters (ρ, c) are pieces with parameters (ρ', c') for ρ ≤ ρ' < 1 and c ≤
c'. 

 ### From the oracle to the algorithm 

### `passOrRun`

 The machine that answers a query of either kind: a query of the first kind is asked again and
its answer handed back; a query to the pieces is answered by running Alg. 

### `withAlgorithm`

 M with the queries to the pieces answered by running Alg. 

### `OracleFromAlgorithm`

 From the oracle to the algorithm. Let M be any machine with two kinds of queries, of which the
second are queries to the pieces, and let it ask the pieces only for strings of at most Λ bits. If M
returns b within T operations when the pieces are an oracle at the prices `price c` and a query x of
the first kind
costs w x + 2, then `withAlgorithm M Alg` returns b within T operations when x costs w x. Its states
are larger by the room of the algorithm at Λ and by the size S_Q of a query of the first kind with
its answer. 

 ### From the padding string 

### `ofPadded`

 The data that belong to pieces in the sense of `AppRunningTime.IsPieces`, for a padding string
of 2^{cλ} units: 𝓘 = {0, …, cnt − 1} shifted by `shift λ`. 

### `FromPadded`

 From the padding string to counted operations. Pieces with parameters (ρ, c) in the sense of
`AppRunningTime.IsPieces` are, with a larger constant c', pieces in the sense of this file, for
every shift of the index set that is computed in polynomial time from λ in unary and is below
2^{(2λ)^c} − (2λ)^c in absolute value. The
algorithm writes the padding string, one unit in each step, and then runs the program that is asked
for in one step. 

 ### The sentences after Definition 7 

### `MayAssume`

 «We may and do assume c^row_i, c^col_i ≤ 2λ: … a longer factorization is replaced by this one
(and c by c + 2, which pays for computing c^row_i or c^col_i first).» Pieces with parameters (ρ, c)
give pieces with parameters (ρ, c + 2) with the same d, 𝓘 and A_i and with all numbers of bits at
most 2λ. 

### `EightSquarePieces`

 «By Lemma 2, the functions A_0, …, A_t of Definition 5 are pieces with parameters (11/12, c),
with 𝓘 = {0, …, t}, d = 2^t and the numbers c^row_i, c^col_i defined there … This holds for every
integer c ≥ 8 such that 2^{cλ} exceeds the polynomial running times in Lemma 2 for all λ ≥ 1.» There
is ONE algorithm, and a
number c₀ ≥ 8, such that for every c ≥ c₀ the data made from Lemma 2's functions, with this
algorithm, are pieces with parameters (11/12, c); and these data are as the sentence says. (The
programs of Lemma 2's functions do not read the padding string, so `ofPadded` is taken with c = 0
there, a padding string of one unit. They are
polynomial-time, so the algorithm need not count operations: it writes that one unit and answers in
the next step, two steps in all, and c₀ comes from the sizes alone.) 

 ### Theorem B 

### `HalfPieces`

 **Theorem B**, for the functions of its proof: there are pieces with parameters (1/√2, c), for
an absolute constant c, namely, with h = `AppHalfPieces.hOf λ` and μ(x) the partition of h with
number x in the lexicographic list: 𝓘 = {−2h, …, 2h}, d = h!, A_s = `AppHalfPieces.piece`, c^row_s =
⌈log R^row_s⌉ and c^col_s = ⌈log R^col_s⌉. 

### `HalfPiecesExist`

 Theorem B in the paper's words. 

### `HalfPiecesFrom`

 The step: Theorem B in this form, from Theorem B with the padding string
(`AppRunningTime.ThmHalfPieces`) and `FromPadded`, with the index set shifted by −2h. 
