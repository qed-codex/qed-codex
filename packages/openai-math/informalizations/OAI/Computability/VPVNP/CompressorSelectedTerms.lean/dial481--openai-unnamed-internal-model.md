---
{
  "module": "OAI/Computability/VPVNP/CompressorSelectedTerms.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorSelectedTerms.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorSelectedTerms.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Native term rows for the selected shrinking and refresh levels

Both kinds of level run a fixed demand/supply grid. The finite row family
below uses the original pass's choice at the actual motif or port block.
Consequently a successful scan writes the demand grid point, repetition
count and supply coordinates for that same branch. Its charged probes
depend on the number of motifs and fixed grid, while the local arithmetic
also depends on the word width.


### `Grid`

 A single fixed grid, with the physical order of its demand and supply columns. 

### `Grid.J`

 Vertex set shared by the demand and supply graphs of this motif. 

### `Grid.D`

 Index set for the motif's demand edges. 

### `Grid.E`

 Index set for the motif's supply edges. 

### `Grid.src`

 Source vertex of each demand edge. 

### `Grid.dst`

 Target vertex of each demand edge. 

### `Grid.graph`

 Supply graph on the motif vertices with edges indexed by `E`. 

### `Grid.p`

 Positive rational weight used to measure the demand on each demand edge. 

### `Grid.q`

 Positive rational weight used to measure the payload on each supply edge. 

### `Grid.comparison`

 Demand-to-supply energy comparison constant used to construct the strict grid. 

### `Grid.relaxed`

 Coefficient of the squared demand norm in the padded supply-energy bound. 

### `Grid.block`

 Fixed motif identities and width bounds for these edges, weights, and comparison
  constants. 

### `Grid.demandOrder`

 Physical order of the demand columns in each motif row. 

### `Grid.supplyOrder`

 Physical order of the supply columns in each selected term record. 

### `shrinkGrid`

 Grid for the six-vertex shrinking motif, with two demand columns and eight supply columns. 

### `refreshGrid`

 Grid for a refresh block, with tie demands and supply edges indexed by port and expander
slot. 

### `grid`

 Select the shrinking or refresh grid according to the pass origin. 

### `Batch`

 Actual input and selected output rows of the grid, in the same motif order
as the compression pass. 

### `Batch.demand`

 Width requested on each demand edge at each physical motif ordinal. 

### `Batch.choice`

 Selected admissible term for the demand row at each motif ordinal. 

### `batch`

 Arrange the actual pass demands and selected terms in physical motif order. 

### `d`

 Number of demand columns scanned in one motif row. 

### `e`

 Number of supply columns written in one motif row. 

### `fitConstant`

 Fixed contribution to the word width required by this grid's term-record scan. 

### `charge`

 Upper bound on the cost of scanning one motif, counting the five native calls and the probe
bound for one term row. 

### `stepConstant`

 Grid-dependent coefficient in the event bound for one row as a function of word width and
log demand width. 

### `phaseConstant`

 Common per-row call and probe charge for the two pass grids. 

### `fitConstant`

 Maximum fixed word-width allowance for the shrinking and refresh term-record scans. 

### `stepConstant`

 Common coefficient in the per-row event bound for the shrinking and refresh grids. 

### `run`

 The real five-call scans for all terms of one selected level. The
input is the physical demand array, including its disjoint term-row arena. 
