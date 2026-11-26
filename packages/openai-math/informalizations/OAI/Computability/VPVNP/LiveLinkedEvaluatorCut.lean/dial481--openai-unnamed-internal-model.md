---
{
  "module": "OAI/Computability/VPVNP/LiveLinkedEvaluatorCut.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveLinkedEvaluatorCut.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveLinkedEvaluatorCut.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The two ordinary incident cuts of an evaluator tail group

The physical header contains the configuration bits in its left or right
bank. The mode guard and padding guard check the other two fields of exactly
the cut used by the chain contraction. Hence gathering this bank feeds the
same configuration decoder as the semantic boundary, including malformed
word encodings.


### `tail_incoming`

 Incoming configuration after the first evaluator group. The midpoint
itself supplies the explicitly initialized input. 

### `tail_outgoing`

 Outgoing configuration before the last evaluator group. The terminal
endpoint uses the explicitly prepared accepting sentinel. 
