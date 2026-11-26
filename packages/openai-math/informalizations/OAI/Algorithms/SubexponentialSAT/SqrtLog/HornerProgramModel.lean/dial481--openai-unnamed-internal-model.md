---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/HornerProgramModel.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/HornerProgramModel.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/HornerProgramModel.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Native Horner evaluation in the actual arbitrary-degree unramified
RingModel. The instruction table is independent of precision, extension
degree and polynomial length. Ring caches are explicit runtime inputs. 

### `modelCommand`

 Actual fixed Horner command, using native arbitrary-degree arithmetic. 

### `modelCommand_run`

 All arithmetic service hypotheses are discharged by the actual native
programs. Remaining assumptions describe supplied bytes and clean scratch. 

### `modelMachine_correct`

 A single fixed finite BitProgram evaluates the represented polynomial in
its actual RingModel. The output witness is produced by the executable fold. 

### `modelBudget_polynomial`

 Concrete polynomial native-step bound, before the fixed primitive-machine
simulation constant. 

### `prepared_zero_canonical`

 A standard constructed zero cache meets the only extra canonicality
condition required by the vector-contraction implementation. 
