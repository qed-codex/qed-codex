---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/LeafStatisticsSemanticsTransport.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/LeafStatisticsSemanticsTransport.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/LeafStatisticsSemanticsTransport.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Scope transport for the actual native factor IDs. 

### `nativeScope`

 Read the scope from exactly the emitted `(original owner, native factor)`
records, retaining the original free-coordinate subtype. 

### `nativeScope_transport`

 The concrete rank-based bijection transports every native scope exactly to
the residual original factor or the singleton of its numbered uncovered owner. 
