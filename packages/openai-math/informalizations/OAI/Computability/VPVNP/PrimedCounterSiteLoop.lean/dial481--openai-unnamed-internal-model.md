---
{
  "module": "OAI/Computability/VPVNP/PrimedCounterSiteLoop.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PrimedCounterSiteLoop.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PrimedCounterSiteLoop.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Accumulating all primed sites in one histogram

Every site gets its own empty mark array and its prescribed root frame. The
histogram passes from one site to the next. After the last site, comparing
the entire array against the nomination accepts precisely the binary tapes
whose joint production count equals the nominated histogram.


### `runSites`

 Ordered complete site parses, with only the histogram shared between them. 

### `runSites_local`

 Any site reached by a complete successful execution passes its own
mark and tree checks, even if the incoming histogram is nonzero. 

### `runSites_paths`

 Along arbitrary accepted branch tapes, the online shared histogram sums
the per-site increments in visit order. 

### `compareAll`

 At the final site every dense histogram component must agree with its
nomination. The linear comparison consumes no binary choice. 

### `sitePaths_length`

 Each accepted site consumes exactly one word-choice list at each of
its `2*d+1` preorder visits. 

### `siteArray`

 Convert a path to its fixed-length array of per-node choice lists. 

### `siteLoopEquiv`

 The actual loop over the rows, restricted by the final full histogram
comparison, is parsimonious with the site path model. 
