---
{
  "module": "proof/rates/CountedRecursion/RecursionDefs.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "AI models",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright": "Copyright (c) 2026 Anthropic, PBC. All rights reserved.",
  "source": "https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/CountedRecursion/RecursionDefs.lean",
  "source_commit": "11b6c7e3c927df2658f513b6b68ea7f8929c62c5",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [11b6c7e](https://github.com/anthropics/formal-math/blob/11b6c7e3c927df2658f513b6b68ea7f8929c62c5/eth/proof/rates/CountedRecursion/RecursionDefs.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

```text
/-
Copyright (c) 2026 Anthropic, PBC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0
-/
```

 # Theorem A (b) on counted operations: the statements

Definitions and statements only; nothing is proved here.

**The text.** «One deterministic algorithm, given ℓ ≥ 0, λ, B ≥ 1 and query access to tables with |W_w|
< 2^B, outputs the value of the (K_ℓ, λ)-clique within 2^{e_ℓK_ℓ²λ}(K_ℓ(λ+B))^{C₀K_ℓ²} operations.»
The machine is `recursion c x₀` (SolverDefs.lean).

**The forms.** `RecursionCountedUpTo`: the pieces are an oracle, and a query about strings of λ'
bits costs 2^{cλ'} + 2 operations (`PiecesCounted.price`: the cost that Definition 7 (c) prints, and
two for handing over the question and taking the answer); then ALL states have size at most
(K_ℓ(λ+B))^{C₀K_ℓ}, which is within the factor (K_ℓ(λ+B))^{C₀K_ℓ²} that the printed bound has
anyway; states within that factor are what it takes for the exponent e_ℓK_ℓ²λ to carry over to a
Turing machine with that oracle without a constant factor (`CliqueLevels.SolvesInFactor`).
`RecursionPlugged`: the pieces are computed by their algorithm; the machine has query access to the
tables alone, and its states are larger by the room of that algorithm, about 2^{cΛ} for the largest
label length Λ of the recursion; so there the exponent carries over to a Turing machine only up to a
constant factor.
`RecursionSolves`: the sentence of the theorem as `CliqueLevels.Solves` has it, the ONE definition
that is also the hypothesis of Theorem D (a).

**Lemma 8** is used in its form up to the call (`GroupingWithCall`, with `EntryCostExplicit` for the
entries), not as `GroupingExplicit`: the call is a call of the tower, not a substitution.

**The order of this file.**
1. The pieces in the form in which the plain functions and the theorems of this development take
   them (`piecesOf`, `listsOf`), and the networks of a pattern (`patternNet`).
2. What the recursion is to compute (`spec`, of type `QueryMachines.Tower.Spec`), and the bounds
   that λ and B obey along the recursion from one outermost instance (`boundsDown`). These are
   devices of the statements, not parts of the machine; they may and do use ρ.
3. The steps of the printed proof, in its order.
4. The costs of the solver and of the procedure as functions of the depth (`solverCost`,
   `entryCost`), that the machines meet the specification with them (`RecursionMeets`), and the
   count (`TotalCount`).
5. The theorem, in its two forms, and how the steps give it.

**Where this differs from the printed algorithm.** (1) An operation is a step of a machine with
query access; every statement carries a bound on the sizes of the states. (2) ℓ, λ, B are given in
unary; K and g are written in unary by a loop of ℓ rounds at the start of every activation of the
solver. (3) 𝓘 is handled as the list of its elements in increasing order, and a pattern ι as a
number y < |𝓘|^{|ℛ|}, whose digit in base |𝓘| at the number of a
rectangle is the place of ι(q) in that list. (4) A number c^row_i or c^col_i that the pieces return
is cut at 2λ when it is used («We may and do assume c^row_i, c^col_i ≤ 2λ»). (5) A setting of a row
has g³λ bits, not g(g² − 1)λ (a slot of λ bits for the edge from a grid point to itself, which must
be 0). (6) Every string of g³λ bits is a setting, so the test for membership says yes without a
query.
(7) If the totals are equal the row network is taken. (8) A call and each level that a query runs up
    cost 2 operations more (the tower's own steps). (9) The numbers c_{a,a'} are not stored with the
    callee: the procedure writes the input of Definition 2(iii) anew, from the lists in the context,
    when it is handed a query (this is not counted as an operation; it is polynomial-time in the
    context). (10) In the same way «finding the numbers c_{a,a'} and the totals of both networks for
    one ι» is the plain function by which the solver hands the network over to the procedure of
    Lemma 8; it is polynomial-time in what the solver holds, and is not counted.
(11) c^row_i, c^col_i ≤ 2λ is a hypothesis of the statements here (`Setting.short`). The paper says
     after Definition 7: «We may and do assume c^row_i, c^col_i ≤ 2λ … (and c by c + 2 …)»; we read
     this so: from there on the pieces ARE short, and the c of Theorem A is the c after the
     replacement. The statements here are for short pieces only. 

 ## 1. The pieces and the networks of a pattern 

### `Setting`

 The hypotheses of the theorem: pieces with parameters (ρ, c) (clauses (a), (b) and the sizes of (c)
of Definition 7, without its algorithm), with c^row_i, c^col_i ≤ 2λ; «x₀ ≥ 18 an integer with 2^{x₀}
≥ c + 5». 

### `indexAt`

 The element number j of 𝓘, in increasing order. 

### `piecesOf`

 The pieces in the form of proof/rates/ClauseBound/Alg/Data.lean: numbered by their place in 𝓘;
the pad is not read, and neither is the parameter h. The functions of a factorization are taken as 0
at a string θ that has not c^row_i (or c^col_i) bits, where Definition 7 says nothing of them. 

### `listsOf`

 The lists that the solver has after its queries to the pieces. 

### `patternNet`

 **The row network (tr = false) or the column network (tr = true) of the pattern number y**, for
the (g², λ)-clique with the tables W, as the data of Definition 2. As `Eight.ViaGrouping.levelNetP`,
for these pieces: the network `ClauseBound.Alg.GridNet.gridN` on words, with Ψ_{a,a'} the sum that
its factorization defines and P_a = g³λ. It has g nodes (`nParts g g tr` is g). 

### `mkParent`

 The parent for these numbers. 

### `Xi`

 Ξ = g²(λ + B). 

 ## 2. What the recursion is to compute 

### `answersOf`

 Tables as an oracle of the tower: the entry v is the answer `Sum.inl v`. 

### `readTables`

 Back: the tables that an oracle gives (0 where it gives nothing). 

### `Fits`

 The instance (a, f) is «the (K_ℓ, λ)-clique with |W_w| < 2^B», λ, B ≥ 1. 

### `readyOf`

 What the solver has computed when the loop over the patterns begins. 

### `groupTables`

 The tables W̃ of the (K, L)-clique of the groups, for the network of the parent p and the
caller's tables W. 

### `spec`

 **What the recursion is to compute.** The depth of an instance is ℓ; its value is the value of
the clique; the solver may call, for each pattern y, the context that it makes from y and the first
grouping x that the test accepts («find the first such grouping among all K^g»); the tables of a
callee are the tables W̃ of the clique of the groups. `Bound` holds λ and B within bounds (see
`InBounds`). 

### `boundsDown`

 Bounds for (λ, B) after k levels down from the outermost instance (ℓ, λ, B). With K, g, ζ of the
level j = ℓ − (k + 1) and (Λ, 𝔅) the bounds one level up: «K²L ≤ (ρ + 3ζ)N + (c/4)g⁴log(2λ) + K²», N =
g⁴Λ; and B' = ⌈2gP/K⌉ + g²B₁ for P = g³Λ, B₁ = g𝔅 + g²(2Λ)^c. 

### `lamAt`

 The bound for λ at the depth j ≤ ℓ. 

### `bitsAt`

 The bound for B at the depth j ≤ ℓ. 

### `InBounds`

 The context lies within the bounds that hold along the recursion from the outermost instance (ℓ,
λ, B). 

### `lamMax`

 The largest label length of the recursion from (ℓ, λ, B). 

### `piecesUpTo`

 The pieces as an oracle that answers only questions about strings of at most Λ bits. A run
against it is a run in which no other question is asked. (This is the function that is written out
in `PiecesCounted.OracleFromAlgorithm`.) 

### `askCost`

 What a query to the pieces about strings of λ bits costs: 2^{cλ} + 2 operations. 

### `solPrices`

 The prices: a call tc, a query to the tables tq, a query to the pieces about strings of λ' bits
2^{cλ'} + 2. 

### `upPrices`

 The same without calls: the prices of the queries of the procedure and of the one machine. 

 ## 3. The steps of the printed proof 

### `ListsAgree`

 The numbers read from the lists are those of the pieces. 

### `SolverBase`

 «For ℓ = 0, brute force sums 2^{λK₀(K₀−1)/2} ≤ 2^{e₀K₀²λ} terms, each at a cost of at most
(K₀(λ+B))^{C₅}.» With explicit numbers: a term costs K₀ queries and K₀ + 1 steps. One constant for
all x₀. 

### `Expansion`

 «Thus d^{|ℛ|}Z = Σ_ι Z_ι over the |𝓘|^{|ℛ|} … functions ι : ℛ → 𝓘, and each Z_ι is the value of
the row network and of the column network»: whichever of the two is taken for each ι. «this part of
that proof works for every g ≥ 2». 

### `PatternsFew`

 «|𝓘|^{|ℛ|} ≤ Ξ^{cg⁴/4}». 

### `BothNetworks`

 «so again P = g³λ, gP = N, and moreover c_{a,a'} ≤ g²λ = P/g. By Definition 7 (c), Definition 2
holds with B₁ = gB + g²(2λ)^c in the role of B and with τ = 2^{cλ}Ξ^{C₂}.» For the procedures
`gridProcsData c`: the network is a network with these parameters; the input that the procedure
writes is the input that belongs to it; and every query of Definition 2(iii) is answered within
(2^{cλ} + 2 + tq)·Ξ^{C₂} operations, if a query to the tables of the clique costs tq and a query to
the pieces 2^{cλ} + 2, on states of size at most Ξ^{C₂}. Only questions about strings of λ bits are
asked. C₂ depends on c only. 

### `pieceValue`

 A_i at four strings given as lists. 

### `PairIsProduct`

 «Ψ_{a,a'} is the product of the factors of the g straight edges between rows a and a' and of
A_{ι(q)}(x_q, y_q, u_q, v_q) over the g(g−1)/2 rectangles q with these two rows»: on settings, the Ψ
of `patternNet`, which is the sum that the factorization defines, is this product, in the form in
which `rowPair` computes it. 

### `TotalsAre`

 The totals that the solver compares are the totals U of the two networks. 

### `SmallerTotal`

 «U = min(U^row, U^col) ≤ N/g + |ℛ|(4ρλ + c·log(2λ)) ≤ N(ρ + 1/g) + (c/4)g⁴log(2λ).» 

### `CaseTwoApplies`

 «Case (ii) of Lemma 8 applies to the network with the smaller total (with B₁ in the role of B)»:
for K = K_ℓ, g = g_ℓ, ζ = ζ_ℓ, and either network. 

### `LabelBound`

 «So the lemma's L satisfies K²L ≤ U + 2ζN + K² ≤ (ρ + 3ζ)N + (c/4)g⁴log(2λ) + K².» 

### `LabelCrude`

 «Crude bounds give L ≤ N + 1», for the lemma's L and either network of a pattern. 

### `CrudeBounds`

 «Crude bounds give L ≤ N + 1 [`LabelCrude` for the L of a call, a clause of `ChainLabel` for the
bounds; here a hypothesis], B' ≤ N + g²B₁, g(P + B₁) ≤ Ξ^{c+4} and K(L + B') ≤ Ξ^{c+5}.» 

### `ChildIsGood`

 A call goes to the (K_ℓ, L)-clique of the groups of the network with the smaller total of some
pattern: one level down, well formed (λ = L ≥ 1, B = B' ≥ 1, |W̃_γ| < 2^{B'}), with the value Z_ι
for the pattern ι whose number stands in the child's parent, with L as bounded in `LabelBound` and
B' as printed. 

### `ProcedureCost`

 **One entry of the callee's tables**: «an entry is a sum of at most 2^{2gP/K} terms …»
(`EntryCostExplicit`), each query of Definition 2(iii) answered by the procedures of the network
(`BothNetworks`): within 2^{P⌊2g/K⌋}·(2^{cλ} + 2 + tq)·Ξ^{C} operations, on states of size at most
Ξ^{C}; P = g³λ; λ, B are the caller's. C depends on c only. 

### `SolverStep`

 **The solver at a level ℓ + 1**, with its calls answered by the values Z_ι at the price tc: «The
set 𝓘 and the numbers d, c^row_i, c^col_i are computed once. … each of the following takes at most
Ξ^{C₃} operations: finding the numbers c_{a,a'} and the totals of both networks for one ι; adding
one Z_ι; computing d^{|ℛ|} and dividing by it.» It returns Z within
|𝓘|^{|ℛ|}·(Ξ^{C₃}·K^g + tc) + (2|𝓘| + 2)·(2^{cλ} + 2) + Ξ^{C₃} operations, on states of size at most
Ξ^{C₃}, and the contexts of its calls have size at most Ξ^{C₃}. C₃ depends on c only. 

 ### How the steps rest on each other 

### `BothNetworksFrom`

 The two networks, from: Ψ is the product that `rowPair` computes; the numbers read from the
lists are those of the pieces. 

### `ChildIsGoodFrom`

 A call is good, from Lemma 8 up to the call, its L, the bound on the entries, «whose value is
that of the network», and the printed steps on the network with the smaller total. 

### `ProcedureCostFrom`

 An entry of the callee's tables, from Lemma 8 up to the call, its L and case (ii) (the grouping
in the callee's context is the first that the test accepts, so it has the two properties), the cost
of an entry with one constant (which asks L ≤ 2gP, and this follows from «Crude bounds give L ≤ N +
1» for the L of the call), the procedures of the network, «g(P + B₁) ≤ Ξ^{c+4}», and «answer each
query by computing …», the rule of substitution. 

### `SolverStepFrom`

 The solver at a level ℓ + 1, from the numbers of the level, the expansion, Lemma 8 up to the
call on the network with the smaller total, and the rule of substitution by which the call is passed
on. 

 ## 4. The costs as functions of the depth, and the count 

### `xiAt`

 Ξ for the callers of the depth j + 1, at the bounds for λ and B: g_j²(Λ_{j+1} + 𝔅_{j+1}). 

### `patternsAt`

 The bound ((2Λ)^c)^{|ℛ|} for the number of patterns at the depth j + 1. 

### `solverOwn`

 The cost of the solver at a depth, for all instances within the bounds, but for its calls and
its queries to its tables: `SolverBase` and `SolverStep` at the bounds for λ and B, with |𝓘| ≤
(2λ)^c. 

### `solverCalls`

 The number of its calls. 

### `solverAsks`

 The number of its queries to its tables. 

### `solverCost`

 The cost of the solver at the depth j if a call costs tc and a query to its tables tq: own +
calls·tc + queries·tq. 

### `entryAsks`

 The number of queries to the caller's tables in the procedure for a callee of the depth j, as
bounded by `ProcedureCost` at the bounds for the caller's λ and B: 2^{P⌊2g/K⌋}·Ξ^C. 

### `entryOwn`

 The rest of its cost: 2^{P⌊2g/K⌋}·Ξ^C·(2^{cΛ} + 2). 

### `entryCost`

 The cost of the procedure for a callee of the depth j if a query to the caller's tables costs
tq: own' + queries'·tq. 

### `roomAll`

 One bound for the sizes of the states of the solver and of the procedure and of the contexts, at
all depths: the sum over j ≤ ℓ of (K_j(Λ_j + 𝔅_j))^C. 

### `RecursionMeets`

 **The solver and the procedure meet the specification**, for every outermost instance (ℓ, λ, B),
with these costs and sizes, and with the pieces asked only about strings of at most Λ bits, Λ the
largest label length of the recursion. C depends on c only. 

### `RecursionMeetsFrom`

 How the steps give it. 

### `sizeBound`

 The bound on the sizes of the states when the pieces are an oracle: (K_ℓ(λ+B))^{C₀K_ℓ}. The
exponent is C₀K_ℓ, sharper than the C₀K_ℓ² of the printed factor; it is what the tower achieves
(`TotalRoom`). The statements here ask only that the states stay within the printed factor
(`CliqueLevels.SolvesInFactor`), which already keeps the exponent e_ℓK_ℓ²λ; with the sharper bound,
besides, all K·2^{(K−1)λ} entries of the
tables fit into a state only where λ is at most about 2C₀·log(K(λ+B)), and there brute force is
within the printed polynomial factor anyway. 

### `timeBound`

 The bound of the theorem: 2^{e_ℓK_ℓ²λ}·(K_ℓ(λ+B))^{C₀K_ℓ²}. (It is
`CliqueLevels.bound (e_ℓ) (K_ℓ) C₀ λ B`.) 

 ### The chain: from one depth to the next, at the bounds for λ and B 

### `baseAt`

 X_j = K_j(Λ_j + 𝔅_j): the base of the polynomial factor at the depth j. (X_{j+1} is `xiAt … j`.) 

### `Numbers`

 The hypotheses on the numbers, for the arithmetic. 

### `ChainLabel`

 «K²L ≤ (ρ + 3ζ)N + (c/4)g⁴log(2λ) + K²» and «L ≤ N + 1», for the bounds: 1 ≤ Λ_j ≤ g_j⁴Λ_{j+1} +
1 and K_j²Λ_j ≤ (ρ + 3ζ_j)g_j⁴Λ_{j+1} + (c/4)g_j⁴log(2Λ_{j+1}) + K_j²; also 1 ≤ 𝔅_j. 

### `ChainBase`

 «K(L + B') ≤ Ξ^{c+5}», for the bounds: X_j ≤ X_{j+1}^{c+5}. 

### `ChainLevels`

 «(c + 5)K² ≤ 2^{x₀}K² ≤ g⁴/2», k times: 2^k(c + 5)^kK_{ℓ−k}² ≤ K_ℓ²; and (c + 5)^ℓ ≤ K_ℓ. 

### `ChainExponent`

 The exponents of 2: e_jK_j²Λ_j ≤ e_{j+1}K_{j+1}²Λ_{j+1} − 3K_{j+1}²Λ_{j+1}/K_j +
(c/4)K_{j+1}²log(2Λ_{j+1}) + K_j² (by e_{j+1} = (ρ + 3ζ_j)e_j + 3/K_j and e_j ≤ 1). 

### `ChainBaseFrom`

 The bound for X_j, from the bounds for Λ_j and the crude bounds. 

### `ChainExponentFrom`

 The inequality between the exponents of 2, from the bounds for Λ_j and part (a) of the theorem. 

 ### The count 

### `levelBound`

 The bound of the theorem for the depth j, at the bounds for λ and B. 

### `BoundBelow`

 **«By the induction hypothesis and e ≤ 1, the lemma's 𝒯 may be taken as 𝒯 = 2^{eK²L}(K(L +
B'))^{C₀K²} ≤ 2^{e(ρ+3ζ)N}·Ξ^{cg⁴/4+K²+(c+5)C₀K²}.»** For the bounds: the bound of the theorem for
the depth j, at (Λ_j, 𝔅_j), against the numbers of the depth j + 1, for every C₀. The exponent of 2
is written e_{j+1}N − 3N/K_j, which is e_j(ρ + 3ζ_j)N by e_{j+1} = (ρ + 3ζ_j)e_j + 3/K_j; N =
K_{j+1}²Λ_{j+1} = g_j⁴Λ_{j+1}; cg⁴/4 is the natural number c·(g⁴/4), and 4 divides g⁴. 

### `BoundBelowFrom`

 How: from the chain. 

### `CountBase`

 «For ℓ = 0, brute force sums 2^{λK₀(K₀−1)/2} ≤ 2^{e₀K₀²λ} terms, each at a cost of at most
(K₀(λ+B))^{C₅}»: the cost of the solver at the depth 0, if a query to its tables costs t ≥ 1, is at
most t times the bound, for every C₀ ≥ 1. 

### `CountStep`

 **«So the total number of operations is at most |𝓘|^{|ℛ|}((K^g + 𝒯·2^{2N/K}τ)Ξ^{(c+4)C₁} +
2Ξ^{C₃}) + (2|𝓘| + 2)2^{cλ} + Ξ^{C₃} ≤ Ξ^{cg⁴/4+g+C₄}·𝒯·2^{2N/K+cλ} ≤
2^{e_{ℓ+1}N}·Ξ^{cg⁴/2+g+K²+C₄+(c+5)C₀K²}.»** For the costs of this file: with 𝒯 the bound of the
depth j, a call costs (cost of an entry + 2)·𝒯 + 2 operations if a query to the tables of the
depth j + 1 costs t ≥ 1. C₄ depends on c and C only, not on C₀. 

### `ExponentFits`

 **«Since (c + 5)K² ≤ 2^{x₀}K² ≤ g⁴/2, the exponent of Ξ is at most (c + C₄ + 1)g⁴ + ½C₀g⁴ ≤ C₀g⁴ =
C₀K_{ℓ+1}² by the choice of C₀.»** 

### `CountBaseFrom`

 The base, from the bounds for Λ_j. 

### `CountStepFrom`

 The step, from the bounds for Λ_j, the bound for 𝒯, and part (a) of the theorem (for e_j ≥ 0). 

### `TotalCount`

 **The count**, for the recursion `QueryMachines.Tower.cost` of these costs: for every c and C
there is a C₀ such that the cost of the tower, at one operation for a query to the tables of the
outermost instance, is at most the bound of the theorem. 

### `TotalCountFrom`

 By induction on the depth: the cost of the tower at the depth j, if a query costs t ≥ 1, is at
most t times the bound of the depth j. 

### `TotalRoom`

 The sizes of the states of the tower are at most (K_ℓ(λ+B))^{C₀K_ℓ}. (The paper bounds no
memory. The reason: K_j(Λ_j + 𝔅_j) ≤ (K_{j+1}(Λ_{j+1} + 𝔅_{j+1}))^{c+5} by the crude bounds, and (c + 5)^ℓ
≤ K_ℓ.) 

### `TotalRoomFrom`

 How. 

### `RoomIsWithinTheBound`

 The room of the algorithm of the pieces, at the largest label length of the recursion, is within
the bound of the theorem. (The reason: c ≤ K_j ≤ e_jK_j², so 2^{cΛ_j} ≤ 2^{e_jK_j²Λ_j}, and the
bound of the level j at (Λ_j, 𝔅_j) is at most that of the level j + 1 at (Λ_{j+1}, 𝔅_{j+1}), as in
the printed display for 𝒯; the other factors of the room are polynomial in Λ_j.) 

### `RoomIsWithinTheBoundFrom`

 From the bounds for Λ_j, the bound for 𝒯 with the sentence on the exponent of Ξ (so the bound of
a depth is at most that of the next), the inequalities between the K_j, and part (a) of the theorem
(for c ≤ e_jK_j²). 

 ## 5. The theorem 

### `RecursionPoly`

 The solver and the procedure have polynomial-time steps: one certificate each, for all levels. 

### `RecursionPolyFrom`

 So the one machine has. 

### `RecursionCountedUpTo`

 **Theorem A (b), with the pieces as an oracle at 2^{cλ'} + 2 operations a query**: the pieces
are asked only about strings of at most Λ bits, Λ the largest label length of the recursion. 

### `RecursionCountedUpToFrom`

 How the steps give the theorem. 

### `RecursionPlugged`

 **Theorem A (b), with the pieces computed by their algorithm.** For pieces WITH their algorithm
(all of Definition 7): the machine `recursionWith c x₀ Alg` has query access to the tables alone, at
one operation for a query. It outputs the value within three times the bound (a query that is passed
on costs 2 operations more); its states are larger by the room of Alg at Λ, the largest label length
of the recursion. That room is about 2^{cΛ}: so a Turing machine that carries this machine out has
the exponent of the bound only up to a constant factor, where `RecursionCountedUpTo` keeps it
exactly, relative to the oracle. 

### `RecursionPluggedFrom`

 How: the price of a query to the tables is raised from 1 to 3 (`PricesScale`), and then the
queries to the pieces are answered by the algorithm (`PiecesCounted.OracleFromAlgorithm`). 

### `RecursionWithPoly`

 Given an algorithm for the pieces with polynomial-time steps, the machine with that algorithm
built in, and the algorithm of the theorem (`cliqueMachine`), have polynomial-time steps. 

### `RecursionWithPolyFrom`

 How: from the certificate of the one machine for all levels. 

### `RecursionSolves`

 **Theorem A (b)**, in the ONE form that is also the hypothesis of Theorem D (a)
(`CliqueLevels.Solves`): «One deterministic algorithm, given ℓ ≥ 0, λ, B ≥ 1 and query access to
tables with |W_w| < 2^B, outputs the value of the (K_ℓ, λ)-clique within
2^{e_ℓK_ℓ²λ}(K_ℓ(λ+B))^{C₀K_ℓ²} operations», on states of at most that size. C₀ depends on c only.
(The states hold the room of the algorithm of the pieces; see `RecursionPlugged`.) 

### `RecursionSolvesFrom`

 How. 
