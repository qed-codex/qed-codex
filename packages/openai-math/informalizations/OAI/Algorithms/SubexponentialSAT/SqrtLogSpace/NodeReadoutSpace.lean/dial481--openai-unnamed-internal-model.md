---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/NodeReadoutSpace.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/NodeReadoutSpace.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/NodeReadoutSpace.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Actual node-array readout after all finite-difference pairs. The fixed
cleanup pays for transient lower words and clears the old output. Preserved
masters supply the coefficient zero vector and both truncation bounds. 

### `ports`

 Shared inputs are restored by the original native readout. 

### `Ready`

 Only actual retained words are hypotheses; scratch is physically cleared. 

### `result_frame`

 All input masters and other high query buffers survive exactly. 

### `command_eval`

 One fixed instruction sequence clears scratch and performs the actual readout. 

### `run_space`

 The same concrete run has the exact flattened output and a bound at every
source prefix, including paid cleanup and every retained caller stack. 

### `output_codes_dense`

 The actual output is the unframed Taylor coefficient stream, in increasing
Taylor order, and its decoded polynomial is the additive dense readout. 
