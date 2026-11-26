---
{
  "module": "src/Lib/PadicHodge/Kisin/PeriodMatrixFrame.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/PadicHodge/Kisin/PeriodMatrixFrame.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/PadicHodge/Kisin/PeriodMatrixFrame.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The frame theorem for a period matrix, with Frobenius and Galois action on the frame

The frame theorem `New.Lift.Chart.IsPeriodMatrix.exists_frame` for a period matrix `U`
(`New.Lift.Chart.IsPeriodMatrix`) over a chart with ring `S ⊂ A_inf`: the basis `Q`, `Z` of
`New.Lift.Chart.IsPeriodMatrix.exists_basis` is completed by partial inverses of `Q` and `Z`, a
Frobenius matrix `B` over `S`, and the Galois action on `Z`. The key point is `p ∤ det Q`; it rests
on

* `New.Lift.Chart.exists_det_ne_zero`: a nonzero determinant from a separating set of rows;
* `New.exists_mulVec_eq_zero_and_forall_comp_eq`: Artin's minimal support argument over a valuation
  ring, applied to the reduction of `Q` modulo `p` over the tilt `O^♭`.

Here `π` is `WittVector.constantCoeff`, the reduction `A_inf → O^♭` modulo `p`, `ainfToBPlus` is the
map `A_inf → B⁺`, and `(n, g)` in `New.Period.FrobGal` acts as `φ ^ n g`.

Notions from other files:
* `New.Lift.Chart.E`: The image in S of the series X^e A + p; it equals ξ times a unit of A_inf.
* `New.Lift.Chart.bicommutant`: The S-subalgebra S_B of those y in B⁺ whose multiplication commutes
  with every S-linear endomorphism of B⁺ that maps `New.Period.amaxImage` into itself.
* `New.Period.tau`: The element τ = [ε^{1/p}] − 1 of A_inf, where the brackets denote the
  Teichmüller lift.
* `New.Lift.Chart.S`: For a chart, the Λ-subalgebra S of A_inf that is the image of the chart's map
  Λ[[X]] → A_inf.
* `New.Lift.Chart`: A chart: a Λ-algebra map Λ[[X]] → A_inf, Λ = W(F_{p^f}), sending X to a non-unit
  Teichmüller lift z = [u] and a series X^e A + p, A a unit, to ξ times a unit.

## Relation to the literature

Known result: Kisin lattice (Breuil–Kisin module) of a crystalline lattice. Only existence is proved
here, of a frame over A_inf with a Frobenius matrix over S, which spans the crystalline periods up
to powers of E. Finite height is not stated, and there is no equivalence of categories. The proof
works directly by linear retractions onto the Breuil–Kisin ring, without slope theory or étale
φ-modules. Source: M. Kisin, Crystalline representations and F-crystals, Progr. Math. 253 (2006),
459–496; Bhatt–Morrow–Scholze, Integral p-adic Hodge theory, Publ. IHÉS 128 (2018), 4.26–4.34;
Cais–Liu, On F-crystalline representations, Doc. Math. 21 (2016).


### `exists_det_ne_zero`

 Let R: S → D be a homomorphism to a nontrivial semiring and X a set of vectors over S. If
R(t·x) = 0 for all x in X forces R(t) = 0, some square matrix N with rows in X has R(det N)
≠ 0. 

### `_root_.New.exists_mulVec_eq_zero_and_forall_comp_eq`

 A square matrix M of determinant 0 over a valuation ring R has a kernel vector a, with some
coordinate 1, such that g(a) = a for every ring endomorphism g of R with M·g(a) = 0 (Artin's
minimal support argument). 

### `exists_det_ne_zero_and_mulVec_eq_coord`

 For a chart `c` (a Λ-algebra map Λ[[X]] → `A_inf`, Λ = `WittFq f`, sending X to z = [ϖ^♭]), let
`S = c.S` be its subring of `A_inf`, with `c.adicBasis` a (p, z)-adic topological basis of `A_inf`
over `S` whose `S`-linear coordinates are `c.adicBasis.coord i`. Let `Q` be a matrix over `A_inf`
such that, for `t` over `S`, `p` divides every entry of `Q t` only if `p` divides every entry of `t`
(`π (t i) = 0`). Then there are `N` over `S` with `p ∤ det N`, and `σ`, `τ`, such that `(N t) k` is
the coordinate `σ k` of entry `τ k` of `Q t`. 

### `_root_.RingHom.map_det_eq_zero_of_map_mulVec_eq_zero`

 Let `ψ : S → T` be a map of commutative rings, `M` a square matrix over `S` and `s` a vector
over `S` such that `ψ` kills every entry of `M s` and `ψ (s ν) = 1` for some `ν`. Then
`ψ (det M) = 0`. 

### `map_mulVec_comp_eq_zero_of_eq_mul_smul`

 Let `m ∈ FrobGal` and `C = ρ m(Q)` for matrices over `A_inf`. Then `m` maps the kernel of the
reduction of `Q` modulo `p` into the kernel of the reduction of `C`: if `π(Q) a = 0` then
`π(C) m(a) = 0`. 

### `not_dvd_det_of_frobenius`

 Let `Q` over `Ainf` be `p`-saturated over `S` (`p` divides every entry of `Q t`, for `t` over
`S`, only if `p` divides every entry of `t`), with `Q B` a left multiple of the Frobenius twist of
`Q`, `p ∤ det B`, and `Q` a left multiple of `(1, g) • Q` for each `g` in `Gp p` fixing `S` (`g`
acts on `A_inf` as `(1, g)` in `FrobGal`). Then `p ∤ det Q`. 

### `mul_smul_mul_smul_eq_smul_map_of_mul_eq`

 Apply `m` to `U Z = E ^ h Q`, given `ρ m(U) = U F` and `w m(E) = E r`: then
`U w ^ h F m(Z) = E ^ h r ^ h ρ m(Q)`. Here `m` in `FrobGal` acts entrywise on matrices. 

### `map_dvd_of_forall_mul_eq_smul_map`

 Let `c` be a chart, let `E` be the image of its series X^e A + p (ξ times a unit),
`τ = [ε^{1/p}] - 1`, and `B⁺ = A_max[1/p]`. Let `U`, `U'` over `B⁺` satisfy `U U' = (E τ) ^ h`. If
every solution of `U Y = E ^ h X` with `X` over `A_inf` and `Y` over `B⁺` has `X = Q L` for some `L`
over `A_inf`, then `U = Q Y` for some `Y` over `B⁺`. 

### `constantCoeff_det_ne_zero`

 If `det Q ≠ 0` and `φ Q = v Q B` with `v` a unit and `B` over `S`, then `p ∤ det B`. 

### `exists_mul_map_eq_frobenius_smul`

 Frobenius step of the frame theorem. Let `U Z = E ^ h Q` with `Z` over `S_B`, let every `x`
over `A_inf` with `U y = E ^ h x` for some `y` over `S_B` be `Q s` with `s` over `S` (`hspan`), let
`φ(U) = v U F` with `F` over `S_B`, and let `u ∈ S_B` invert `φ(E)`. Then `Q B = v⁻¹ φ(Q)` for a
matrix `B` over `S`; here `(ofAdd 1, 1)` in `FrobGal` acts as the Frobenius `φ`. 

### `IsPeriodMatrix.exists_mul_smul_eq_of_fixesThetaZ`

 Galois step of the frame theorem. Let `U` be a period matrix of height `h` with `U Z = E ^ h Q`.
For `g` satisfying `c.FixesThetaZ` (this holds when `g` fixes `S` pointwise; the Frobenius factor
`v` is not used) there is `ρ` over `A_inf` with `U g(Z) = E ^ h ρ g(Q)`; here `(1, g)` in `FrobGal`
acts as `g`. 

### `constantCoeff_eq_zero_of_p_dvd_mulVec`

 Saturation step of the frame theorem. Let `det Q ≠ 0`, `U Z = E ^ h Q` with `Z` over `S_B`,
let `hspan` be as in `exists_basis`, and let `q ∈ S_B` invert `p`. If `p` divides every entry of
`Q s` for `s` over `S`, then `p` divides every entry of `s`: `π (s i) = 0`. 

### `IsPeriodMatrix.exists_eq_mul_smul_of_forall_smul_eq`

 Galois step for `p ∤ det Q`. Let `U Z = E ^ h Q` with `Z` over `S_B` for a period matrix `U`.
For an element `g` of `G_p` that fixes `S` pointwise there is `ρ` over `A_inf` with `Q = ρ g(Q)`;
here `(1, g)` in `FrobGal` acts as `g`. 

### `exists_mul_eq_of_mul_eq_smul`

 Span step of the frame theorem. Let `p ∤ det Q`, `det Q ≠ 0`, and let `hdvd` be as in
`exists_basis`. Then every solution of `U Y = E ^ h X` with `X` over `A_inf` has `X = Q L` for
some `L` over `A_inf`. 

### `IsPeriodMatrix.exists_frame`

 The frame theorem. Let `U` be a period matrix of height `h` with Frobenius factor `v`; among
other things, `U` over `B⁺` divides `(E τ) ^ h` with τ = [ε^{1/p}] − 1, and `φ U = v U F` with `F`
over `S_B` = `c.bicommutant`. There are `Q`, `L` over `A_inf`, `Z`, `Z'` over `B⁺` and `B` over `S`
such that: (a) `Q L = τ ^ h`; (b) `Z` has entries in `S_B`; (c) `U Z = E ^ h Q`; (d) `Z' Z = E ^ h`;
(e) `φ Q = v Q B`; (f) if `g` satisfies `c.FixesThetaZ` (fixes Λ and θ(z)), then `g(Z) = Z G` for
some `G` over `A_inf`. Scalars stand for scalar matrices.

This proves the case of Kisin's theorem on the φ-module of a crystalline lattice over the
Breuil–Kisin ring that is used: it is stated for matrices, starts from a given period matrix over
`B⁺`, and says nothing on finite height. 
