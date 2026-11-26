---
{
  "module": "OAI/Computability/VPVNP/LiveProgramUnit.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveProgramUnit.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveProgramUnit.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The live unit branch after header verification

Once the physical header has checked both modes and every padding bit, the
unit group has one possible sequence of native bursts. The last burst costs
three units, including the outer tag read and the checked mode read.


### `report`

 Terminating report of the unit-mode router after header verification, with one outer tag
read and one mode read. 

### `run`

 The conclusion records every native report, as well as the entire
choice stream. It holds at the same clock that executed the header. 

### `accepted_iff`

 Arbitrary valid choice streams in unit mode agree with the unique forced
trace, even if the cap examines every report rather than just the total cost. 

### `card_one`

 A valid unit group contributes the integer one at every permitted clock
and resource cap covering its verified trace. 
