---
{
  "module": "OAI/Computability/VPVNP/CompressorRefreshTraversalHeaders.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRefreshTraversalHeaders.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRefreshTraversalHeaders.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Refresh operands at a completed DFS node

The persistent state names the input level header. Public operands zero, one and two
name the owner site, popped parent node, and current level header. The sole child is
read through the parent row pointer. The parent node uses the canonical inverse-slot
and width columns named by the current header.


### `level`

 Read the six level-plan operands from the old header. The first table pointer
starts the packed refresh scratch region. 

### `traversal`

 Refresh traversal expressions for the saved arena start and stride, the sole child's
address read through the parent pointer, the parent and owner operands, and the old
incoming-slot head. 

### `current`

 Load the field at the given offset in the successor level header whose base is public
operand two. 

### `input`

 Retain the old level's segment and term addresses, while sourcing the new incidence
columns from the successor's canonical header. 

### `Geometry`

 Typed values in the persisted level headers used by the actual refresh expression
bank. The two canonical incidence arrays may occupy separate physical regions. 

### `Geometry.keep`

 Transfer retained header facts through later planner and traversal writes. 

### `child_read`

 The two external loads at the popped parent read its first and unique child. 

### `describes`

 The fixed header expressions evaluate to all typed operands of the chosen map.
The old and current headers, saved site, and popped parent are the four live DFS words. 

### `HeadBank`

 Both pointer banks as emitted by the native incidence/table-head publisher. 

### `headBanks_of_substep`

 The scalar relabel and successor publisher retain the old pointers and produce
the new incidence/table heads in the same memory. 

### `arena_of_packet`

 Read the private frame origin and stride from the twelve published metadata words.
These are positions two and three of the packet starting at header offset fifteen. 

### `Geometry.ofPublished`

 The actual scalar publisher, old and current incidence head banks, table zero,
and the published metadata packet provide the traversal geometry. 

### `run_metadata`

 Run the native metadata visits over the emitted scalar and pointer banks.
Only the input-length cell of the initial header is needed to calculate the
private argument frame. The result supplies its actual readback at the old header. 
