---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/SparseCodeBasic.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/SparseCodeBasic.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/SparseCodeBasic.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Shared interfaces for sparse ternary parity checks

The definitions distinguish edge coordinates from graph vertices. Parallel
edges have different ports. All construction theorems built on these interfaces
must eventually discharge the local-distance and graph-mixing hypotheses.


### `PortGraph`

 A regular bipartite graph represented by its bijection of left and right
ports. Edges are left ports. No simplicity assumption is made. 

### `HasMixing`

 The only spectral consequence needed by the global distance proof. 

### `IsTannerCodeword`

 Semantic Tanner constraints before turning the local checks into one
explicit sparse matrix. 
