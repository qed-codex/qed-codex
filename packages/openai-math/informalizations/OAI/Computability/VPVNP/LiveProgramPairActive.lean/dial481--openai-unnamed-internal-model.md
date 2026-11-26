---
{
  "module": "OAI/Computability/VPVNP/LiveProgramPairActive.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveProgramPairActive.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveProgramPairActive.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # The native first-half count following the physical mode router

The only stage-specific trace input in the count below concerns the
compressed pair table itself. The histogram sweep, descriptor initialization,
sparse copy and final exponent test use their verified native programs.


### `labelCount`

 Number of exponent-test counters, including both grammar-production and motif labels. 

### `expWidth`

 Bit width of each label’s exponent field in the live header. 

### `PairCall`

 Exact-use path semantics of the separately implemented compressed pair
stage, at its literal input ABI and the actual memory produced by the copy. 

### `PairCall.indexed`

 Path index for the compressed pair program running from the memory actually produced by
  the auxiliary copy. 

### `fst`

 The live first-half bit assignment extracted from the physical cuts by the live-cut
equivalence. 

### `post_header_count`

 The exact contribution on a valid first-half branch after the actual
header and router prefix. The cap is evaluated on every physically joined
report, retaining the prefix costs. 
