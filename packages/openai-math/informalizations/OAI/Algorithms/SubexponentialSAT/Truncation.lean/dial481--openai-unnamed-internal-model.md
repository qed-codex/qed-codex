---
{
  "module": "OAI/Algorithms/SubexponentialSAT/Truncation.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/Truncation.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/Truncation.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Canonical truncation before substitution

Polynomials are represented with U outermost, Z in the middle, and the X variables
innermost.  Truncation is an operation on canonical polynomial representatives;
we never assert that U = 1 defines a map out of the truncated quotient.


### `trunc`

 Delete all coefficients of degree at least n. 

### `xTrunc`

 Delete X monomials whose total degree exceeds N. 

### `canonical`

 Retain precisely U^j Z^r X^a with j < μ, r < D, and |a| ≤ N. 

### `substX`

 Evaluate only the X coordinates, leaving both U and Z formal. 

### `mapCoeffs`

 Apply an additive map to every polynomial coefficient. 

### `clipAddHom`

 Lift a coefficient reduction and a monomial cutoff together. 

### `clipAddHom_mul`

 A stable coefficient reduction stays stable after adjoining a variable
and deleting high powers of that variable. 

### `canonical_mul`

 Multiplying canonical representatives and reducing again gives the same
representative as reducing the full product. This is the quotient-product
bridge needed when the two factor groups were truncated separately. 

### `truncZ`

 Truncate Z, separately in each complete U coefficient. 

### `substX_canonical`

 The X cutoff is harmless in all retained U,Z coefficients, while the
discarded complete U coefficients vanish after substitution. 

### `canonical_substitution`

 Lemma 4.2's central truncation/substitution identity. Its hypotheses are
the independently established support-degree invariant and nilpotence of
high U coefficients after X substitution, not the desired equality itself. 

### `canonical_substitution_of_divisible`

 Divisibility by powers of a nilpotent coefficient implies the high-U
vanishing required by the preceding theorem. In the application q is C(p). 

### `truncated_groups_substitution`

 The exact order of operations in Lemma 4.2, including independently
truncated groups and their product in the truncated polynomial ring. 

### `evalXU`

 Ordinary evaluation on the full polynomial, first in X and then at U=1. 

### `evalXU_incidenceArgument`

 Substitution cancels the arbitrary residue lift beta and restores the
original row's constant value together with all positive-Z coefficients. 

### `incidenceProduct`

 A finite group of factors evaluated at the actual marked incidence
arguments of equation (4.3). 

### `restoredProduct`

 The original local expansion after the input coordinates have been
substituted. The residue-section values beta no longer occur. 

### `incidence_groups_truncation`

 Revised Lemma 4.2 for actual incidence arguments and arbitrary factor
tables. Both the support-degree and high-U hypotheses of the abstract
truncation theorem are derived from local linearity, positive Z order,
divisibility of the lifted defect, and nilpotence of p. 

### `linear_incidence_groups_truncation`

 For finite linear forms, even the local degree assumptions disappear:
they are proved from the actual coefficient arrays. 
