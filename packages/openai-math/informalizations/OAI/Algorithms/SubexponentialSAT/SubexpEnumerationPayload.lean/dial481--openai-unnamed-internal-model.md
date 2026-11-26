---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SubexpEnumerationPayload.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpEnumerationPayload.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpEnumerationPayload.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# A fixed machine emitting the encoded increment schedule

The input contains the actual one-pass increment payload and the unary number
of outer basepoints.  `BlockCopyProgram.program` preserves that payload and
emits one copy for each outer basepoint.  The payloads below are computed from
the supplied vector arrays, and their lengths follow from the proved coset
cardinalities rather than from numerical premises about execution.

This is the increment schedule used by the separate color sums.  It does not
construct the basis arrays, add outer basepoints, or evaluate the summands.
The cost of preparing the input stacks remains a separate obligation.


### `scalarWidth`

 One field coordinate occupies this many binary cells. 

### `scalarBits`

 The canonical little-endian binary word for an actual field element. 

### `vectorBits`

 Coordinate words in increasing ambient-coordinate order. 

### `vectorsBits`

 Fixed-width vector words concatenated in their supplied list order. 

### `innerVectors`

 Every color's increment list is scanned separately in increasing color
order.  Shared vectors, such as zero, remain distinct visits. 

### `workVectors`

 The actual list of increment visits, one complete pass per outer datum. 

### `workPayload_length_exact`

 The machine's emitted cells are tied to the actual coset dimensions. 

### `preparedState`

 Prepared input: stack 0 is the one-pass payload; stack 1 is the output
suffix; stack 2 is empty; stack 3 is the unary number of outer basepoints. 

### `program_trace`

 A trace of the same twelve-label Boolean-stack program for every p, D,
number of colors, and supplied array. No evaluation callback is assumed. 

### `finished_output_length`

 The output-stack length includes the unchanged suffix. 

### `traceSteps_le_real`

 The proved coset bound now controls actual finite-control steps. The
linear encoding factor retains the variable coordinate width. 

### `program_primitive`

 A run of the fixed primitive binary machine supplied by the verified
compiler. Its overhead depends only on the fixed copy program. 
