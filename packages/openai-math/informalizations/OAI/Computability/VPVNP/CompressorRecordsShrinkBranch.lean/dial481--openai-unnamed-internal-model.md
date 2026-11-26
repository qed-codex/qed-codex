---
{
  "module": "OAI/Computability/VPVNP/CompressorRecordsShrinkBranch.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRecordsShrinkBranch.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRecordsShrinkBranch.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The ordered shrinking branch through the selected geometry

Starting from an old represented wire graph and unused workspace, generate the
greedy geometry, sort and split the demand bundles, and transpose their old arc IDs.
The deterministic prefix is independent of the forthcoming term stream. At the
following worker the legal tapes are in bijection with the original shrinking
choices. On each such choice, use its output words to build the selected role and
preimage directories while retaining the dense absolute-ID table.


### `PrefixFits`

 Numerical bounds of the deterministic input scans and the admitted-term worker. 

### `Prefix`

 Actual chronological reports before the first nondeterministic shrinking call. 

### `Prefix.input`

 The deterministic shrinking-input run that produces the sorted AB and CD width data. 

### `Prefix.absolute`

 Reports of writing the absolute old arc identifiers into the bundle directory before term
  selection. 

### `Prefix.gather`

 Reports of gathering the demand data into dense motif rows for the term chooser. 

### `beforeTerm`

 The memory at entry to the term chooser, after input construction, absolute arc indexing,
and demand gathering. 

### `reports`

 All reports before the first term choice, in the order of input preparation, absolute arc
indexing, and demand gathering. 

### `Selected`

 Fixed chronological term and chosen-geometry runs for a specified shrinking choice. 

### `Selected.terms`

 Reports of the term-selection calls for the specified motif choices. 

### `Selected.geometry`

 The native construction of the layout, role records, and child directory determined by
  those choices. 

### `beforeOutput`

 The memory supplied to the output sweep after the term rows and their chosen geometry have
been written. 

### `reports`

 The selected branch's term reports followed by the reports of its geometry construction. 

### `build`

 The same deterministic prefix serves every later shrinking choice. Legal tapes
at its exit are exactly the admitted choices in compact motif order. 
