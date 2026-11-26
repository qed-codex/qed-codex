---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/HashCandidates.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/HashCandidates.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/HashCandidates.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


The hash stream visits binary payloads in increasing unsigned order and reduces
each indexed ternary digit modulo3*m before the existing row assembler. Every
original candidate is attained and unchanged by normalization. Extra normalized
duplicates preserve the minimum. Visits are bounded by the square of the old family.


### `digitWidth`

 Positive chunk width, computed from the ternary coordinate alphabet. 

### `payloadWidth`

 Number of retained payload bits, rather than the number of candidates. 

### `payload`

 Proof-level accessor for the word present at a binary odometer rank. 

### `candidate_count_le_square`

 All binary trials, including duplicate decoded rows, fit a fixed square
of the original explicit ternary family count. 

### `visit_count_binary_width`

 Even the value of the exponential visit count needs only one more bit
than the retained candidate word. The iterator uses overflow, not this count. 

### `chunks`

 A proof-level partition of the one retained raw payload. Its length is
only the number of hash slots, never the number of candidates. 

### `normalize`

 Canonicalization modulo the indexed ternary alphabet is performed before
lifting coefficients into the existing characteristic-3-power ring. 

### `normalize_mem`

 The actual normalizer emits the original valid candidate encoding family,
so the old native row assembler can be reused with its original hypotheses. 
