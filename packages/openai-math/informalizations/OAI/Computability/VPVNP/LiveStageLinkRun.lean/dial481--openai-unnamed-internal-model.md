---
{
  "module": "OAI/Computability/VPVNP/LiveStageLinkRun.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveStageLinkRun.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveStageLinkRun.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Executing a linked native stage

The dispatcher adds one external read per call. Within the selected component,
registers, private memory, the persistent word and all branches have their
ordinary meanings. Transferring an accepting exit adds one external write.


### `withExtras`

 Append the linker's address, tag, and temporary register values to the component registers. 

### `embedConfig`

 Embed an arbitrary component configuration at its own relocated program counter. 

### `transferEvents`

 Overhead at an accepting exit that transfers to another stage. 

### `exitReport`

 On an accepting exit with a successor, append the stage transfer events and return cursor
zero. In other cases retain the component report. 

### `boundedExit`

 An exact native report includes one final dispatch in addition to its events. 

### `execute_body`

 Exact finite-fuel semantics of a relocated component. In particular no
additional successful paths are admitted by increasing the caller's fuel. 

### `dispatchEvents`

 The dispatch instructions before the first opcode of the chosen component. 

### `prependLog`

 Prepend dispatch events to a component report, retaining its result. 

### `execute_linked`

 Native call semantics, with the tag read, every comparison tick and the
optional transition write displayed. `fuel` is the number of dispatches left
for the component and its optional handoff. 

### `execute_invalid`

 An out-of-range stage tag rejects for every bit string and every instruction cap. 
