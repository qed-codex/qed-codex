---
{
  "module": "src/Lib/Weil/Fock/WeightedNorms.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Weil/Fock/WeightedNorms.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Weil/Fock/WeightedNorms.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Moments on Fock space, approximation by polynomial vectors, bounds for functionals

The Fock space `New.Fock.fockSpace` consists of functions on ℂ^ι reproduced by the Gaussian. This
file defines weighted L¹ norms ∫ (1 + ‖y‖)^N |v y| dy on it, with values in [0, ∞], and proves
growth estimates that justify integrals and limits at the real places. Vectors whose moments are all
finite are approximated in all these norms by polynomial vectors. A functional controlled by its
differences under short Heisenberg translations is then bounded by moments.

## Main definitions and results

* `New.Fock.fockMoment`: the weighted L¹ norm ∫ (1 + ‖y‖)^N |v y| dy, with values in [0, ∞];
  `New.Exchange.IsSchwartzVector`: all these norms are finite (a Schwartz vector).
* `New.Fock.fockMoment_realHeisenbergOp_le`, `New.Fock.fockMoment_realWeil_le`,
  `New.Fock.fockMoment_integral_le`: bounds under the Heisenberg translations
  `New.Fock.realHeisenbergOp`, the Weil representation `New.Fock.realWeil`, and integrals of
  vectors.
* `New.Fock.fockMoment_polyVector_ne_top`, `New.Fock.exists_tendsto_fockMoment`: the vectors
  polynomial times Gaussian (`New.Fock.polyVector`) have finite norms, and approximate in all norms
  at once every vector whose norms are finite.
* `New.Fock.exists_norm_realHeisenbergOp_polyVector_le`: for a functional ℓ controlled by its
  differences under translations of size at most t ≤ 1, the value at the translate by z of a
  polynomial vector is at most C ‖ℓ‖ tᴺ (1 + ‖z‖)ᴺ.
* `New.Fock.exists_enorm_le_mul_fockMoment_of_norm_sub_le`: the bound ‖ℓ v‖ ≤ C ‖ℓ‖ tᴺ times the
  N-th moment of v, for every vector v.

Notions from other files:
* `New.Fock.fockSpace`: the Fock space of integrable functions c on ℂ^ι with c(x) = ∫ c(y) β(y,x)
  e(x−y) dy, where e is the Gaussian exp(−|x|²/2), under the L¹ norm.
* `New.Fock.realHeisenberg`: For signs ε, the Heisenberg datum on ℂ^ι given by the continuous
  unit-modulus bicharacter β(x,y) = exp((y*εx − x*εy)/2) = exp(i Im y*εx).
* `New.Fock.realHeisenbergOp` y: the Heisenberg translation c ↦ (z ↦ β(y,z) c(z − y)) on the Fock
  space.
* `New.Fock.vacVector`: the Gaussian `New.Fock.realVac` as a vector of the Fock space.
* `New.Fock.holomorphicCoord` ε x: the holomorphic coordinates of x, x̄ᵢ where εᵢ = 1 and xᵢ
  otherwise.

## Relation to the literature

Known; see `Lib.Weil.Fock.OscillatorPair` for sources.



## Moments, Schwartz vectors and polynomial approximation

The common device: a vector v is the integral of the translates of the vacuum weighted by v.


 ### The weighted norms 

### `fockMoment`

 The moment `fockMoment N v` = ∫ (1 + ‖y‖)^N |v(y)| dy in [0, ∞], with ‖y‖ the sup norm and dy
Lebesgue measure divided by π^|ι|. 

### `fockMoment_zero`

 The moment of order 0 is the L¹ norm of the Fock vector `v`. 

### `fockMoment_realHeisenbergOp_le`

 The Heisenberg translation by `y` multiplies the moment of order `N` by at most
`(1 + ‖y‖) ^ N`. 

### `_root_.New.Exchange.IsSchwartzVector`

 The Fock vector v is a Schwartz vector: all its moments `fockMoment N v` are finite. 

 ### Functionals, polynomial vectors and integrals 

### `enorm_le_mul_fockMoment`

 A bounded functional `ℓ` that is at most `S (1 + ‖z‖)ᴺ` on the translate of the vacuum by `z`,
for all `z`, is at most `S` times the `N`-th moment on every vector `v`. The bound is stated in [0,
∞], so no finiteness is assumed. 

### `fockMoment_polyVector_ne_top`

 For every complex polynomial `P`, the polynomial vector `polyVector ε P` has finite moment of
every order `N`. Here `polyVector ε P` is x ↦ P(ζ(x)) exp(−|x|²/2), with ζ(x)ᵢ equal to x̄ᵢ where
`ε i = 1` and xᵢ otherwise. `fockMoment N c` = ∫ (1 + ‖y‖)^N |c(y)| dy, with ‖y‖ the sup norm and dy
Lebesgue measure divided by π^|ι|. 

### `fockMoment_integral_le`

 Minkowski's inequality for moments: for a family `F t` of Fock vectors over an s-finite measure
`ν`, the moment of the Bochner integral `∫ F t dν(t)` is at most the lower integral of the moments
`fockMoment N (F t)`. 

### `isSchwartzVector_integral`

 Let `F` be almost everywhere strongly measurable, with finite lower integral of every moment of
`F t`. Then `F` is Bochner integrable and its integral has all moments finite. 

### `lintegral_fockMoment_smul_le`

 Let `F y` be Fock vectors (for signs `η` on `κ`) whose moment of order `N'` is at most
`C (1 + ‖y‖) ^ N`. Then `∫ fockMoment N' (v y • F y) dy` is at most `C` times the moment of order
`N` of `v`. 

 ### Approximation by polynomial vectors 

### `pow_mul_realVac_le`

 For reals s, t ≥ 0 and u in ℂ^ι with s ≤ (‖u‖ + 1)t, where ‖u‖ is the sup norm, the
Gaussian absorbs the factor: s^N · ‖realVac u‖ ≤ exp(N²) · t^N, where
‖realVac u‖ = exp(−Σ |u_i|² / 2). 

### `pow_mul_realVac_mul_realVac_mul_exp_le`

 Gaussian domination of the Fock kernel: for `y, w` in ℂ^ι with sup norms,
`(1 + ‖w‖)^N · |e(w)| · |e(y)| · exp |Σᵢ conj(ζ(y)ᵢ) ζ(w)ᵢ| ≤ exp(N²) · (1 + ‖y‖)^N`. Here
`e = realVac` is the Gaussian x ↦ exp(−|x|²/2), and `ζ = holomorphicCoord ε` has i-th coordinate x̄ᵢ
if `ε i = 1` and xᵢ otherwise. So the kernel trades a polynomial weight in `w` for one in `y`. 

### `prodX`

 The monomial `∏ j, X (p j)` of a word `p : Fin k → ι`. 

### `partialKernelOp`

 The `n`-th partial sum of the exponential series of the reproducing kernel, as an operator:
`∑_{k < n} (1 / k!) ∑_{p : Fin k → ι} ⟨w_p, ·⟩ w_p`, where `w_p` is the polynomial vector of
`prodX p`, and `⟨a, ·⟩` is the continuous linear functional `fockInner a`, linear in the second
slot. 

### `smul_one_sub_partialKernelOp_apply`

 The kernel of `1 - partialKernelOp ε n`: its value on the translate of the vacuum by `y`, at
`w`, is `e(w) e(y)` times the tail `exp s - ∑_{k < n} sᵏ / k!` of the exponential series at
`s = ζ(y)* ζ(w)`, with `e` the Gaussian and `ζ = holomorphicCoord ε`. Here it is multiplied by
`v y`. 

### `norm_smul_mul_sum_le`

 Domination of the partial sums: with `ζ = holomorphicCoord ε`, `e = realVac` the Gaussian and
`s = ζ(y)* ζ(w)`, the weighted `n`-th partial sum `(1 + ‖w‖)^N v(y) e(w) e(y) ∑_{k < n} sᵏ / k!` has
norm at most `exp((m + N)²) (1 + ‖y‖)^(m + N) |v(y)| (1 + ‖w‖)^(-m)`, for every `n` and `m`. 

### `exists_tendsto_fockMoment`

 For a Fock vector `v` all of whose moments are finite, there is a single sequence of polynomials
`P n` such that `fockMoment N (v - polyVector ε (P n))` tends to 0 for every `N`. Here
`fockMoment N c` = ∫ (1 + ‖y‖)^N |c(y)| dy in [0, ∞], with ‖y‖ the sup norm on ℂ^ι and dy Lebesgue
measure divided by π^|ι|. `polyVector ε P` is the Fock vector x ↦ P(ζ(x)) exp(−|x|²/2), where ζ(x)ᵢ
is x̄ᵢ if `ε i = 1` and xᵢ if `ε i = -1`. 

 ### The Weil representation 

### `one_add_enorm_mulVec_le`

 For the sup norms on vectors and the induced operator norm on matrices,
`1 + ‖A y‖ ≤ (1 + ‖A‖) (1 + ‖y‖)`. 

### `realWeil_eq_integral`

 The Weil operator of `u` as an integral: `realWeil u v` is `realMultiplier u` times
`∫ v(y) realHeisenbergOp (u y) vacVector dy`. This is the definition of the Weil representation. 

### `fockMoment_realWeil_le`

 The Weil representation of `u` multiplies the `N`-th moment `fockMoment N v` = ∫ (1 + ‖y‖)ᴺ
|v(y)| dy in [0, ∞] (sup norm ‖y‖, Lebesgue measure divided by π^|ι|) by at most
`‖realMultiplier u‖` (the scalar factor of the Weil operator) times `(1 + ‖u‖)ᴺ` times the moment of
the vacuum. Here `u : USign ε` acts through its matrix `(u : Matrix ι ι ℂ)`, and `‖u‖` is the
operator norm, for the sup norms, of the matrix of `u`. 


## Bounds for functionals controlled by short differences

The hypothesis: ℓ is a bounded functional whose values are controlled by its differences under
Heisenberg translations `New.Fock.realHeisenbergOp` of size at most t.


### `New.Fock.hasDerivAt_realHeisenbergOp_realHeisenbergOp`

 The derivative of a translate of a polynomial vector along a line. Let `ρ` be the Heisenberg
translation `realHeisenbergOp` and `v_P = polyVector ε P` the product of a polynomial and the
Gaussian. For `y`, `z` in `ℂ^ι`, the curve `s ↦ ρ(s y) ρ(z) v_P` has the derivative
`ρ(s y) ρ(z) v_Q` with `Q = κ P + heisenbergDeriv ε y P`. Here `heisenbergDeriv ε y` is the
derivative of `ρ(s y)` at `0` on polynomials, and `κ = z* ε y - y* ε z`, with `ε` the diagonal
matrix of signs, comes from commuting `ρ(s y)` with `ρ(z)`. 

### `New.Fock.exists_norm_realHeisenbergOp_polyVector_le`

 Each derivative gains a factor `t` and costs a factor `1 + ‖z‖`. For each `N` and polynomial `P`
there is `C` as follows. Let `0 ≤ t ≤ 1`, and let `ℓ` be a bounded functional on the Fock space such
that, for every `f`, a bound for all `‖ℓ f - ℓ (ρ(y) f)‖` with `‖y‖ ≤ t` bounds `‖ℓ f‖`; here `ρ` is
the Heisenberg translation `realHeisenbergOp`. Then `‖ℓ (ρ(z) v_P)‖ ≤ C ‖ℓ‖ t ^ N (1 + ‖z‖) ^ N` for
all `z`, where `v_P = polyVector ε P` is the product of `P` and the Gaussian. 

### `New.Fock.exists_enorm_le_mul_fockMoment_of_norm_sub_le`

 For each `N` there is a constant `C ≥ 0` as follows. Let `t ≥ 0` and let `ℓ` be a bounded
functional on the Fock space. Suppose that, if `t < 1`, every real `B` that bounds
`‖ℓ f - ℓ (realHeisenbergOp y f)‖` for all `y` with `‖y‖ ≤ t` also bounds `‖ℓ f‖`, for every vector
`f`. Then `‖ℓ v‖` is at most `C ‖ℓ‖ tᴺ` times the `N`-th moment of `v`, for every vector `v`. 
