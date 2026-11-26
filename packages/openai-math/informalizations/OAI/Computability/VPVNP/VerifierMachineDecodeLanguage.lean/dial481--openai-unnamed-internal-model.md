---
{
  "module": "OAI/Computability/VPVNP/VerifierMachineDecodeLanguage.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/VerifierMachineDecodeLanguage.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/VerifierMachineDecodeLanguage.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# A dynamic program for reading the table

Fix the declared table length and the number of running states. After reading each row,
the parser marks the offsets at which the first rows could have ended. A requested slot
constrains just the indexed row. After the prescribed number of rows the marks stay fixed.


### `header`

 Bits preceding the rows of a nonempty table, or the length field for an empty one. 

### `Reach`

 Position reached by the first `min t (9*extra)` rows, when their bits agree with the input. 
