---
{
  "module": "proof/machines/QueryMachines/Kernel.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/machines/QueryMachines/Kernel.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/machines/QueryMachines/Kernel.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Machines with query access: own steps and queries are counted (definitions and statements only)

Section 3 of the paper counts time in «operations: operations on words … and table queries», and
Definition 3 says of the tables of a clique: «an algorithm queries them by naming w and z_w ∈ S_w,
and receives W_w(z_w) at the cost of one operation».
The step machines of this development (`Groundwork.Stepped`,
proof/statements/StepMachineStatements.lean) have no way to ask: without this file the number of
queries is not a notion.
This file adds the notion. A `QueryMachine` is a step machine with two more fields: `ask` (in this
state the machine waits for the answer to this query) and `resume` (the state after the answer has
come).
* `Reaches`, `Runs`: the run against an oracle, with the number of own steps and THE LIST OF THE
  QUERIES ASKED, in order.
* `Within`: the cost of a run when the query x costs w x operations. With w = 1 this is the unit of
  cost of Definitions 3 and 4; with w = τ it is Definition 2(iii).
* `close`: the oracle built in, one step per query: a step machine of this development. `plug`: each
  query answered by running a step machine. `subst`: each query answered by running a machine that
  has query access of its own («Answer each of its … queries by computing the entry», proof of Lemma 1).
* `IsPolyQ`: all five functions of the machine are computed in polynomial time.
The statements `St…` at the end are what proof/machines/QueryMachines/ proves about these notions;
all bounds in them are explicit (no unnamed constant).

**What an operation is here, and what a number of operations can hide.** One operation is one
application of `step`, or one query. `step` may be any function that a Turing machine computes in
time polynomial in the length of the word of the state (`IsPolyQ`). The encoding of the states is
chosen with the proof of `IsPolyQ` and need not determine the state. This hides nothing: the machine
is deterministic, so the word of the next state, of a query and of the result depend only on the
word of the state; the words of queries and results determine them (true of the encodings of
proof/machines/ToTuring/Enc.lean for every type used here), so whatever a state holds beyond its
word cannot affect the queries or the result, and `Carried` makes the word at most 7 times the size.
`init`, `out`, `ask` and `resume` are not counted as operations; each is computed in polynomial time
in the length of its argument (`IsPolyQ`), and `exists_tmW` counts `init` and `out`. So one
operation may read and rewrite the whole state, where an operation
of the paper's word RAM touches a bounded number of words. For this reason a number T of operations
means something only together with the bound S on the sizes of all states, and every statement
carries S. What the pair (T, S) can hide is bounded, for step machines on bit strings with a bit
string as result, by a theorem of this development (`CountKSat.exists_tmW`,
proof/consequences/CountKSat/Host.lean):
if the machine has polynomial-time steps and halts within T steps on states of size at most S, ONE
Turing machine of Mathlib does the same within q·(T + 1)·(|x| + S + 1)^q steps, where q depends on
the machine and not on the input: linear in T. It applies to a machine of this file once its queries
are answered by polynomial-time computation (`StPolyClose`, `StPolyPlug`)
and its input and result are written as bit strings. It does not apply to a machine whose oracle is
an arbitrary table (Definitions 3 and 4, Lemma 1); for these the same bound, for a Turing machine
with an oracle, is an argument outside Lean. In the other direction: T operations of a word RAM on a
memory of S bits are T operations here on states of size O(S) (an argument outside Lean).
So an algorithm whose memory is polynomial loses nothing; for one with more memory, this translation
gives no polynomial S. Three cases follow.
(1) S is polynomial in the quantity whose powers the printed bound leaves unnamed: B + λ in
    Definition 4, P + B in Lemma 1. The paper prints no bound on memory there; a bound S = C·(B +
    λ)^C, or S = C₁·(P + B)^{C₁}, on the sizes of the states is a condition that the paper does not
    state. With it the hidden factor is of the kind that the printed bound contains already, and the
    Lean statement gives the printed sentence with a larger unnamed constant.
(2) S is exponential in a parameter. Then T operations may stand for T·2^{O(parameter)} operations
    on words, and a printed bound 2^{c·parameter} follows only with a larger c. No statement of
    proof/machines/QueryMachines/ is of this kind; a statement of Definition 7 (c) in this model
    would be, and would have to say so.
(3) The extreme: a machine may write T units in T operations and then do work polynomial in T in a
    single operation. Nothing in the model forbids this; what shows that a given statement does not
    do it is its S.
A function with a certificate of polynomial time that is to be charged with more than one operation
can be treated as a query priced by `w` and built in at the end (`plug`, `close`).
This file has no proofs. 

 ## The machine 

### `QueryMachine`

 A step machine with query access. Q is the type of queries, A the type of answers. A state s is
read in this order: if `out s = some b` the machine has halted with the result b; else, if
`ask s = some x`, it asks the query x, and goes on in the state `resume s v`
once it has received the answer v; else it makes the step of its own `step s`. The fields σ, init,
step, out and the measure of size are those of `Groundwork.Stepped`. 

 ## Runs against an oracle 

### `Reaches`

 From the state s, with the oracle O: the machine halts with the result b after at most `own`
steps of its own; L is the list of the queries that it asks, in order; all states have size at most
S.
`O x = none` says that x is not a query that the oracle answers: a machine that asks such an x has
no run. So a run also says that every query asked was a legitimate one. 

### `Runs`

 On the input a, with the oracle O: the result is b, after at most `own` own steps and exactly
the queries L, on states of size at most S. 

### `Within`

 On the input a, with the oracle O, **if the query x costs w x operations**: the result is b
within T operations (own steps plus the costs of the queries asked), on states of size at most S. 

### `WithinFrom`

 The same from a state s. 

### `unitCost`

 «At the cost of one operation» (Definition 3). 

 ## Three ways to answer the queries 

### `close`

 The oracle built in: a step machine of this development in which a query is answered in one
step. (At a query that the oracle does not answer the machine stays where it is, and so never
halts.) 

### `plug`

 Each query x is answered by running the step machine R on (c, x); c is a context, handed over
with the input and kept to the end: it stands for whatever the caller holds in memory. A query costs
the steps of R and two more (to start R, to take its result). 

### `subst`

 «Answer each of its … queries by computing the entry» (proof of Lemma 1): each query x of M is
answered by running N on (c, x), where N has query access of its own, to another oracle. The step
machine underneath is `plug M N.toStepped`; the queries of the new machine are those that N asks. 

 ## Polynomial-time steps 

### `IsPolyQ`

 Every part of the machine is computed in polynomial time (`Groundwork.PolyT`: on Mathlib's
multi-stack Turing machines), and the words of its states are at most linear in their size:
`Groundwork.IsPolyT` with the two new fields. The class holds data (the encoding of the states), so
statements say `PolyTimeSteps`. 

### `PolyTimeSteps`

 The machine has polynomial-time steps. Without this a number of steps says nothing, since a step
is an arbitrary function. 

 ## What proof/machines/QueryMachines/ proves about these notions 

### `StMono`

 Bounds may be raised. 

### `StWithinRules`

 The cost from a state, rule by rule: a halted state costs nothing; an own step costs 1; the
query x costs w x. 

### `StUnique`

 The result and the list of the queries are determined by the input and the oracle. 

### `StClose`

 Cost at one operation per query is the number of steps of the step machine with the oracle built
in. (This is what carries the counts proved for the step machines of this development over to
machines with query access.) 

### `StQueriesLe`

 An algorithm that takes at most T operations makes at most T queries. 

### `StSlowDown`

 So if a query costs t ≥ 1 operations in place of one, T operations become at most T·t. 

### `StPlug`

 Queries answered by a step machine: if R answers the query x within t x steps on states of size
at most S', the whole takes own + Σ_{x asked} (t x + 2) steps. R need answer only the queries that
are asked. 

### `StSubst`

 Queries answered by a machine with query access of its own: own steps add up as in `StPlug`, and
the queries asked are those of the answering runs, in order. 

### `StSubstWithin`

 The same in costs: if the query x of M is priced at w x, and N answers it within w x − 2
operations at the prices w', then the whole stays within the cost of M. 

### `StCloseSubst`

 Building the outer oracle into a substitution is plugging in the answering machine with that
oracle built in. 

### `StPolyPlug`

 Polynomial-time steps are kept by `plug` (for `subst` and `close` see `StPolySubst` and
`StPolyClose`). (For tables that are part of the input: `plug` with C the tables and R a machine
that looks an entry up.) 

### `StPolySubst`

 Polynomial-time steps are kept by `subst`. 

### `StPolyClose`

 Polynomial-time steps are kept by `close`, for an oracle computed in polynomial time from the
query alone. 
