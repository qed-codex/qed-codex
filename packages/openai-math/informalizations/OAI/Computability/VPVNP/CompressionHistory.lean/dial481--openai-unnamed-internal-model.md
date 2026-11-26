---
{
  "module": "OAI/Computability/VPVNP/CompressionHistory.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressionHistory.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressionHistory.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Local histories of placed wire kernels

A term of (7.1) sends each complete old vertex to one new vertex. At a fixed
new vertex the recursive expansion visits precisely this placement fiber and
its local maps and fields. For a selected sequence of terms, Theorem 7.1 bounds
both the occurrence count and the largest field or individual map-entry degree
by exponentiating a constant per compressor block.


### `SiteRecords`

 The field and map occurrences of a kernel at one site, with their bit lengths
and monomial degree bounds. Occurrences can have equal lengths or identical values. 

### `SiteRecords.Field`

 Finite index type of individual bit-field occurrences recorded for a kernel at one output
  site. 

### `SiteRecords.width`

 Length in bits of each recorded field occurrence at the site. 

### `SiteRecords.Map`

 Finite index type of local map occurrences recorded for a kernel at one output site. 

### `SiteRecords.degree`

 Monomial degree bound attached to each recorded local map occurrence, controlling its
  individual entries. 

### `SiteRecords.count`

 Count the vertex itself and all its immediate map and field occurrences. 

### `SiteRecords.largest`

 The largest field length or degree of an individual map entry at this site. 

### `Term.Preimage`

 The same finite placement fiber occurs in `Term.pushWitness`. 

### `Term.pushHistorySize`

 A new vertex visits all local records and each old history in its own fiber once. 

### `TermChain`

 One selected branch with its actual terms, placements and records. 

### `length`

 Number of selected kernel terms along the branch from the initial network to the final
network. 

### `occurrences`

 Count occurrences of the initial vertices and subsequent local records at each final site. 

### `largest`

 The next length bound includes every field and degree at every output site. 

### `peak`

 Maximum over the initial stage and all intermediate stages on this branch. 

### `AllRecordsLe`

 Every bit field and every individual map entry on every intermediate level. 

### `Bounded`

 Local bounds used at every substep. `W` is a bound on its incoming fields.
The next substep uses the actual largest field or degree from this one. 

### `growth`

 Iteration bounds both the number of operations at each final site and the
largest field or single-entry degree reached anywhere on the selected branch. 

### `blockGrowth`

 A block with at most `s` elementary substeps costs a fixed factor `C^s`.
The constant in Theorem 7.1 is uniform in the number of blocks and the branch. 

### `State.maxWireWidth`

 The largest actual wire width of a lifted state. 

### `StatePass.Records`

 A substep supplies its local records on every branch, even when its topology
and placement depend on the selected terms. 

### `StatePass.Bounded`

 The substep count and width estimates needed by the history recursion. 

### `Records`

 Local site records for every pass and each branch-dependent continuation of the execution,
with the unit record at a terminal state. 

### `termChain`

 The recursive data contains exactly the terms selected by this execution path. 

### `Bounded`

 Every pass on every branch satisfies its local bounds with constant `C`, controlling record
and preimage counts, field widths and map-entry degrees. 

### `final_maxWireWidth_le_peak`

 The maximum actual final arc width is among the quantities controlled by
this branch's peak, even when the terminal layout depends on all earlier choices. 

### `localHistory_bounds`

 Theorem 7.1's local growth conclusion for a chosen branch of an execution
of `T` blocks, each containing at most `s` substeps with bounded local records. 
