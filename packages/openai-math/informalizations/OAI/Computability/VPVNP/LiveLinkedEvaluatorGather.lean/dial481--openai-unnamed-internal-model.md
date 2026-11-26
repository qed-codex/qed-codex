---
{
  "module": "OAI/Computability/VPVNP/LiveLinkedEvaluatorGather.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveLinkedEvaluatorGather.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveLinkedEvaluatorGather.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The two evaluator configuration gathers in the complete live group

On a noninitial tail group the incoming gather hands off to the last-group
router. On a nonfinal group the outgoing gather hands off to the evaluator
transition. In each case the source is the actual bit scratch region and
the continuation receives the packed word bank and the new stage tag.


### `stage`

 The two actual rows of the outer table which gather cut configurations. 

### `destination`

 The stage reached after a configuration gather, the last-group router for incoming data or
transition checking for outgoing data. 

### `operands`

 The live configuration-gather operands selecting the left or right cut source and the
corresponding old or new state bank. 

### `reports`

 The native word reports for gathering a serialized configuration, in destination-word
order. 

### `Fit`

 Conditions on the four physically computed operands and their memory
regions. A separate destination region preserves all unread source bits. 

### `handoff`

 Remove the entire deterministic gather prefix from an accepting outer
path. Its retained log includes all native reads and writes and all dispatch
and transfer costs, and the tail starts in the actual post-gather memory. 

### `linked_cost`

 Number of reports, native probes, and the unique final transfer all
contribute to the resource accounting of this gather in the outer table. 
