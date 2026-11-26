---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/TotalOrderArray.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/TotalOrderArray.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/TotalOrderArray.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Explicit fixed-length arrays and truncated convolution for the shared marker. 

### `CoeffArray`

 Exactly t retained coefficients. This is a finite executable function. 

### `arrayCoeff`

 Out-of-range reads are zero. 

### `mulArray`

 Each output coefficient is a finite convolution over i+j=k. 

### `sumArray`

 Summation of the canonical coefficients; not a quotient ring map. 

### `rowArray`

 Executable row construction, with local coefficients supplied as arrays. 

### `asPolynomial`

 Polynomial semantics of the finite array. 

### `asPolynomial_mulArray`

 Explicit convolution is exactly multiplication followed by canonical truncation. 

### `trunc_mul_trunc`

 Canonical truncation is stable under a later multiplication and truncation. 

### `sum_productArray_eq`

 The executable array loop computes the canonical retained-coefficient sum. 

### `sum_productArray_of_powerDivisible`

 General list form of the shared nilpotent total-order identity. 

### `sum_productArray_rows_exact`

 Direct executable form: multiply local rows, keep only total order <t,
and sum; this equals the product of all local exact values. 

### `convolution_terms_le_square`

 Each coefficient k uses k+1 products; the complete convolution uses at most t². 
