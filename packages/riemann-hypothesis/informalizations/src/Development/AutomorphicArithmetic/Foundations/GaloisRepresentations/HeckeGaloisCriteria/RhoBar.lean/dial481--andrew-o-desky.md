---
{
  "module": "src/Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/HeckeGaloisCriteria/RhoBar.lean",
  "declarations": [
    "UpperTheory.GalC.CutD.Good",
    "UpperTheory.GalC.Tie4"
  ],
  "author": "dial481",
  "writer": "Andrew O'Desky",
  "origin": "other-author",
  "source": "https://andrewodesky.com/rh/",
  "source_commit": "40e56bab026552e089d7afcfeff08d2defb9c005",
  "license": "with-permission"
}
---

As published on 26 November 2026.

## Projection defects under restriction of eigensystems

[Theorem ALG.0169](https://andrewodesky.com/rh/lean/UpperTheory.GalC.etaJ_le/)

Fix the source's arithmetic datum. At each local coefficient index $i$, let $X_i$ be its Hecke eigensystems, $Z_i^{\mathrm{good}}$ its good selected systems, and $Z_i$ its larger selected set. Choose a subset $X'_i\subseteq X_i$, retaining exactly those indices with $Z_i^{\mathrm{good}}\ne\varnothing$. Assume this is a good restriction in the sense below. Let $H>0$ be the supplied finite group order. For every $1\le j\le m$ and coefficient place $v$, $$\eta_j(v)\le\eta'_j(v)+\left(\sum_{i\in I(j,v)}\sum_{\pi\in Z_i^{\mathrm{good}}}m_{i,\pi}\right)v_{p_v}(H).$$ Here $\eta'_j(v)$ is the projection defect in the restricted datum, $m_{i,\pi}$ is the eigenspace multiplicity, $I(j,v)$ the local indices for lift $j$ and place $v$, and $p_v$ the residue prime. In particular, if the multiplicity sum is at most $d_j$, then $\eta_j(v)\le\eta'_j(v)+d_jv_{p_v}(H)$.

## Conditions on twisting, Galois data and cutting a datum

[Definition / hypothesis AGR.D036](https://andrewodesky.com/rh/lean/UpperTheory.GalC.GaloisPreconditions/)

This entry states the outer form of three hypotheses used in "A divisibility bound for a family from twisting and Galois conditions". A datum and a family are as in ([Data, families of data, classes of families, and properties of all sufficiently constrained families of a class](https://andrewodesky.com/rh/lean/Formalism.MainNotions.Closed/)). At each member above the starting scale, use the coefficient choices, period maps and selected theta-input sets in ([Twist period lattices and coefficient comparisons](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.NChoice/)).

**Twisting condition.** Require ([Integral twisting conditions for arithmetic families](https://andrewodesky.com/rh/lean/Formalism.MainNotions.TwIn/)), with the same selected theta-input sets and choices at the coefficient places.

**Conditions on a datum and its choice.** The first condition is a conjunction of 18 clauses. Their full constituent predicates are not expanded. Their outer forms include: a record of five conditions, three themselves records of respectively 10, 4 and 6 conditions, plus a condition at every local index and a rank equality for every size datum; a conjunction of three conditions; a second conjunction of three conditions; and a three-part statement about kernels, images and a sum of multiplicities. Another clause requires, for each relevant residual representation, irreducibility after scalar extension and nonvanishing of a specified characteristic polynomial at a specified scalar away from the two distinguished primes. Two clauses give the multisets of weights at a pair of embeddings as $\{p-\tfrac12\}$ and $\{-(p-\tfrac12)\}$, for $p$ in an attached multiset, and the weights of another object as singletons $\{-a-\tfrac12\}$ and $\{a+\tfrac12\}$, respectively. The multiset, integer and objects are not expanded.

Further clauses require an unramified condition away from the two distinguished primes; at specified places above either of them, the polynomial of every indicated wild-inertia element is $(X-1)^{n_V}$; an implication between two conditions on spherical base change; a condition for each used tuple and every $1\le j\le m$; and uniqueness of a local index when two indices have the same row and place and a good object occurs at both. The remaining clauses assert conjunctions and universally quantified conditions on residual eigenvalues, coefficients, choices, triples, twists and good objects; their predicates are not expanded. The choice-compatibility clause requires the character and embedding compatibilities in ([Twist period lattices and coefficient comparisons](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.NChoice/)) for those same coefficient choices.

**Four further conditions on a datum.** These are a conjunction of four assertions. The first imposes, at each of two distinguished primes and each relevant place, equations identifying linear polynomials with $X-u$ or $X-u^{-1}$, where $u$ is one of a specified unit and its inverse. The second asserts existence of a record containing finite-group idempotents, characters of inertia, actions on modules and compatibility equations, and satisfying two more conditions: a polynomial factorisation and inverse-root relation under a squarefreeness hypothesis, and an implication carrying a scalar action to a Hecke eigenspace. The third is a polynomial annihilation condition for a potentially crystalline representation, under its stated local hypotheses. The fourth says that nonzero action of a specified idempotent on an indicated parameter space forces its polynomial label to equal the parameter's label. The objects, remaining hypotheses and constructions in these four assertions are not expanded.

**Cutting assertion.** For every datum and choice satisfying both preceding conditions, there is a cut with the following properties. A cut selects local indices and a subset of labels at each local index, nonempty whenever that index is selected. It selects exactly the indices for which the set of good labels is nonempty, contains every good label, and among labels in a specified set contains only good labels. At each selected index there is an endomorphism commuting with all the Hecke operators, acting by a specified finite-group cardinality on every good-label eigenspace and by zero on every eigenspace with label outside the selected subset. For every selected index, selected label, matching object, and place above either distinguished prime, a conjunction of three local conditions holds; these conditions are not expanded.

The cut gives a new datum and transports the choice; neither construction is expanded. The new datum and transported choice satisfy the four further conditions above and a record of norm conditions. That record has a core of 15 clauses and seven additional clauses. Among its core clauses are the first three clauses of the 18 conditions, the residual, weight, local, base-change and used-tuple conditions listed above, a three-part conclusion whose last part is the kernel, image and multiplicity statement above, and two further requirements: a condition for every good pair and a second condition on such pairs at the distinguished primes, including equality of two weight lists and distinctness of constituents; and, for every size datum, an implication from an admissibility condition to a conjunction of six conditions. The seven additional clauses include the uniqueness, coefficient, choice, triple, twist and good-object conditions above and another conjunction of four conditions. The internal predicates and quantifiers of these additional requirements are not expanded.
