---
{
  "module": "OAI/Computability/VPVNP/TallyPrograms.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/TallyPrograms.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/TallyPrograms.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Composing the fixed tally programs for the input widths

A program packages its finite control, tally update, exact instruction count and scratch
precondition. Sequential composition checks the second precondition on the first output and
counts both runs. The transition code consists of the previously verified stack routines.


### `Program`

 A finite-control routine on unary registers together with its register update, exact
instruction count, and a proof that it realizes both on ready inputs. 

### `Program.Q`

 The finite type of local control labels of the tally routine. 

### `Program.code`

 The executable stack routine implementing the tally register update. 

### `Program.eval`

 The final natural-number register state specified for each initial tally state. 

### `Program.work`

 The exact number of stack instructions used by the tally routine on a ready input. 

### `Program.ready`

 The precondition on the initial tally registers under which the specified update and
  instruction count hold. 

### `seq`

 Link the two finite controls at the normal-return boundary. 

### `copy`

 Add a preserved source to the destination. 

### `mul`

 Add the product of the two preserved sources to the destination. 

### `triangle`

 Add the triangular number `1 + … + s src` to the destination. 
