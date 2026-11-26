---
{
  "module": "OAI/Algorithms/SubexponentialSAT/Subexp/GlobalBasisRows.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/Subexp/GlobalBasisRows.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/Subexp/GlobalBasisRows.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Actual traversal of one dense global-matrix row

The fixed iterator parses every generated column descriptor and invokes the
concrete entry program.  Its output is the reversed row prefixed to an
arbitrary accumulator, so successive rows can be emitted without copying
previous output.  A final transfer restores the complete matrix order.


### `command_eval`

 The actual iterator consumes exactly the descriptor list. Its old source
suffix and reverse-output accumulator are preserved without being copied. 

### `budget_polynomial`

 A uniform quartic bound in serialized descriptor bytes and retained
unary row metadata. It does not charge the old matrix accumulator. 
