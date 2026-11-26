---
{
  "module": "src/New/Congruences/Lifting/HodgeExpansion.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Congruences/Lifting/HodgeExpansion.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Congruences/Lifting/HodgeExpansion.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Exponents of lattice elements in a Hodge basis and the length of one step on a line

Let `L` be a crystalline lattice over a Kummer chart `k` with prime `p` and residue degree
`f = k.f`. A letter is a unit of the field with `p ^ f` elements; it singles out some of the
embeddings of the coefficients into `ℂ_p`, and `i.stepBack a` is the letter `j` with `j^(p^a) = i`.
Take an element `x` of `L.kisinLocAinf` lying in the letter `i`. Then `x ∈ L.withOrders i c` says
the following: for every level `a : ℕ` and every form `μ` of a type `u ∈ L.jumpSet j` at the letter
`j = i.stepBack a`, the value `valueAt a μ x = μ (φ^(-a) x)` lies in `t^(c a u) B_dR⁺`. The file
shows how exponents behave under coordinates and Frobenius. It then shows that among sufficiently
many elements with given exponents some primitive `ℤ_[p]`-combination gains a step: it splits into
parts with raised exponents. The line `u` of a system `c` of exponents is the family `a ↦ c a u`.

## Main definitions and results

* `New.Lift.KummerChart.JumpLattice.mem_withOrders_stdOrders_iff`: the standard exponents
  `New.Lift.KummerChart.stdOrders l` cut out, at the letter, the span
  `New.Lift.KummerChart.JumpLattice.frobKisinAinf l`, the image of `L.kisinAinf` under `φ^l`.
  On the line `u` these exponents are `0` below level `l` and `-u` from level `l` on.
* `New.Lift.KummerChart.JumpLattice.prod_frobEUnit_zpow_smul_mem_kisinLoc_and_withOrders_iff`:
  for a product `F` of integer powers of the `φ^a(E)`, the module `F` times the `S`-span of the
  image under `φ^l` of the Kisin module `L.kisinModule` is cut out in `L.kisinLoc`, at the letter,
  by the standard exponents raised by those of `F`.
* `New.Lift.KummerChart.JumpLattice.wittPairing_mem_withOrders`: exponents add under an
  equivariant bilinear map of lattices.
* `New.Lift.KummerChart.JumpLattice.raiseOrder`, `New.Lift.KummerChart.JumpLattice.raiseOrdersAt`:
  the system of exponents `o` with the single value `o a u`, or all values at the level `a`, raised
  by one.
* `New.Lift.KummerChart.JumpLattice.exists_sum_smul_mem_locKisinPart_sup`: let the chart be
  unramified and the jump `u` of multiplicity at most `n` at the letter `b` steps before `l`. Let
  `o b u < o b v` on the lines `v < u` in `L.jumpSet (l.stepBack b)`. Then any `k.f * n + 1`
  elements of `L.kisinLoc` with exponents `o` at the letter `l` have a `ℤ_[p]`-combination with one
  coefficient `1` that is the sum of two elements of `L.kisinLoc`: one with all exponents at level
  `0` raised by one, and one with the exponent at level `b` on the line `u` raised by one.

Notions from other files:
* `JumpLattice O`: a finite free `O`-module `L` with a crystalline action and, for each letter `i`,
  a finite set `L.jumpSet i` that holds its jumps. `L.Ambient` is `W(C^♭) ⊗ L`, and `L.Functional`
  is the type of `A_inf`-linear maps `L.Ambient → B_dR`.
* `L.forms`, `L.formsOfType i u`: the functionals that are `Γ'`-equivariant on `1 ⊗ L`, and those
  among them that send the letter-`i` projection of `1 ⊗ L` into `t^(-u) B_dR⁺`.
* `L.ainfLattice` is the `A_inf`-span of `1 ⊗ L`. `L.kisinAinf` consists of the `x` in
  `A_inf[1/τ] ⊗ L` with `μ (φ^n x) ∈ B_dR⁺` for all forms `μ` and all `n ≥ 1`, and
  `L.kisinLocAinf` is its saturation by the elements `k.frobE a = φ^a(E)`.
* `saturateBy M P`: the elements that some member of the submonoid `M` multiplies into `P`.

## Relation to the literature

See `New.Congruences.Lifting.SafeMoves` and `New.Congruences.Lifting.CupOrthogonalityBounds` for
related work. For sources see `Lib.PadicHodge.Kisin.PeriodMatrixFrame`.


 ## Standard exponents, Frobenius on exponents, and additivity of exponents 

### `wittPairing`

 The `W(C^♭)`-bilinear extension `(W(C^♭) ⊗ A) × (W(C^♭) ⊗ L) → W(C^♭) ⊗ C` of an `O`-bilinear
map `b : A × L → C` of lattices. The tensor products are over `ℤ_p`. 

### `IsEquivariantPairing`

 The `O`-bilinear map `b : A × L → C` of lattices is equivariant: `b (g y, g x) = g b (y, x)` for
all `g` in `Γ`. 

### `wittPairing_letterProj_left`

 The `W(C^♭)`-bilinear extension of an `O`-bilinear map `b` moves the projector `e_i` onto the
letter `i` from the first argument to the value: `b (e_i y, x) = e_i b (y, x)`. 

### `wittPairing_mem_saturateBy`

 If the pairing `wittPairing b` maps `s × t` into `Q`, it maps the saturations of `s` and `t` by
the submonoid `T` into the saturation of `Q` by `T`. 

### `shiftedOrders`

 The family of exponents `c` shifted by `l` levels: the value at `(a, u)` is `n` for `a < l` and
`c (a - l) u` for `a ≥ l`. 

### `ShiftsHodgeFil`

 A `B_dR`-linear map `D` from functionals to `B_dR` shifts the Hodge filtration by `κ`:
`D μ ∈ t^(m + κ) B_dR⁺` whenever `μ (1 ⊗ L) ⊆ t^m B_dR⁺`. 

### `RespectsGaloisAction`

 A `B_dR`-linear map `D` from functionals to `B_dR` respects the action of `Γ'`:
`D μ₂ = g • D μ₁` whenever `μ₂ (1 ⊗ g t) = g • μ₁ (1 ⊗ t)` for all `t` in `L`. 

### `apply_mem_hodgeFil_of_forall_formsOfType`

 Let `x` lie in `L.fracSpan` and let `μ` be any `A_inf`-linear functional `W(C^♭) ⊗ L → B_dR`. A
form of type `κ` at the letter `i` is a functional that is equivariant for `Γ' = k.subgroup` on
`1 ⊗ L` and sends the projection of `1 ⊗ L` to the letter `i` into `t^(-κ) B_dR⁺`. Then `μ x` lies
in `hodgeFil n = tⁿ B_dR⁺` provided `D μ * ν x` does for every integer `κ`, every form `ν` of type
`κ` at `i`, and every `B_dR`-linear map `D` from functionals to `B_dR` that shifts the Hodge
filtration by `κ` and respects the action of `Γ'`. 

### `valueAt_coordRetract_sub_mem_hodgeFil`

 Let `μ` be a form, that is, a functional equivariant on `1 ⊗ L` for the subgroup
`Γ' = k.subgroup`. Let `y` lie in `L.kisinLocAinf`: some product of the `φ^j(E)` multiplies it into
`L.kisinAinf`. Let `v` lie in `valueField a`, the subfield of `B_dR` generated over the fixed field
of `Γ'` by the products of constants in `k.bicommutant` and images of `φ^(-a) S`, for `S = k.S`. If
the value `valueAt a μ y = μ (φ^(-a) y)` is congruent to `v` modulo `hodgeFil n = tⁿ B_dR⁺`, then so
is the value at `coordRetract y`. 

### `valueAt_coordRetract_mem_hodgeFil`

 If `μ` is a form and the value `valueAt a μ y = μ (φ^(-a) y)` at an element `y` of
`L.kisinLocAinf` lies in `hodgeFil n = tⁿ B_dR⁺`, so does the value at `coordRetract y`. 

### `coordRetract_mem_withOrders`

 If `y` in `L.kisinLocAinf` has exponents `c` at the letter `i`, so does its image under the
coordinate retraction `coordRetract`, which sends `r • w` to `k.coord₀ r • w` for `r` in `A_inf` and
`w` in `L.kisinLoc`. 

### `apply_phi_pow_succ_smul_mem_hodgeFil_zero`

 Let `μ` be a form. Let `x` lie in `L.kisinLocAinf`, that is, a product of elements `φ^j(E)`
multiplies it into `L.kisinAinf`, the module of the `z` in `A_inf[1/τ] ⊗ L` with `ν (φ^j z) ∈ B_dR⁺`
for all forms `ν` and all `j ≥ 1`. Then `μ (φ ^ (m + 1) • x)` lies in `hodgeFil 0 = B_dR⁺`. 

### `phi_pow_smul_mem_withOrders`

 Frobenius shifts exponents. If `x` has exponents `c` at `i.stepBack l`, then `φ ^ l • x` has the
following exponents at `i`: `0` at levels `a < l`, and `c (a - l)` at levels `a ≥ l`. 

 ### The standard exponents 

### `smul_mem_ainfLattice_of_frobE_smul_mem`

 Let `x` have the standard exponents `stdOrders l` at the letter `i`. Let `l ≤ a` and let `r` lie
in `A_inf`. If `r φ^a(E) x` lies in `L.ainfLattice`, the `A_inf`-span of `1 ⊗ L`, so does `r x`.
Here `E = k.E` is the distinguished element of the chart and `k.frobE a = φ^a(E)`. 

### `mem_saturateBy_powers_of_mem_withOrders`

 Let `x` have the standard exponents `stdOrders l` at the letter `i`, a unit of the field with
`p ^ k.f` elements. Then some power of `φ^l(τ)` multiplies `x` into `L.ainfLattice`, the
`A_inf`-span of `1 ⊗ L`. Here `τ = [ε^(1/p)] - 1`. 

### `mem_withOrders_stdOrders_iff`

 An element `x` has the standard exponents `stdOrders l` at the letter `i` if and only if it lies
in `L.letterPart i`, where `ζ` acts by the Teichmüller lift of `i`, and in `L.frobKisinAinf l`, the
image under `φ ^ l` of `L.kisinAinf`. 

### `mem_stdOrdersPart_iff`

 An element `x` lies in `L.stdOrdersPart l i`, that is, in `L.kisinLoc` with the standard
exponents `stdOrders l` at the letter `i`, if and only if it lies in the letter `i` and in
`L.frobKisinAinf l`, the image of `L.kisinAinf` under `φ ^ l`, and all forms take values in the
field `valueField 0` on it. 

### `prod_frobEUnit_zpow_smul_mem_withOrders_stdOrders_add_iff`

 Multiply `x` by the product of the powers `k.frobEUnit b ^ r b` over `b ∈ s`. The result lies in
`L.withOrders i` with orders `stdOrders l a u`, raised by `r a` at each level `a ∈ s`, if and only
if `x` lies in `L.letterPart i` and in `L.frobKisinAinf l`, the image of `L.kisinAinf` under
`φ ^ l`. 

### `prod_frobEUnit_zpow_smul_mem_kisinLoc_and_withOrders_iff`

 Let `F = ∏_{b ∈ s} p_b ^ r b` be a product of integer powers of the units `p_b = φ^b E`
(`k.frobEUnit b`), and put `r a = 0` for `a ∉ s`. Then `F • x` lies in `L.kisinLoc`, the Kisin
module with all `p_a` inverted, and has at the letter `i` the exponents `r a` at the levels `a < l`
and `r a - u` at the levels `a ≥ l`, if and only if `x` lies in `L.letterPart i` (where `ζ` acts by
the Teichmüller lift of `i`) and in the `k.S`-span of the image of the Kisin module `L.kisinModule`
under `φ ^ l`. To have exponents `c` at `i` means to lie in `L.kisinLocAinf` and `L.letterPart i`
and to be sent by `μ ∘ φ^(-a)` into `t^(c a u) B_dR⁺` for every level `a`, every `u` in
`L.jumpSet (i.stepBack a)` and every form `μ` of type `u` at `i.stepBack a`. 

### `letterProj_mem_withOrders`

 The projection to the letter `i` of an element of `L.frobKisinAinf l` has the standard
exponents `stdOrders l` at `i`. 

### `letterProj_mem_stdOrdersPart`

 Let `x` lie in `L.frobKisinAinf l`, and let all forms take values in the subfield
`valueField 0` of `B_dR` on `x` (this is membership in `L.valueFieldPoints _`). Then the projection
of `x` to the letter `i` lies in `L.stdOrdersPart l i`: it lies in `L.kisinLoc` and has the
standard exponents `stdOrders l` at `i`. 

### `frobEUnit_pow_smul_mem_frobKisinAinf_one`

 If all members of the finite sets `L.jumpSet i`, which contain the Hodge–Tate jumps of `L` at
the letters `i`, are at most `n`, then `E ^ n` carries `L.kisinAinf` into `L.frobKisinAinf 1`. 

 ### Exponents add 

### `apply_smul_wittPairing_mem_hodgeFil`

 Let `b : A × L → C` be an equivariant bilinear map of lattices, `y` any element of `W(C^♭) ⊗ A`,
and `x` an element of `W(C^♭) ⊗ L` that a non-zero element of `A_inf` multiplies into the span of
`1 ⊗ L`. A form is an `A_inf`-linear functional to `B_dR` that is `Γ'`-equivariant on the lattice;
it has type `κ` at the letter `j` if it sends the projection of the lattice to `j` into
`t^(-κ) B_dR⁺`. Let `η` be a form on `C`, `n` an integer and `m` in `FrobGroup Γ = ℤ × Γ`. Then
`η (m • b(y, x))` lies in `hodgeFil n = tⁿ B_dR⁺` if the products `σ (m • y) * ν (m • x)` do, for
every integer `κ`, every form `ν` on `L` of type `κ` at `j`, and every form `σ` on `A` that has type
`u - κ` at `j` in case `η` has type `u` at `j`. 

### `wittPairing_mem_ainfLattice`

 The extension `wittPairing b` of a bilinear map `b` of lattices maps
`A.ainfLattice × L.ainfLattice` into `C.ainfLattice`. 

### `wittPairing_mem_kisinAinf`

 The extension of an equivariant bilinear map `b` of lattices maps `A.kisinAinf × L.kisinAinf`
into `C.kisinAinf`. 

### `wittPairing_mem_withOrders`

 Let `b : A × L → C` be an `O`-bilinear equivariant map of crystalline lattices and
`wittPairing b` its `W(C^♭)`-bilinear extension. An element `x` of `L.kisinLocAinf` in the
eigenspace of the letter `i` has exponents `c` if `μ (φ^(-a) x) ∈ t^(c a u) B_dR⁺` for all levels
`a` and all forms `μ` of a type `u ∈ L.jumpSet j` at `j = i.stepBack a`, the letter whose `p^a`-th
power is `i`. If `y`, `x` have exponents `c'`, `c` at `i`, then `wittPairing b y x` has exponents
`c''` at `i`, provided `c'' a v ≤ c a u' + c' a u` for all `a` and all `u ∈ A.jumpSet j`,
`u' ∈ L.jumpSet j`, `v ∈ C.jumpSet j` with `u + u' ≤ v`. 


## The length of one step on one line of exponents

`New.Lift.KummerChart.JumpLattice.withOrders l o` is the module of elements at the letter `l`
with exponent at least `o a v` at every level `a` on every line `v`.


### `raiseOrder`

 The system of exponents obtained from `o` by raising the single value `o a u` by 1. 

### `raiseOrdersAt`

 The system of exponents obtained from `o` by raising all values `o a v` at level `a` by 1. 

### `exists_thetaBdR_sub_sum_smul_eq_zero`

 Let `t` be an `N × r` matrix over `B_dR⁺`. There are `d ≤ r` rows `s i` such that, modulo the
kernel of `θ : B_dR⁺ → ℂ_p`, every row of `t` is an `A_inf`-combination of the rows `s i`. 

### `exists_sub_sum_smul_mem_withOrders_raiseOrder`

 Let `o` be a system of exponents. Let `i = l.stepBack b` and assume `o b u < o b v` for all
`v < u` in `L.jumpSet i`. Among points `x j` with exponents `o` at `l` there are `d` points
`x (s m)`, with `d` at most the multiplicity `L.jumpMultiplicity i u` of the jump `u` at `i`. Every
`x j` is an `A_inf`-combination of them modulo an element with exponents `raiseOrder o b u`. 

### `exists_eq_one_and_sum_smul_eq_zero`

 Let `WittFq k.f = W(𝔽_q)`, `q = p ^ k.f`, be the ring of constants of the chart `k`; it has rank
`k.f` over `ℤ_p`. For `d ≤ n`, any `k.f * n + 1` vectors in `W(𝔽_q)^d` satisfy a `ℤ_p`-linear
relation in which one coefficient is `1`. 

### `exists_sub_smul_one_eq_E_mul`

 If the Kummer chart `k` is unramified (`h_unram`), every `r` in `k.S` is congruent modulo `k.E`
to a constant: there are `w` in `WittFq k.f` and `y` in `k.S` with `r - w • 1 = k.E * y`. 

### `exists_sum_smul_mem_locKisinPart_sup`

 Let `L` be a lattice over an unramified Kummer chart `k` with constants `W(𝔽_q)`, `q = p ^ k.f`.
Let `i = l.stepBack b` have at most `n` Hodge–Tate jumps equal to `u`, counted with multiplicity,
and let `o b u < o b v` for all `v < u` in `L.jumpSet i`, the finite set that contains the jumps at
`i`. Among `k.f * n + 1` points of `L.kisinLoc` (the Kisin module with all `φ^a E` inverted) with
exponents `o` at `l`, some combination over `ℤ_p` with one coefficient equal to `1` is the sum of
two points of `L.kisinLoc`: one with all exponents `o 0 v` at level `0` raised by one
(`raiseOrdersAt o 0`), and one with `o b u` raised by one (`raiseOrder o b u`). 
