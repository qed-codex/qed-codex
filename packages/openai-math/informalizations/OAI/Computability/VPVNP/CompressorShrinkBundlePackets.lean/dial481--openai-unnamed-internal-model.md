---
{
  "module": "OAI/Computability/VPVNP/CompressorShrinkBundlePackets.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorShrinkBundlePackets.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorShrinkBundlePackets.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Dense shrinking packets at their global block-program ordinals

The window starts after the three header visits and six greedy visits of
the selected shrinking substep. Each packet uses the corresponding worker
table, physical bank and number of empty choice tapes from the native run.


### `shape`

 The fixed block-program geometry used to locate the shrinking bundle's level headers and
operand tables. 

### `origin`

 The scratch-table-zero address expression used as the origin of bundle preparation in this
substep. 

### `exponent`

 The input degree exponent selecting the dimensions of this substep's bundle workers. 

### `entries`

 The planned catalog visits for the eleven dense bundle stages at this shrinking substep. 

### `window`

 Locate all dense bundle visits together in the fixed block, after the header and greedy
passes and before later shrinking work. 

### `stages`

 The ordered bundle stages from preliminary placement to the absolute motif-ID scan. 

### `localIndex`

 Reindex a stage's position in the bundle order as a position in the matching visit list. 

### `index`

 The global script index of the bundle stage at the given position in this substep's window. 

### `visit`

 Build the source packet for one bundle stage with its global worker index, physical operand
bank, cursor range and empty choice tapes. 

### `field_values`

 Runtime expressions for the global occurrence give the physical packet's
two cursors and operand bank, including the cast from the catalog arity. 

### `maxFuel`

 A finite worker-fuel cap for this substep, independent of input length. 

### `packets`

 All global packets run on consecutive data memories. Each packet retains
the physical header, row-count cell and pitch whenever they precede the arena. 
