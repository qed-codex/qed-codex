---
{
  "module": "OAI/Computability/VPVNP/PairShrinkPartyColumns.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairShrinkPartyColumns.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairShrinkPartyColumns.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Native frame schedule for one party of a shrinking motif

The AB interval, when present, is followed by the incident surviving
subdivisions in source and then target order. Each assembled operand
occupies its own stride in scratch. This permits all frames to run in
one program while every operand has the value it would have in isolation.


### `Column`

 AB has one staging region. Each surviving type has a region at each end. 

### `active`

 Test whether the selected party gathers the AB demand or the given oriented surviving
supply field in the chosen layout. 

### `columns`

 The fixed list of candidate gather columns filtered to the ones incident to this party. 

### `At`

 An active gather column together with its membership in this party's filtered list. 

### `frames`

 The number of frame copies in a column, given by the AB arc count or the selected supply
role's subdivision count. 

### `base`

 Private staging destination for the AB demand or the oriented surviving supply word of this
column. 

### `Visit`

 A copy visit consisting of an incident column and a valid frame ordinal within that column. 

### `visits`

 Enumerate the active columns in party order and every frame within each column in
increasing ordinal order. 

### `gather`

 The finite instruction table visits every frame of every incident column. 

### `setup`

 Use the thick-wire worker on AB and the reverse subdivision worker on each supply field. 

### `InBuffer`

 Every nonempty slice stays within the stride reserved for its column. 

### `inBuffer_of`

 A frame written at its assigned base is confined whenever its last bit is within the stride. 

### `memory`

 The final memory at each operand agrees with running that column alone.
All addresses below staging retain the child packets and shared hidden fields. 

### `native`

 Run the fixed concatenated frame code at this party. Each target contains the same
operand as in its own column run, and all previously supplied inputs below staging survive. 

### `ab_bound`

 Every nonempty frame from the AB worker fits the logical demand word. 

### `surviving_bound`

 A surviving reverse frame has precisely the endpoint's subdivision width. 
