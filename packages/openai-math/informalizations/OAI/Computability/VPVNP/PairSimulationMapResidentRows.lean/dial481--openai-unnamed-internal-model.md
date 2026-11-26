---
{
  "module": "OAI/Computability/VPVNP/PairSimulationMapResidentRows.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationMapResidentRows.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationMapResidentRows.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Reading a shrinking map occurrence and its demand-grid point

The count and ID arrays published in the old level's header at offsets 34
and 35 are indexed by packed site. Each ID has the dense motif ordinal
as its quotient by six and the party as its remainder. The quotient indexes
the term table published at offsets 36 and 37, whose first word selects
the demand-grid point for that occurrence.


### `Site`

 A packed site in the selected shrinking layout. 

### `siteIndex`

 The site numeral used by the count and ID arrays. 

### `order`

 The restriction of dense motif-and-party order to one packed site. 

### `entry`

 The motif and party of a position in a packed site’s ordered map row. 

### `ordinal`

 The term-table ordinal of a shrinking motif. 

### `capacity`

 The number of map occurrences at each packed site. 

### `Directory`

 The compressor’s map directory specialized to the selected layout. 

### `id_read`

 A site ordinal indexes the ordered fiber. The word stored there is
the global motif-and-party ordinal, even if several parties share the site. 

### `directory_fit`

 The physical arena bounds the count address and even the exclusive
end of the last packed site's map row. 

### `allocated_id`

 Read the dense ID from the actual allocated map bank. 

### `HeaderResult.directory`

 The output cursor and stop registers delimit exactly this site's ordered
map row. Registers four and five recover the term head and ten-word stride. 

### `ItemResult.selected`

 At a position of this site's ordered map row, the native reader returns
the dense motif ordinal, its six-valued party, and the demand-grid point
written by the term worker for this motif. 
