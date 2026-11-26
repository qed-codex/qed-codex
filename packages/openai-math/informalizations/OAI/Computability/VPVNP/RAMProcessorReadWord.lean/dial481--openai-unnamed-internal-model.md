---
{
  "module": "OAI/Computability/VPVNP/RAMProcessorReadWord.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMProcessorReadWord.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMProcessorReadWord.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Taking one external read guess on bit stacks

The template word determines the number of bits to take from the private
choice stream. The reader restores that template and writes the guessed word
in its original order. Exhausting the stream early reaches a rejecting row.


### `Port`

 Stacks holding the width template, choice stream, output value, saved template bits and
collected guess bits of the read-guess routine. 

### `State`

 Control states for clearing an old value, pairing each template bit with a guessed bit,
restoring the template and emitting the guessed word. 

### `code`

 Stack instruction table that consumes one choice per template bit, restores the template
and writes the guess in its original order. A short choice stream reaches the rejecting
row. 

### `bank`

 Place the template word, choice stream, current value and the two partially collected bit
lists on their respective reader ports. 
