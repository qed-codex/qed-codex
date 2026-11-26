---
{
  "module": "OAI/Computability/VPVNP/LiveProgramCompressedPairPaths.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveProgramCompressedPairPaths.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveProgramCompressedPairPaths.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Relocating the compressed pair's complete native paths into the live table

The pair instruction table runs on eleven public words. Relocation preserves
every supplied tape, report and memory write. A common prefix and the
branch-dependent terminal calls thus enter the outer linker on their original
chronological list. Only the dispatch and successor-tag events are appended
when charging the outer reports.


### `publicWords`

 Eleven words supplied to the pair stage, obtained by selecting its operands from the live
group’s geometry and literal prefix. 

### `native`

 Unrelocated burst RAM program of the group’s pair table instantiated at the group word
width and pair operands. 

### `fuel`

 Per-call instruction allowance assigned to the pair stage by the live group’s clock. 

### `Raw`

 Lists of call tapes that take the native pair from cursor zero and the specified memory to
an accepting halt within the per-call fuel. 

### `reports`

 Chronological reports returned by running the call tapes of an accepting native pair path. 

### `Reachable`

 The memory and state of any actual continuing prefix, including one
which may later reject. 

### `PreservesTag`

 Every continuing call in this physical component preserves the outer
tag, even when the supplied tape has no accepting extension. 

### `preservesTag_of_protectsAddress`

 The generic address-preservation proof on the original native table
supplies the tag invariant required after relocation. 

### `room_of_work`

 Room for the final transfer follows from a private-instruction bound on
the actual, unrelocated pair reports. All earlier pair calls return directly. 

### `ordinary`

 Equality on the entire tape list gives a bijection between the original
pair completion and its ordinary stage in the outer table. 

### `indexed`

 Classify the physical stage by the range of the descriptor/arc/DFS tape
emission and its decoding equivalence to the *same* monomial witness. 

### `indexed_tapes`

 The chronological descriptor prefix, arc bits and independent site
tapes all survive relocation. 

### `indexed_budget`

 Charge the outer dispatch and control transfer to the slack left by the
native pair simulator. The resulting reports fit the exact pair allowance
in the first-half chronology. 
