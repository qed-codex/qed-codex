---
{
  "module": "OAI/Computability/VPVNP/LiveLinkedEvaluatorSentinel.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveLinkedEvaluatorSentinel.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveLinkedEvaluatorSentinel.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Native control-word writes at evaluator endpoints

The first group writes its initial state and the last group writes the accepting
state. Both single-call stages have a unique empty choice string. They enter the
next row of the actual live program with an updated control word and stage tag.


### `stage`

 Select the initial-state or final-state control writer for the corresponding endpoint. 

### `destination`

 The successor of the endpoint writer, accounting for a halted initial evaluator and for
prefix preparation on a running one. 

### `tag`

 The evaluator control word to install, accepting at the final endpoint or giving the
program's initial control state. 

### `operands`

 The public control-write operands selecting the old state bank at the start or the new
state bank at the end. 

### `report`

 The terminating source report that writes the endpoint control word after two local steps. 

### `put`

 Store the endpoint control tag at the selected state bank's control-word address. 

### `transferred`

 The endpoint-writer memory after the enclosing linker also writes the destination stage
tag. 

### `handoff`

 Every accepted continuation has a unique preimage after the initial or
final control write, with its complete linked report added to the cap. 

### `final_image`

 After the tag transfer the final bank still stores precisely the accepting
configuration, including all zero tape cells. 
