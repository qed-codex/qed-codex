---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/NativeOuter.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/NativeOuter.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/NativeOuter.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 The fixed outer instruction sequence composes actual parameter setup,
disjoint counting DFS, and full-word positivity. The existing concrete-leaf
contract remains an explicit development obligation, not a final endpoint. 

### `outer_from_setup`

 Every phase uses the same physical state. The setup's proved final bound
supplies the DFS input cap; the final enlargement occurs once, after counting. 

### `counting_primitive_from_entry`

 Compile an actual bounded execution of the fixed outer sequence after the
canonical entry. Both physical outputs and all primitive prefixes use this run. 
