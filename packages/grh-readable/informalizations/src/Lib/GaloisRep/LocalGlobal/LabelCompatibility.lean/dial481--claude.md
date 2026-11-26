---
{
  "module": "src/Lib/GaloisRep/LocalGlobal/LabelCompatibility.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/GaloisRep/LocalGlobal/LabelCompatibility.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/GaloisRep/LocalGlobal/LabelCompatibility.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Tame exponents of inertia and local-global compatibility for labelled forms

Let `w` be a finite place of `E` whose residue field `k_w` has order `q`, let `A` be a valuation
subring of an algebraic closure `Ω` lying over `w`, and let `T` be an injective complex-valued
multiplicative character of an algebraically closed extension `K` of `k_w`.

## Main definitions and results

* `New.GaloisRep.IsTameExponent w A T f s a`: the inertial element `s` moves a `(q ^ f - 1)`-th root
  of a uniformiser by the root of unity that `T` reads as `exp (2πi a / (q ^ f - 1))`.
* `New.GaloisRep.IsLabelledAt`: for a polynomial `c` over the residue field, the polynomial with
  roots `ιℓ ((T ^ a) x)` satisfies a given condition at each such `s`. Here `x` runs over the roots
  of `c`, `ιℓ` is the fixed map from `ℂ` to `PadicAlgCl ℓ`, and `T ^ a` is the `a`-th power of the
  character `T`.
* `New.GaloisRep.IsTameExponent.pow_apply_charName`: comparison with the local Artin map, for
  characters of `k_wˣ`.
* `New.GaloisRep.exists_isTameExponent`: exponents exist when `f` is a factorial.
* `New.GaloisRep.Attached.isLabelledAt`: if an eigenform has, at a split place `w`, a type for
  `GL n` of the residue field given by a label (`New.HasProductLabel`: a polynomial `c` of degree
  `d` and characters `χ l` with multiplicities `t l`, where `d + ∑ l, t l` is the rank and the roots
  of `c` and the names of the `χ l` are all distinct), then inertia at `w` acts on the attached
  Galois representation through the tame characters given by the roots of the polynomial of the
  label (`New.GaloisRep.IsLabelledAt`, `New.GaloisRep.IsTameExponent`). The proof uses base changes
  of prime degree in which `w` is inert to reduce to the case where `c` splits into linear factors.
  That case follows from `New.GaloisRep.Attached.local_global_of_eigencharacter` applied to local
  units.

Notions from other files:
* `New.IsPlaceOver A w`: the valuation subring `A` of `Ω` lies over `w`, that is, an integer of `E`
  is in the maximal ideal of `A` exactly when it lies in `w`.
* `New.Cohomology.centrePrime Ω A`: the integers of `Ω` that lie in the maximal ideal of `A`.
* `New.charName T χ`: the unit of `k_w` that names the character `χ` of `k_wˣ`; the map `χ ↦ x_χ` is
  an isomorphism from the character group of `k_wˣ` to `k_wˣ` that depends on `T`.
* `New.GaloisRep.PolyKillsAt r A s Q`: the polynomial `Q` kills `r s` if `ℓ` is a unit at `A`, and
  kills the action of `s` on the periods of `r` if `A` lies above `ℓ`.

## Relation to the literature

Known result: Local-global compatibility at tame level, away from ℓ and at ℓ. Here it is proved only
at split places, for depth-zero types induced from a squarefree type and characters of the
determinant. It is stated as polynomials that kill inertia elements, without the local Langlands
correspondence, and it is reduced by cyclic base change to the case of sorted tame Iwahori
eigencharacters. Source: Harris, Taylor, The geometry and cohomology of some simple Shimura
varieties (2001); Taylor, Yoshida, J. Amer. Math. Soc. 20 (2007); Barnet-Lamb, Gee, Geraghty,
Taylor, Local-global compatibility for l = p, II (2014), Thm 1.1.

See also `Lib.ClassField.Local.ArtinMap`.


 ## Tame exponents of inertial elements and inertia acting through labels 

### `exists_resField_hom`

 A ring homomorphism `g` from `𝓞 E` to a field that kills the prime `w` factors through the
residue field of `w`. 

### `IsTameExponent`

 The automorphism `s` has tame exponent `a` at level `f`. With `q = w.q` the order of the residue
field `k_w` and `Q = q ^ f`: (a) `A` lies over `w`; (b) `f ≠ 0`; (c) `s` lies in the inertia group
of `A`; and there are (d) a ring homomorphism `φ : 𝓞 Ω →+* K` that kills the centre of `A` and
extends the map `𝓞 E → k_w → K`, (e) a uniformiser `π ∈ E` and `z ∈ Ω` with `z ^ (Q - 1) = π`, and
(f) an integer `t` of `Ω` equal to `s z / z` with `T (φ t) = exp (2πi / (Q - 1)) ^ a`. 

### `IsLabelledAt`

 Inertia acts through the tame characters of level `f` given by the roots of `c`. This is in the
sense of the relation `P` between automorphisms and polynomials (such as "the polynomial kills the
image of `s`"). Whenever `s` has tame exponent `a` (`New.GaloisRep.IsTameExponent`), `P` holds for
`s` and `∏ x, (X - ιℓ ((T ^ a) x))`. The product is over the roots `x` of `c` in `K`, with
multiplicity. Here `T ^ a` is the `a`-th power of the character `T`. 

### `IsTameExponent.pow_apply_charName`

 Let `s` have tame exponent `a` at `A` over `w` (`New.GaloisRep.IsTameExponent`), let `K` be
algebraically closed and `T` injective, and let `u` be a local unit whose local Artin symbol is the
class of `s`. Then for every character `χ` of `k_wˣ`, the value of `T ^ a` at the image in `K` of
the unit `charName T χ` of `k_w` that names `χ` is the value of `χ` at the residue of `u`. 

### `_root_.New.IsLabel.root_pow_eq_one`

 Let `c` be a label of degree `r` over the residue field `k_w` of order `q` (monic, squarefree,
`c(0) ≠ 0`) and `x` a root of `c` in `K`. Then `x ^ (q ^ r! - 1) = 1`, and `x ^ (q ^ d - 1) = 1` for
some `d` with `1 ≤ d ≤ r`. 

### `exists_ringHom_centrePrime_le_ker`

 If `A` lies over `w` and `K` is algebraically closed, the embedding of the residue field of `w`
in `K` extends to a homomorphism `𝓞 Ω →+* K` that kills the centre of `A`. 

### `exists_isTameExponent`

 Let `A` lie over `w`, let `K` be algebraically closed and `T` injective (both are asked by
`IsFaithfulMulChar K T`), and take the level `f !`. Then (a) some element of the inertia group has
tame exponent `1`; (b) every element `s` of the inertia group has a tame exponent `a`, and if `s` is
the chosen generator `hA.tameGenerator` of tame inertia, this `a` is prime to `q ^ f ! - 1`, where
`q = w.q` is the order of the residue field. 

### `IsTameExponent.exists_tower_of_unramified`

 Tame exponents after an unramified base change. Let `u` be a place of `L / E` above `w` and
below `A`, unramified and with `q_u = q_w ^ p`. If `σ ∈ Gal(Ω/L)` has tame exponent `a` at level
`p * g` over `E`, then the residue fields form a tower `k_w → k_u → K`, whose first step has degree
`p` and is induced by `𝓞 E → 𝓞 L`, and `σ` has tame exponent `a` at level `g` over `L`. 

 ## Local-global compatibility at a split place for a labelled form 

### `New.GaloisRep.Attached.isLabelledAt_one`

 Local-global compatibility at level `1`. Let the Galois representation `r` be attached to the
Hecke polynomials `P` of the eigenform `f` of weight `κ`. At the split place `w`, `f` has the label
`labelChar T c * ∏ l, (χ l ∘ det on GL (t l))` (`New.HasProductLabel`: `c` of degree `d`,
`d + ∑ l, t l = card n`), where `T` embeds `Kˣ` in `ℂˣ` and `K` is algebraically closed. Let `A` lie
above `w`, and suppose the roots of `c` in `K` satisfy `x ^ (q - 1) = 1`, with `q = w.q`. Then
inertia at `A` is labelled (`New.GaloisRep.IsLabelledAt`) at level `1` by
`c * ∏ l, (X - charName T (χ l)) ^ t l`, in the following sense. For `σ` of tame exponent `a`, `r`
is of finite type at `A` (trivial on inertia near `1` if `ℓ` is a unit at `A`, and potentially
crystalline along embeddings inducing `A`) and has the Hodge–Tate jumps of `κ`. Also
`Q = ∏ x, (X - ιℓ ((T ^ a) x))` kills the action of `σ`, the product being over the roots `x` in `K`
of the label. 

### `New.GaloisRep.exists_isStepOfLocalChar_inert`

 Let `w` be a split place of the CM field `E` with Weil data, let `A` lie above `w`, and let `p`
be prime. There are a character `η` of `E_wˣ`, a continuous character `μ : Gal(Ω/E) → ℚ/ℤ` and a
place `u` of `stepField μ` (the field cut out by the symmetrised character `symmetrise μ`) such that
(a) these form a step of degree `p` with local character `η` (`New.GaloisRep.IsStepOfLocalChar`; in
particular `symmetrise μ` sends the local Artin symbol at `A` of each `x` to `η x`, and `u` is the
only place above `w`), and (b) `w` is inert in the step: `symmetrise μ` kills the inertia group of
`A`, the place `u` is unramified, and `q_u = q_w ^ p`. 

### `New.Lift.mul_prod_rankPart_detChar`

 Let `k' / k` be finite fields inside `K`. If `F : Hall k` lifts to `F' : Hall k'` (`New.Lift ℕ`:
for every `m`, one `ℕ`-combination of characters of `GL_m(k') ⋊ Gal(k'/k)` descends to both) and the
name of `χ' l` is the image of the name of `χ l`, then the lift extends to the products with the
`χ l ∘ det` and `χ' l ∘ det` in size `t l`. 

### `New.GaloisRep.Attached.isLabelledAt_of_root_pow_eq_one`

 Local-global compatibility at level `g`. Let `r` be attached to the Hecke polynomials of the
eigenform `f` of weight `κ`, which has the label `c`, `χ l`, `t l` at the split place `w`, and let
`A` lie above `w`. If the roots `x` of `c` in `K` satisfy `x ^ (q ^ g - 1) = 1`, where `q = w.q`,
then, as in `New.GaloisRep.Attached.isLabelledAt_one`, whenever `σ` has tame exponent `a` at level
`g`, `r` is of finite type at `A`, has the jumps of `κ`, and `∏ x, (X - ιℓ ((T ^ a) x))` kills the
action of `σ`, over the roots `x` of `c * ∏ l, (X - charName T (χ l)) ^ t l`. 

### `New.GaloisRep.Attached.isLabelledAt`

 Let the Galois representation `r` be attached to the Hecke polynomials `P` of the eigenform `f`
of weight `κ`, which has the label `c` (of degree `d`), `χ l`, `t l` at the split place `w`
(`New.HasProductLabel`), and let `A` lie above `w`. Then (a) `r` is of finite type at `A` (finite on
inertia, or potentially crystalline above `ℓ`), (b) it has the Hodge–Tate jumps of `κ`, and (c) if
`σ` has tame exponent `a` at level `d!` (`New.GaloisRep.IsTameExponent`), then
`∏ x, (X - ιℓ ((T ^ a) x))` kills the action of `σ` (`New.GaloisRep.PolyKillsAt`), the product being
over the roots `x` in `K` of `c * ∏ l, (X - x_l) ^ t l`, where `x_l = New.charName T (χ l)`.

This is local-global compatibility at tame level, away from `ℓ` and at `ℓ`, restricted to inertia at
a split place and to depth-zero types.

Clause (c) is a weak form of what this compatibility (Barnet-Lamb–Gee–Geraghty–Taylor, Caraiani)
gives together with the description of the inertial parameters of depth-zero representations of
`GL_n` (see Emerton–Gee–Herzig). 
