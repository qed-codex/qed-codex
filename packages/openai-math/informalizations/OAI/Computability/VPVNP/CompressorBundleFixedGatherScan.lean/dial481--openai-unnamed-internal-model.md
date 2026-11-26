---
{
  "module": "OAI/Computability/VPVNP/CompressorBundleFixedGatherScan.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorBundleFixedGatherScan.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorBundleFixedGatherScan.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# A complete fixed-program scan of the two bundle key tables

A cursor visits the live positions of the uniform-stride rectangle. At each
position the program reads the stored arc ID, follows it to the original key,
and writes the key at the same physical slot in the output. The slot embedding
determines every live address and lets the frame include all padding.


### `ScanLayout`

 Fit and pairwise separation from the output rectangle. 

### `Filled`

 Readback and memory frame after the first `k` calls. 

### `FullRun`

 The same public bank and program execute every visit. All live slots
contain the corresponding original classifier key. Every other cell,
including a padding slot in the output rectangle, retains its value. 

### `full_run`

 Run the whole native gather through its actual cursor in increasing order. 
