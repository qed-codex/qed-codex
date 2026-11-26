---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SubexpIncidenceGuardProgram.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpIncidenceGuardProgram.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpIncidenceGuardProgram.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# A source-preserving incidence-degree parameter program

Local stacks 0 and 1 hold binary `u` and `B`; stack 2 receives `1 + u * B`.
Stacks 3 and 4 hold a physically loaded one and a product, then are cleared.
The five arithmetic work stacks are 5 through 9. All instructions and port maps
are fixed independently of the input words.


### `Ready`

 The source words are arbitrary, including leading zeroes. 

### `command_eval`

 An actual execution with exact numeric output, source preservation,
cleared work storage, a linear word bound, and quadratic instruction cost. 

### `output_pos`

 The returned natural number is positive, as needed by the field helper. 
