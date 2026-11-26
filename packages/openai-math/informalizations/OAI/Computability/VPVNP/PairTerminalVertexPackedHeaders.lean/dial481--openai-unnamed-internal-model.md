---
{
  "module": "OAI/Computability/VPVNP/PairTerminalVertexPackedHeaders.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairTerminalVertexPackedHeaders.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairTerminalVertexPackedHeaders.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Terminal bootstrap fields at the native vertex handoff

The prefix scan changes the total and role displacement. The traversal writes
the selected rows and tags, and the shared-bit scan writes the selected bit
bank. All three physical phases preserve the bootstrap values used by the
root gather and by the per-site geometry initializer.


### `Start.prefixField`

 Only the running total, the role offset and the two terminal controls
can differ from the bootstrap image inside the header. 

### `Start.bootstrapField`

 Read every unaffected bootstrap publication from the exact physical prefix
exit. The width and prefix pointers, terminal site count, row interval, and
both radices are instances of this one formula. 

### `VertexPacked.traversalField`

 The traversal controller's physical handoff preserves all high data
fields. The raw memory image comes from its verified native Segment. 

### `VertexPacked.gatherValues`

 Numeric operands of the root gather, decoded from the selected bootstrap
publications. Each natural address is strictly below the word modulus. 
