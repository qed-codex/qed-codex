---
{
  "module": "src/New/UpperBound/Divisibility/MarkOperator.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Divisibility/MarkOperator.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Divisibility/MarkOperator.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Elementary divisors of one scaled Hecke operator on the integral source forms

Let `l` be a place of a marked set `Λ` above a prime `p`, and write `o₀ = D.o₀ p`. This file
applies the theorem on elementary divisors, `New.FrobeniusCycle.elementary_divisors`, to the
normalised Hecke operator `New.Data.IsMarked.scaledHeckeOperator` at `l`, acting on the integral
source forms `New.Data.integralSourceForms`. The a-places that induce `l` or its conjugate form one
orbit under the place named by `-p ^ o₀` (`New.Data.exists_orbit_of_mem_aPlaces`), where the place
named by an integer acts on infinite places by multiplication. This orbit gives a Frobenius cycle.

## Main definitions and results

* `New.Data.IsMarked.exists_frobeniusCycle`: such a Frobenius cycle exists.
* `New.Data.IsMarked.isOntoUpToColength_scaledHeckeOperator`: the operator keeps the integral source
  forms and is onto modulo `p ^ j₀` up to a bounded colength.

Notions from other files:
* `New.IsOntoUpToColength`: The endomorphism `y` keeps `M`, and for some natural number `i ≤ c` the
  sum `y (M) + p ^ j₀ • M` has index dividing `p ^ i` in `M` (in the sense of `New.ColengthDvd`):
  `y` is onto on `M` modulo `p ^ j₀` up to an index `p ^ i`.
* `New.Data.IsMarked`: a marked set `Λ` of primes of `E` is disjoint from its complex conjugate,
  each of its primes is induced by an a-place (an element of `D.aPlaces`), `p` is exceptional
  (`New.Data.IsExceptional`), and `p` is below `D.x₁` and not split in the imaginary quadratic
  field.
* `New.Data.integralSourceForms`: the module of the elements of `D.SourceForm` of gauge at most `1`.
* `New.FrobeniusCycle`: ring maps `T.embedding i : W → R` for `i` in `ℤ/N`, alternately even and
  odd, with `T.embedding (i + 1) ≡ T.embedding i ^ P` modulo `p`, where `P = p ^ frobExp` and the
  residue field of `W` has `P ^ N` elements.

## Relation to the literature

An integrally scaled Hecke operator above p, acting on forms at a-places linked in a circle by
Frobenius and conjugation, has elementary divisors of small mean exponent outside a small share. So
using it once per theta lift, to keep divisibility when the partner of an a-place is an a-place,
costs little colength. Slopes of T_p of at most about k/(p+1) for GL(2) over Q and regular p, and
integral scalings of Hecke operators, are known. Related work: Arsovski, Limiting measures of
supersingularities, 2019; Liu–Truong–Xiao–Zhao, Slopes of modular forms and geometry of eigencurves,
2023; Fakhruddin–Pilloni, Hecke operators and the coherent cohomology of Shimura varieties, 2021.


### `isLargeDegree_of_le_card`

 Let `T` be a Frobenius cycle with `N` letters: a cycle of `N` ring maps from a local ring `W`,
each congruent modulo the prime `p = T.p` to the `P`-th power of the one before, with
`P = p ^ T.frobExp`; put `q = P ^ N`, the size of the residue field. Let `13 ≤ p < D.x₁`, let
`0 < T.frobExp ≤ r`, where `r = D.ceilLogLifts p` is the least natural number with `D.m ≤ p ^ r`,
let `N` be at most the number of infinite places, and let `D.m ≤ T.frobExp * N`. With `k = D.k`,
`a = D.a` and `θ = 1 / (m ^ 2 f)` for the numerical parameters `m = D.m`, `f = D.f` of the data, the
size conditions `IsLargeDegree` then hold: `0 < r`, `2 r ≤ k`, `0 < θ ≤ 1`, `a ^ 4 ≤ q` and
`(N k log q / θ) ^ 5 P ^ (3 r) ≤ a`. 

### `three_mul_divisorConstant_le`

 For a Frobenius cycle with `N = ℓ + ℓ` letters, prime `p = T.p` and `P = p ^ T.frobExp`, where
`0 < T.frobExp ≤ r` and `r = D.ceilLogLifts p` is the least natural number with `D.m ≤ p ^ r`, the
divisor constant `c = T.divisorConstant D.k a r = N a (P ^ (-2 r) + r ^ 2 / (k P))` for `k = D.k`
and `a = D.a` satisfies `3 c ≤ 12 a ℓ / (m p)`, with `m = D.m`. 

### `exists_orbit_of_mem_aPlaces`

 Let `p` be inert in the imaginary quadratic field of discriminant datum `P.d`
(`chiK P.d p = -1`), let `o₀` be odd, let `τ` be an a-place and let `N` be the order of the `o₀`-th
power of the place named by `-p`. Then some injective family `t` of places, indexed modulo `N`, goes
from each member to the next by multiplication with the place named by `-p ^ o₀` and consists of
exactly the a-places that induce the same prime as `τ` or its conjugate prime. 

### `embeddingToward`

 The embedding at the infinite place `σ`, composed with conjugation if `σ` does not induce the
prime `l`. 

### `placeOfEmb_embeddingToward`

 If `σ` induces `l` or its conjugate, then `embeddingToward l σ` induces `l`. 

### `embeddingToward_mem_embValRing`

 If `σ` induces `l` or its conjugate, then `embeddingToward l σ` maps the valuation ring of `l`
into `embValRing`. 

### `letterEmbedding`

 For an infinite place `σ` that induces `l` or its conjugate, `embeddingToward l σ` as a map
from the valuation ring of `l` to `embValRing`. 

### `dvd_letterEmbedding_sub_pow`

 Let `D` be data for the parameters `P`, let `p` be inert in the imaginary quadratic field, let
`l` be a split finite place of `D.E` and let `e` be odd. The infinite places form a group `(ℤ/q₁)ˣ`,
in which an integer prime to `q₁` names its class; let `σ'` be the product of `σ` and the place
named by `-p ^ e`, and let the primes induced by both through `ιₚ : ℂ → ℂ_p` be `l` or its
conjugate. For every `x` in the valuation ring of `l`, the image of `x` under `letterEmbedding σ'`
is congruent modulo `p` to the `p ^ e`-th power of its image under `letterEmbedding σ`. 

### `IsExceptional.card_residueField`

 Let `p` be exceptional: inert in the imaginary quadratic field, not `±1` modulo the number `D.m`
of lifts, and with `D.o₀ p` odd and at most `D.ceilLogLifts p`. Then the residue field of a prime
`l` of `D.E` above `p` has `p ^ o` elements, where `o = orderOf (D.placeOfInt (-p))` is the order of
the infinite place named by `-p`. 

### `IsMarked.exists_frobeniusCycle`

 Let `Λ` be a marked set for `p`, let `l ∈ Λ`, and let `o₀ = D.o₀ p`, the order modulo `q₀` of
the place named by the integer `-p`. Let `o₀ N` be the order of this place itself, and let `t i`,
for `i` modulo `N`, be infinite places that induce `l` or its conjugate, with `t (i + 1)` the place
named by `-p ^ o₀` times `t i`. Then the maps `New.Data.letterEmbedding (t i)` from the valuation
ring of `l` to the ring `embValRing` of `p`-integral complex numbers form a Frobenius cycle for the
prime `p` and the exponent `o₀`: each is congruent modulo `p` to the `p ^ o₀`-th power of the one
before, and a letter `i` is flagged as even (`isEven`) exactly if `t i` induces `l`, so parities
alternate. 

### `IsMarked.isOntoUpToColength_scaledHeckeOperator`

 Let `Λ` be a marked set of finite places above `p`, let `l ∈ Λ`, and let `j₀` be a natural
number. The scaled Hecke operator at `l` acts on `D.SourceForm`, the forms of weight `D.columnCount`
and level `D.levelX 0`; it is `p ^ A` times the Hecke operator of index `r` at `l`, where
`A = D.heckeScalingExponent l` is `D.a` times the number of a-places inducing `l` and
`r = D.ceilLogLifts p` is least with `m ≤ p ^ r`. It maps the module of integral source forms (gauge
at most `1`) to itself, and it is onto modulo `p ^ j₀` up to an index dividing `p ^ i` for some
natural `i ≤ (12 A / (m p) + j₀ / (m ^ 2 f)) * dim`, the divisions being those of real numbers. Here
`m = D.m` and `f = D.f` are the numerical parameters of `D`, and `dim` is the complex dimension of
`D.SourceForm`. 
