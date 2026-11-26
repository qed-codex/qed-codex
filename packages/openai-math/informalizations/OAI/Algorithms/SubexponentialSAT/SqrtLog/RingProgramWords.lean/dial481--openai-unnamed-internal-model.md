---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/RingProgramWords.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/RingProgramWords.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/RingProgramWords.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Fixed-width base-ring words for arbitrary extension degree. The arithmetic
programs below are the audited fixed scalar programs; the degree does not occur
in their instruction tables. Extension-vector scanning is a separate layer. 

### `prepareScalarCache`

 The cache is computed using literal-word preparation and modular negation.
Its correctness proofs do not enter the executable data. 

### `scalar_add_run`

 Exact byte refinement, including normalization, for the base addition. 

### `scalar_mul_run`

 Exact byte refinement, including normalization, for the base product. 

### `scalar_neg_run`

 Negation is the same fixed multiplier with a cached minus-one operand. 

### `flat`

 Flat coefficient-vector ABI: coefficient zero first, each word little endian. 
