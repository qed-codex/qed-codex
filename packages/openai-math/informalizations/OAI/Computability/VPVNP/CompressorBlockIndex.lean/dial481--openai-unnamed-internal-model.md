---
{
  "module": "OAI/Computability/VPVNP/CompressorBlockIndex.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorBlockIndex.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorBlockIndex.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Selector visits in the fixed chronological block

A shrinking selector follows its header, greedy, bundle and dense demand
passes. A refresh selector follows its header, three segment scans and all
tie demands. The ordinal formulas below locate the same native worker in
every repeated block and identify its compiled calendar phase.


### `Focus`

 A particular occurrence in a list, recorded with the prefix and suffix that locate it. 

### `Focus.before`

 Entries preceding the distinguished occurrence. 

### `Focus.item`

 The entry at the distinguished occurrence. 

### `Focus.after`

 Entries following the distinguished occurrence. 

### `append`

 Retain the distinguished occurrence when a suffix is appended to the list. 

### `prepend`

 Retain the distinguished occurrence when a prefix is prepended to the list. 

### `cast`

 Transport a distinguished occurrence along an equality of lists. 

### `index`

 The zero-based list index of the distinguished occurrence. 

### `shrinkSelector`

 The shrinking motif-selection visit, with its demand count, term-record heads and supply
order. 

### `shrink`

 The occurrence of the motif selector in shrinking step `i`. 

### `refreshSelector`

 The term-selection stage of the degree refresh, evaluated from its published level inputs. 

### `refresh`

 The occurrence of the term selector in the complete degree-refresh visit list. 

### `earlier`

 All shrinking visits in the block strictly before step `i`. 

### `later`

 The shrinking visits strictly after step `i`, followed by the block's refresh. 

### `blockShrink`

 The occurrence of step `i`'s shrinking selector in the complete block. 

### `blockRefresh`

 The occurrence of the refresh selector in the complete block after all shrinking visits. 
