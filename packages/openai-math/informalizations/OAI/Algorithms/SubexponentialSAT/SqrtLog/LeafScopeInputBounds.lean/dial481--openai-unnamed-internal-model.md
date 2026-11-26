---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/LeafScopeInputBounds.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/LeafScopeInputBounds.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/LeafScopeInputBounds.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Input-size bounds for explicit scopes. These bounds use actual duplicate-free
original-coordinate scope rows, with no value-only replacement for their bytes. 

### `encoded_member_length`

 A field occupies no more bytes than its containing framed list. 

### `scope_row_wire`

 Unary original IDs are explicitly charged in each serialized scope row. 
