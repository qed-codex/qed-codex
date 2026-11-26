---
{
  "module": "OAI/Computability/VPVNP/LiveEvaluatorAdviceTag.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveEvaluatorAdviceTag.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveEvaluatorAdviceTag.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The stage tag and the evaluator's advice banks

The linked program keeps its stage tag below the advice sources, destination
arrays and operand frames. Updating the tag therefore commutes with every
packed row write and with publication of the four operand frames.


### `packSource_write_tag`

 A packer's source array agrees before and after a lower tag write. 

### `packMemory_write_tag`

 Any prefix of a packing sweep commutes with a write below its destination bank. 

### `published_write_tag`

 The frame builder reads the same validated length and writes the same
operand words, leaving the independent stage tag at the supplied value. 
