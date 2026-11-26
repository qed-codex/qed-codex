---
{
  "module": "src/Lib/Adelic/Adeles/LocalFactors.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Adelic/Adeles/LocalFactors.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Adelic/Adeles/LocalFactors.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Idelic generators of ideals, semilocal fields and tame local characters

The file collects local and idelic facts about number fields. For a CM field `E` it computes values
of the splitting character `υ`, and with `New.HasPrimitiveRoot5040 E` it shows that `New.Ô E` in the
finite adeles forms an adelic pair. It defines Schwartz–Bruhat functions, semilocal fields and tame
local characters, and shows that a finite product of completions is a semilocal field. An auxiliary
fact gives the valuation of natural numbers prime to one of valuation less than 1.

## Main definitions and results

* `New.exists_reduction_and_idele_generator`: a nonzero ideal `I` of `𝓞 E` has an idelic generator
  `t` in the integral finite adeles `New.Ô`, and `Ô / t Ô = 𝓞 / I`.
* `New.upsilon_toAdele`: the splitting character `υ` (`New.SplittingChar`) is trivial on the
  principal ideles.
* `New.upsilon_eq_prod_mul_of_v_eq`, `New.upsilon_eq_atUniformizer_zpow`,
  `New.upsilon_atUniformizer_mul_star`: values of `υ`, which is unramified at all finite places,
  computed from the valuations of the finite part and the values at the chosen uniformisers.
* `New.schwartzBruhat`: locally constant, compactly supported complex functions that vanish outside
  a set. `New.schwartzBruhat.comp`, `New.schwartzBruhat.isLocallyConstant_curry` and
  `New.integral_mem_of_isLocallyConstant` are tools for substituting and averaging.
* `New.SemilocalField`: conditions on a topological ring `F` that a finite product of
  non-archimedean local fields meets, with ring of integers `O` and uniformiser `ϖ`.
* `New.invOnUnits`, `New.TameLocalChar`: `χ⁻¹` cut off to the units of `O`, and the data showing
  that it comes from a primitive character (`New.Exchange.IsPrimitiveMulChar`) of the finite ring
  `O / ϖ`.

Notions from other files:
* `New.IsAdelic`: The properties of the pair Ô ⊂ 𝔸_f abstracted to R ⊂ A: R is open, compact and
  stable under conjugation, locally a valuation ring, contains a skew element i with −i·i = 1 and an
  element of trace 1, and −1 is a norm from R.
* `New.HasPrimitiveRoot5040`: `E` contains a primitive root of unity of order `7! = 5040`.
* `New.SplittingChar`: a unitary Hecke character `υ` of `E` that complex conjugation inverts and
  whose value at an idele `x` with unit finite part is `∏ x_τ / |x_τ|` over the infinite places
  `τ`; `υ.atUniformizer w` is its value at the chosen uniformiser at the finite place `w`.

## Relation to the literature

Known; see `Lib.ClassField.Global.CMSplittingCharacters` and `Lib.Weil.TameGaussSum` for sources.



## Idelic generators and the splitting character

An adele `x` is a pair: `x.1` the infinite and `x.2` the finite components. The valuation `v` is
multiplicative, with value `exp (-1)` at a uniformiser.


### `exists_idele_v_eq_exp_neg_multiplicity`

 For a nonzero ideal `I` of `𝓞 E` there is a finite idele `t` whose order at every finite place
`w` is the multiplicity of `w` in `I` and which is `1` at the places not dividing `I`. 

### `under_span_singleton_of_v_eq`

 Let `I` be a nonzero ideal of `𝓞 E` and `t` an integral finite adele whose order at every finite
place `w` is the multiplicity of `w` in `I`. Then the ideal `t Ô` of the ring `Ô` of integral finite
adeles contracts to `I`. 

### `forall_smul_mem_Ô_iff_of_map_eq_span`

 Let `Ô` be the ring of integral finite adeles and `y` a finite adele. If the ideal `I` of `𝓞 E`
generates the principal ideal `t Ô` of `Ô`, then `I y ⊆ Ô` if and only if `t y ∈ Ô`. 

### `exists_reduction_and_idele_generator`

 A nonzero ideal `I` of `𝓞 E` becomes principal in the ring `Ô` of integral finite adeles
(a subring of the finite adeles `𝔸f E`), and `Ô / I Ô = 𝓞 / I`. There is a ring
map `ρ : Ô → 𝓞 / I` that (a) extends the reduction modulo `I` and (b) has kernel `I Ô`, and a
finite idele `t` that (c) is integral, is `1` at the places not dividing `I` and generates the
kernel, and (d) has order `ord_w I` at every `w`; (e) for a finite adele `y`, `I y ⊆ Ô` if and
only if `t y ∈ Ô`. 

### `upsilon_toAdele`

 The splitting character `υ` is trivial on the principal ideles, the images of `Eˣ`. 

### `upsilon_eq_prod_mul_of_v_eq`

 Let υ be the splitting character. If an idele x and a finite idele y have the same valuation at
every finite place, then υ(x) is υ(y) times the product of x_τ/|x_τ| over the infinite places τ.
Here y is read as an idele with component 1 at the infinite places. 

### `upsilon_eq_atUniformizer_zpow`

 Let `υ` be the splitting character and let the idele `x`, with infinite components `x.val.1`
and finite components `x.val.2`, be a unit at all finite places other than `w`. Then `υ x` is
`∏ x_τ / |x_τ|` over the infinite places `τ`, times the value `υ.atUniformizer w` of `υ` at the
uniformiser at `w` to the power `ord_w x` (which is `-log (v (x.val.2 w))`). 

### `upsilon_atUniformizer_mul_star`

 The values of the splitting character at the uniformisers of a finite place `w` and of its
complex conjugate are inverse to each other. 

 ## Natural numbers of valuation one 

### `Nat.Coprime.valuation_eq_one`

 If the natural number `p` has valuation less than `1` at a valuation subring `B` of a field,
then every natural number `q` prime to `p` has valuation `1` at `B`. 


## The integral finite adeles as an adelic pair

The instance `New.isAdelic_Ô` lets the local results, proved for an abstract pair `R ⊆ A` with
`New.IsAdelic R`, be applied to the integral finite adeles `New.Ô E` of a CM field `E` with
`New.HasPrimitiveRoot5040 E`.


### `New.isAdelic_Ô`

 The integral finite adeles of a CM field `E` with `HasPrimitiveRoot5040 E` have the properties
collected in `IsAdelic`. 


## Schwartz–Bruhat spaces, semilocal fields and tame characters

Schwartz–Bruhat functions on topological spaces, then semilocal fields `F` (rings that behave like
finite products of non-archimedean local fields) and tame characters of them.


 ### Locally constant functions with compact support 

### `schwartzBruhat`

 The space of locally constant, compactly supported complex functions on X that vanish
outside s. 

### `schwartzBruhat.comp`

 Let `f : Y → X` be continuous with a continuous left inverse `g` that maps `s` into `t`. If
`φ` is locally constant, compactly supported and zero outside `s`, then `φ ∘ f` is locally
constant, compactly supported and zero outside `t`. 

### `eventually_eqOn_of_isLocallyConstant_uncurry`

 Let `ψ γ` be a family of functions on `X` that is locally constant jointly in the parameter `γ`
and the point. On a compact set `K`, the functions `ψ γ` agree with `ψ k` for `γ` near `k`. 

### `schwartzBruhat.isLocallyConstant_curry`

 Let `f γ : Y → X` be a family of maps with left inverses `g γ`, both jointly continuous in the
parameter `γ` and the point. If `φ` is locally constant, compactly supported and zero outside `s`,
then the function `y ↦ φ (f γ y)` depends on `γ` in a locally constant way. 

### `integral_mem_of_isLocallyConstant`

 The pointwise integral of a locally constant family of functions over a compact space, for a
finite measure, lies in every subspace `P` that contains all members of the family. 

 ### Semilocal fields and their characters 

### `SemilocalField`

 Conditions met by a finite product of non-archimedean local fields: a locally compact ring with
Haar measure, compact open subring O of volume one, an element ϖ of O that is invertible in F and
topologically nilpotent, and `New.IsValuationPair O`. 

### `SemilocalField.O`

 The ring of integers. 

### `SemilocalField.ϖ`

 The element called the uniformiser: a unit of `F`, only required to be integral and
  topologically nilpotent. 

### `SemilocalField.ϖ_mem`

 The uniformiser is integral. 

### `SemilocalField.isCompact_O`

 The ring of integers is compact. 

### `SemilocalField.volume_O`

 The Haar measure gives the ring of integers volume one. 

### `SemilocalField.isOpen_O`

 The ring of integers is open. 

### `SemilocalField.isTopologicallyNilpotent_ϖ`

 The powers of the uniformiser tend to zero. 

### `SemilocalField.isValuationPair`

 As in a product of valuation rings, for `a, b` in `F` there is an idempotent `e` of `O` such
  that `a` and `b` are `O`-multiples of `(1 - e) a + e b`. 

### `IsIntegralUnit`

 x is a unit of the subring O. 

### `invOnUnits`

 `χ⁻¹` on the units of `O`, zero elsewhere. 

### `TameLocalChar`

 A finite residue ring O/ϖO with the reduction π from O onto it, and a primitive character η
(`New.Exchange.IsPrimitiveMulChar`) of it such that η ∘ π is χ⁻¹ on the units of O and 0 on the rest
of O. 

### `TameLocalChar.ResidueRing`

 The residue ring `O / ϖ`. 

### `TameLocalChar.commRing`

 The ring structure of the residue ring. 

### `TameLocalChar.finite`

 The residue ring is finite. 

### `TameLocalChar.reduction`

 The reduction `π` from `O` to the residue ring. 

### `TameLocalChar.resChar`

 The character `η` of the residue ring through which `χ⁻¹` factors on the units of `O`. 

### `TameLocalChar.reduction_surjective_and_eq_zero_iff`

 The reduction is surjective with kernel `ϖ O`. 

### `TameLocalChar.isPrimitive_resChar_and_invOnUnits_eq`

 `η` is primitive, and `η ∘ π` is `χ⁻¹` on the units of `O` and zero on the rest of `O`. 

### `HasIntegralConductor`

 The additive character ψ is continuous and has conductor O: ψ is trivial on tO exactly when t
lies in O. 


## Finite products of completions

For a finite set `P` of finite places of a number field `E`, the product `New.LocProd` of the
completions `New.LocField` at `P` satisfies the conditions `New.SemilocalField`.


### `LocProd`

 The product of the completions E_w over the places w in P. 

### `noncomputable instance : SemilocalField (LocProd P)`

 The product of the completions at the places in `P` is a semilocal field: `O` is the product of
the local rings of integers and `ϖ` is the family of the chosen uniformisers. 

### `mem_O_locProd`

 An element of the product of the completions at `P` lies in the ring of integers `O` exactly
when each of its components has valuation at most `1`. 
