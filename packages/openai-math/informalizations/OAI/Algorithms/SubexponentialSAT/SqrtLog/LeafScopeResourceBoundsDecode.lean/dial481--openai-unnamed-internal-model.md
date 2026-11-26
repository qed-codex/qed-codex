---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/LeafScopeResourceBoundsDecode.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/LeafScopeResourceBoundsDecode.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/LeafScopeResourceBoundsDecode.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 A single raw-slot decoder for the actual logical records returned by the
selector's parser. It retains zero-coefficient and repeated entries. 

### `rawDecode_generated_payload`

 Exact physical payload recovery for every generated candidate. 

### `initialPayloads_encoding`

 This is an equality of existing bit streams, not an uncharged reversal.
`candidateEncoding` already frames the reverse of every logical record. 
