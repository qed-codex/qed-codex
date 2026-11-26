---
{
  "module": "OAI/Computability/VPVNP/CompressorShrinkResidentLayout.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorShrinkResidentLayout.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorShrinkResidentLayout.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Workspace for the shrinking history's two resident directories

The absorbed-field records start after the chosen placement's child rows.
The map records follow them. Each stores one owner word and one ordered
row word per occurrence, and one counter per packed site.


### `radix`

 Occurrences per motif in a resident scan, four for absorbed fields and six for party maps. 

### `rowCapacity`

 Number of occurrence slots reserved per packed site in the selected field or map directory,
accounting for degree, pieces and occurrences per motif. 

### `Layout`

 Dimensions and starting address for two consecutive resident directories, each with an
owner column, per-site counts and ordered preimage rows. 

### `Layout.sites`

 Number of packed output sites, each with its own count and preimage row in both
  directories. 

### `Layout.motifs`

 Number of shrinking motifs whose field and party-map occurrences must be assigned to
  owners. 

### `Layout.first`

 Base of the hidden-field owner column, the first address of the combined resident
  workspace. 

### `size`

 Number of occurrences in the selected directory, the motif count times four hidden fields
or six party maps. 

### `owner`

 Start of the selected owner column. The hidden-field column comes first and the map column
follows the complete hidden-field directory. 

### `counts`

 Start of the per-site counts immediately following the selected occurrence-owner column. 

### `rows`

 Start of the selected preimage rows, following one count word per packed site. 

### `endAddr`

 First free address following the party-map preimage rows and hence both resident
directories. 

### `params`

 Six public collector operands in order, occurrence count, owner base, site count, count
base, row capacity and row base. 

### `layout`

 Instantiate the resident workspace at `first` using the actual number of packed sites and
the motif order of the shrinking state. 

### `frame`

 No index is truncated when the next free address fits the word. 
