---
{
  "module": "OAI/Algorithms/SubexponentialSAT/ModularDivisionPrograms.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/ModularDivisionPrograms.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/ModularDivisionPrograms.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# A finite binary long-division program

The modulus and dividend are Boolean words stored on stacks. Every routine below
has a fixed finite table, independently of the lengths and values of these words.


### `seven`

 Ports 5 and 6 hold the preserved modulus and unprocessed dividend.
Ports 1--4 are reusable work stacks. 

### `divisionLoopProgram`

 Four control instructions followed by the fixed reduction-step table.
The step table's halt becomes a jump back to the input loop. 

### `reduceFrom`

 The mathematical fold executed by the loop on its MSB-first input stack. 

### `remainderProgram`

 One fixed finite program computing binary remainder. 
