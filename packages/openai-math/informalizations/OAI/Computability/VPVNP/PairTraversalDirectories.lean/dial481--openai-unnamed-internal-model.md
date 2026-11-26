---
{
  "module": "OAI/Computability/VPVNP/PairTraversalDirectories.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairTraversalDirectories.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairTraversalDirectories.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Connecting the placement directories to the native traversal table

The native Appendix E scan records each old identifier under its placed new
site. Those directories, a common zero count for the leaves, and the end of
the raw arena supply all inputs to the traversal-table writer. The source
records retain the physical numbering of the chosen compression branch.


### `Directory`

 A completed numerical placement pass with its concrete raw memory regions.
The native owner map is the term's actual placement in the two site orders. 

### `Directory.pub`

 Six public directory words locating the old-site, output-site, count, and preimage row
  data for a selected pass. 

### `Directory.source`

 Expose the per-site child count and preimage-row start as source pointers for the selected
directory reader. 

### `Directories`

 Persistent directories of all non-leaf terms on this particular branch. 

### `directorySources`

 Collect the child-count and preimage-row source pointers along the chain of selected
compression directories. 

### `selected_sources_ready`

 The source-count and source-list pointers of an actual selected branch
satisfy all the native writer's preconditions. 
