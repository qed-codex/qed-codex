---
{
  "module": "OAI/Computability/VPVNP/CompressorScriptWindow.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorScriptWindow.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorScriptWindow.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Embedding a contiguous native substep in the fixed block program

A window identifies each occurrence by its ordinal inside the complete
static block. Equal worker tables can occur many times. An indexed map
of a chronological source walk retains this distinction while keeping
the original input memories, tapes and reports.


### `Window`

 A decomposition of the script block around a specified contiguous list of visits. 

### `Window.before`

 Visits in the block preceding the first occurrence in the window. 

### `Window.after`

 Visits in the block following the window. 

### `position`

 Index of a window occurrence in the block, obtained by skipping its preceding visits. 

### `index`

 Index of a window occurrence in the whole script, including the initialization prefix. 

### `ofWorker`

 Form a script visit from a native worker, transporting its operands to the matching catalog
entry. 
