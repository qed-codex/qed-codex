---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/CodeCandidates.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/CodeCandidates.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/CodeCandidates.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 The retained domain of the code search is one word of two-bit scalars.
The tuple counter visits all four digits; the physical converter rejects the
unused digits and produces the original scalar-frame arithmetic format. 

### `digitBits`

 The two bits are little endian, as in the supplied scalar encoding. 

### `fieldWords`

 Physical counter words for a single field vector, never a family of vectors. 

### `fieldWords_injective`

 Each field vector has one unique counter state. 

### `ternary_digit_sound`

 Rejecting binary digit 3 leaves precisely the original ternary alphabet. 

### `binary_digit_sound`

 The binary graph search uses the same width-two scalar format. 

### `ternary_attempts_le_square`

 Invalid binary candidates and final overflow are charged: four to the
number of scalars is bounded by the square of the original ternary family. 

### `pairs_of_shape`

 Any width-two odometer state is exactly a list of scalar bit pairs. 

### `ternary_field_valid`

 Every actual ternary field vector passes the physical digit guard. 

### `binary_field_valid`

 The same assertion includes both scalar values of the graph alphabet. 

### `covers_field`

 The streamed visit log covers every actual field word. The list in the
hypothesis is proof-only telemetry from the bounded-memory odometer. 

### `matrixWords`

 Row-major matrix indexing is the supplied `finProdFinEquiv` convention. 

### `ternary_matrix_digits_sound`

 Every range-checked current matrix is an actual ternary matrix, with
the supplied row-major convention and including zero-sized dimensions. 

### `covers_matrix`

 There is no exceptional matrix case when a dimension is zero. 

### `saveFirst`

 Specification of one saved-candidate update. This is not an enumeration:
only the first accepted word is retained by the native selection command. 

### `saveFirst_fold_eq_find`

 The concrete loop's rank log specifies first success, not an arbitrary
successful witness. The log is not stored by the program. 

### `saveFirst_fold_success`

 Coverage of one successful rank forces the physical saved-word fold to
contain a successful candidate. The rank log is proof evidence only. 
