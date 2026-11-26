---
{
  "module": "OAI/Computability/VPVNP/PairNativeFrameGeometry.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairNativeFrameGeometry.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairNativeFrameGeometry.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Terminal header words and the private address layout of the leaf verifier 

### `regions`

 The exclusive node bound uses the entire address interval, including
the cells below the first absolute descriptor address. 

### `fromHeader`

 Private leaf layout reconstructed from the terminal row base and row word count, the public
input length and label count, and the fixed degree. 

### `frameBase`

 First address after the private histogram, where the terminal vertex installs its geometry
fields. 

### `fields`

 Offsets 0 through 5 serve the leaf decoder. Offsets 6 through 8
supply the argument and cache addresses for leaf preparation. 

### `Ready`

 Values required by the thirteen private stores. The frame starts
immediately after the histogram and ends before the scalar operand cache. 
