---
{
  "module": "OAI/Computability/VPVNP/RAMTapeCoefficient.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeCoefficient.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeCoefficient.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Fixed bit-stack processors as literal coefficients of the integer family

The original raw input is already the contents of stack zero. The blank tail
of that tape supplies the separators of every unused stack. Consequently the
table reads its own prefix in exactly the same way as any subsequent bit.


### `program`

 The concrete universal-machine program that simulates the indexed stack code. 

### `inputStacks`

 Put the input word on the first stack and initialize the others to empty. 

### `prefix_count`

 The same prefix serves every length and every payload that fits the
clock. All branch counts include the literal table's prefix in the input. 

### `site_count`

 The processor receives exactly its local fields and the shared prefix
under the length-`n` site encoding used by the contraction. 
