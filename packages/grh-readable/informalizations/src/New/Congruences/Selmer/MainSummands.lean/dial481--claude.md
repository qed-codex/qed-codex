---
{
  "module": "src/New/Congruences/Selmer/MainSummands.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Congruences/Selmer/MainSummands.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Congruences/Selmer/MainSummands.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Main summands are Selmer data

A row is an `ℓ`-adic representation `R` that satisfies `IsMainSummandLike`. A main summand is a
lattice `u` in a row `R`, with the crystalline conditions above `ℓ`; the row is the main summand
with scalars extended to `ℚ̄_ℓ`.

* `New.Selmer.IsMainSummandLike.eventually_exists_selmerDatum`: over all large coefficient rings a
  row has a lattice that is a Selmer datum, with bounds for the global and the local terms.

Notions from other files:
* `New.Selmer.IsMainSummandLike`: the hypotheses on an `ℓ`-adic representation of the Galois group
  of `D.E` under which its Selmer groups are estimated.
* `New.Selmer.IsLatticeIn`: `u` over the coefficient ring `O` is conjugate to `R` over `ℚ̄_ℓ`.
* `New.Selmer.SelmerDatum`: a lattice `T` with local conditions and the number `β_T`.
* `New.Selmer.crysCocyclesAt`, `New.Selmer.crysRelations`: the crystalline cocycles at a place above
  `ℓ`, and the linear relations that hold on them.
* `New.CoeffRing.normLength`: a length over `O`, rescaled so that `O / ℓ` has length `1`.

## Relation to the literature

See `New.Congruences.Selmer.TwistingTheorem` for related work.


### `exists_dvd_ell_pow`

 A nonzero element `a` of a coefficient ring `O` divides some power of `ℓ`. 

### `ne_top_of_normLength_le`

 A length `k` over `O` whose normalisation `O.normLength k` has a finite bound is finite. 

### `IsMainSummandLike.trace_lattice_conjGal`

 Conjugate self-duality of a lattice `u` in a main summand `R`, on traces: `tr u
(g^c) = cyclotomicInv(g) ^ (t - 1) * tr u (g⁻¹)` (truncated `ℕ` subtraction), where
`g^c = conjGal g` is the conjugate of `g` by complex conjugation and `cyclotomicInv` is the inverse
of the cyclotomic character `cyc`. 

### `IsMainSummandLike.conjGal_inv_eq_smul_one`

 Let `u` be an `O`-lattice (`IsLatticeIn R u`) in a main summand `R`
(`IsMainSummandLike D t J R`, of which conjugate self-duality is used) whose image spans all
matrices. If `g` acts by the scalar `y`, then `(conjGal g)⁻¹ = (c g c)⁻¹`, with `c` the complex
conjugation, acts by the scalar `cyc(g) ^ (t - 1) * y`. Here `cyc` is the cyclotomic character and
`cyclotomicInv` is its inverse. 

### `IsMainSummandLike.isUnit_of_eq_smul_one`

 A scalar by which a Galois element acts through `u` is a unit. The hypothesis `hrow` is used
only to know that `n` is not empty. 

### `IsMainSummandLike.sum_countP_neg_le`

 For a main summand `R`, the number of negative integers among the Hodge–Tate jumps `J σ`,
counted with multiplicity and summed over all complex embeddings `σ` of `D.E`, is at most the number
of infinite places of `D.E` times `card n`. 

### `IsMainSummandLike.sum_finrank_crysCocyclesAt_le`

 The rank inequality for an `O`-lattice `u` (`IsLatticeIn R u`) in a main summand `R`. For a
place `v` above `ℓ` let `crysCocyclesAt v u` be the `O`-module of crystalline cocycles of the
decomposition group at `v` with values in `O ^ n`, acted on through `u`. The ranks of these modules
add up to at most `card n` times the sum of the numbers of places of `D.E` above `ℓ` and of infinite
places of `D.E`. 

### `IsMainSummandLike.normLength_congruenceTerm_le`

 The global term. Let `u` be an `O`-lattice (`IsLatticeIn R u`) in a main summand `R` whose image
spans all matrices. Let some `g` act by a scalar `α` and have cyclotomic character `p_l ^ card n`,
where `p_l = D.levelPrime l` is one of the primes `p₀, p₁` of the data and `Ω = New.Ω` is the
algebraic closure of `ℚ`. The number `congruenceTerm ℓ u` is the supremum, over nonzero `a` in `O`,
of the lengths of the modules of equivariant maps from `W = (O / a) ^ n` to its conjugate dual: the
character module of `W`, on which `x` acts by `y ↦ cyc(x^c) · y ∘ (x^c)⁻¹`, with `cyc` the
cyclotomic character and `x^c = conjGal x`. Normalised so that `O / ℓ` has length `1`, it is at most
`card n` times the `ℓ`-adic valuation of `D.chosenGroupOrder`, the product of the orders of
`GL (D.r * D.t)` over the residue fields of the chosen places above `p₀` and `p₁`. 

### `IsLatticeIn.normLength_addVal_det_sub_one`

 For a lattice `u` in `R`, the valuation of `det (u g - 1)` in `O`, normalised by `v(ℓ) = 1`, is
the valuation `ellVal` of `det (R g - 1)` in `ℚ̄_ℓ`. 

### `IsMainSummandLike.normLength_localTerm_le`

 The local term. Let `u` be an `O`-lattice (`IsLatticeIn R u`) in a main summand `R` and `v` a
place above one of the primes `p₀, p₁` of the data and prime to `ℓ`. The number `localTerm u v` is
the supremum, over nonzero `a` in `O`, of the excess over the length of `W = (O / a) ^ n` of the
length of the module of restrictions to the decomposition group at `v` of the locally constant
global cocycles with values in `W`. Normalised so that `O / ℓ` has length `1`, it is at most
`card n` times the `ℓ`-adic valuation of `D.chosenGroupOrder`, the product of the orders of
`GL (D.r * D.t)` over the residue fields of the chosen places above `p₀` and `p₁`. 

### `IsMainSummandLike.normLength_firstPrimeTerms_le`

 The terms at the tame generator. Let `R` be a main summand and let `u` be a lattice in `R`. Let
`w` be a chosen place above `p₀ p₁` and prime to `ℓ`, and let `γ` be the tame generator at `w`. The
number `firstPrimeTerms ℓ u γ` is the sum of the valuations of `det (u g - 1)` for `g = γ` and
`g = (conjGal γ)⁻¹`. Its normalised length `O.normLength` is at most `2 · card n` times the `ℓ`-adic
valuation of `D.chosenGroupOrder`. 

### `IsMainSummandLike.normLength_placeTerms_add_firstPrimeTerms_le`

 The sum of the local terms. Let `u` be an `O`-lattice (`IsLatticeIn R u`) in a main summand `R`,
let `S` be the set of places above `ℓ p₀ p₁`, and let `w` be a chosen place above `p₀ p₁` and prime
to `ℓ`. Add the terms `localTerm u v` at the places `v` of `S` prime to `ℓ` and the valuations of
`det (u g - 1)` for `g` the generator `γ` of tame inertia at `w` and for `g = (conjGal γ)⁻¹`
(`firstPrimeTerms`). The normalised sum is at most `(4 f + 2) · card n` times the `ℓ`-adic valuation
of `D.chosenGroupOrder`, the product of the orders of `GL (D.r * D.t)` over the residue fields of
the chosen places above `p₀` and `p₁`; `f = D.f` is the number of infinite places. 

### `IsMainSummandLike.exists_mem_inertiaAbove_eq_smul_one_isUnit`

 For an `O`-lattice `u` (`IsLatticeIn R u`) in a main summand `R`, some element `γ` of an inertia
group (`inertiaAbove`) at a place above the primes `p₀ p₁` of the data `D` and prime to `ℓ` acts
through `u` by a scalar `ζ` in `O` such that `ζ ^ 2 - 1` is a unit. 

### `IsMainSummandLike.eventually_exists_selmerDatum`

 Main summands are Selmer data. Let `D` be the data for the parameters `P`, with field `D.E`, and
let `n` be a finite index type. Fix a prime `ℓ` and an isomorphism `ℂ ≃ ℚ̄_ℓ` (`PadicIso ℓ`). Let
`R` be a row (`IsMainSummandLike`): a continuous representation on `n`-vectors of the Galois group
of `D.E` over `ℚ̄_ℓ`, unramified off `ℓ p₀ p₁`, with `R^c ≅ R^∨(1 - t)` on traces (`t = 0` read as
`1`) and Hodge–Tate jumps `J σ` at the complex embeddings `σ`, such that the images of its lattices
span all matrices and contain suitable scalars, and `det (R g - 1)` has bounded valuation for
suitable inertia elements `g` above `p₀ p₁`. Let `w` be a chosen place above `p₀ p₁` and prime to
`ℓ`, and `γ` the chosen generator of tame inertia at `w`.

Over all large coefficient rings `O` there is a Selmer datum `T` for `γ` and the places
`badPlaces D ℓ` dividing `ℓ p₀ p₁` or the level `D.N`, such that `T.ρ` is a lattice in `R`, and
`T.places` consists of the places above `ℓ p₀ p₁`; the linear relations `T.localRelations` that hold
on the allowed cocycles are those that hold on the crystalline cocycles at the places above `ℓ`
(`crysRelations`); and `T.β` has normalised length `O.normLength T.β` at most `(4 f + 3) · card n`
times the `ℓ`-adic valuation of `D.chosenGroupOrder`, with `f = D.f` the number of infinite
places. 
