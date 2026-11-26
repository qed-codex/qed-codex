---
{
  "module": "OAI/Computability/VPVNP/SliceArithmeticStreamBank.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/SliceArithmeticStreamBank.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/SliceArithmeticStreamBank.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Arithmetic registers and stream ports for the finite Horner control 

### `StreamPort`

 The caller supplies its own disjoint ports for the loop markers and saved inputs. 

### `Port`

 Eight-register arithmetic bank and coefficient-stream ports used by a Horner row, including
the caller's ports of type `X`. 

### `state`

 The finite arithmetic register bank and the caller's stream stacks. 
