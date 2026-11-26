---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SubexpGlobalPolynomial.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpGlobalPolynomial.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpGlobalPolynomial.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Arbitrarily many factor groups and their local expansion

This file supplies the finite-color algebra in Section 4 of the subexponential
manuscript. A color partition is constructed by filtering the actual factor
indices. Products of separately truncated groups are compared with the full
product through canonical representatives, before substitution of X and U.
No hypothesis fixes the number of colors or assumes a final product identity.


### `colorSet`

 The actual factors assigned to one color. 

### `prod_colorSets`

 Every factor occurs in exactly its own color group, including when some
color groups are empty. 

### `canonical_mul_left`

 Canonical reduction can also be inserted on just one factor. 

### `canonical_prod`

 Any finite number of groups can be reduced separately before their
product is reduced. The assertion includes the empty product. 

### `truncated_groups_substitution`

 The arbitrary-group version of the canonical substitution theorem. 

### `truncated_groups_substitution_of_divisible`

 The high-U condition can be derived from divisibility of the actual
substituted group polynomials and nilpotence, for any finite group count. 

### `colored_rowGroup_product`

 Product of all concrete color groups is the full symbolic factor product. 

### `canonical_colored_rowGroup_product`

 The canonical representative of the arbitrary color product has no
extra dependence on the chosen grouping. 

### `colored_rowGroup_highU`

 Local residue defects imply high-U vanishing of the whole color product;
the conclusion is not an assumed global nilpotence property. 

### `colored_rowGroups_truncation`

 Lemma 4.1 for actual polynomial rows and arbitrarily many colors.
Admissibility and discarded high-U coefficients are derived from the row
construction and local residue defects. 

### `evalXU_colored_rowGroups`

 After evaluation, the product of the color groups is the actual shifted
factor product, independently of the residue-section values beta. 

### `sum_evalXU_colored_rowGroups`

 Sum over inputs gives the local expansion of the actual global H. 

### `sum_trunc_evalXU_colored_rowGroups`

 Truncating the evaluated sum yields the requested length-D jet. 

### `sum_canonical_colored_rowGroups`

 Full arbitrary-color truncation-to-global-jet identity. The groups are
reduced before their product and before evaluating X and U; all hypotheses
are local row bounds, local p-divisibility, and p^μ = 0. 
