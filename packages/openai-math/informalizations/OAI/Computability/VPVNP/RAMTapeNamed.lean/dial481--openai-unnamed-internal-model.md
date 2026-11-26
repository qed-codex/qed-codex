---
{
  "module": "OAI/Computability/VPVNP/RAMTapeNamed.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeNamed.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeNamed.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Named stack ports for the literal coefficient machine

Port zero receives the raw input tape. All other labels in the finite bank
are sent to distinct positive ports, so a program can be compiled directly
from its named stack control. Renaming preserves each branch's halting bound
and the integer count of accepting paths.


### `stopsWithin_lift`

 Relabel a finite-control machine with all instructions preserved,
including both targets of each binary choice. 

### `labeledPort`

 The physical compiler uses a spare positive port to avoid subtracting
one from the bank size when moving the designated input to port zero. 

### `labeledCode`

 Relocate the named stack instructions to numerical stack indices. 

### `labeledInput`

 Initialize the designated input stack with the raw input word. 

### `labeledProgram`

 The literal universal-machine program for the named stack machine. 

### `input_count_labeled`

 The fixed two-tape table for a labeled stack program computes its exact
bounded accepting-path count from a raw input. 

### `site_count_labeled`

 At a site, the input on the designated named port contains the fixed
program's own prefix, header, incidence messages, and padding to length n. 
