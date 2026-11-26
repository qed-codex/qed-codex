---
{
  "module": "proof/rates/ExplicitCost/GroupingDefs.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ExplicitCost/GroupingDefs.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/ExplicitCost/GroupingDefs.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # The lemma on groupings with explicit cost (Lemma 8), on counted operations

Definitions and statements only; nothing is proved here.

**The text.** «Let K, g ≥ 2 be integers and 0 < ζ ≤ 1. Take a network on [g] with parameters P, B, τ
and total U, and assume that (i) g = 3K⁸ and ζ = 1/(2K), or (ii) K divides g, c_{a,b} ≤ P/g for all
a ≠ b, and 2ζ²g ≥ K·ln(2gK). Put L = ⌈(U + 2ζgP)/K²⌉ and B' = ⌈2gP/K⌉ + g²B. If an algorithm outputs
the value of every
(K, L)-clique with |W_w| < 2^{B'} within 𝒯 operations, then the value of the network is computed
within (K^g + 𝒯·2^{2gP/K}τ)(g(P+B))^{C₁} operations, by one procedure, the same for all K, g, ζ and
all networks, which calls that algorithm.» Its proof: «The algorithm is that of Lemma 1: find the
first such grouping among all
K^g, define the (K, L)-clique with the tables W̃_γ, whose value is that of the network, run the
given algorithm on it, and answer each query by computing the entry.»

**What is here.**
* `GroupingInput`: what the procedure is given: ζ as a fraction, K and g in unary, and the input of
  Definition 2(iii).
* `labelLength`, `bitsOut`: L and B', computed from the input. `goodData`: «at most 2g/K nodes in
  every group and Y_{γ,γ'} ≤ L for all γ ≠ γ'». `searchData`: «find the first such grouping among
  all K^g».
* `groupingCall`: the procedure up to the point where it «calls that algorithm»: the search, and
  then ONE query, the call, which asks for the value of the (K, L)-clique of the groups of the
  grouping x that the search has found (its entries are below 2^{B'}). `GroupingWithCall`: with the
  call answered rightly, at any price, it returns the value of the network.
* `groupingData E arg`: the whole procedure, made from ANY machine E for cliques: `groupingCall`,
  with the call answered by E on `arg (K, L, B')`, each of whose queries is answered by `entryData`
  (`QueryMachines.QueryMachine.subst`, twice).
* `GroupingExplicit`: the lemma for this procedure, with ONE constant C₁. `GroupingPoly`: it has
  polynomial-time steps if E has. The steps of the proof, each as a statement: `LabelLengthIsL`,
  `SearchFinds`, `SearchCost`, `ValueIsKept`, `EntryCostExplicit` (EntryDefs.lean), `SizesStmt`,
  `GroupingWithCall`.

**Where this differs from the text.** (1) An operation is a step of a machine with query access, and
every statement carries a bound on the sizes of the states; here it is polynomial in g(P+B) and the
length of ζ, plus what E needs. (2) The hypothesis on E therefore names a bound S_E on the sizes of
ITS states, which the
text lacks. It restricts nothing: S_E is arbitrary, and there are only finitely many tables for
given K, L, B', so every machine that is right on all of them has such a bound; it only enters the
bound on the states of the procedure. (3) ζ is a fraction a/b of natural numbers, part of the input;
in both uses of the lemma ζ is such a fraction (1/(2K), 2^{−ℓ−5}). (4) K, g, P, B, the P_a and
c_{a,b} are given in unary. (5) E is handed K besides L and B' (through `arg`, which may drop it or
put a level in its place). 

### `GroupingInput`

 What the procedure is given: ζ = a/b as the pair (a, b), and (K, g) in unary with the input of
Definition 2(iii). 

### `inK`

 The K of the input. 

### `inG`

 The g of the input. 

### `inP`

 The P of the input. 

### `inB`

 The B of the input. 

### `inU`

 The total U, the sum of the numbers c_{a,b} of the input over the ordered pairs a ≠ b. 

### `labelLength`

 «L = ⌈(U + 2ζgP)/K²⌉», for ζ = a/b: ⌈(bU + 2agP)/(bK²)⌉. The lemma has ζ ≤ 1; the procedure
reads min(a, b) for a, so that on EVERY input, also one with a > b, the number is at most U + 2gP +
1 and can be written in unary in polynomial time. 

### `goodData`

 «at most 2g/K nodes in every group and Y_{γ,γ'} ≤ L for all γ ≠ γ'», for the grouping number x. 

### `searchData`

 «find the first such grouping among all K^g». The loop halts at the first one. It reads only the
numbers of the input and asks nothing. 

### `CliqueInput`

 What a machine for cliques is given: K, λ, B in unary. 

### `CliqueCall`

 The call: the number x of the grouping, and (K, L, B'). It asks for the value of the (K,
L)-clique of the groups of x. 

### `callOf`

 The call that the procedure makes on the input c when the search has found x. 

### `groupingCall`

 **The procedure of the lemma, up to the call**: the search; then one query, the call, whose
answer is the result. The result is 0 if no grouping is good (which does not happen in cases (i) and
(ii)). 

### `entryInput`

 How a query (γ, Θ) to the tables of the clique of the groups becomes an input of `entryData`,
for the input c of the procedure and the grouping x. 

### `answerCall`

 The call carried out by a machine E for cliques: E on `arg (K, L, B')`, and its query (γ, Θ) is
answered by `entryData`, which asks the queries of Definition 2(iii). 

### `groupingData`

 **The procedure of the lemma**, made from a machine E for cliques. 

### `groupingInput`

 The input for ζ = a/b, K, g and the network N with the parameters P, B. 

 ### The steps of the proof 

### `LabelLengthIsL`

 The number computed is the L of the lemma, and `Printed.bitsOut` is its B'. 

### `SearchFinds`

 «Some grouping has at most 2g/K nodes in every group and Y_{γ,γ'} ≤ L for all γ ≠ γ'»
(`AppRunningTime.SomeGrouping`), so the search finds one: in case (i) or (ii) there is a first x <
K^g that the test accepts, and its grouping has the two properties. 

### `SearchCost`

 «Testing a grouping … take[s] time polynomial in g(P+B)»: here a test is one step, so the search
takes at most C·K^g steps, on states of size polynomial in g(P+B) and the length of ζ; that a step
takes polynomial time is `GroupingPoly`. One constant for all inputs. 

### `ValueIsKept`

 «… the (K, L)-clique with the tables W̃_γ, whose value is that of the network». This is
`Value.StValueEqualsZ` (proof/networks/Value/Defs.lean), which holds for all K and g. (It speaks of
procedures that run; the clique of the groups reads only the numbers of the procedures, so it is the
same for `asked.under` and for `asked` with the
oracle built in.) 

### `SizesStmt`

 «K ≤ g in both cases and L ≤ gP + 1» (`AppRunningTime.GroupingSizes`). 

 ### The lemma 

### `GroupingWithCall`

 **The lemma up to the call.** There is ONE constant C such that in case (i) or (ii) the search
finds a grouping number x < K^g, the first that its test accepts, with the two properties, for
which: whenever the call of x is answered by the value of the (K, L)-clique of the groups of x, at
the price tc, the procedure `groupingCall` returns the value of the
network within C·K^g + tc operations, on states of size at most (g(P+B) + the length of ζ)^C. (What
is known of that clique: its entries are below 2^{B'} and are computed by `entryData`:
`EntryCostExplicit`.) 

### `SolvesCliques`

 E, on the input `inp`, outputs the value of every (K, L)-clique with |W_w| < 2^{B'} within 𝒯
operations, a query counted as one operation, on states of size at most S_E. 

### `GroupingExplicit`

 **Lemma 8**, for the procedure of its proof. There is ONE constant C₁ such that for all K, g ≥
2, every fraction 0 < ζ = a/b ≤ 1, every network N on [g] with parameters P, B, τ and total U in
case (i) or (ii), and EVERY machine E that outputs the value of every (K, L)-clique with |W_w| <
2^{B'} within 𝒯
operations: the procedure `groupingData E arg` outputs the value of N within (K^g +
𝒯·2^{2gP/K}·τ)·(g(P+B))^{C₁} operations, where each query of Definition 2(iii) costs τ operations;
its states have size at most S_E + (g(P+B) + the length of ζ)^{C₁}. 

### `GroupingPoly`

 The procedure has polynomial-time steps, up to the call and as a whole if E has and `arg` is
polynomial-time: one certificate for all K, g, ζ. 

### `GroupingWithCallFrom`

 How the steps give the lemma up to the call. 

### `GroupingExplicitFrom`

 How the lemma up to the call, the cost of an entry and the rules of substitution give the lemma.
(The rule for a machine run on a function of its input, `Printed.mapIn_within`, is used besides.) 
