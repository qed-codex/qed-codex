---
{
  "module": "OAI/Computability/VPVNP/CompressorExecutionLevels.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorExecutionLevels.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorExecutionLevels.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Selected compressor levels for the descriptor passes

The labels in this file distinguish the scheduled six-party shrinking kernels
from the expander refresh kernel. Each label indexes the actual state pass of
the selected execution. Thus a native descriptor implementation may recover
the original input state and term index by cases on the label, including after
dependent sequencing and iteration.


### `PassOrigin`

 Origin of a pass in the executable compression block. 

### `PassOrigins`

 Keep the origin of every elementary step, including on branch-dependent tails. 

### `executeOrigins`

 Identify the actual kernel at every substep of the selected compression tree. 

### `SelectedLevel`

 One concrete level with its input graph, selected term and selector encoding. 

### `SelectedLevel.inputExponent`

 Base-two exponent of the graph degree entering this selected pass. 

### `SelectedLevel.inputLanes`

 Number of binary lane coordinates in the input state of the selected pass. 

### `SelectedLevel.outputExponent`

 Base-two exponent of the graph degree produced by the selected pass. 

### `SelectedLevel.outputLanes`

 Number of binary lane coordinates remaining in the output state of this pass. 

### `SelectedLevel.input`

 Compression state on which the selected pass operates. 

### `SelectedLevel.pass`

 State transition with the specified input state and output degree and lane dimensions. 

### `SelectedLevel.origin`

 Witness identifying the pass as a particular scheduled shrink or refresh. 

### `SelectedLevel.term`

 Local kernel choice taken by this execution of the pass. 

### `SelectedLevel.selector`

 Boolean selector encoding of the chosen term for the native descriptor workers. 

### `units`

 Charge counting one unit per input position and input slot, together with the selector
bits. 

### `executeLevels`

 Chronological list of the actual passes, input states, and selected terms along the given
block execution. 
