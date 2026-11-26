---
{
  "module": "OAI/Computability/VPVNP/CompressorRecordSlots.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRecordSlots.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRecordSlots.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Recording the two slot numbers of each surviving arc

In the third scan of Appendix E, each new position receives two lists of
actual arc identifiers, one for each orientation. Translating the original
CD source to lane zero gives the integer key used by the packed graph.
Each key occurs once per incidence list. Counting smaller keys in that list
therefore computes the same slot number as sorting. The two ranks occupy
separate fields at a common absolute arc address.


### `IncidentRow`

 The list at one endpoint after the arc-generation scan, in visitation order. 

### `IncidentRow.ids`

 The duplicate-free list of all arc identifiers incident at the row's specified endpoint. 

### `collectRows`

 One pass over all generated actual identifiers, appending each to the row
at its endpoint. Incoming and outgoing arrays use the same code with different
endpoint functions. 

### `collectRows_eq`

 Each local array contains exactly its incident identifiers in scan order. 

### `collectedRow`

 Visiting each generated ID once supplies the incidence rows used by
`actualSlot_numbers` without separate searches over the graph at each site. 

### `baseId`

 Forget the absolute lane but retain the entire original CD arc, type and subdivision. 

### `incidentBaseEquiv`

 At either end, normalizing all motif lanes gives a bijection of the actual
incidence fiber with the fiber used in the sorted base graph. 

### `keyCount`

 The radix of the unconsumed-lane-independent relative key. 

### `relativeKey`

 Integer key stored in the incoming or outgoing incidence row. 

### `arcAddress`

 A record ID keeps the original absolute lane of the motif. Dummies are
indexed by their absolute source site and local dummy number. 

### `endpointAddress`

 Two directly addressed endpoint fields for each generated actual arc. 

### `endpointAddress_size`

 Even with unoccupied mixed-radix keys, the space for both endpoint fields
is linear in the number of absolute sites. 

### `rowRank`

 Counting smaller keys computes the zero-based position in the sorted row. 

### `incidentRow_length`

 The count in one absolute row is the fixed surviving degree; the role map
may designate either orientation, including roles shared by parallel edges. 

### `actualSlot_numbers`

 Both word-sort ranks agree with the regularized graph, for every absolute
arc and arbitrary input visitation order in the two local lists. 

### `actualSlot_route`

 The numerical incoming field and the source-relative displacement describe the
actual destination of this absolute arc. 

### `dummySlot_route`

 A dummy's endpoint numbers are obtained by a single addition at both ends.
The arc advances the tag at its base and preserves the absolute lane. 

### `directWrite`

 Write the known slot of a padding or degree-refresh arc into one endpoint field. 

### `refresh_internal_route`

 At a refresh, the indexed expander's reverse arc supplies the incoming
slot in the promoted graph. Both fields can be written by `directWrite`. 

### `keyWord`

 Encode the relative key into a machine word with headroom for the increment
used by the unsigned rank comparison. 

### `recordRank_native`

 A single native call ranks one actual arc in its unsorted endpoint row and
writes that rank. `actualSlot_numbers` identifies these returned words with the
two fields of the regularized graph. 

### `rankExecution`

 Execution of one endpoint call with its actual write log. The number of
keys is fixed by the compressor block. 

### `actualSlot_writeback`

 Starting with the two incident arrays at the actual source and target,
run both rank calls on the same arc. The second call reads the first call's
post-memory. The resulting arc record contains both correct slot numbers. 

### `writeback_probes`

 The total number of endpoint-writeback probes in a complete shrinking scan.
Each genuine arc costs one rank scan per endpoint and each dummy costs two
single-word writes. The coefficient of the position count depends only on the
two fixed degrees and the subdivision profile. 
