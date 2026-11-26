---
{
  "module": "OAI/Computability/VPVNP/RAMTapeLiveProcessor.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeLiveProcessor.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeLiveProcessor.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# A literal universal coefficient for the live RAM transcript

Given a fixed private instruction table and its finite list of public operand
formulas, compile the actual raw-input processor into a two-tape program.
At every sufficiently large fitted length, each site's coefficient is the
exact cardinal of its private incident paths. The program reads its own
literal prefix to obtain operands that refer to that prefix.


### `machine`

 Literal two-tape program combining the fixed private template with the startup that
evaluates its operands from the physical site and the program’s own prefix. 

### `CountsAt`

 All group headers and compatible incident words at one live geometry. 

### `eventually_machine_count`

 At the live exponent the explicit physical clock and the literal-prefix
fit are simultaneous for every site, header and shared-bit assignment. 
