---
{
  "module": "OAI/Algorithms/SubexponentialSAT/Subexp/MatrixEntryScalar.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/Subexp/MatrixEntryScalar.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/Subexp/MatrixEntryScalar.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# A scalar generating polynomial for the actual matrix entries

The coefficient of degree j equals 2^j times the j-th elementary projector
kernel. Consequently normalized coefficients need only scalar polynomial
arithmetic, with no enumeration of subsets in the eventual implementation.


### `coeff_kernelPolynomial`

 The factor 2^j is precisely canceled by using normalized coefficients. 

### `matrixEntry_eq_weighted_coeff`

 This is equality with the existing operator's entry, not an assumed
specification for a replacement matrix. 

 The scalar kernel has only three nonzero local factors: 1, -X, and 1+X. 

### `AllCompatible`

 The physical counter may test all Q coordinates without masking t. 

### `allUnchanged_card_joint`

 Remove one token from the physical all-coordinate unchanged counter. 


# Exact binomial formula for the implemented multicolor matrix

This connects scalar additions and sign changes to the very same matrix
used in the support and rank proofs. The only normalization hypothesis is
that the field has characteristic different from two.


### `matrixEntry_normalized`

 Exact scalar entry, including incompatible rows and columns and the
case where the mandatory number of differences exceeds the cutoff R. 

### `jointMatrixDP_normalized`

 The dynamic-programming matrix used by the implementation has these
same scalar entries; no equality to an independently chosen basis is used. 

### `jointMatrixDP_all_normalized`

 The physical all-coordinate counter needs only one decrement: jointness
makes the anchor an unchanged, nonfixed pair whenever compatibility holds. 
