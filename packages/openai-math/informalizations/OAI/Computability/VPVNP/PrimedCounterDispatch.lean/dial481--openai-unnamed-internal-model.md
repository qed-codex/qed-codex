---
{
  "module": "OAI/Computability/VPVNP/PrimedCounterDispatch.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PrimedCounterDispatch.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PrimedCounterDispatch.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The common dispatch on every item of a primed pair

An absolute cursor selects one assembly, clear, initialization, node, or
comparison routine. The prefix installs the required local operands and the
call successor and total. Every selected routine preserves the latter two
registers until the machine's exit instruction.


### `branch`

 Routine selected by an absolute schedule item. 

### `prepared`

 Register file at the entry of the selected routine. 

### `overhead`

 Exact number of ticks before entry to the selected routine. 

### `body_pref`

 The prefix passes the decoded operands to the selected branch, with no
choice bits or external probes consumed before that branch starts. 

### `prepared_controls`

 The final comparison uses the next absolute cursor and the full call count. 

### `prepared_input`

 Input dispatch leaves every assembly register at its incoming value. 

### `branch_controls`

 Executing any selected routine leaves the two exit registers alone. 
