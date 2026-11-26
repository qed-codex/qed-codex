---
{
  "module": "OAI/Computability/VPVNP/PairShrinkCDFieldAddress.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairShrinkCDFieldAddress.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairShrinkCDFieldAddress.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Direct pointers to the two unsplit CD operands

The motif's rank is relative to its bundle. Its classified row contains old
arc IDs in append order. A fixed-size rank comparison retrieves the matching
original ID. The thickness column at its source chooses which of the two
private child halves belongs to C and which belongs to D.


### `Header`

 Runtime operands for finding the CD demand's old arc and choosing the correct private half
at C or D. 

### `Header.fields`

 The shared bundle lists, ranks, motif ordinal, and old half-wire geometry used by the CD
  lookup. 

### `Header.owners`

 Number of classified owner rows. Half this count is the displacement to the CD half of
  the row rectangle. 

### `Header.thickness`

 Head of the array of old-site thickness flags used to orient the two CD endpoints. 

### `Header.row`

 CD rows occupy the second half of the classified row rectangle. 

### `Header.candidate`

 Read an old arc ID at a fixed column of the selected bundle's CD row. 

### `equal`

 A nonzero modular difference divided by itself is one. A zero
difference divided by itself is zero, including at the largest word. 

### `Header.select`

 Keep the candidate's arc ID exactly when its stored rank equals the motif's piece number,
and return zero otherwise. 

### `Header.arc`

 Sum the rank-filtered CD row entries to recover the old arc ID at the selected piece. 

### `Header.flag`

 Read the thickness flag of the old source site, whose ordinal is the selected CD arc ID
divided by the old degree. 

### `Header.field`

 C follows the incoming half when its old source is thick. D follows
the complementary half. Each source address uses the numbered child arena. 

### `noncomputable local instance : DecidableEq X.Base`

 Classical equality of base vertices used in the classified CD fiber lookup. 

### `members`

 Each row index decodes to a different motif, and every motif in the
bundle occurs at one index. 

### `load`

 Read the external word at a fixed scalar offset from the runtime old-level header address. 

### `header`

 Level header offsets 0, 1 and 2 give the old base, degree and lane counts.
The original bucket owner and appended-ID rectangles determine the count of
classified buckets and the preceding thickness column. 

### `geometry`

 Resolve both calculated heads to the values that the shrinking scan
actually published into its bucket and preliminary placement operand banks. 

### `child`

 The physical child field expressions use the published old DFS geometry
and the incidence heads following the 54-word scalar header. 

### `abHeader`

 The raw rank, ID and AB bank heads in the old header select the
corresponding ranked input and physical copy setup. 
