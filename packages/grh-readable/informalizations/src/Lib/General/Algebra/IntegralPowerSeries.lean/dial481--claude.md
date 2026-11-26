---
{
  "module": "src/Lib/General/Algebra/IntegralPowerSeries.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/General/Algebra/IntegralPowerSeries.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/General/Algebra/IntegralPowerSeries.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Integral power series over ℂ_p: jets, the chain rule and the exponential

A power series over `ℂ_[p]` is called integral if it comes, through `New.seriesToCp`, from a series
with coefficients in the ring of integers of `ℂ_[p]`.

## Main definitions and results

* `New.mem_range_seriesToCp`: a series in one variable is integral iff all its coefficients have
  norm at most one.
* `New.pderiv_subst`: the chain rule for partial derivatives of a substitution of power series.
* `New.jet_subst_linearSeries`: for a linear substitution `M`, the jet `P(∂) (F ∘ M) (0)` is the jet
  of `F` along the polynomial `New.linSubst M P` obtained from `P` by the transposed substitution.
* `New.expSubst`: the exponential `exp a` of a power series `a` in several variables without
  constant term; it turns finite sums into products (`New.expSubst_add`, `New.expSubst_sum`).
* `New.padicValNat_factorial_mem_Icc`: `n / (p - 1) - v_p(n!)` lies in `[0, K]` for `n < p ^ K`.
* `New.rpow_le_norm_factorial`: the lower bound `p ^ (-n / (p - 1)) ≤ ‖n!‖` for the `p`-adic norm.

Notions from other files:
* `New.jet`: the bilinear pairing `P(∂)F(0)` of a polynomial `P` with a power series `F`, the sum
  over exponents `d` of `d!` times the product of the `d`-th coefficients of `P` and `F`.
* `New.linearSeries`: the linear form `∑ c_i z_i`, as a power series in the variables `z_i`.
* `New.linSubst`: for a matrix `M` over `R`, the `R`-algebra map of polynomial rings that sends
  `X_b` to `∑_t M_(t b) X_t`.

## Relation to the literature

Known results: the chain rule and the functional equation of the exponential for formal power
series, and Legendre's formula for the valuation of a factorial.


 ## The inclusion of integral power series 

### `New.seriesToCp`

 The inclusion of power series over the integers `valRingCp p` into power series over `ℂ_[p]`, as
a ring homomorphism. 

 ## Integral series, units, partial derivatives and linear forms 

### `mem_range_seriesToCp`

 A power series `f` in one variable over `ℂ_[p]` comes from a series over the ring of integers
`valRingCp p` if and only if all its coefficients have norm at most one. 

 ## The chain rule and jets of linear substitutions 

### `New.continuous_pderiv_of_continuousMul`

 Partial derivatives of power series are continuous for the coefficientwise topology. 

### `New.pderiv_subst`

 The chain rule for power series: if the family `a` can be substituted into series in the
variables `ι`, then `∂_k F(a) = ∑_i (∂_i F)(a) * ∂_k a_i`. 

### `New.jet_subst_linearSeries`

 Jets of a linear substitution. Let `M` be a matrix and substitute the linear forms
`(M z)_i = ∑_k M_(i k) z_k` into the series `F`. The jet `P(∂) F(M z) (0)` equals the jet of `F`
along `linSubst M P`, the polynomial `P(Mᵀ x)`. 

 ## The exponential of a series and p-adic norms of factorials 

### `expSubst`

 The series `exp a`, obtained by substituting `a` into the exponential series over `ℂ_[p]`. It is
meaningful when `a` has no constant term. 

### `constantCoeff_subst_of_constantCoeff_eq_zero`

 Substituting a series `a` without constant term into `f` keeps the constant term of `f`. 

### `expSubst_add`

 The functional equation `exp (a + b) = exp a * exp b` for series `a`, `b` without constant
term. 

### `expSubst_sum`

 The exponential of a finite sum of series without constant term is the product of their
exponentials. 

### `norm_natCast_eq_inv_pow_padicValNat`

 The norm of a nonzero natural number `n` in `ℂ_[p]` is `p ^ (-v_p(n))`. 

### `padicValNat_factorial_mem_Icc`

 For `p` prime and `n < p ^ K` one has `n / (p - 1) - K ≤ v_p(n!) ≤ n / (p - 1)`, a consequence
of Legendre's formula. 

### `rpow_le_norm_factorial`

 For a prime `p` and a natural number `n`, the norm of `n !` in the `p`-adic complex numbers
`ℂ_[p]` is at least `p ^ (-(n / (p - 1)))`, where the exponent is a real number. 

### `subst_rescale_eq_subst_smul`

 Substituting `a` into the rescaled series `f(c X)` is substituting `c • a` into `f`. 

 ## Renaming the variables of a jet 

### `New.jet_rename`

 The jet pairing `P(∂)F(0)` of a polynomial `P` with a power series `F` is unchanged when both
are renamed along an injective map `e` of variables; `Q` is the renamed polynomial. 
