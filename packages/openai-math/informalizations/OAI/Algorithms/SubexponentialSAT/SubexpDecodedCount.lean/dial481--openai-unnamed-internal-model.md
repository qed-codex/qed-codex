---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SubexpDecodedCount.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpDecodedCount.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpDecodedCount.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Exact natural decoding of the first coefficient word

Equality in the residue ring is not equality of unreduced binary words.
The final routine reduces the first word once; its raw value then lies below
the modulus, so the proved count bound makes natural-number decoding exact.


### `raw_eq_of_canonical`

 A bounded residue equality uniquely identifies the raw natural value. 

### `first_residue_eq`

 Equality to a natural scalar in the actual quartic quotient identifies
the zeroth base-ring coefficient, using the proved coordinate injection. 

### `decodeConstantRun_correct`

 Exact decoding needs both canonical output and the strict count bound. 

### `firstWord_correct`

 When a caller already proves canonicality, no final reduction is needed. 

### `first_mod_eq`

 This version composes directly with the actual binary remainder program,
whose output may have extra leading zero bits. 
