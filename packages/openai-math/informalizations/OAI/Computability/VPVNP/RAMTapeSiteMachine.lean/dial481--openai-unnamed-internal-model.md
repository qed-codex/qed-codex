---
{
  "module": "OAI/Computability/VPVNP/RAMTapeSiteMachine.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeSiteMachine.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeSiteMachine.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Compiling the site's counted stack program into a literal two-tape table

The public reader is run once before the shared guard and private choice
tree. Only the bank produced by that deterministic startup enters the
counted computation. The literal table may be supplied as its own input
prefix, since the instruction table is fixed before that input is formed.


### `linked`

 Sequence deterministic public startup with the site’s guarded, choice-counted verifier. 

### `inputPort`

 Processor port initially containing the raw site input for two-tape compilation. 

### `table`

 Compile the linked startup and site verifier to a literal two-tape program with the raw
input at its designated port. 
