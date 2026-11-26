---
{
  "module": "src/New/OneLift/HeckeValues/PeriodAtOne.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/OneLift/HeckeValues/PeriodAtOne.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/OneLift/HeckeValues/PeriodAtOne.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The period of a determinant theta kernel (used in rank two for the L-value at z = 1)

The period of a theta kernel for the pair `(I_n, I_n)` of standard definite spaces (`New.stdSpace`),
with polynomial `∏ τ, det ^ c τ` and finite datum a character of the determinant modulo `𝔪`.

* `New.Rows.detKernel`, `New.Rows.detPeriod`: the kernel on the finite adelic group and its class
  sum.
* `New.Rows.detPeriod_eq_stdClassSum_sum`: the period is the class sum of the sums, over
  `GL_n(O/𝔪)`, of the kernel values for the indicator of the unit matrix.
* `New.Rows.detPeriod_insert`: if `α` has weight `-c` and tame part `ψ` trivial outside `𝔪`, adding
  a prime `v` to `𝔪` multiplies the period by `∏ l < card n, (1 - q ^ l X)`. Here `q` is the norm of
  `v` and `X` is the inverse of the scalar `α.frobValue n v` (`New.AutChar.frobValue`).

`New.stdClassSum K f` is the sum of `f g / #Aut g` over the classes of level `K`; `New.stdLevel` is
the stabiliser of the standard lattice; `α.HasWeight e ψ` says that `α` has weight `e` and tame part
`ψ`; `𝔪.places` is the set of primes of the modulus `𝔪` and `𝔪.charOfTamePart ψ` the character
modulo `𝔪` made of `ψ`.

Notions from other files:
* `New.Modulus`: a nonzero ideal of O_E prime to its complex conjugate, that is, never divisible by
  both w and w̄.
* `New.WeilData`: the fixed choices on the CM field E that define the Weil representations (a purely
  imaginary element, a self-dual finite idele and a splitting character).
* `α.frobValue n v`: the number χ(ϖ) q ^ (N/2), where N is the cardinality of `n`, χ is the Hecke
  character `α.spaceChar N`, ϖ a uniformiser at `v` and q the norm of `v`.

## Relation to the literature

See `New.Congruences.Selmer.ClassSums`.


### `detKernel`

 The theta kernel (`New.modKernelStdSpace`) of the pair (I_n, I_n) of standard definite spaces,
at the point (1, h) with h finite adelic. Both characters of the pair are α, the datum is the
function Ψ on matrices modulo 𝔪 and the polynomial is the product over τ of the c_τ-th powers of
the determinant of the matrix of variables at τ (`New.Rows.variableMinor τ id id`). The character α
twists the Weil action, so the factor α(det h) is part of the kernel. 

### `detPeriod`

 The period: the class sum, at the level of the standard lattice, of `New.Rows.detKernel` for the
datum `x ↦ χ (det x)`. Here `ψ` is a family of characters `ψ w` of the residue fields and `χ` is the
character modulo `𝔪` with local components `ψ w`. 

### `prod_range_corank_one_sub_q_pow`

 For a square matrix `x` over the residue field at `v`, the product of `1 - q ^ l` over
`l < card n - x.rank`, with `q = v.q` the norm of `v`, is the value of the trivial character at
`det x`. So it is `1` if `x` is invertible and `0` otherwise. 

### `liftFn_charOfTamePart_det_eq_residueDatum`

 Let `ψ` be a family of multiplicative characters `ψ w` of the residue fields of `E`, and let `χ`
be the character modulo a modulus `𝔫` with local components `ψ w`. The lift to finite adelic
matrices of `x ↦ χ (det x)` sends a matrix integral at all primes `w` of `𝔫` to the product of the
`ψ w (det (S w))`, with `S w` its reduction at `w`, and every other matrix to `0`. 

### `residueDatum_singleton_mul`

 Let `ψ` be a family of multiplicative characters `ψ w` of the residue fields of `E`. The residue
datum (`New.residueDatum`) of a function at some places is that function of the reductions of an
adelic matrix integral at these places, and `0` elsewhere. If the primes of `𝔪'` are those of `𝔪`
and one new prime `v`, the datum of `S ↦ ∏ ψ w (det (S w))` over the primes `w` of `𝔪'` is the
product of the datum of `ψ v ∘ det` at `v` and of the same datum over the primes of `𝔪`. 

### `detKernel_stdEmbFin_mul`

 Let α have weight −c and tame part ψ. Then `detKernel n α c 𝔪 Ψ`, the theta kernel of the pair
(I_n, I_n) with datum Ψ modulo 𝔪 and polynomial ∏_τ det ^ c_τ, is, as a function on the finite
adelic points of U(I_n), invariant under left multiplication by rational points. 

### `detPeriod_eq_stdClassSum_sum`

 Let `α` have weight `-c` and tame part `ψ` trivial outside the primes of `𝔪`. Write
`detKernel n α c 𝔪 Ψ` for the theta kernel of the pair `(I_n, I_n)` with characters `α`, datum `Ψ`
modulo `𝔪` and polynomial `∏ τ, det ^ c τ`, a function on the finite adelic points of `U(I_n)`.
The period `detPeriod n α c 𝔪 ψ` is its class sum, at the level of the standard lattice, for the
datum `χ ∘ det`, with `χ` the character modulo `𝔪` made of `ψ`. It equals the class sum of the
function sending `g` to the sum, over `y` in `GL_n(O/𝔪)`, of the values at `g * liftMod y` of the
kernel for the indicator of the unit matrix; `liftMod y` is a lift of `y` to the stabiliser of the
standard lattice. 

### `stdLevel_le_rightStabilizer_detKernel`

 Let `α` have weight `-c` and tame part `ψ` trivial outside the primes of `𝔪`. Write
`detKernel n α c 𝔪 Ψ` for the theta kernel of the pair `(I_n, I_n)` of standard definite spaces
with characters `α`, datum `Ψ` modulo `𝔪` and polynomial `∏ τ, det ^ c τ`, a function on the finite
adelic points of `U(I_n)`. For the datum `x ↦ χ (det x)`, with `χ` the character modulo `𝔪` made
of `ψ`, it is invariant under right translation by the stabiliser `stdLevel E n` of the standard
lattice. 

### `sum_heckePolyCoeff_smul_modDatum_eq_modDatum`

 Let `α` have weight `-c` and tame part `ψ` trivial outside the primes of `𝔪`, and let the primes
of `𝔪'` be those of `𝔪` and one new split prime `v`. Translate the datum of `χ ∘ det` modulo `𝔪`,
with `χ` the character made of `ψ`, in the Weil representation `pairWeil` by the transposed Hecke
coset representative of a subspace `U` of `(O/v)^n`, placed at `v` in the unitary group by
`ofSplitPlace`. The sum over `U` of these translates, with coefficients
`heckePolyCoeff X U = (-X) ^ i * q ^ (i choose 2)` for `i = dim U`, `q` the norm of `v` and `X` the
inverse of `α.frobValue n v`, is the datum of `χ ∘ det` modulo `𝔪'`. 

### `detPeriod_insert`

 Let `α` have weight `-c` and tame part `ψ` trivial outside the primes of `𝔪`, and let the primes
of `𝔪'` be those of `𝔪` and one new prime `v`, of norm `q`. Let `X` be the inverse of
`α.frobValue n v`, which is the value at a uniformiser at `v` of the Hecke character `α.spaceChar N`
times `q ^ (N/2)`, where `N = card n`. Then the period for `𝔪'` is `∏ l < N, (1 - q ^ l X)`, which
is `qPochhammer q N X`, times the period for `𝔪`.

The factor is the sum, over the subspaces `U` of `(O/v)^n`, of the coefficients
`heckePolyCoeff X U`, evaluated by the q-binomial theorem. 
