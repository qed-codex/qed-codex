---
{
  "module": "OAI/Computability/VPVNP/RankCoordinateSelectedAdvice.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RankCoordinateSelectedAdvice.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RankCoordinateSelectedAdvice.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Static advice of the two selected slice determinants

Both greedy scans and the ordinary entry reads start from the supplied
base matrix reader. The target uses a zero monomial, mark, and scale in the
cloned template. The two advised scales are the certificate power and its
product with the field order. The dynamic preparation then fills in the
replacement row and the powered monomial for each requested matrix entry.


### `Den`

 Workspace ports for reading a denominator entry, with the base matrix reader serving both
pivot scans and the final entry query. 

### `Raw`

 Ports for the numerator's pivot scans, original matrix entries and powered target entries. 

### `Side`

 Private ports of the rank-prefix scan that recovers the source row ordinal. 

### `Parts`

 Port families for the determinant pair, the dynamic index calculation and unary label
conversion. 

### `Advice`

 Read-only preparation ports carrying the component templates and the two possible target
scales. 

### `Work`

 Writable preparation ports for the template copies and their temporary stack. 

### `powers`

 The certificate power for a label step, or its product with the field order for a Frobenius
step. 

### `den`

 Denominator template with both pivot scans initialized and the selected row and column
words empty. 

### `raw`

 Initial numerator reader banks for the base matrix, its pivot scans and the powered target
template. 

### `num`

 Numerator workspace before staging, with replacement ordinal zero and empty
selected-address words. 

### `side`

 Idle bank for scanning row ranks of the base matrix with the slice's column count. 

### `selectorCap`

 Stack-height bound for the greedy row scan together with its ordinal input and output
registers. 

### `portBound`

 Maximum advised stack height accounting for selected-minor reads, ordinal selection and
determinant initialization. 

### `selectedAdvice`

 Static advice for one slice, including the two determinant templates, equation rank, row
counts and target scales. 

### `selectedExtra`

 The static slice advice paired with an initially empty private preparation workspace. 

### `extra_length`

 Every advised stack and every initially empty private stack fits the
same concrete cap for all current/next ordinals and for both operations. 

### `fit`

 The clone and the public entry words fit their actual initialization and
ambient capacities before the physical preparation machine starts. 
