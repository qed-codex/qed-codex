---
{
  "module": "OAI/Computability/VPVNP/VerifierMachineDecodeMatch.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/VerifierMachineDecodeMatch.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/VerifierMachineDecodeMatch.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Literal substring tests for the universal machine

The table interpreter tests an encoded field or row at a specified position
in its input. Every bit is checked by an input literal. An empty word can match
at the end of the input, and any test that extends past the input fails.


### `matchAt`

 Conjunction of the literals of `word`, starting at zero-based position `j`. 

### `MatchAt`

 The input contains `word` after a prefix of length `j`. 

### `matchAt_append_iff`

 Matching two adjacent words is equivalent to matching their concatenation. 

### `eval_matchAt`

 Acceptance is exactly occurrence of the specified word after a prefix of length `j`. 

### `size_matchAt`

 Each bit contributes at most an input node, a negation, and a conjunction. 
