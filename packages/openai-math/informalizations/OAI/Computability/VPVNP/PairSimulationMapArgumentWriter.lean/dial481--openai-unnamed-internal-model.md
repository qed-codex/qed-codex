---
{
  "module": "OAI/Computability/VPVNP/PairSimulationMapArgumentWriter.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationMapArgumentWriter.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationMapArgumentWriter.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Publishing the live arguments of a motif call

The register compiler reads a fixed family of expressions from external records.
The last expression computes the private descriptor base. The writer sets the
map's descriptor pointer, stores the preceding results in consecutive words and
jumps to the map call. Its instruction and probe counts depend only on the
expressions, including when their values depend on the chosen term.


### `recipes`

 The map's descriptor base is computed in the same pass as the argument values. 

### `lines`

 Assignment list for all fields followed by the descriptor base. 

### `Address`

 Code slots for the assignment list, pointer setup, and individual stores. 

### `setupPC`

 Enter the indexed assignment or the pointer setup after the final one. 

### `text`

 Relocatable instructions for expression evaluation, pointer installation
and publication of the argument words. The last store jumps through its
increment instruction to the caller's map-entry continuation. 

### `clock`

 Exact instruction count, including the private pointer copy and all stores. 

### `native_raw`

 External reads use the live six input registers and private stores preserve
every address outside the descriptor. The returned trace composes with every
fuel and branch-bit continuation on the same external memory. 

### `native`

 External reads use the live six input registers and private stores preserve
every address outside the descriptor. The returned trace composes with every
fuel and branch-bit continuation on the same external memory. 
