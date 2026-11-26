---
{
  "module": "OAI/Computability/VPVNP/LiveLinkedEvaluatorFrame.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveLinkedEvaluatorFrame.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveLinkedEvaluatorFrame.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Returning from a framed evaluator stage in the linked program

A native scan supplies its exact reports at fixed operands. If its writes
leave the operand frame and tag intact, the physical program reads the same
operands on every call. Its last call writes the destination stage tag and
returns persistent cursor zero.


### `framedReturning`

 Lift a certified native source run through the physical operand loader
and stage dispatcher, including the transfer tag and the private clock. 
