---
{
  "module": "OAI/Computability/VPVNP/CompressorSlotLevel.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorSlotLevel.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorSlotLevel.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The shrinking level's slot directory

The current level supplies the old-arc records, the chosen layout's role
table, the fixed subdivision counts and the cyclic tag-successor table.
From the current level counts one computes all five native pass frames.
The last two arrays are the next graph's base-slot matching and displacement.


### `Shape`

 Counts at a shrinking level. The four subdivisions are chosen for the new degree. 

### `Shape.bases`

 Number of old base vertices whose tags form the next level's packed base vertices. 

### `Shape.tags`

 Number of tag values per old base vertex in the packed graph. 

### `Shape.lanes`

 Number of residual lanes over each packed base vertex. 

### `Shape.oldDegree`

 Degree of the input slot graph used to enumerate the old arc records. 

### `Shape.colors`

 Number of bits in an old position's color mask. 

### `Shape.subdivisions`

 Number of surviving subdivisions for each of the four role edge types. 

### `Shape.newDegree`

 Target degree of the next graph after padding with dummy slots. 

### `Heads`

 Source tables selected by the current branch and the start of fresh scratch space. 

### `Heads.oldArc`

 Start of the old arc records containing three role sites and a CD indicator for each arc. 

### `Heads.role`

 Start of the eight-entry table selecting a source and target role for each edge type. 

### `Heads.subdivisions`

 Start of the four published subdivision counts indexed by edge type. 

### `Heads.nextSite`

 Start of the table of cyclic tag successors used to choose dummy target sites. 

### `Heads.scratch`

 First fresh word for constructing the endpoint owner, count, row, and inverse tables. 

### `sites`

 Number of packed sites across all base vertices, tags, and residual lanes. 

### `pad`

 Number of dummy slots per packed site needed to bring the surviving degree up to the new
degree. 

### `genuineCount`

 Number of endpoint fields scanned in the genuine candidate range, counting both ends even
for candidates that decode to holes. 

### `dummyCount`

 Number of endpoint fields in the dummy range, two per padding slot at every packed site. 

### `fields`

 Total number of absolute endpoint field addresses in the genuine candidate and dummy
ranges. 

### `owners`

 Number of real endpoint owners, with separate outgoing and incoming rows at each packed
site. 

### `baseArcs`

 Number of outgoing slots over packed base vertices, before lifting the matching to residual
lanes. 

### `rowsHead`

 First word of the rectangular endpoint rows, after the field owner column and all append
counters. 

### `inverseHead`

 Start of the table mapping absolute field IDs back to rectangular slots, after the reserved
row space. 

### `targetsHead`

 Start of the base-target column, immediately after the inverse field table. 

### `shiftsHead`

 Start of the base arc displacement column, immediately after the base targets. 

### `stopAddress`

 First free address after the base-target and displacement columns built by the five slot
passes. 

### `Phase`

 Pass order used by the descriptor controller. 

### `limit`

 Exclusive cursor stop for the selected owner, append, inverse, or base-matching scan. 

### `arity`

 Number of public parameter words required by the worker for each slot phase. 

### `bank`

 The five public banks. Each worker starts its own cursor at zero. 

### `frame`

 The controller row begins with the dispatch tag, initial cursor and exclusive stop. 

### `input_of_tables`

 Assemble the array-scan input from the paper's actual selected role and
original-arc words, using only the four numerical input-region bounds. 
