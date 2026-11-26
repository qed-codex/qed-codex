---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/DisjointReuse/CountModel.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/DisjointReuse/CountModel.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/DisjointReuse/CountModel.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Data for the exact-counting statement, corresponding to source lines 45–77.
The primitive execution and space obligations are separate from these data definitions. 

### `RawCNF`

 Raw clauses retain order and repetitions on all declared variables. 

### `rawCount`

 Count every assignment on the declared ambient variable type. 

### `encodeRawCNF`

 Explicit list framing retains the raw syntax and the declared variable count. 

### `binaryNat`

 Canonical least-significant-bit-first binary, with a one-bit representation of zero. 

### `binaryNat_eq_append_true`

 Positive binary words have no redundant most-significant zero bit. 

### `eq_binaryNat_of_decode`

 A decoded word with the canonical terminal bit is the specified binary output. 
