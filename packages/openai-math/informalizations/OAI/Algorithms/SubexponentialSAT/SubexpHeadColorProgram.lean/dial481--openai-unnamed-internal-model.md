---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SubexpHeadColorProgram.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpHeadColorProgram.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpHeadColorProgram.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Read a head color from its physical one-hot type encoding

Ports 0, 1, and 2 hold the flat type bytes, unary position, and unary color
width. The fixed array reader preserves these inputs. A five-label bit loop
counts the false prefix of the selected one-hot word; the remaining suffix is
cleared. Only output port 3 changes, and scratch ports 4--9 are restored.


### `program`

 Each false bit emits one true counter bit; the first true bit terminates. 

### `command_eval_oneHot`

 A generic valid one-hot cell is decoded by the actual selected-bit loop. 

### `encodeType_head_split`

 Decompose the serialized type at the requested head-position cell. 

### `command_eval`

 The typed endpoint obtains the head color from encoded input bytes. 

### `program_run_raw_lengths`

 A uniform polynomial in the lengths of the three actual input words. 
