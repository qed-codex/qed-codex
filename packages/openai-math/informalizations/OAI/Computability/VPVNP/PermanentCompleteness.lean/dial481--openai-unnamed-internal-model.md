---
{
  "module": "OAI/Computability/VPVNP/PermanentCompleteness.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PermanentCompleteness.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PermanentCompleteness.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Valiant's completeness theorem for the generic permanent

Ryser's formula supplies the Boolean-sum verifier over every field. The
permanent reduction uses the inverse of two for its occurrence gadgets.


### `permanent_isVNP`

 The generic permanent belongs to VNP over every field. Numbering its matrix
entries in row-major order gives the family computed by the Ryser verifier. 

### `permanent_vnpComplete`

 Over every field of characteristic different from two, the generic permanent
belongs to VNP and every VNP family is a p-projection of it. 
