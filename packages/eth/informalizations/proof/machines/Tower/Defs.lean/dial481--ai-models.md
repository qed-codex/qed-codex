---
{
  "module": "proof/machines/Tower/Defs.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/machines/Tower/Defs.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/machines/Tower/Defs.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # A tower: one machine for a recursion whose depth is data

Definitions and statements only; nothing is proved here. The machines are
`QueryMachines.QueryMachine` (a step machine with a pending query; `Within O w a T S b`: with the
oracle O, if the query x costs w x operations, the
result on a is b within T operations on states of size at most S; `PolyTimeSteps`).

**Why.** Theorem A (b) says: «One deterministic algorithm, given ℓ ≥ 0, λ, B ≥ 1 and query access to
tables with |W_w| < 2^B, outputs the value of the (K_ℓ, λ)-clique within … operations.» Its proof is
a recursion on ℓ: the
algorithm for K_{ℓ+1} nodes goes through the functions ι : 𝓡 → 𝓘, and for each of them calls the
algorithm for K_ℓ nodes on a clique whose tables, in the words of Definition 3, «are not written
out»: every query of the callee is answered by computing the entry, which
in turn queries the tables of the caller. So at depth ℓ a query of the innermost call runs up
through ℓ procedures. For a fixed depth one could build, by recursion in Lean, one machine and one
type of
states for each ℓ; here ℓ is part of the input, so there must be ONE machine, with one type of
states and one certificate that a step takes polynomial time.

**What is here.**
* `selfCall M`: M may, besides its queries, CALL ITSELF on another input (query `Sum.inr a'`, answer
  `Sum.inr b`). `selfCall M` is ONE machine that runs M with all its calls; its state is the list of
  the activations of M, the running one first.
  `SelfCallPoly`: it has polynomial-time steps if M has. `SelfCallRuns`: if M, with every call of a'
  answered by `val a'` at the price `T a' + 2`, returns `val a` at the cost `T a`, and calls go down
  in a measure `dep`, then `selfCall M` returns `val a` at the cost `T a`.
* `nest Sol Inn`, `tower Sol Inn`: the shape of the appendix's recursion. A solver `Sol` (input: a
  context c; it may call the solver on another context c', query `Sum.inl c'`, and may query its own
  tables, `Sum.inr (Sum.inl q)`) and a procedure `Inn`
  (input: the context c' of a callee and a query q of that callee to its tables; it may query the
  tables of the caller, `Sum.inl q'`). The tables of a callee are a function of the caller's tables,
  so the recursion is of higher order as printed. It
  becomes a machine that calls itself when every activation carries the list `env` of the contexts
  through which its table queries have to run up: a query with `env = []` goes to the tables of the
  outermost instance, and a query
  with `env = c :: env'` is a call of the procedure on c, whose own queries run up through `env'`.
* A second kind of query, of type G, is the same at every depth and is passed on unchanged
  (`Sum.inr g`): for what every level may ask, such as the algorithm of the pieces, or a certified
  function used as one instruction at a price. Take G empty if there is none.
* `TowerPoly`: the tower has polynomial-time steps if `Sol` and `Inn` have.
* `TowerRuns`: the tower returns the value, within the cost given by the recursion `cost`: T(ℓ+1, t) =
  T_Sol(ℓ+1; a call costs T(ℓ, T_Inn(ℓ, t) + 2) + 2, a query costs t). With T_Sol = own +
  calls·(cost of a call) and T_Inn = own' + q'·t
  (`CostShape`, `CostSlowDown`) this is the recursion behind the display «So the total number of
  operations is at most …» in the proof of Theorem A (b).

**What these statements do not show.** That the solver and the procedure of Theorem A (b) exist with
these properties. That a number of operations is a number of steps of a Turing machine: that is
`StPolyPlug` or `StPolyClose` with
`CountKSat.exists_tmW`, and it costs a factor polynomial in the sizes of the states. These sizes are
part of every claim; those of the tower are quadratic in the depth, because every activation carries
its own list env. 

 ### A machine that calls itself 

### `rstep`

 One step of the stack of activations, the running one first. If the running activation has
halted, its result goes to the one below it; a call starts a new activation on top; else the running
activation makes a step. Where the
whole has halted or the running activation asks a query that is not a call, the step does nothing. 

### `rask`

 The query of the whole: a query of the running activation that is not a call. 

### `rresume`

 The answer goes to the running activation. 

### `rout`

 The whole has halted when the only activation has. 

### `selfCall`

 M with all its calls of itself, as one machine. 

### `callOracle`

 How the queries of M on the input a are to be answered: a query that is not a call by O; a call
of a', if a' is a good input of smaller depth than a, by `val a'`. Any other call has no answer. 

### `SelfCallPoly`

 `selfCall M` has polynomial-time steps, once and for all depths of the recursion, if M has. 

### `SelfCallRuns`

 Let M, on every good input a, return `val a` within `T a` operations on states of size at most
S, when its queries are answered by O at the prices w and every call of a good input a' of smaller
depth is answered by `val a'` at the price
`T a' + 2`. Then `selfCall M`, on every good input a, returns `val a` within `T a` operations, with
queries answered by O at the prices w, and its states have size at most (dep a + 1)·(S + 1) + 1. 

 ### The tower: tables of the callee computed from the tables of the caller 

### `NIn`

 The inputs of the machine that calls itself. `Sum.inl (env, c)`: solve the instance with the
context c, whose table queries run up through env. `Sum.inr (c, env, q)`: the entry q of the tables
of the callee with the context c, where the
queries to the caller's tables run up through env. 

### `upQuery`

 Where a query goes. A query q to tables that run up through env: to the tables of the outermost
instance, or to the procedure on the first context of env. A query g of the second kind: out of the
tower, unchanged. 

### `nest`

 The solver and the procedure as one machine that calls itself; every activation carries its list
env. 

### `tower`

 The tower: `selfCall (nest Sol Inn)`, started on the outermost instance with the context c,
whose table queries are queries of the tower. 

 ### What the tower computes, and at what cost 

### `Spec`

 What a recursion is to compute. An instance is a context c with tables f (a function from
queries to answers that need not answer every query). `lev c` is its depth, `Good c f` says that it
is well formed, `val c f` is its value, `Child c f c'` says that the solver may call
c' when it works on (c, f), and `tab c' f` are the tables of the callee c' when f are the tables of
the caller. This is a device of the statement, not a part of the machine. It may be chosen anew for
every outermost instance, and so may the
costs and sizes in `Meets`: so `Good` may hold the parameters (in the appendix: λ and B) within the
bounds that they have along the recursion from that instance, and the costs, which are indexed by
the depth alone, may depend on that instance. 

### `Spec.oracle`

 How the queries of the solver on (c, f) are to be answered: a call of a permitted c' by the
value of c' with its tables; a query to the tables by f; a query of the second kind by gl. A call
that is not permitted has no answer. 

### `Spec.Meets`

 The solver and the procedure meet the specification, with these costs and sizes; gl answers the
queries of the second kind, at the prices wg. `TS l tc tq`: cost of the solver at depth l if a call
costs tc and a query to its tables tq; it must hold
for all instances of depth l that `Good` admits (in Appendix A the number L of a callee depends on
ι; the bound is one for all ι). `TI l tq`: cost of the procedure for a callee of depth l if a query
to the caller's tables
costs tq. SS, SI, SC: sizes of the states of the solver, of the procedure, and of the contexts of
calls. 

### `Spec.Meets.child_lev`

 a call goes one level down 

### `Spec.Meets.child_good`

 to a well-formed instance 

### `Spec.Meets.child_size`

 with a small context 

### `Spec.Meets.sol`

 the solver, with its calls and queries answered as specified, returns the value 

### `Spec.Meets.inn`

 the procedure, with the caller's tables, returns the entries of the callee's tables 

### `cost`

 The cost of the tower at depth l if a query to the tables of the instance costs t. 

### `towerSize`

 The bound on the sizes of the states of the tower at depth l: at most 2l + 2 activations, each
with a list of at most l contexts. 

### `TowerPoly`

 The tower has polynomial-time steps, once and for all depths, if the solver and the procedure
have. 

### `TowerRuns`

 The tower returns the value of every well-formed instance, at the cost of the recursion, for
every cost tq of a query to the tables of that instance. 

### `shapeS`

 The costs of the shape own + calls·tc + queries·tq and own' + q'·t, as in the appendix. 

### `shapeI`

 See `shapeS`. 

### `CostShape`

 The recursion written out for these shapes: T(l+1, t) = own + calls·(T(l, own' + q'·t + 2) + 2) +
queries·t. 

### `CostSlowDown`

 For these shapes, queries that cost x times as much make the whole cost at most x times as much.
This is what turns T(l, cost of an entry) into the product 𝒯·(cost of an entry) of the appendix. 
