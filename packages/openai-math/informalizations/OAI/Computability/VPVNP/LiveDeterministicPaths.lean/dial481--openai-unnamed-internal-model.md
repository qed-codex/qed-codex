---
{
  "module": "OAI/Computability/VPVNP/LiveDeterministicPaths.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveDeterministicPaths.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveDeterministicPaths.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Removing a completed deterministic segment from a native group path

A canonical verified run can be a proper initial part of the group, ending
with a returned word. Exact-use choice strings force every accepting group
path to have precisely those initial bursts, including their full reports.
The remainder retains the original cap applied to the concatenated reports.


### `PathsFrom`

 All accepting paths from a given optional call state. 

### `split_empty_segment`

 Every native accepting run beginning at the given state contains the
entire verified deterministic prefix in both its choice stream and its log. 

### `emptySegmentEquiv`

 The equivalence is concatenation on branch strings, so even different
branch choices in the suffix with the same output state remain distinct. 
