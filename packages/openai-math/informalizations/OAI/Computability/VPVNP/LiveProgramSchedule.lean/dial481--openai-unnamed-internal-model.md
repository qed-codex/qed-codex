---
{
  "module": "OAI/Computability/VPVNP/LiveProgramSchedule.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveProgramSchedule.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveProgramSchedule.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Mode-dependent stage schedules of the native live group

The header emits zero, one or two. The same finite table serves every mode.
The following lists give the complete sequence of stage tags after ordinary
continuing calls within a stage are suppressed. The first tail group uses its
middle-cut exponents, later groups gather an incoming configuration, and the
last group installs the required accepting image instead of gathering an
outgoing configuration.


### `GroupMode`

 The unit, pair, and evaluator-tail modes of the native live group. 

### `GroupMode.flag`

 Encode unit, pair, and tail modes by the header flag ordinals zero, one, and two. 

### `prepareTail`

 The seven stages that prepare a running evaluator's initial tape, from prefix-length
recovery through exponent scattering. 

### `schedule`

 Stage sequence for this group's mode and endpoint flags. A first tail group runs the tape
preparation only when the evaluator has extra states. 

### `destination`

 For a known checked header the three dynamic destinations are read from
exactly the same native router tables used by the complete instruction table. 

### `successor`

 Select the next stage from the mode or endpoint flag at a router and from the program's
ordinary successor map elsewhere. 

### `Follows`

 The full stage list, including the exact terminal stage, follows the
successor function at each position. 

### `stageEquiv`

 Exact decomposition at any ordinary stage of the outer native program.
The source path has its original binary choices. The remaining path starts
with its specified transfer word and tag, retaining the cap on all reports. 
