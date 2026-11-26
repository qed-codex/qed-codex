---
{
  "module": "proof/rates/CountedToPadded/Defs.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/CountedToPadded/Defs.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/CountedToPadded/Defs.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # From counted operations to the padding string

Definitions and statements only; nothing is proved here.

**Why.** Appendix D, the joining theorem and the Main Theorem of this development stand on
`ClauseBound.Alg.Solver` with `Solver.Seq` (proof/rates/ClauseBound/Alg/Interfaces.lean): an
algorithm for cliques is a polynomial-time function of (padding string, index, instance with its
tables written out) that is right once the padding string has 2^need units. Theorem A (b) and the
hypothesis of Theorem D (a) speak of ONE algorithm with query access and of its number of operations
(`CliqueLevels.Solves`). This file is the step from the second form to the first, for EVERY machine
M: `solverOfMachine M num C₀` is a definition, a function of M and of its certificate of
polynomial-time steps (the cut reads the coding of the states, which comes with the certificate; on
the inputs of which `Solver.Correct` speaks the result does not
depend on it). So a statement about `solverOfMachine M` has a binder `[IsPolyQ M]`.

**What is here.**
* `runFor N fuel room a`: the step machine N on the input a, run for as many steps as `fuel` has
  units; a state whose word has more than `room` symbols ends the run without a result.
  `RunForIsRight`: it returns the result of N if N halts within that many steps on states that are
  small enough. `RunForPoly`: it is
  polynomial-time in (fuel, room in unary, a) if N has polynomial-time steps, whether or not N
  halts.
* `EveryWordIsCompared`: whether the word of a value is at most as long as a given padding string is
  decided in polynomial time, for EVERY coding. This development can compute the length of the word
  for the codings of numbers, pairs and lists (`PaddedDescent.F.Meas`); the coding of the states of
  M comes with the certificate of M and is arbitrary, so
  `RunForPoly` needs this in general.
* `entry`, `lookup`, `onTables M`: the queries of M answered from tables that are written out
  (`QueryMachine.plug`). `bitsOfTables`: the number B that M is given; an instance here does not
  hold it.
* `needOf`, `solverOfMachine`, `pickOf`; `SolverOfMachineLevels`, the main statement.

**Where the solver differs from the machine.**
* The sequence of levels is for e′_ℓ = `CliqueLevels.cutNumber K num ℓ`, the number in [e_ℓ, 2e_ℓ]
  that can be computed, cut at 1, and not for e_ℓ: the exponent `need` must be computed, e_ℓ is a
  real number, and `Solves` says only that some number of operations below the bound exists.
* The constant is 2C₀ + 1 in place of C₀. It does not depend on the certificate of M: the padding
  string has to be as long as the run (three times the number of operations) and as the states of M,
  not as the run of a Turing machine.
* The tables do not have to fit into the padding string: a state of `onTables M` holds them twice,
  and the room that `solverOfMachine` allows is 7 times the padding string and 14 times the word of
  the tables. (For small e_ℓ and large λ the tables, of 2^{(K−1)λ} entries each, are longer than
  2^need.)
* M is given B′ = the largest number of bits of an entry, at least 1. If all entries are at most 2^B
  in absolute value, as `ClauseBound.Alg.WFe` says, then B′ ≤ B + 1 and all entries are below
  2^{B′}, as `Solves` asks. So `need` is the bound at B + 1. 

 ### A step machine run on a padding string 

### `stay`

 One step of N; a state that has halted stays as it is. 

### `cutAt`

 x if its word has at most `room` symbols, else nothing. (This is `PaddedDescent.F.cap` with a
padding string of `room` units and `none` as the value to fall back on.) 

### `runFor`

 N on the input a, run for as many steps as `fuel` has units. A state whose word (as an optional
value) has more than `room` symbols ends the run. The result, if N has halted. 

### `RunForIsRight`

 If N halts on a with the result b within T steps on states of size at most S, then `runFor`
returns b once the fuel has at least T units and the room is at least 7S + 2. (`Carried`: the word
of a state has at most 7 times its size minus 2 symbols; as an optional value it has 4 more.) 

### `EveryWordIsCompared`

 Whether the word of a value has at most as many symbols as a padding string has units is decided
in polynomial time, for every type and every coding. (A machine sees the word and not the type. The
proof visits the nodes of the tree that the word writes, one in each round, for as many rounds as
the padding string has units, and counts their symbols.) 

### `RunForPoly`

 `runFor N` is polynomial-time in the fuel, the room in unary and the input, for every step
machine N with polynomial-time steps. Nothing is asked of the runs of N. 

### `RunForPolyFrom`

 `RunForPoly` follows from `EveryWordIsCompared`. 

 ### Tables that are written out 

### `entry`

 The entry that the query (w, z) of Definition 3 names in tables that are written out: row w,
place z read as a number, low bit first; 0 if there is no such place. It is
`PaddedDescent.F.look T (w, ls)` for every list ls of strings whose concatenation is z. 

### `lookup`

 The step machine that answers a query from the tables, in one step. 

### `bitsOfTables`

 The largest number of bits of an entry, at least 1. 

### `TablesValue`

 The value of the clique of Definition 3 with the tables read from T is the sum that this
development calls the value of the instance (λ, T). (It is `Printed.StCliqueValue` for these
tables.) 

### `BitsOfTablesFacts`

 B′ = `bitsOfTables T` is at least 1, and all entries are below 2^{B′} in absolute value; if all
entries are at most 2^B in absolute value (`ClauseBound.Alg.WFe`), it is at most B + 1. 

### `onTables`

 M with its queries answered from tables that are written out; the input is (tables, (ℓ, λ, B)). 

### `OnTablesState`

 The states of `onTables M`. 

### `ceilMul`

 ⌈min(a/b, 1)·n⌉ in natural numbers, for b > 0. (For b = 0 it is n, while a fraction with the
denominator 0 is 0 in Lean's real numbers. Under `Levels` and `NumberBetween` the denominator is not
0, which is why the statements on `needOf` have these premises.) 

### `needOf`

 The exponent of a padding string that suffices, from ((ℓ, K_ℓ), λ, B), all in unary: ⌈e′K²λ⌉ +
C₀K²·(number of bits of K(λ + B + 1)) + 2, where e′ = min(a/b, 1) for the numerator a and the
denominator b that `num` returns. 

### `solverOfMachine`

 **The solver that a machine gives.** The index is (ℓ, K_ℓ), both in unary. `run`: M on (ℓ, λ,
B′), its queries answered from the tables of the instance, for as many steps as the padding string
has units, in room for 7 times the padding string and 14 times the word of the tables; 0 if that
gives no result. The coding
of the states of M, which the cut looks at, is that of the certificate of M: the solver is a
function of M AND of its certificate, and whoever speaks of it needs a binder `[IsPolyQ M]`. 

### `pickOf`

 From a bound b in unary: the largest ℓ with K_ℓ ≤ b, in unary, and its index (ℓ, K_ℓ); for b <
K₀ it is ℓ = 0 with its index. `kf` is the function of `CliqueLevels.ComputesLevels`, K₀ the number
K at the level 0. Since K_ℓ > ℓ, only ℓ ≤ b are tried; ℓ in unary is the list of the first ℓ units
of b. 

### `cutFraction`

 The fraction that `num` returns, cut at 1. 

 ### The statements on the solver 

### `CutNumberFacts`

 The number e′_ℓ = `cutNumber K num ℓ` lies in [e_ℓ, 2e_ℓ], is positive and at most 1, and is
itself computed from ℓ and K_ℓ in polynomial time, as the fraction `cutFraction num`. So the clause
«a number in [e′_ℓ, 2e′_ℓ] can be computed» holds for the new sequence too. 

### `PrecisionCarriesOver`

 The form of Theorem D (a) in `MainTheoremForms.ThmVariablesA` takes, in place of the number in
[e_ℓ, 2e_ℓ], a precision function for the numbers e of the sequence of levels
(`MainTheoremForms.Precision`). It carries over from e to every e′ with e_ℓ ≤ e′_ℓ ≤ 2e_ℓ and e′_ℓ ≤
1, with twice the constant: 2/e ≤ 4/e′ ≤ (2/e′)². 

### `NeedSuffices`

 The exponent, from below: 2^need is at least 4 times the printed bound for e′, C₀ and B + 1. 

### `NeedIsSmall`

 The exponent, from above: need ≤ e′K²λ + (2C₀ + 1)·K²·log(K(λ + B)). 

### `SolverOfMachinePoly`

 The solver is polynomial-time, for every machine with polynomial-time steps and every
polynomial-time `num`. Nothing is asked of what M computes. 

### `SolverOfMachinePolyFrom`

 `SolverOfMachinePoly` follows from `RunForPoly`. The certificate of `onTables M` to which
`RunForPoly` is applied has to be `QueryMachine.plug_isPolyT M lookup` with `IsPolyT.ofFun` for
`lookup`: its coding of the states is by definition the one in `solverOfMachine`. (`StPolyPlug` says
only that some certificate exists, and
so does not fix the coding.) 

### `PickOfFacts`

 The program that picks the level: it is polynomial-time, returns an index of the sequence, the
largest one whose K is within the bound. 

### `SolverOfMachineLevels`

 **The main statement.** Let M be a machine with query access and polynomial-time steps (with any
certificate of that) which, given ℓ, λ, B and query access to tables with |W_w| < 2^B, outputs the
value of the (K_ℓ, λ)-clique within 2^{e_ℓK_ℓ²λ}·(K_ℓ(λ+B))^{C₀K_ℓ²} operations on states of at most
that size; let K and e
be as in the hypothesis of Theorem D (a), K_ℓ computed by `kf` and a number in [e_ℓ, 2e_ℓ] by `num`.
Then the named solver `solverOfMachine M num C₀` is polynomial-time and has a sequence Q of levels
for the numbers e′_ℓ = `cutNumber K num ℓ` with the constant 2C₀ + 1, whose ℓ-th index is (ℓ, K_ℓ),
so that K at this
index is K_ℓ, and whose level is picked by the named program `pickOf kf (K 0)`. (The fields of Q
say: K_ℓ ≥ 2, K_ℓ < K_(ℓ+1) ≤ K_ℓ^(2C₀+1), (log K_ℓ)^(−2C₀−1) ≤ e′_ℓ ≤ 1, the solver is right when
the padding string has 2^need units, and need ≤ e′_ℓK_ℓ²λ + (2C₀+1)K_ℓ²·log(K_ℓ(λ+B)).) 

### `SolverOfMachineLevelsFrom`

 The main statement follows from these: `StPlug` (queries answered by a step machine), and the
statements of this file on the run, the tables, the number e′, the exponent, polynomial time and the
program that picks the level. 
