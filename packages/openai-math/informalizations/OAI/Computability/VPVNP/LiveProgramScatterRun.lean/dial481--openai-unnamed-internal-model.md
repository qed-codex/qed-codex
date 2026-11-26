---
{
  "module": "OAI/Computability/VPVNP/LiveProgramScatterRun.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveProgramScatterRun.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveProgramScatterRun.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Permuting the exponent bits in the linked evaluator

The scatter writes the exponent payload positions of the initial tape. The incoming
order table bounds each computed destination. Consequently the linked scatter can reload
the five operands of its frame at each call and transfer the stage tag on its final call.


### `Outside`

 Addresses outside the interval containing all reversed, tagged exponent payloads. 

### `reports_outside`

 Replaying any one of the actual call reports on any memory only writes inside the
payload interval. Earlier scatter writes preserve the advised permutation. 

### `operandBase`

 Base word address of the five scatter operands, seventeen words past the advice frame base. 

### `returning_outside`

 Execute the complete framed scatter in the linked group. Its last report hands
control to the last-group router and the tape bank stores the evaluator's initial
configuration with the formal-coordinate exponents. 

### `returning`

 Execution and configuration at the scatter handoff. 
