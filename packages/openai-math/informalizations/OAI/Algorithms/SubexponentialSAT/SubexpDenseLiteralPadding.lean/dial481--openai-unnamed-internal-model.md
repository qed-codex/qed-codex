---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SubexpDenseLiteralPadding.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpDenseLiteralPadding.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpDenseLiteralPadding.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Padding arbitrary literal payloads for the dense interpreter

The existing five-label padding table already truncates long inputs. This
module proves that behavior without a length precondition, then connects the
table to the actual framed operand stack. The cached dense zero array supplies
the requested bit width; no dimension is baked into the program control.


### `command_run`

 The complete actual loader replaces the top literal with exactly the
cached width, preserving every other stack and restoring all work buffers. 

### `program_runsIn`

 A fixed byte loader for arbitrary raw literal payloads, including short
constants and X. Its terminal registers and work buffers are all restored. 
