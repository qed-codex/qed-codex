---
{
  "module": "src/New/Congruences/Lifting/TameCharts.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Congruences/Lifting/TameCharts.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Congruences/Lifting/TameCharts.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Tame Kummer charts and the power of p that kills cokernels of Kisin modules

A tame chart `New.Lift.TameChart` is a Kummer chart `New.Lift.KummerChart`, with coordinate `z` and
exponent `e`, together with an element `s` of inertia. The power `s ^ k` multiplies `z` by `ξ ^ k`,
for some `ξ` in Λ = W(𝔽_{p^f}) that is a primitive e-th root of unity modulo `p`. The degree of a
polynomial that kills the operator induced by `s` bounds the power of `p` that kills the cokernel of
the map of Kisin modules attached to an extension of a trivial lattice `C` by a lattice `Y`. The
file also shows that, if Γ maps onto G_p, tame charts exist for each ramification index e dividing
p^f − 1, when p does not divide f.

## Main definitions and results

* `New.Lift.TameChart.exists_z_smul_eq_sum_tameGen`: if a polynomial `q` over `ℤ_p` kills the
  operator β induced by `s`, then `q(s)` maps the Kisin module into `z` times
  `New.Lift.KummerChart.JumpLattice.kisinAinf`.
* `New.Lift.TameChart.killsCokernel_of_isKilledBy`: if `Y` is potentially crystalline and a monic
  `q` kills β on `Y`, then `p ^ κ` kills the cokernel, that is, multiplies the constants of `C` into
  the image, as soon as `m (deg q + 1) ≤ κ`, `e ≤ p ^ m` and `p` is large against `κ` and the jumps.
* `New.Lift.exists_tameChart`: tame charts exist.

Notions from other files:
* `New.Lift.WittFq`: The ring Λ = W(𝔽_{p^f}) of constants, 𝔽_{p^f} taken inside the tilt O^♭.
* `New.Period.linearFrob`: For s in inertia, `linearFrob ρ s 0` is the B-linear operator β on B ⊗ T
  (B = `Bmax`) that acts as s on the vectors fixed by the elements of Γ near 1.
* `New.Lift.KummerChart.Letter`: A letter is a unit i of 𝔽_{p^f}. The coefficient ring O carries an
  element ζ with ζ^{p^f−1} = 1, and the letter-i part of W(C^♭) ⊗ L is where ζ acts as [i].

## Relation to the literature

See `New.Congruences.Lifting.CupOrthogonalityBounds` for related work.



## Tame charts and the power of p killing the cokernel of Kisin modules

Idea of the proof of `New.Lift.TameChart.killsCokernel_of_isKilledBy`: start from a power `z ^ ν`,
`ν < e`, in the ideal of multipliers and lower the exponent one step at a time.


### `TameChart`

 A tame Kummer chart for `Γ → G_p`. A Kummer chart gives constants `Λ = W(𝔽_{p^f})`, a
coordinate `z = chart.z ∈ A_inf`, an exponent `e` and a subgroup `Γ'` of `Γ` that fixes `Λ` and
`θ(z)`. A tame chart has `Γ'` normal and `p ∤ e`, an element `ϖ ∈ ℚ̄_p` fixed by `Γ'` with
`ϖ ^ e = p`, and an element `s ∈ Γ` with image in inertia (`IsWeilPair (toGp s) 0`) whose powers fix
`Λ` pointwise in `A_inf` (`FixesLambda`), such that `s ^ k` multiplies `z` by `ξ ^ k`. Here `ξ ∈ Λ`
is, modulo `p`, a primitive `e`-th root of unity. 

### `TameChart.tameMultiplier`

 The element ξ of Λ = W(𝔽_{p^f}) by which the tame generator multiplies z. 

### `TameChart.tameGen`

 The tame generator s, an element of Γ. 

### `TameChart.isPrimitiveRoot_tameMultiplier`

 Modulo p, ξ is a primitive e-th root of unity, e the exponent of the chart. 

### `TameChart.tameGen_pow_smul_z`

 s^k z = ξ^k z. 

### `TameChart.isWeilPair_tameGen`

 s lies in inertia. 

### `TameChart.fixesLambda_tameGen_pow`

 Every power of s fixes Λ. 

### `TameChart.ϖ`

 An element ϖ, an e-th root of p. 

### `TameChart.apply_varpi`

 Every element of Γ' fixes ϖ. 

### `TameChart.varpi_pow_eq`

 ϖ^e = p. 

### `TameChart.tame`

 p does not divide e. 

### `TameChart.normal`

 Γ' is normal in Γ. 

### `conjForm_mem_crysForms`

 Let `Γ` be a group with a map to `G_p = Gal(ℚ̄_p/ℚ_p)` of open image, and let `d` be a tame
chart for it. In particular, `d` gives a normal subgroup `Γ'` of `Γ` of index prime to `p`. Let `O`
be a finite free `ℤ_p`-algebra and `L` a finite free `O`-module with an action of `Γ` whose
restriction to `Γ'` is crystalline. Let `μ : W(C^♭) ⊗ L → B_dR` be a crystalline form: it is
`A_inf`-linear, `Γ'`-equivariant on `1 ⊗ L`, and its values on `1 ⊗ L` come from a `ℤ_p`-linear map
`L → Bmax`. Then its conjugate `x ↦ g⁻¹ μ(g x)` by `g ∈ Γ` is a crystalline form. 

### `sum_coeff_smul_conjForm_apply_eq_zero`

 Let `d` be a tame chart for a group `Γ → G_p`, with subgroup `Γ'` and inertia element
`s = d.tameGen`. Let `O` be a finite free `ℤ_p`-algebra and `L` a finite free `O`-module with an
action of `Γ` that is crystalline over `Γ'`.
* `β = linearFrob L.ρ s 0` is the `Bmax`-linear operator on `Bmax ⊗ L` that acts as `s` on the
  vectors fixed by the elements of `Γ` near `1`, and `q = ∑ q_k X ^ k` is a polynomial over `ℤ_p`
  with `q(β) = 0`.
* `μ : W(C^♭) ⊗ L → B_dR` is a crystalline form: it is `A_inf`-linear, `Γ'`-equivariant on `1 ⊗ L`,
  and its values on `1 ⊗ L` come from a `ℤ_p`-linear map `L → Bmax`.
* `x` lies in `L.kisinAinf`: it lies in `A_inf[1/τ] ⊗ L`, `τ = [ε^{1/p}] - 1`, and every
  `A_inf`-linear map to `B_dR` that is `Γ'`-equivariant on `1 ⊗ L` sends `φ ^ n x` into `B_dR⁺` for
  all `n ≥ 1`, with `φ` the Frobenius.

Then `∑ q_k • μ_k x = 0`, where `μ_k = conjForm μ (s ^ k)` is the conjugate `y ↦ s⁻ᵏ μ(sᵏ y)`. 

### `exists_z_smul_eq_sum_tameGen`

 Let `Γ` be a group over `G_p = Gal(ℚ̄_p/ℚ_p)` with a tame chart `d`: this gives an element
`z = d.z` of `A_inf`, a subgroup `Γ'` of `Γ`, and an element `s = d.tameGen` with image in inertia
that multiplies `z` by a constant. Let `L` be a finite free module over a finite free `ℤ_p`-algebra,
with an action of `Γ` that is crystalline over `Γ'`. Let `q` over `ℤ_p` kill the operator
`β = linearFrob L.ρ s 0` that `s` induces on `Bmax ⊗ L`.

The `A_inf`-module `L.kisinAinf` consists of the `y` in `A_inf[1/τ] ⊗ L`, `τ = [ε^{1/p}] - 1`, such
that every `Γ'`-equivariant form sends `φ ^ n y` into `B_dR⁺` for all `n ≥ 1`, with `φ` the
Frobenius. Such a `y` is in `L.kisinModule` if, moreover, these forms take at `y` values in the
subfield `valueField 0` of `B_dR`, which the chart generates over the field fixed by `Γ'`.

Then, for `x` in `L.kisinModule`, `∑ q_k • s ^ k • x` is `z` times an element of `L.kisinAinf`. 

### `aeval_linearFrob_extensionLattice_eq_zero`

 Let `Γ` be a group over `G_p = Gal(ℚ̄_p/ℚ_p)`, `d` a tame chart for it, with tame generator `s`,
and `O` a finite free `ℤ_p`-algebra. A pairing side `S` consists of two lattices `Y` and `C` over
`O` with actions of `Γ` and an `O`-linear map from `C` to the crystalline cocycles of `Y`. It gives
the extension `Ỹ = S.extensionLattice` of `C`, with trivial action, by `Y`.

The hypothesis `IsKilledBy` says that `Y` is potentially crystalline and that `q`, a polynomial over
`ℤ_p` read over `O`, kills the operator `β` induced by `s` on `Bmax ⊗ Y`. Then `q * (X - 1)` kills
the operator `β` on `Bmax ⊗ Ỹ`. 

### `count_constantCoeff_aeval_tameMultiplier_pow_le`

 A tame chart `d` has an exponent `e`, prime to `p`, and an element `ξ = d.tameMultiplier` of
`Λ = W(𝔽_{p^f})` whose residue in `𝔽_{p^f}`, its `constantCoeff`, is a primitive `e`-th root of
unity. So, for a monic polynomial `Q` over `ℤ_p` and `ν ≤ e`, at most `deg Q` of the `k < ν` make
the residue of `Q(ξ ^ k) ∈ Λ` zero. 

### `aeval_tameMultiplier_pow_mul_mem_liftIdeal`

 Let `d` be a tame chart. It gives a coordinate `z = d.z ∈ A_inf` and a tame generator `s`, an
element of inertia that multiplies `z` by the constant
`ξ = d.tameMultiplier ∈ W(𝔽_{p^f}) = WittFq d.f`. Let `Ỹ` be the extension of `C` by `Y` given by
the pairing side `S`, and let `Q` over `ℤ_p`, with `Q(1) = 0`, kill the operator induced by `s` on
`Bmax ⊗ Ỹ`.

The ideal `S.liftIdeal r 0 i` of `A_inf` is generated by the natural number `r` and by the elements
that multiply the letter-`i` part of `A_inf ⊗ C` into the image of the letter-`i` part of
`S.extensionLattice.kisinAinf`, the Kisin module of `Ỹ` over `A_inf`: this consists of the elements
of `A_inf[1/τ] ⊗ Ỹ`, `τ = [ε^{1/p}] - 1`, whose images by all positive powers of Frobenius are sent
into `B_dR⁺` by the equivariant forms.

If `p ^ t * z ^ (k + 1)` lies in this ideal, then so does `Q(ξ ^ (k + 1)) * p ^ t * z ^ k`. 

### `killsCokernel_of_isKilledBy`

 Let `Γ` be a group over `G_p = Gal(ℚ̄_p/ℚ_p)`. Let `d` be a tame chart for it: a coordinate
`z ∈ A_inf` of exponent `e` prime to `p`, with an element `s` of inertia that multiplies `z` by a
constant `ξ`, a primitive `e`-th root of unity modulo `p`. Let `O` be a finite free `ℤ_p`-algebra
with its element `O.ζ`, `ζ ^ (p ^ f - 1) = 1`. Let `S` be a pairing side over `O`: lattices `Y`, `C`
with a map from `C` to the crystalline cocycles of `Y`, hence an extension `Ỹ` of the trivial
lattice `C` by `Y`. For a letter `i ∈ 𝔽_{p^f}ˣ`, the finite set `S.jumpSet i` holds the jumps of the
Hodge filtration of `Y` at the embeddings of `O` that send `O.ζ` to the Teichmüller lift of `i`.

Suppose that all these jumps are `≤ n`, that `Y` is potentially crystalline and that a monic `q`
over `ℤ_p` kills the operator induced by `s` on `Bmax ⊗ Y`; the last two conditions are
`IsKilledBy`, whose `0` is the power of Frobenius composed with `s`. If `e ≤ p ^ m`,
`m (deg q + 1) ≤ κ` and `n + κ + 2 < p`, then `S.KillsCokernel i κ 0`: multiplication by
`p ^ κ * E ^ 0 = p ^ κ`, `E` the generator of `ker θ`, kills the cokernel at `i`. 


## Existence of tame Kummer charts of given ramification index


### `exists_normal_fixer_index_coprime`

 Let `f` be a positive integer prime to `p`, let `e` divide `p ^ f - 1`, and let `ϖ ^ e = p` in
`ℚ̄_p`. The elements of `Gp p = Gal(ℚ̄_p/ℚ_p)` that fix `ϖ` and the image of the Witt vectors
`W(𝔽_{p^f})` in `A_inf` (`FixesLambda f`) form an open normal subgroup of index prime to `p`. 

### `exists_chart_untilt_varpiFlat_eq`

 A chart is given by constants `W(𝔽_{p^f})`, an exponent `e` and an element `ϖ^♭` of the tilt of
`O_{ℂ_p}`, with coordinate `z = [ϖ^♭]`. If `ϖ ^ e = p`, some chart with the given `f` and `e` has
a `ϖ^♭` that untilts to `ϖ`. 

### `exists_inertia_smul_z_eq_teichmuller`

 Inertia is transitive on towers of roots of `p`: if `ϖ^♭` of a chart `c` (with coordinate
`z = [ϖ^♭]`) and `x` both untilt to `e`-th roots of `p`, an element of inertia maps `z` to `[x]`. 

### `fixesLambda_of_mem_inertiaGroup`

 An element of inertia fixes the constants `W(𝔽_{p^f})`. 

### `exists_inertia_smul_z_eq_teichmuller_mul`

 Let `ϖ^♭` of the chart `c` (with coordinate `z = [ϖ^♭]` and exponent `e`) untilt to an `e`-th
root of `p`, and let `a ∈ 𝔽_{p^f}` be an `e`-th root of unity. Then an element of inertia multiplies
`z` by the constant `[a]`. 

### `pow_smul_z_eq_pow_mul`

 If `g` fixes the constants `W(𝔽_{p^f})` of the chart `c` and multiplies its coordinate `z` by a
constant `ξ`, then `g ^ n` multiplies `z` by `ξ ^ n`. 

### `exists_coe_eq_of_pow_eq_p`

 An `e`-th root `ϖ` of `p` in `ℚ̄_p`, `e ≠ 0`, is an element of the ring of integers of `ℂ_p`. 

### `exists_tameChart`

 Let the structure map `Γ → G_p = Gal(ℚ̄_p/ℚ_p)` be surjective and `f` a positive integer prime
to `p`. Let `e` divide `p ^ f - 1`, so that `𝔽_{p^f}` contains a primitive `e`-th root of unity.
Then there is a tame chart for `Γ` of exponent (ramification index) `e`. 
