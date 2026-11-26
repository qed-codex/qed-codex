---
{
  "module": "OAI/Computability/VPVNP/RAMValidatorPaths.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMValidatorPaths.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMValidatorPaths.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Private binary multiplicity of the executable site validator

A successful site's raw choice string is exactly the concatenation of its
branch bits and its guessed words. Hence one genuine computation path
contributes once to the sum over shared bits of the product of local counts.


### `Machine.IncidentPaths`

 An accepting binary branch path for a fixed local input. 

### `Machine.incidentPathEquiv`

 Reading and emitting the successful report is inverse to choosing its
specified bits. Distinct original binary branches remain distinct even when
their continuations coincide. 

### `Machine.parsimoniousIncidentPaths`

 Native capped path count expressed using the actual site machines and
their own private choice strings. 
