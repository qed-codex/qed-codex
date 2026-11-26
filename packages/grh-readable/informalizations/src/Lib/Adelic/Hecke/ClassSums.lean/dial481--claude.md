---
{
  "module": "src/Lib/Adelic/Hecke/ClassSums.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Adelic/Hecke/ClassSums.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Adelic/Hecke/ClassSums.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Class sums as integrals over Γ\G, orbit unfolding and means over compact subgroups

For subgroups `Γ`, `K` of a topological group `G`, `New.classSum Γ K f` is the sum of
`f g / #(Γ ∩ g K g⁻¹)` over representatives `g` of `Γ \ G / K`, where
`Γ ∩ g K g⁻¹ = New.classAut Γ K g`. The integral over `Γ \ G` with `vol K = 1` is defined from class
sums as the finite sum `New.classIntegral`, also called the mean (it is an average when `Γ = ⊥` and
`K` is the whole group). No measure theory is used. The mean `New.classIntegral` is used to average
smooth representations over compact subgroups.

## Main definitions and results

* `New.classIntegral`: the class sum at the level `rightStabilizer f ⊓ K`, divided by its index in
  `K`.
* `New.HasFiniteType`: finitely many classes and finite stabilisers, with `K` open and compact.
* `New.classSum_eq_relIndex_smul`: change of level, by double counting.
* `New.classIntegral_eq_classSum_mul`, `New.classIntegral_eq_inv_smul_classSum`: for left
  Γ-invariant f, the mean can be computed at a smaller open level that fixes f, or one whose
  conjugate by some a lies in K and fixes f (then for the right translate of f by a).
* `New.classIntegral_sum`: for smooth left Γ-invariant functions, the mean commutes with finite
  sums, additive maps and right translation.
* `New.compactMean ρ H`: the mean over H. It is invariant under H on both sides
  (`New.apply_compactMean`, `New.compactMean_apply`), projects onto the H-fixed vectors
  (`New.compactMean_mem_levelSpace`, `New.compactMean_eq_self`), and is self-adjoint for an
  invariant scalar product (`New.IsUnitary.compactMean_adjoint`).

Notions from other files:
* `Subgroup.FixesLeft`: `Γ.FixesLeft f` says that `f (γ * g) = f g` for all γ in Γ and g in G.
* `New.levelSpace π K χ`: For a representation π of G, a subgroup K and a character χ of K (by
  default trivial), the submodule of vectors v with π(k)v = χ(k)v for all k in K.

## Relation to the literature

Known result: weighted class sums for a pair (G,K), as in the theory of abstract Hecke operators and
of algebraic modular forms. They make sense for values in any rational vector space, without a Haar
measure. Source: G. Shimura, Introduction to the Arithmetic Theory of Automorphic Functions
(1971), ch. 3; B. Gross, Algebraic modular forms, Israel J. Math. 113 (1999) 61-93; M. Greenberg and
J. Voight, Lattice methods for algebraic modular forms on classical groups, arXiv 1209.2460.


 ### Definitions 

### `rightStabilizer`

 The subgroup of k in G with f(gk) = f(g) for all g. 

### `classIntegral`

 The class sum of `f` at the level `K ∩ Stab f`, divided by the index of that level in `K`. It is
the finite-sum analogue, defined without measure theory, of the integral of `f` over `Γ \ G` for the
Haar measure with `vol K = 1`, and is meant for `(Γ, K)` of finite type and `f` smooth and left
`Γ`-invariant. 

### `HasFiniteType`

 The pair `(Γ, K)` has finite type: `K` is compact and open, `Γ \ G / K` is finite and every
`Γ ∩ g K g⁻¹` is finite. 

### `HasFiniteType.finite_classes`

 There are finitely many double cosets `Γ g K`. 

### `HasFiniteType.finite_aut`

 The stabiliser `Γ ∩ g K g⁻¹` of each point `g K` is finite. 

### `HasFiniteType.isOpen`

 `K` is open in `G`. 

### `HasFiniteType.isCompact`

 `K` is compact. 

 ### Smooth invariant functions, double cosets and their stabilisers 

### `surjective_doubleCoset_mk_mul`

 Every class in Γ\G/K' is the class of x q, with x the representative of a class in Γ\G/K and q
the representative of a coset in K/(K ∩ K'). 

### `smoothInvariants`

 The set of left Γ-invariant functions G → W whose stabiliser under right translation is open. 

### `exists_transporter`

 Let `u` be an injection into `G` whose range contains `Γ` (for example `id`, or the inclusion of
a group that contains `Γ`), and let `(Γ, K)` have finite type. The `γ` with `u γ ∈ Γ` and
`g⁻¹ (u γ) h ∈ K` form a finite set, with as many elements as `Γ ∩ g K g⁻¹` if `g` and `h` lie in
one class of `Γ \ G / K` and with none otherwise. 

### `card_classAut_out`

 The order of the stabiliser `classAut Γ K g` depends only on the class ΓgK. 

### `classIntegral_const_mul`

 The integral over `Γ \ G` of a complex function commutes with multiplication by a constant. 

### `classIntegral_eq_classSum`

 For subgroups `Γ`, `K` of `G` and `f : G → W`, `classSum Γ K f` is the sum over double cosets
`c ∈ Γ\G/K` of `f(g_c)/#(Γ ∩ g_c K g_c⁻¹)`. The integral `classIntegral Γ K f` is the class sum at
level `K ∩ Stab f` divided by that level's index in `K`. If `K` fixes `f` under right translation,
the two are equal. 

### `apply_doubleCoset_out`

 A left `Γ`-invariant and right `K`-invariant `f` takes the same value at `g` and at the chosen
representative of the double coset `Γ g K`. 

 ### Finite sums over the classes 

### `HasFiniteType.of_le`

 If `(Γ, K)` has finite type (finitely many classes, finite stabilisers, `K` compact open),
then so has `(Γ, K')` for every open subgroup `K'` of `K`. 

### `card_classes_eq_classSum`

 For a pair `(Γ, K)` of finite type (`K` compact open in the topological group `G`, `Γ \ G / K`
finite and every `Γ ∩ g K g⁻¹` finite) in which every stabiliser `classAut Γ K g = Γ ∩ g K g⁻¹` is
trivial, the class sum of the constant function `1` equals the number of double cosets `Γ g K`, as a
real number. Here `classSum Γ K f` is the sum over double cosets `c` in `Γ \ G / K` of
`f(g_c) / #(Γ ∩ g_c K g_c⁻¹)`, where `g_c` is a chosen representative of `c`. 

### `classIntegral_mem_nsmul`

 Suppose `(Γ, K)` has finite type and all `Γ ∩ g K g⁻¹` are trivial, and let `f` be right
`K`-invariant with values in `A`. Then `classIntegral Γ K f`, the class sum of `f` at level
`K ∩ Stab f` divided by the index of that level in `K`, is a sum of elements of `A`, one for each
double coset in `Γ \ G / K`. 

### `classSum_pos`

 The class sum of a nonnegative function that is positive at some class representative is
positive. 

### `map_classSum`

 Additive maps commute with class sums. 

### `classSum_sum`

 The class sum commutes with finite sums of functions. 

 ### Change of level 

### `card_filter_out_inv_mul_mem_eq_one`

 For `k ∈ K`, exactly one coset `q` in `K / (L ∩ K)` has `q.out⁻¹ * k ∈ L`. 

### `classSum_eq_relIndex_smul`

 Change of level and of variable in a class sum, for `(Γ, K)` and `(Γ, K')` of finite type. Let
`L = a⁻¹ K' a ≤ K`, and let `F g` be the value of `f` at the representative of the class
`Γ (g a) K`. Then the class sum `∑ F g / #(Γ ∩ g K' g⁻¹)` over `Γ \ G / K'` is the index `[K : L]`
times the class sum of `f` over `Γ \ G / K`. 

### `classSum_one_of_le`

 For `K' ≤ K` with `(Γ, K)` and `(Γ, K')` of finite type, the class sum of `1` at level `K'` is
`[K : K']` times that at level `K`. 

### `classIntegral_eq_classSum_mul`

 For left `Γ`-invariant `f`, and `(Γ, K)`, `(Γ, K')` of finite type, the integral is
`[K : K']⁻¹` times the class sum for `K'` of `g ↦ f (g * a)`, whenever `K' ≤ K` and `a⁻¹ K' a`
(written `K'.comap (conj a)`) lies in both `K` and the right stabiliser of `f`. 

### `classIntegral_eq_inv_smul_classSum`

 For left `Γ`-invariant `f`, the integral is `[K : K']⁻¹` times the class sum at a level
`K' ≤ K` that fixes `f`, for `(Γ, K)` and `(Γ, K')` of finite type. 

 ### Additivity and translation invariance 

### `classIntegral_sum`

 Let `(Γ, K)` have finite type, let the `f i` be smooth and left `Γ`-invariant, `φ i` additive
maps and `F g = ∑ i ∈ s, φ i (f i (g * a i))`. Then the integral of `F` is the sum of the `φ i` of
the integrals of the `f i`: the integral is additive, commutes with additive maps of the values and
does not change under right translation. 

 ## Linearity of the integral over `Γ \ G`, and smooth functions 

### `classIntegral_add`

 Let `(Γ, K)` have finite type. The integral `classIntegral Γ K` over `Γ \ G` is additive on
`smoothInvariants Γ`, the left `Γ`-invariant functions fixed on the right by an open subgroup. 

### `classIntegral_map_mul_right`

 Let `(Γ, K)` have finite type, let `f` be smooth and left `Γ`-invariant, `L` an additive map and
`F g = L (f (g * a))`. Then the integral of `F` over `Γ \ G` is `L` of the integral of `f`: the
integral commutes with additive maps and does not change under right translation. 

### `smoothFunctions`

 The smooth functions `G → W`, those fixed under right translation by an open subgroup, as a
subrepresentation of the right regular representation. 


## Unfolding class sums along an orbit

`New.classSum_card_orbit`: under `New.HasFiniteType`, if `G` acts on a set and `H` is the stabiliser
of a point `e`, the class sum of the number of points of `Γ e ∩ g K e` is the class sum of `1` for
the preimages of `Γ` and `K` in `H`.


### `New.card_filter_smul_eq_ite_card_classAut`

 Let `ι` embed `H` with image the stabiliser of `e`, let `Δ`, `L` be the preimages of `Γ`, `K`,
with `(Δ, L)` of finite type (finitely many classes, finite stabilisers, `L` compact open), and let
`ι h = a⁻¹ g k` with `a ∈ Γ`, `k ∈ K`. Among the `γ ∈ Γ` with `g⁻¹ γ (ι d) ∈ K`, those with
`γ • e = a • e` are as many as the elements of `Δ ∩ h L h⁻¹` if `Δ h L = Δ d L`, and there are none
otherwise. 

### `New.classSum_ite_card_classAut`

 The class sum of the function that is `#(Γ ∩ g K g⁻¹)` on the double coset `Γ g₀ K` and `0`
elsewhere is `1`: only the class of `g₀` contributes, and its weight cancels. 

### `New.indicator_orbit_eq_sum`

 Let `ι` embed `H` with image the stabiliser of `e`, let `Δ`, `L` be the preimages of `Γ`, `K`,
with `(Δ, L)` of finite type (finitely many classes, finite stabilisers, `L` compact open), and let
`S = Γ e ∩ g K e`. Let `T h` be the set of `γ ∈ Γ` with `g⁻¹ γ (ι h) ∈ K`. Then the indicator of
`S` is the sum, over the classes `d` of `(Δ, L)` and the `γ ∈ T d`, of point masses
`1 / #(Δ ∩ d L d⁻¹)` at `γ • e`. 

### `New.classSum_card_orbit`

 Let `G` act on `X`, let `ι` embed `H` with image the stabiliser of `e`, and let `Δ`, `L` be the
preimages of `Γ`, `K`; both pairs have finite type (finitely many classes, finite stabilisers,
compact open levels). Then the class sum for `(Γ, K)` of the number of points of `Γ e ∩ g K e`,
that is `∑ #(Γ e ∩ g K e) / #(Γ ∩ g K g⁻¹)` over `Γ \ G / K`, is the class sum of `1` for
`(Δ, L)`. 


## Smooth and unitary representations and the mean over a compact subgroup

Averaging a smooth representation over a compact subgroup, without Haar measure: the mean is the
finite average `New.classIntegral` of a function that is fixed by a subgroup of finite index.

* `New.map_compactMean_of_const`: a semilinear map that is constant on the `H`-orbit of `x` takes
  the same value at the mean of `x`.
* `New.map_compactMean_of_factor`: the case of `φ ∘ ρ g` with `φ` invariant under a subgroup `K`
  and `H ⊆ (g⁻¹ K g) · Stab x`.


### `IsUnitary`

 The sesquilinear form `B` is positive definite and invariant under `ρ`. 

### `IsUnitary.pos`

 `B x x` is a positive real number for `x ≠ 0`. 

### `IsUnitary.map_map_eq`

 Every `ρ g` preserves `B`. 

### `IsUnitary.adjoint_eq_inv`

 For a `ρ`-invariant scalar product `B`, the adjoint of `ρ g` is `ρ g⁻¹`. 

### `IsSmoothRep`

 The representation `ρ` is smooth: every vector is fixed by all `g` in some neighbourhood
of `1`. 

### `IsSmoothRep.eventually_fixed`

 The vector `x` is fixed by all `g` in some neighbourhood of `1`. 

### `local instance : Module ℚ V`

 A complex vector space is a rational vector space, so class integrals can take values in it. 

### `instance : Unique (DoubleCoset.Quotient ({1} : Set G) (Set.univ : Set G))`

 There is one double coset `{1} \ G / G`. 

### `instance [CompactSpace G] : HasFiniteType (⊥ : Subgroup G) ⊤`

 For a compact group `G` the pair `({1}, G)` has finite type. 

### `orbit_mem_smoothInvariants`

 For `ρ` smooth and `H` compact, the function `(a, b) ↦ ρ (a⁻¹ b) x` on `H × H` lies in
`smoothInvariants ⊥`: its stabiliser under right translation is open. 

### `compactMean`

 The mean of `ρ` over a compact subgroup `H`: the mean of `ρ (a⁻¹ b)` over `(a, b) ∈ H × H`.
Invariance of class integrals under right translation (`classIntegral_map_mul_right`) then gives
both sides: right translation in `a` multiplies `a⁻¹ b` on the left, and in `b` on the right. 

### `map_compactMean`

 An additive map `L` applied to the mean of `x` over `H` is the mean of
`L (ρ (h⁻¹ a⁻¹ b k) x)` over `(a, b) ∈ H × H`, for any `h, k ∈ H`. 

 ### Properties of the mean 

### `apply_compactMean`

 The mean over `H` of any vector is fixed by `H`. 

### `compactMean_apply`

 Vectors in one `H`-orbit have the same mean over `H`. 

### `map_compactMean_of_const`

 A semilinear map `φ` that takes the value `c` on the whole `H`-orbit of `x` takes the value `c`
at the mean of `x` over `H`. 

### `map_compactMean_of_factor`

 If `φ` is `K`-invariant and `H ⊆ (g⁻¹ K g) · Stab x`, then `φ ∘ ρ g` takes the same value on `x`
and on its mean over `H`. 

### `compactMean_mem_levelSpace`

 The mean over `H` lies in `levelSpace ρ H`, the space of `H`-fixed vectors. 

### `IsUnitary.compactMean_adjoint`

 For `ρ` smooth with invariant scalar product `B`, the mean of `ρ` over a compact subgroup `H`
is self-adjoint for `B`. 


## Sums over coset representatives

`New.sum_mul_out`: for `H` of finite index in `G` and `f` right `H`-invariant, the sum of `f` over
the chosen representatives `q.out` of the cosets `q` equals the sum of `f (a * q.out)`.


### `New.sum_mul_out`

 A sum over coset representatives of `G ⧸ H` of a right `H`-invariant function does not
change under left translation. 


## Commutation, integrality and a bound for class sums

Under `New.HasFiniteType`, the class sum commutes with a second class sum and with multiplication by
a constant.


### `classSum_comm`

 Class sums over `Γ \ G / K` and over `Γ' \ G' / K'` commute. 

### `smul_classSum_mem`

 Integrality of class sums: if the order of every stabiliser `Γ ∩ g K g⁻¹` divides `M` and `f`
takes values in the additive submonoid `p`, then `M` times the class sum of `f` lies in `p`. 

### `classSum_le_card_mul`

 If the real function `f` is bounded above by `C ≥ 0`, its class sum is at most the number of
double cosets `Γ \ G / K` times `C`, since every weight `1 / #(Γ ∩ g K g⁻¹)` is at most `1`. 

### `classSum_le_card_mul_sq`

 If `√(f g) ≤ M` for every `g`, the class sum of the real function `f` is at most the number of
double cosets `Γ \ G / K` times `M ^ 2`. 
