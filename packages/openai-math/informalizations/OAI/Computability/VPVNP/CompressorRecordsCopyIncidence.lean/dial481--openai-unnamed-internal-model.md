---
{
  "module": "OAI/Computability/VPVNP/CompressorRecordsCopyIncidence.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRecordsCopyIncidence.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRecordsCopyIncidence.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Copying the six incidence columns into the next level

The worker copies one external word per call. Each column starts at cursor zero
and stops after its populated rows. The three base columns therefore copy only
base ports, even when the actual columns have many more lane positions.


### `copyPass`

 The scheduled worker that copies one external incidence word per call. 

### `copyPublic`

 The copy worker's public bank, containing zero followed by the source and destination
column bases. 

### `copyPhase`

 Schedule a tagged column copy from cursor zero to the supplied stop using the source and
destination address expressions. 

### `cell`

 The copy cursor adds a word offset to each array head. 

### `row`

 The report returned by the native one-word copy. 

### `scan`

 Chronological reports of one column, beginning at an arbitrary row. 

### `scan_native`

 Twelve units of private fuel suffice. Each call has eleven events,
two probes and no branch choices. Its charge includes one unit for the call. 

### `scan_valid`

 If the destination rows avoid the tag and active frame, every call
retains the dispatch parameters and satisfies the exclusive cursor guard. 

### `rows`

 The populated length of an incidence column, counting base ports for the first three
columns and actual ports for the other three. 

### `Regions`

 Only live cells of the six arrays participate in the separation hypotheses.
The source may lie on either side of any destination column. 

### `Regions.of_intervals`

 Natural disjoint half-open intervals give the word-address conditions,
including at the largest address representable by a machine word. 

### `Regions.refresh_to_level`

 The native degree-refresh output can occupy either side of the canonical
level directory. Each column has room for the new state's actual slots,
and the copy scan uses the shorter base-port count in its first three columns. 

### `columnScan`

 The complete copy scan for one incidence column between the source and destination level
directories. 

### `reports`

 Execute each column in sequence, feeding its actual final memory to
the next worker. Each column has a fresh zero cursor and public operands. 

### `Runs`

 Each worker call sequence runs with its own two column heads. 

### `allColumns`

 The six column indices in the order used to copy the full incidence directory. 

### `copy_directory`

 The scratch incidence state is transferred in six actual native segments.
All populated destination cells represent the same graph, including inverse
ports, displacements and widths. The charge is three units per copied cell. 
