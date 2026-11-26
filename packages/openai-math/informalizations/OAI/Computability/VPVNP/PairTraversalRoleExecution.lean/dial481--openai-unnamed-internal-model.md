---
{
  "module": "OAI/Computability/VPVNP/PairTraversalRoleExecution.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairTraversalRoleExecution.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairTraversalRoleExecution.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Native role directory for the selected history

One pass per physical level writes the cursor, shrink, or refresh tag at the
public offset from each live descriptor header. Each pass starts with the
memory left by its predecessor. A separate final-bit interval can occupy
the gap between the descriptor region and these sparse tags.


### `writeTags`

 Post-memory of the per-layer writes. 

### `tagWords`

 The word region occupied by these tags has the same extent as the
corresponding row region, translated by the public offset. 

### `write_tags_outside`

 Tag writing cannot alter any earlier descriptor, final bit, or memory cell
outside its own layer intervals. 

### `writeTags_reads`

 Every selected layer's role can be read back at each site's actual header
address. 

### `RolePasses`

 Replay of the fixed-width-independent role worker over all selected layers. 

### `native_write_tags`

 Exactly one burst and one external write per stored role. The final memory
agrees with the directory read by the visit dispatcher. 

### `probe_word_add`

 The arithmetic performed by the dispatcher reads the same natural address
as the tag directory when the public offset and node pointer fit together. 

### `selected_tags_and_rows`

 Build the tags and the DFS descriptors in disjoint intervals of the same
memory. With `F` final-bit words between the intervals, all `F` cells retain
their original contents. The pointer offset used by the dispatcher is exactly
`rowWords + F`. 

### `native_selected_roles`

 Initialize the selected branch's role tags using one native write per site.
The running time and probe cost use the actual number of compressor stages. 
