---
{
  "module": "src/Lib/GaloisRep/Main/CuspidalTypes.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/GaloisRep/Main/CuspidalTypes.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/GaloisRep/Main/CuspidalTypes.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Cuspidal types, multiplicity-free sums and the Hodge–Tate cocharacter

The file proves four results on unitary groups and Galois representations. Here `O_w` is the ring of
integers at a place `w` of `E` with uniformiser `ϖ`, and `χ` is the cyclotomic character.

## Main definitions and results

* `New.Variety.exists_isCuspidalType`: a character of `1 + ϖ M_N(O_w)`, trivial on
  `1 + ϖ² M_N(O_w)`, that is nontrivial on every unipotent radical. It is
  `k ↦ exp (2πi u (tr (b (k - 1))))` for an integral matrix `b` with irreducible characteristic
  polynomial modulo `w` and an additive character `u : E_w / ϖ² → ℚ/ℤ` with `u ϖ ≠ 0`.
* `New.Variety.exists_levelGU_invTransposeGL_le`: an open subgroup that contains the integral points
  trivial at a finite set `S` of places contains a principal level `𝔑` (up to inverse transpose).
  The primes of `𝔑` are those of a given `N` and of a set `B` meeting each pair `w, w̄` of `S`.
* `New.GaloisRep.exists_rep_span_diagonal`: Galois representations `ρ τ`, one for each embedding `τ`
  of `E` in `ℂ`, combine into one representation `r`. This `r` is multiplicity free (the span of its
  image contains the diagonal matrices) and has the prescribed integers among its Hodge–Tate jumps
  at every `τ`. It is built from the semisimplification of the sum of the `ρ τ`, keeping each
  irreducible constituent once.
* `New.Period.aeval_cocharacter_eq_zero`: let `x i ∈ ℂ_p` and integers `κ i` be given. A polynomial
  over `ℂ_p` that vanishes at `(χ(g) ^ (-κ i) g(x i))_i` for all `g ∈ G_p` near `1` also vanishes at
  `(T ^ (κ i) x i)_i`, with `T` the variable of the Laurent polynomials over `ℂ_p`.

Notions from other files:
* `New.localCongruence n w m`: the subgroup of `GL_n(E_w)` of integral matrices congruent to `1`
  modulo `ϖ ^ (m + 1)`; so `m = 0` gives `1 + ϖ M_n(O_w)` and `m = 1` gives `1 + ϖ² M_n(O_w)`.
* `New.stdLevel E n`: the integral points of the finite adelic unitary group, the stabiliser of
  `Ô ^ n`.
* `New.Variety.IsCuspidalType`: for every idempotent matrix ε ≠ 0, 1, the character is nontrivial on
  the elements of its group that lie in 1 + εM_n(1 − ε).
* `New.Variety.levelGU`: the principal level K(𝔑), the similitudes in `GL_n(Ô E)` that are congruent
  to `1` modulo `𝔑`.
* `New.Gf`: The finite adelic unitary group G_f: matrices g in GL_n(𝔸_f) with gᴴg = 1;
  `New.Gf.trivialOn n S` is the subgroup of elements with component 1 at every place of `S`.
* `New.Period.hodgeTateMaps`: The γ-semilinear maps f : T → ℂ_ℓ with f(gx) = χ(g)^(−u)·g f(x) for g
  near 1; their dimension is the multiplicity `New.Period.jump` of the jump u at γ.

## Relation to the literature

Known result: The Hodge-Tate cocharacter lies in the algebraic monodromy group. It is stated on
coordinates in C_p as the fact that a polynomial that vanishes at the cyclotomically twisted Galois
translates of a point, near the identity, vanishes along the one-parameter torus. No algebraic
groups or Tannakian categories are used. Source: Serre, Groupes algébriques associés aux modules de
Hodge-Tate, Astérisque 65 (1979), §1; Sen, Ann. of Math. 97 (1973).

See also `Lib.GaloisRep.WeightCongruence`, `Lib.Adelic.Unitary.CongruenceLevels` and
`Lib.GaloisRep.Main.OddRank`.


 ## Existence of a cuspidal type and of a principal level 

### `exists_irreducible_charpoly_residue`

 Some `N × N` matrix over `LocInt w` (the integers `O_w` of the completion `LocField w = E_w`)
has irreducible characteristic polynomial modulo `w`: lift the matrix of multiplication by a
generator of the extension of degree `N` of the residue field. 

### `exists_ne_zero_of_irreducible_charpoly`

 A matrix with irreducible characteristic polynomial is not block triangular: if `p` holds for
some indices but not for all, some entry in a row with `p` and a column without `p` is nonzero. 

### `exists_eq_one_add_mul_mul_and_map_trace_ne_zero`

 Let `b` be an integral `N × N` matrix whose characteristic polynomial modulo `w` is
irreducible, and let `u` be an additive map from `E_w / ϖ² O_w` to `QZ = ℚ/ℤ` with `u a ≠ 0` for
some `a` whose valuation `v a` is `exp (-1)`. Then for every idempotent matrix `ε ≠ 0, 1` over
`E_w`, some `k` in `1 + ϖ M_N(O_w)` has the form `1 + ε Y (1 - ε)` and satisfies
`u (tr (b (k - 1))) ≠ 0`. 

### `exists_isCuspidalType`

 For N ≥ 1 and a finite place w, some character of 1 + ϖM_N(O_w) is nontrivial on every
unipotent radical (`New.Variety.IsCuspidalType`) and trivial on 1 + ϖ²M_N(O_w). 

### `exists_levelGU_invTransposeGL_le`

 Let `H` be an open subgroup of the finite adelic unitary group `Gf E n` that contains every
element of `stdLevel E n` (the stabiliser of the standard lattice) that is trivial at each place of
`S`, and suppose each `w ∈ S` has `w` or its conjugate in `B`. Then for every `N : 𝓞 E` there is a
multiple `𝔑` of `N` that (a) lies in exactly the primes that contain `N` or belong to `B`, and (b)
satisfies `u ∈ H` whenever the inverse transpose of `u` lies in `levelGU n 𝔑`, the group of
similitudes in `GL_n(Ô E)` congruent to `1` modulo `𝔑`. 


## Multiplicity-free sums of irreducible constituents with all jumps

`New.GaloisRep.IsSphericalAbove r R J w P` says three things at every place over `w`. The
representation `r` is unramified (crystalline above `ℓ`). `R` relates the multiplicity of each
integer in `J τ` to its multiplicity as a jump at `τ`. `P` kills geometric Frobenius. With
`R = OccursIn` the middle condition reads: every element of `J τ` occurs as a jump.


### `New.exists_retract_of_trace_map_piMatrixUnit_eq_one`

 Let `f` and `f'` be algebra maps from a product of matrix algebras `∏ M_{d i}(k)` to matrix
algebras, with `k` algebraically closed of characteristic `0`. If `f` kills no block unit
`piMatrixUnit i` (the matrix unit `E₀₀` in factor `i`, zero in the other factors) and every
`f' (piMatrixUnit i)` has trace `1`, then `f'` is a retract of `f`: some `B` with a left inverse `C`
satisfies `f z * B = B * f' z` for all `z`. 

### `New.diagonal_mem_span_range_blockDiagonal`

 If the image of `s` spans the product of matrix algebras `∏ M_{d i}(k)`, then every diagonal
matrix lies in the span of the image of `s` under the block diagonal embedding, whose rows
`Σ i, Fin (d i)` are renumbered as `Fin (∑ i, d i)`. 

### `New.GaloisRep.exists_continuous_isTraceNondeg_trace_eq_sum`

 Let `ρ τ` be continuous representations of `Gal(Ω/E)` by matrices over `ℚ̄_ℓ = PadicAlgCl ℓ`
(`(ρ τ).rep`, rows indexed by `(ρ τ).Index`), one for each index `τ` of a finite type. Some
continuous representation `σ` with non-degenerate trace form has as trace the sum of the traces of
the `ρ τ`; it acts on the rows `Σ τ, (ρ τ).Index` of their block diagonal sum. 

### `New.GaloisRep.jump_eq_zero_of_jump_eq_zero_of_trace_eq_one`

 Let `s` be a homomorphism from `Gal(Ω/E)` to a product `∏ᵢ M_{d i}(ℚ̄_ℓ)` of matrix algebras,
and let `f` and `f'` be `ℚ̄_ℓ`-algebra maps out of this product with `σ = f ∘ s`, where `f'` lands
in square matrices of size `∑ i, d i`. Suppose each `f' (piMatrixUnit i)` has trace `1`, where
`piMatrixUnit i` is the matrix unit `E₀₀` in factor `i` and zero elsewhere. If `u` is not a
Hodge–Tate jump at `γ` of the representation `f' ∘ s` restricted to the decomposition group of `A`,
then it is not a jump at `γ` of `σ` restricted to that group. 

### `New.GaloisRep.exists_rep_span_diagonal`

 Suppose that for each embedding `τ` there is a continuous `ρ` which, at `F`-almost all places
`w`, is unramified or crystalline, has every member of `J τ` among its jumps at `τ`, and has
geometric Frobenius killed by `P w`. (`Set.indicator {τ} J` is `J τ` at `τ` and the empty multiset,
no condition, elsewhere.) Then there is one continuous `r` such that (a) every diagonal matrix is
in the span of its image, and (b) the same conditions hold at `F`-almost all `w`, with the jumps
`J τ` at all `τ` at once. 

 ## The Hodge–Tate cocharacter and the Zariski closure of the image 

### `New.Period.aeval_cocharacter_eq_zero`

 Let `p` be a prime, `x i ∈ ℂ_p` and `κ i` integers. The absolute Galois group `G_p = Gp p` of
`ℚ_p` (that is, Gal(Q̄_p/Q_p)) acts on `ℂ_p` by `g • ·`, and `χ = cyclotomicGp` is its p-adic
cyclotomic character. If a polynomial `F` over `ℂ_p` vanishes at `(χ(g) ^ (-κ i) g(x i))_i` for all
`g ∈ G_p` near `1`, then `F` vanishes at `(T ^ (κ i) x i)_i` in the Laurent polynomials over
`ℂ_p`. 
