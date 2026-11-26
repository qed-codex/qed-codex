---
{
  "module": "OAI/Algorithms/SubexponentialSAT/RankAssignmentProgram.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/RankAssignmentProgram.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/RankAssignmentProgram.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Preserving conversion of a binary rank to a fixed-width assignment

Copy the binary rank and the unary shape, then call the existing padding
program. The master rank and shape stay available for enumeration and repeated
evaluation. All lengths remain Boolean-stack data.


### `paddingPorts`

 The padding routine's shape, input, and output use three work stacks. 

### `command`

 Ports 0 and 1 are preserved masters; port 2 becomes the working assignment;
ports 3, 4, and 5 are scratch. 

### `program`

 Twenty-six labels, independently of rank length and declared width. 

### `output_frame`

 The rank, shape, and all scratch stacks are unchanged in the final state. 
