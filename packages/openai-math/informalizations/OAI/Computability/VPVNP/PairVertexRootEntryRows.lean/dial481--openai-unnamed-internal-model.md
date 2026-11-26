---
{
  "module": "OAI/Computability/VPVNP/PairVertexRootEntryRows.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairVertexRootEntryRows.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairVertexRootEntryRows.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The three terminal gather arrays at vertex entry

The final packed incidence bank supplies the inverse and width columns.
The prefix worker fills the disjoint offset array. Header slots 9, 10 and
11 point to these very arrays in the layout read by the root gather.


### `gather_rows_of_columns`

 Recover the gather rows in any handoff memory that retains the final
incidence columns and the freshly computed start offsets. 

### `VertexEntry.gather_heads`

 The native header loads resolve to the two final incidence columns and
the selected prefix table, uniformly over the current site ordinal. 

### `VertexEntry.gather_rows`

 The selected packed calendar supplies the gather rows in the actual
vertex-entry memory, through the header's loaded addresses. 

### `Start.quiet_gather_rows`

 The quiet traversal-row builder leaves all three endpoint arrays in place.
This supplies the physical row input before the shared-wire choice is made. 
