---
{
  "module": "src/Lib/SiegelWeil/NeighbourLattices.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/SiegelWeil/NeighbourLattices.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/SiegelWeil/NeighbourLattices.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Neighbours of the standard lattice

Let E be a CM field with Weil data (`WeilData E`, used here for a primitive 5040th root of unity,
hence √-1, and an element of trace 1), so that every finite place of its real subfield is split or
inert; let L = Ô^n be the standard lattice (`New.stdLattice`) with the form ⟨x, z⟩ = x* z, and w a
finite place of E with uniformiser ϖ and residue field k_w of order q_w. A vector x that is
supported at w, lies outside L, and has ϖx ∈ L and ⟨x, x⟩ integral defines a neighbour L₁ = L₀ + Ôx
of L, where L₀ = {z ∈ L : ⟨x, z⟩ integral}. A quasi-reflection ρ supported on w and its conjugate
maps L₁ into L. The same ρ serves all x with the same line of ϖx in k_w^n and the same residue of
ϖ⟨b, cx − b⟩, where b is a fixed such vector with this line and c a unit with cx − b ∈ L; these
residues number at most √q_w, and at most one if w is split. A lattice γL ≠ L, for γ unitary, holds
such a vector x at some place w, and passing from γ to ργ divides the index [L : L ∩ γ⁻¹L] = [γL : L
∩ γL] by at least q_w. So a step from L to L₁ towards γL is read as a step from γL to ργL towards L.
This file treats one step; the steps are summed in `Lib.SiegelWeil.UnramifiedSeries.RallisSeries`.

If w is split, L₁ is L enlarged by a line at w and cut down to a hyperplane at w̄. So the steps at w
and at w̄ go up by a line and down by a hyperplane at w. If w is inert, the line of ϖx determines L₀
and its dual L + Ôx, and the residues index the isotropic lines other than L/L₀ in the hermitian
plane (L + Ôx)/L₀.

## Main definitions and results

* `New.SiegelWeil.IsNeighbourVector`, `New.SiegelWeil.MapsNeighbour`: the vector x, and the relation
  ρL₁ ⊆ L.
* `New.SiegelWeil.neighbourResidues`: the residue classes that tell apart the neighbours with the
  same line; `New.SiegelWeil.card_neighbourResidues_le_one` and
  `New.SiegelWeil.card_neighbourResidues_sq_le` bound their number.
* `New.SiegelWeil.exists_family_mapsNeighbour`: a family of ρ, indexed by lines and residue classes,
  serves all x.
* `New.SiegelWeil.exists_isNeighbourVector_mulVec`: a lattice γL ≠ L holds such a vector.
* `New.SiegelWeil.q_mul_norm_finMultiplier_mul_sq_le`: one step lowers the index.

Notions from other files:
* `New.stdLattice E n`: the standard lattice Ô^n, where `Ô E` is the ring of integral finite adeles
  in the finite adele ring `𝔸f E`; `singleAdele w a` is the finite adele with component a at w and 0
  elsewhere, so `singleAdele w c • x` is the multiple c x at w.
* `New.finMultiplier γ`: its squared absolute value is the index [L : L ∩ γ⁻¹L].

## Relation to the literature

Known result: Kneser's neighbours. Here only the standard lattice over the integral finite adeles
and its translates by unitary elements are treated; split and inert places are treated by the same
step, taken at w or at its conjugate. Source: M. Greenberg, J. Voight, Lattice methods for algebraic
modular forms on classical groups (2014), section 5.


 ### Integral finite adeles and products at one place 

### `mem_Ô_of_eq_zero_of_ne`

 A finite adele that vanishes away from `w` and is integral at `w` is integral. 

### `singleAdele_one_mul`

 Multiplication by the idempotent at `w` keeps the component at `w` and deletes the others. 

### `single_mem_stdLattice`

 The standard lattice contains the vectors with one integral coordinate and all others zero. 

### `star_dotProduct_apply`

 The component at `u` of the adelic product `x* z = ∑ j, x̄ j * z j`, computed in the local field
at `u`. 

 ### Neighbour vectors and their residues 

### `IsNeighbourVector`

 The vector `x` defines a neighbour at `w` of the standard lattice `L`: it is supported at
`w`, `ϖ x ∈ L` and `x ∉ L` for a uniformiser `ϖ` at `w`, and its norm `x* x` is integral. 

### `IsNeighbourVector.eq_zero_of_ne`

 The components away from `w` vanish. 

### `IsNeighbourVector.v_le`

 The coordinates have poles of order at most one at `w`. 

### `IsNeighbourVector.exists_v_eq`

 Some coordinate has a pole at `w`. 

### `IsNeighbourVector.norm_mem`

 The norm is integral. 

### `MapsNeighbour`

 The unitary element `ρ` maps the neighbour `L₀ + Ô x` into the standard lattice `L`, where
`L₀` is the lattice of the `z ∈ L` with `x* z` integral. 

### `MapsNeighbour.mulVec_mem_of_dot_mem`

 `ρ` maps `L₀` into `L`. 

### `MapsNeighbour.mulVec_mem`

 `ρ` maps `x` into `L`. 

### `polarResidue`

 The residue class of `ϖ s` at `w`, for the chosen uniformiser `ϖ` (and `0` if `ϖ s` is not
integral). 

### `neighbourResidues`

 The residue classes of `ϖ s` for the finite adeles `s` that are supported at `w`, have a pole
of order at most one and have integral trace `s + s̄`. They tell apart the neighbours that belong
to the same line: for `w` inert, a neighbour vector `b` and `a ∈ L`, the norm of `b + a` is integral
exactly when `s = b* a` has integral trace. 

### `polarResidue_eq_residue`

 If `s` has a pole of order at most one, its polar residue is the residue of the local integer
`ϖ s`. 

### `polarResidue_eq_zero_iff`

 An element with a pole of order at most one is integral if and only if its polar residue, the
residue class of `ϖ s`, vanishes. 

### `v_add_mul_le`

 If `s` and `s'` have poles of order at most one, so does `s + c s'` for a local integer `c`. 

### `residue_eq_zero_iff_v_ne_one`

 The residue of a local integer vanishes if and only if it is not a unit. 

### `polarResidue_add_mul`

 On elements with a pole of order at most one, the polar residue is linear over the local
integers. 

### `polarResidue_eq_mul_iff`

 For `s`, `s'` with poles of order at most one, the polar residue of `s` is `c` times that of
`s'` if and only if `s - c s'` is integral. 

### `polarResidue_eq_iff`

 Two elements with poles of order at most one have the same polar residue if and only if their
difference is integral. 

### `card_neighbourResidues_le_one`

 At a split place `w` (one that differs from its conjugate) there is at most one class in
`neighbourResidues w`, namely `0`: an integral trace `s + s̄` of an adele supported at `w` makes
`s` integral. 

### `mem_Ô_of_add_mul_mem`

 If `y` is integral, `y - ȳ` has an integral inverse `d`, and `s + y t` and the traces of `s` and
`t` are integral, then `t` is integral. 

### `polarResidue_eq_of_add_mul_eq`

 Let `y` be integral with `y - ȳ` inverted by an integral `d`, and let `s`, `s'`, `t`, `t'`
be supported at `w`, with poles of order at most one and integral traces. If `s + y t` and
`s' + y t'` have the same polar residue at `w` (residue of `ϖ` times the component at `w`), then so
do `t` and `t'`. 

### `card_neighbourResidues_sq_le`

 Let `E` contain a primitive 5040th root of unity (`HasPrimitiveRoot5040`). Then the number of
classes in `neighbourResidues w` (the residues of `ϖ s` for `s` supported at `w` with a pole of
order at most one and integral trace) is at most the square root of the order `q_w` of the residue
field at `w`. 

 ### The line of a neighbour vector 

### `IsNeighbourVector.polarResidue_ne_zero`

 The reduction of `ϖ x` modulo `w`, whose coordinates are the polar residues of those of `x`,
is not zero, for a neighbour vector `x`. 

### `IsNeighbourVector.line`

 The line spanned by the reduction of `ϖ x` modulo `w`, for a neighbour vector `x`. 

### `IsNeighbourVector.smul`

 A multiple of a neighbour vector by a local unit is a neighbour vector. 

### `IsNeighbourVector.exists_smul_sub_mem`

 Two neighbour vectors with the same line differ, after scaling by a local unit, by a vector of
the standard lattice. 

### `IsNeighbourVector.star_dotProduct_sub_eq_zero_of_ne`

 For neighbour vectors `b` and `x` at `w`, the product `⟨b, x - b⟩` vanishes away from `w`. 

### `IsNeighbourVector.v_star_dotProduct_le`

 For a neighbour vector `b` at `w` and a vector `z` of the standard lattice, the product
`b* z = star b ⬝ᵥ z` has a pole of order at most one at `w`. 

### `IsNeighbourVector.residue_eq_of_smul_mem`

 If `a x` and `a' x` are congruent modulo the standard lattice, for a neighbour vector `x` and
local integers `a` and `a'`, then `a` and `a'` have the same residue. 

 ### A quasi-reflection maps the neighbour into the standard lattice 

### `IsNeighbourVector.exists_mul_add_eq_one`

 Let the coordinate `x k` of a neighbour vector have a pole at `w`, and let `t` be integral and,
away from `w`, inverse to an integral `t'`. Then `x k + t` has an integral inverse `c`, and `c x`
lies in the standard lattice. 

### `exists_quasiReflection`

 Let `u` be a vector that vanishes away from a set `S` of places and its conjugate, and let `c`
satisfy `c + c̄ = c̄ c ⟨u, u⟩`. Then the quasi-reflection `z ↦ z - c ⟨u, z⟩ u` is a unitary element
`ρ` supported on `S` and its conjugate, that is, its components at all other places are `1`. 

### `exists_add_star_eq`

 An integral, self-conjugate finite adele `N` supported at `w` is the trace of an integral `t`
that has an integral inverse away from `w`. The Weil data (instance `WeilData E`) supply the
primitive 5040th root of unity, hence `√-1`, and an element of trace `1`. 

### `IsNeighbourVector.exists_mapsNeighbour`

 For a neighbour vector `x` at the finite place `w` (supported at `w`, with `ϖ x ∈ L`, `x ∉ L`
and `⟨x, x⟩` integral), some unitary element `ρ` supported on `w` and its conjugate maps the
neighbour `L₀ + Ô x` into the standard lattice `L` (`MapsNeighbour`). Here `L₀` is the set of
`z ∈ L` with `⟨x, z⟩` integral. The standing data `[WeilData E]` include a primitive 5040th root of
unity in the CM field `E`, so `E/E⁺` is unramified at the finite places. 

 ### A finite family that serves all neighbours 

### `MapsNeighbour.of_smul`

 Let `x` be a neighbour vector at the finite place `w` and `c` a local unit. If `ρ` maps the
neighbour of `c x` into the standard lattice, then it does the same for the neighbour of `x`. 

### `IsNeighbourVector.polarResidue_dot_sub_mem`

 If two neighbour vectors `b` and `x` at the finite place `w` differ by a vector of the standard
lattice, then the polar residue of `s = ⟨b, x - b⟩`, the residue of `ϖ s` at `w`, lies in the set
`neighbourResidues w` of such residues for `s` supported at `w` with a pole of order at
most one and with integral trace. 

### `MapsNeighbour.of_polarResidue_eq`

 Let the neighbour vectors `x₁` and `x₂` at the finite place `w` be congruent to the neighbour
vector `b` modulo the standard lattice. If `⟨b, x₁ - b⟩` and `⟨b, x₂ - b⟩` have the same polar
residue (the residue of `ϖ` times the component at `w`) and `ρ` maps the neighbour of `x₁` into the
lattice, then it does the same for the neighbour of `x₂`. 

### `exists_family_mapsNeighbour`

 There is a family of unitary elements supported on the finite place `w` and its conjugate,
indexed by pairs of a line in `k_w^n` (`k_w` is the residue field at `w`) and a class in
`neighbourResidues w` (the residues of `ϖ s` for `s` supported at `w` with a pole of order at most
one and integral trace). For every neighbour vector `x` at `w`, some member of the family maps the
neighbour `L₀ + Ô x` into the standard lattice `L`. Here a neighbour vector is supported at `w`, has
`ϖ x ∈ L` and `x ∉ L` for a uniformiser `ϖ`, and has integral norm `x* x`, and `L₀` is the set of
`z ∈ L` with `⟨x, z⟩` integral. 

 ### One step towards the standard lattice 

### `exists_isNeighbourVector_mulVec`

 If the unitary element `γ` does not stabilise the standard lattice `L` (that is, lies outside
`stdLevel`), then at some finite place `w` where `γ` has a nontrivial component, `γ L` holds a
neighbour vector: a vector supported at `w`, outside `L`, in `L` after multiplication by a
uniformiser, and with integral norm. 

### `q_mul_norm_finMultiplier_mul_sq_le`

 One step lowers the index. For `ρ`, `γ` in the finite adelic unitary group over the CM field `E`
with Weil data, let `z` be in the standard lattice `L` and let `γ z` be a neighbour vector at the
finite place `w`: it is supported at `w`, `ϖ (γ z) ∈ L` and `γ z ∉ L` for a uniformiser `ϖ` at `w`,
and its norm is integral. If `ρ` maps its neighbour `L₀ + Ô (γ z)` into `L`, where `L₀` is the set
of `y ∈ L` with `(γ z)* y` integral, then `q_w |Δ(ρ γ)|² ≤ |Δ(γ)|²`, where `q_w` is the order of the
residue field at `w` and `|Δ(g)|²` (`Δ` is `finMultiplier`) is the index of `L ∩ g⁻¹ L` in `L`. 
