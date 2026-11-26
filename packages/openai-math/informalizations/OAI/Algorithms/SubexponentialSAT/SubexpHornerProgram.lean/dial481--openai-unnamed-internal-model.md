---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SubexpHornerProgram.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpHornerProgram.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpHornerProgram.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Fixed-control source generation for factored Horner expressions

Input payloads are coefficient representations, never precomputed instruction
streams. The emitter writes the actual serialized postfix tags and frames.


### `program`

 Ports: payload 0, reverse output 1, empty scratch 2. 

### `trace`

 Copy a raw literal payload, frame it, and emit its push opcode. The
payload is restored exactly and the scratch port is again empty. 
