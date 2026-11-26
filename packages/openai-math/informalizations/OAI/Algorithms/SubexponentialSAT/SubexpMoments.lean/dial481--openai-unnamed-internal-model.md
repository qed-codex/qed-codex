---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SubexpMoments.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpMoments.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpMoments.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Family moments for an arbitrary number of color groups

This module connects the dependent-fiber separation theorem to actual
multivariate coefficient extraction and to the nested U/Z/X representation.
The Pi sum is used only as a semantic identity; the separated expressions
contain one inner sum per group and no Cartesian-product enumeration.

The list interfaces accept a verified, duplicate-free exponent enumeration.
They make no assumption about how that enumeration was produced and make no
runtime claim.  Canonical clipping of a product is handled separately by the
counting and truncation modules.


### `familySum`

 The separated r-fold sum, with scalar weights mapped to the value ring. 

### `familySum_eq`

 The definition is the full weighted family moment whenever each group
depends only on its own coordinate and the scalar weight factors. 

### `mvFamilyMoment`

 Actual multivariate polynomial-valued family moment, computed by
independent inner sums at each outer datum. 

### `sum_coeff_mvFamilyMoment_eq`

 Summing actual coefficients of separated family moments restores the
input coordinates in the entire family product. 

### `nestedFamilyMoment`

 The nested U/Z/X family moment used by the symbolic backend. 

### `extractX`

 Extract X while retaining U and Z, as an additive map on representatives. 

### `sum_extract_nestedFamilyMoment_eq`

 Exact nested family-moment restoration.  The support premise concerns
the complete product, not the separate groups.  No clipping or evaluation of
a quotient is hidden in this statement. 

### `list_nested_moments_eval_one_eq_sum_evalXU`

 A duplicate-free explicit exponent list is interchangeable with its
finite-set semantics.  Coverage is a support statement, not an assumed
evaluation identity. 

### `list_nested_moments_eval_one_eq_sum_evalXU_of_degree_bound`

 A verified degree-bounded list supplies coverage without constructing
the full coordinate box used by the denotational `Moments.retained`. 

### `list_extract_nestedFamilyMoment_eq`

 A list-driven moment loop combined with the r-fold separated inner
sums.  All coefficient extraction is performed after constructing each
complete polynomial moment. 
