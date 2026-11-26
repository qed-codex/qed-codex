---
{
  "module": "src/Lib/General/Algebra/MultivariatePolynomials.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/General/Algebra/MultivariatePolynomials.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/General/Algebra/MultivariatePolynomials.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Multivariate polynomials: cost of vanishing, homogenization, Nullstellensatz, Hensel

This file collects lemmas on polynomials in several variables and on algebras of finite type. They
cover commuting partial derivatives, generation by products of polynomials in two sets of variables,
the cost of monomials of polynomials that vanish to high order, and homogenization along a linear
form.

## Main definitions and results

* `New.exists_le_weight_of_mem_vanishingIdeal_pow`: a nonzero polynomial that vanishes to order `d`
  at enough suitable points has a monomial of cost at least `d`.
* `New.exists_isHomogeneous_sub_one_dvd_sub` replaces a polynomial `P` of total degree at most `N`
  by a form `G`, homogeneous of degree `N`, congruent to `P` modulo `F - 1` for a given linear form
  `F`. So `G` and `P` have the same value at every point where `F` equals `1`
  (`New.exists_homogenization`); points are `R`-algebra maps `φ` out of the polynomial ring, with
  values in algebras in `Type`.
* `New.nullstellensatz_exists_le_ker`: the weak Nullstellensatz for an algebra of finite type, with
  points written as `k`-algebra homomorphisms `A → k`.
* `New.exists_mem_colon_of_tangent`: a criterion for an ideal to cut out a section of an affine
  scheme of finite type near a point. Tangent vectors at a `k`-valued point `o` along the fibre are
  the `V`-algebra maps to the dual numbers `k[ε]` that reduce to `o`.
* `New.Variety.IsAbsIntegrallyClosedLocal.multivariate_hensel` is a several-variable Hensel lemma
  for systems `x i = p i (x)` whose coefficients lie in the maximal ideal. Over a local domain in
  which every monic polynomial of positive degree has a root
  (`New.Variety.IsAbsIntegrallyClosedLocal`), it follows from the local structure of étale algebras:
  a standard étale algebra is given by a monic polynomial, whose residual root lifts.

## Relation to the literature

All results are known. `New.exists_le_weight_of_mem_vanishingIdeal_pow` is a form of the
Combinatorial Nullstellensatz with multiplicity, over any field. Each variable u has a positive
integer κ(u) and the weight 1/κ(u). In place of a grid it uses a set of at least ∏κ(u) points at
which each u^κ(u) agrees with a polynomial of lower weighted degree. A nonzero polynomial vanishing
to order d at all these points then has a monomial of weighted degree at least d. Source: Alon,
Combinatorial Nullstellensatz (1999); Ball–Serra, Punctured combinatorial Nullstellensätze (2009).


 ## Partial derivatives of multivariate polynomials commute 

### `New.pderiv_comm`

 The formal partial derivatives of a polynomial in several variables commute. 

 ## Polynomials in two covering sets of variables 

### `New.mem_rename_range_mul`

 If the ranges of `p` and `q` cover the set of variables `ι`, every complex polynomial is a sum
of products of a polynomial in the variables `p k` and one in the variables `q k`. 


## Vanishing to order d and the cost of monomials

Each variable `u` has the cost `1/κ_u`, and a monomial costs the sum of the costs of its variables.


### `New.coeff_translate_eq_zero_of_mem_vanishingIdeal_pow`

 If `p` vanishes to order `d` at the point `w`, then after translating `w` to the origin the
coefficients of `p` of degree below `d` are zero. 

### `New.bind₁_monomial_mem_vanishingIdeal_pow`

 If the polynomials `φ u` vanish at the point `w`, the product `∏ φ u ^ γ u` vanishes at `w` to
every order `d ≤ |γ|`. 

### `New.exists_forall_coeff_translate_eq`

 Chinese remainder theorem for jets: at finitely many distinct points `z t`, the coefficients
of degree below `d` after translation to the origin can be prescribed arbitrarily. 

### `New.mem_of_forall_monomial_mem`

 A submodule that contains the monomials occurring in `p` contains `p`. 

### `New.wellFounded_lt_of_monotone_finsupp`

 Comparing exponents by a monotone real function is well founded (Dickson's lemma). 

### `New.monomial_mul_bind₁_mem_of_weight_le`

 Division by the polynomials `ψ u = X u ^ κ u - g u`, where the variable `u` costs `1 / κ u` and
the monomials of `g u` cost less than `1`. If a submodule `N` contains the products
`X ^ α * ψ ^ γ` with `α < κ` and `|γ| + cost α ≤ r`, then it contains all the products with
`|γ| + cost α ≤ r`. 

### `New.exists_le_weight_of_mem_vanishingIdeal_pow`

 Combinatorial Nullstellensatz with multiplicity. Give the variable `u` the cost `1 / κ u`; the
cost of a monomial is its `weight`. Take at least `∏ κ u` distinct points `z t` at which each
`X u ^ κ u` agrees with a polynomial `g u` whose monomials cost less than `1`. Then every `f ≠ 0`
that vanishes to order `d` at these points has a monomial of cost at least `d`. 

 ## Homogenization with respect to a linear form 

### `New.exists_isHomogeneous_sub_one_dvd_sub`

 Homogenization by a linear form `F`: a polynomial `P` of total degree at most `N` is congruent
modulo `F - 1` to a homogeneous polynomial `G` of degree `N`. 

### `New.exists_homogenization`

 Homogenization by a linear form `F`: for a polynomial `P` over `R` of total degree at most `N`
there is a homogeneous `G` of degree `N` with `φ G = φ P` for every `R`-algebra map `φ` to an
algebra in `Type` (universe zero) with `φ F = 1`. 

 ## The weak Nullstellensatz for finite type algebras 

### `New.nullstellensatz_exists_le_ker`

 Nullstellensatz: in an algebra `A` of finite type over an algebraically closed field `k`,
every proper ideal lies in the kernel of some `k`-algebra homomorphism `A → k`. 

 ## Nakayama's lemma in tangent form 

### `New.exists_mem_colon_of_tangent`

 Nakayama's lemma in tangent form. Let `x : S → V` be a section of a finite type `V`-algebra,
`o : S → k` the field-valued point on it given by `V → k`, and `I ⊆ ker x` an ideal. If every
lift `w` of `o` to the dual numbers `k[ε]` that kills `I` has zero `ε`-part (no nonzero tangent
vector along the fibre kills `I`), then `I` generates `ker x` near `o`: some `b` with `o b ≠ 0`
has `b * ker x ⊆ I`. 

 ## Hensel's lemma in several variables 

### `New.Variety.IsAbsIntegrallyClosedLocal.multivariate_hensel`

 Hensel's lemma in several variables. Let `A` be an absolutely integrally closed local domain
(`IsAbsIntegrallyClosedLocal`: a local domain in which every monic polynomial of positive degree has
a root) and `p i` finitely many polynomials in the variables `X i` with all coefficients in the
maximal ideal. Then the system `x i = p i (x)` has a solution `x` in `A`. 
