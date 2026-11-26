---
{
  "module": "src/New/UpperBound/Divisibility/HeckeEdges.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Divisibility/HeckeEdges.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Divisibility/HeckeEdges.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Elementary divisor bound for the scaled Hecke operator via edges

Let `l` be a place of a marked set `Λ` above a prime `p`. This file carries the theorem on
elementary divisors, `New.FrobeniusCycle.elementary_divisors`, for the edge Hecke operator over
to the normalised Hecke operator `New.Data.IsMarked.scaledHeckeOperator` at `l`. It assumes a
Frobenius cycle that matches the places above `l`. The proof identifies the two operators in
four steps:
* The edges: the cosets of the Hecke operator at `l` are indexed by edges. An edge is determined
  by its origin and its basis change there, because the rational points act freely on the cosets
  of the level (`New.Columns.HeckeEdges.eq_of_origin_eq_of_mem_parahoric`).
* The variables: at an a-place that induces `l` or its conjugate, an edge acts by letter matrices
  and powers of `p` (`New.Columns.kroneckerPi_symPowMatrix_eq_letterRep`).
* The weight space splits into monomials at these a-places and a factor on which the edges act
  integrally (`New.Columns.exists_weylIndex_equiv`, `New.Columns.exists_schur_eq_map`).
* The module: integral source forms are families of integral vectors indexed by the classes
  (`New.Columns.range_sourceFormOfValues`).

## Main definitions and results

* `New.Columns.isOntoUpToColength_scaledHeckeOperator_of_frobeniusCycle`: given a Frobenius cycle
  that matches the places above `l`, the operator is an edge Hecke operator, so the bound of the
  theorem holds for it.
* `New.Columns.HeckeEdges.heckeSplit_apply_rep`: The Hecke operator as a sum over edges.

Notions from other files:
* `New.IsOntoUpToColength`: The endomorphism `y` keeps `M`, and for some natural number `i ≤ c` the
  sum `y (M) + p ^ j₀ • M` has index dividing `p ^ i` in `M` (in the sense of `New.ColengthDvd`):
  `y` is onto on `M` modulo `p ^ j₀` up to an index `p ^ i`.
* `New.Data.IsMarked`: a marked set `Λ` of primes of `E` is disjoint from its complex conjugate,
  each of its primes is induced by an a-place (an element of `D.aPlaces`), `p` is exceptional
  (`New.Data.IsExceptional`), and `p` is below `D.x₁` and not split in the imaginary quadratic
  field.
* `New.Data.integralSourceForms`: the module of the elements of `D.SourceForm` of gauge at most `1`.
* `New.FrobeniusCycle`: ring maps `ι s : W → R` for `s` in `ℤ/N`, alternately even and odd, with
  `ι (s + 1) ≡ ι s ^ P` modulo `p`, where `P = p ^ frobExp` and the residue field of `W` has
  `P ^ N` elements.

## Relation to the literature

See `New.UpperBound.Divisibility.MarkOperator` for related work.


 ### Lattices at a finite place 

### `valuationRingAt`

 The valuation ring in `E` of the finite place `v`. 

### `localGL`

 An invertible matrix over `E`, read over the completion of `E` at `v`. 

### `localGL_mem_localIntGL_iff`

 A rational matrix lies in the maximal compact subgroup at `v` exactly if it is invertible over
the valuation ring of `v`. 

### `atPlace_embFin`

 The component at `v` of the finite adelic point of a rational point `γ` of the unitary group is
`γ`, read over the completion at `v`. 

### `latticeGL`

 The group `GL_k(W)` over the valuation ring `W` of `v`, embedded in `GL_n(E)` by numbering the
coordinates with `q`. 

### `localGL_mem_localIntGL_iff_mem_range`

 A rational matrix lies in the maximal compact subgroup at `v` exactly if it comes from `GL_k`
over the valuation ring of `v`, in the numbering `q` of the coordinates. 

### `localGL_latticeGL_mem_localIntGL`

 The image of `GL_k` over the valuation ring of `v` lies in the maximal compact subgroup at
`v`. 

### `blockScaling`

 The matrix `diag(p, …, p, 1, …, 1)` with `p` at the first `r` coordinates in the numbering
`q`. 

### `blockScaling_mem_basicDoubleCoset`

 Let `p` be a uniformizer at `l`, let `q` number the `k` coordinates, and let `r < k`. The matrix
`blockScaling E q p r = diag(p, …, p, 1, …, 1)`, with `p` at the first `r` coordinates, lies over
the completion at `l` in the double coset `basicDoubleCoset n l r` of the Hecke operator of index
`r`. 

### `mem_parahoric_twoBlock_iff`

 Over a local ring `W`, a matrix is parahoric for the blocks of sizes `r` and `k - r` exactly if
its entries at `(i, j)` with `i < r ≤ j` lie in the maximal ideal. 

### `conj_blockScaling_mem_localIntGL_iff`

 Let `p` be a uniformizer at `l`, with valuation ring `W`, and let `d = diag(p, …, p, 1, …, 1)`
have `r` entries `p`. For `β` in `GL_k(W)`, the conjugate `d⁻¹ β d` is integral at `l`, together
with its inverse, exactly if `β` is parahoric for the blocks of sizes `r` and `k - r`, that is, if
its entries at `(i, j)` with `i < r ≤ j` lie in the maximal ideal of `W`. 

### `conj_mem_localIntGL_of_transposeGL_mem_parahoric`

 Let `p` be a uniformizer at `l` and let `d = diag(p, …, p, 1, …, 1)` have `r` entries `p`. If
`gᵀ g'ᵀ⁻¹` is parahoric for the blocks of sizes `r` and `k - r`, then `d g⁻¹ g' d⁻¹` is integral
at `l`: the inverse transpose keeps integrality and exchanges `d` with `d⁻¹`. 

 ### The cosets of the Hecke operator as origins of edges 

### `edgeStep`

 The element `g_l⁻¹ β d` of `GL_n` over the completion at `l`, where `g_l` is the `l`-component
of `g` and `d = diag(p, …, p, 1, …, 1)`. Multiplying `g_l` by it on the right gives `β d`. 

### `edgeStep_mem_basicDoubleCoset`

 Let `p` be a uniformizer at `l`, let `q` number the `k` coordinates, and let `r < k`. Let the
component `g_l` of `g` at `l` be invertible over the local integers, let `β` lie in `GL_k` over the
valuation ring of `l`, and let `d = diag(p, …, p, 1, …, 1)` have `p` at the first `r` coordinates.
Then `edgeStep q p r g β = g_l⁻¹ β d` lies in the double coset `basicDoubleCoset n l r` of the Hecke
operator of index `r` at `l`. 

### `edgeStep_inv_mul_mem_localIntGL_iff`

 Let `p` be a uniformizer at `l`, and recall that `edgeStep q p r g β = g_l⁻¹ β d`. These
elements for `β` and `β'` lie in the same coset of the maximal compact subgroup at `l` exactly if
`β⁻¹ β'` is parahoric for the blocks of sizes `r` and `k - r`. 

### `exists_edgeStep_eq`

 Let `p` be a uniformizer at the split place `l` and let `g` be integral above `p`. Every coset
in the double coset of the Hecke operator of index `r < k` at `l` is the coset of
`edgeStep q p r g β = g_l⁻¹ β d` for some `β` over the valuation ring of `l`, where `g_l` is the
component of `g` at `l` and `d = diag(p, …, p, 1, …, 1)` has `p` at the first `r` coordinates. 

### `ClassEdges`

 The edges at `l` and level `K`: pairs of a class at level `K`, the terminus of the edge, and a
coset in `GL_k(W)` of the parahoric subgroup with blocks of sizes `r` and `k - r`, where `W` is the
valuation ring of `l`. 

### `HeckeEdges`

 Coordinates for the cosets of the Hecke operator of index `r` at a split place `l`, at
level `K`. Write `W` for the valuation ring of `l` and `d = diag(p, …, p, 1, …, 1)`. The origin
of the edge `(x, b)` is the point obtained from the representative of `x` by replacing its
`l`-component with `β d` (and the component at the conjugate place accordingly), where `β = b.out`
represents the coset `b`. 

### `HeckeEdges.numbering`

 The numbering of the coordinates. 

### `HeckeEdges.rep`

 The representative of a class. 

### `HeckeEdges.mk_rep`

 The point `rep x` lies in the class `x`. 

### `HeckeEdges.rep_mem_integralAbove`

 The representatives are integral above `p`. 

### `HeckeEdges.origin`

 The class of the origin of an edge. 

### `HeckeEdges.rationalPart`

 The rational part: a rational point that takes the representative of the class `origin e` to
  the origin of `e`, up to right multiplication by `K`. 

### `HeckeEdges.levelPart`

 The remaining factor in `K`. 

### `HeckeEdges.originBasisChange`

 The change of basis at the origin. 

### `HeckeEdges.rep_mul_edgeStep_eq`

 The origin is the rational part times the representative of its class times `levelPart`. 

### `HeckeEdges.rationalPart_inv`

 The inverse of the rational part is `g d⁻¹ β⁻¹`, with `g` the change of basis at the
  origin. 

### `atPlace_mem_localIntGL_of_isLevel`

 The component at any place of an element of a level is integral. 

### `nonempty_heckeEdges`

 Let `l` be a split finite place above `p`, let `K` be a level and let `q` number the
coordinates. A class is a double coset of the rational points and `K`. An edge is a pair `(x, b)` of
a class `x`, its terminus, and a coset `b` of the parahoric subgroup with blocks of sizes `r` and
`k - r`. Then there is a choice of the data `New.Columns.HeckeEdges`: for each class a
representative that is integral above `p`, and for each edge a factorisation of its origin (the
representative of `x` moved at `l` to `β d`, with `β = b.out` and `d = diag(p, …, p, 1, …, 1)`) as a
rational matrix (the rational part) times the representative of the class of the origin times an
element of `K`, and a matrix in `GL_k` over the valuation ring of `l` by which the rational part
differs from `β d`. 

### `embFin_rationalPart`

 The rational part of the edge `(x, b)` as a finite adelic point: the origin of the edge, times
the inverse of its factor in `K`, times the inverse of the representative of the class of the
origin. 

### `rationalPart_eq`

 The rational part of the edge `(x, b)` is `β d g⁻¹`, with `β = b.out`,
`d = diag(p, …, p, 1, …, 1)` and `g` the change of basis at the origin. 

### `localGL_rationalPart_mem_localIntGL`

 For coordinates `C` of the edges at `l`, the rational part `C.rationalPart e` is integral at
every place `v` above `p` other than `l` and its conjugate `star l`. 

### `eq_of_origin_eq_of_mem_parahoric`

 Let `p` be a uniformizer at the split place `l`, let the level `K` be maximal at `l`, and let
the rational points act freely on the cosets of `K`. An edge is a pair `(x, b)` of a class `x` at
level `K`, its terminus, and a coset `b` of the parahoric subgroup. Its origin is the representative
of `x` moved at `l` to `β d`, with `β = b.out` and `d = diag(p, …, p, 1, …, 1)`. The data
`C : HeckeEdges k p r K hl` give the class `C.origin e` of the origin and the matrix
`g = C.originBasisChange e` in `GL_k` over the valuation ring of `l` for which the rational point
moving the representative of that class to the origin is `β d g⁻¹`. Then an edge `e` is determined
by `C.origin e` and by the parahoric coset of the transpose of `g`. 

### `heckeSplit_apply_rep`

 Let `p` be a uniformizer at the split place `l`, let the level `K` be maximal at `l`, let `φ` be
an algebraic form of level `K`, and let `T_r` be the Hecke operator of index `r < k` at `l`. The
classes (`StdClasses K`) are the double cosets of the rational points and `K`, and `C.rep x` is the
representative of the class `x` chosen in the data `C : HeckeEdges k p r K hl`. An edge into `x` is
a pair `(x, b)` with `b` a coset of the parahoric subgroup with blocks of sizes `r` and `k - r`.
Then the value of `T_r φ` at `C.rep x` is the sum over `b` of `C.rationalPart (x, b)`, acting in the
weight representation, applied to `φ (C.rep (C.origin (x, b)))`. 

 ### The variables 

### `smul_transpose_map_eq_letterMatrix`

 The action on the variables of one letter `s`. Let `T` be a Frobenius cycle for `p` on the
valuation ring `W` of `l`: it assigns to each letter a ring map `T.embedding s` from `W` to `O` and
a parity. Let `T.embedding s` be the embedding `φ` if `s` is even and `φ ∘ conj` if `s` is odd. Let
`γ` be unitary with `γ⁻¹ = g d⁻¹ β`, where `g` and `β` lie in `GL_k(W)` and
`d = diag(p, …, p, 1, …, 1)` has `p` at the coordinates that `q` numbers below `r`. Here
`latticeGL q l` reads a matrix over `W` in the basis numbered by `q`, and the letter matrix of `g`
is `g` under `T.embedding s`, inverted and transposed for odd `s`. The variable `(i, s)` is deep if
`r ≤ i` for even `s` and if `i < r` for odd `s`; `T.deepIndicator r (i, s)` is `1` for deep
variables and `0` for the others. Apply `φ ∘ conj` to the entries of `γ`, transpose, and multiply by
`p` if `s` is even. The result is the letter matrix of `g`, times the diagonal matrix with `p` at
the deep variables and `1` elsewhere, times the letter matrix of `β`. 

### `kroneckerPi_symPowMatrix_eq_letterRep`

 Let `γ` be unitary with `γ⁻¹ = g d⁻¹ β` (`g`, `β` in `GL_k` over the valuation ring of `l`,
`d = diag(p, …, p, 1, …, 1)` with `r` entries `p`), and let the Frobenius cycle `T` embed that ring
by `φ s` at even letters `s` and by `φ s ∘ conj` at odd ones. Apply `φ s ∘ conj` to `γ`, transpose,
multiply by `p` for even `s`, and take the tensor product over `s` of the `a`-th symmetric powers.
The result is `T.letterRep a g * T.depthPower k a r * T.letterRep a β`. Here `T.letterRep a` is the
representation on the monomials, and `T.depthPower k a r` is the diagonal matrix whose entry at a
monomial is `p` to its total degree in the deep variables. 

 ### The weight space and the module of integral source forms 

### `exists_schur_eq_symPowMatrix`

 On the `k` coordinates `D.X 0`, numbered by `q`, the weight `D.columnCount τ` has one row, of
length `b = a` if the infinite place `τ` is an a-place (in `D.aPlaces`) and `b = 0` otherwise. So
there is a matching `ψ` of the basis with the monomials of degree `b` such that, for all `c` and
`z`, `c ^ b` times the Schur matrix of `z` is the transpose of the `b`-th symmetric power of `c zᵀ`,
with coordinates renumbered by `q`. 

### `exists_weylIndex_equiv`

 Let `q` number the `D.k` coordinates `D.X 0`, and let `t` number a set `Q` of a-places among the
infinite places `D.Φ` of `D.E`. At an a-place the weight `D.columnCount` is one row of length
`a = D.a`. So a basis index of the weight space splits, by `J`, into monomials of degree `a` at the
places `t s` and an index for the places outside `Q`. Let `z` be a family of matrices, one for each
place, which acts on the weight space by its Schur matrix (`schur`), and let `c s` be scalars. Then
`(∏ s, c s) ^ a` times this matrix is the tensor product of the transposed `a`-th symmetric powers
of the `c s • (z (t s))ᵀ`, in the numbering `q`, and the Schur matrix of `z` outside `Q`. 

### `exists_schur_eq_map`

 Let `S` be a set of infinite places of `E = D.E`. A place `τ` has a chosen complex embedding
`Φ τ`, and with `ιₚ : ℂ → ℂ_p` it induces a prime `inducedPlace τ` above `p`. Let `γ` be an
invertible matrix over `E` that lies in `GL(O_v)` for the conjugate `v` of each prime induced by an
a-place (`D.aPlaces`) in `S`. Embed `γ` by `Φ τ ∘ conj` at `τ`. Then its Schur matrix (`schur`), the
action on the factor at `S` of the weight space of weight `D.columnCount`, is an invertible matrix
over `embValRing`, the ring of complex numbers that are integral under `ιₚ`. 

### `weightRep_column_apply`

 On the definite space `D.X 0` the weight `(D.columnCount, D.lastEntry 0)` has no determinant
twist, so `weightRep` sends `γ` to the Schur matrix `schur D.columnCount` of the matrices `γ` with
entries mapped by `Φ τ ∘ conj`, applied to `v`. 

### `sourceFormOfValues`

 The source form with given values in `embValRing`, the `p`-integral complex numbers, at the
representatives `ρ x` of the classes. 

### `sourceFormOfValues_apply_rep`

 The source form with values `F` takes the value `F x` at the representative of the class `x`. 

### `range_sourceFormOfValues`

 Let `ρ` pick a matrix `ρ x` in each class `x`, a double coset for the rational points and the
level. The map `sourceFormOfValues hρ` sends a family of vectors over `embValRing` to the source
form with these values at the `ρ x`. If every `ρ x` is integral at the primes above `p`, then its
range is the module of integral source forms. 

 ### The bound for the scaled Hecke operator 

### `isOntoUpToColength_scaledHeckeOperator_of_frobeniusCycle`

 Let `Λ` be a marked set of primes above `p` and `l ∈ Λ`. Let `T` be a Frobenius cycle on the
valuation ring `W` of `l`: ring maps `T.embedding i` to `embValRing` for `i` modulo `N`, alternately
even and odd, each congruent modulo `p` to the `P`-th power of the one before, with
`P = p ^ T.frobExp` and `P ^ N` the size of the residue field. Assume that `T.p = p` is not a unit,
that `t` numbers the a-places that induce `l` or `star l`, that `T.embedding i` is the embedding
`Φ (t i)`, composed with conjugation unless `i` is even, and that `heckeScalingExponent l` is `a`
times the number of even letters. With `k = D.k`, `a = D.a` and `r` the least natural number with
`D.m ≤ p ^ r` (`D.ceilLogLifts p`), assume the size conditions `IsLargeDegree`: `0 < r`, `2 r ≤ k`,
`0 < θ ≤ 1`, `a ^ 4 ≤ q` and `(N k log q / θ) ^ 5 P ^ (3 r) ≤ a`, where `q = P ^ N`. Let `Y` be the
scaled Hecke operator at `l`. Then `Y` preserves the module `M` of integral source forms, and for
every natural `j₀` the index of `Y M + p ^ j₀ M` in `M` divides `p ^ e` for a natural
`e ≤ (3 c + θ j₀) * dim`. Here `c = T.divisorConstant k a r = N a (P ^ (-2 r) + r ^ 2 / (k P))`, and
`dim` is the complex dimension of `D.SourceForm`. 
