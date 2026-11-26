---
{
  "module": "OAI/Computability/VPVNP/PairTraversalBuildExecution.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairTraversalBuildExecution.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairTraversalBuildExecution.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Native construction of all depth-first traversal rows

The raw preimage records from Appendix E are translated layer by layer.
Every native pass reads identifiers below the descriptor arena, and writes
only the live words of its own row. Consequently the raw inputs and the
completed older layers survive. The final memory is precisely the image
used by the depth-first traversal.


### `Source`

 Locations of the count and old-site identifier list for each site. 

### `Source.counts`

 External address of the cell holding the number of old-site identifiers for each site of
  this layer. 

### `Source.starts`

 External address of the first identifier in each site's list of preimages in the
  preceding layer. 

### `Source.Ready`

 The Appendix E records lie below the fresh traversal arena. 

### `leafSource`

 The shared zero word can supply the zero count for every cursor leaf. 

### `Sources`

 The raw record directories, in increasing compressor-stage order. 

### `SourcesReady`

 Each layer's source directory describes the correct old-site identifier lists in memory,
with all count cells and live identifier cells below `limit`. 

### `BuildPasses`

 Each layer's actual scan begins with the memory left by its predecessor.
The trace lists concatenate the native instruction events in that order. 

### `Layer.probeCount`

 Two probes for each identifier, plus three probes for each header. 

### `native_build`

 Construct all layers from their live raw count and identifier records.
The proof executes each native pass and obtains the exact descriptor image
as its post-memory. 

### `selected_native_traversal`

 On an actual selected compressor branch, the native builder passes their
post-memory directly to the ordered DFS. The two probe counts measure the
whole build and a single final vertex's traversal respectively. 
