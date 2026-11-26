---
{
  "module": "OAI/Computability/VPVNP/PrimedCounterTraces.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PrimedCounterTraces.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PrimedCounterTraces.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The multiplicity of accepting binary preorder traces

For each assignment of the internal primed bits, each site supplies one binary
choice list for every node call. Marking repeated positions and comparing the
sum of the emitted histograms with the nomination gives the integer coefficient
of the primed pair polynomial.


### `SitePaths`

 Branch tapes accepted by one parse's stack and mark checks. 

### `chosenTokens`

 Recover the node selections from the consumed binary branches. 

### `bitTraceEquiv`

 Fixed-width branching preserves the exact multiplicity of token streams. 

### `siteEquiv`

 Complete local parsimony, including malformed code rejection and the
unique leaf bijection recovered from the position marks. 

### `siteHistogram`

 Counter values emitted by this path's actual sequence of stack updates. 

### `PairPaths`

 One shared internal assignment followed by one complete branch path per site. 

### `pairEquiv`

 Identify an internal assignment and one accepted binary preorder path at each site with the
parse choices defining the pair coefficient. 

### `totalHistogram`

 Counts accumulated in the shared histogram across both primed groups. 

### `pairPath_count`

 The number of branch tapes surviving the histogram comparison is precisely
the coefficient of (9.4), including when no tape is accepted. 
