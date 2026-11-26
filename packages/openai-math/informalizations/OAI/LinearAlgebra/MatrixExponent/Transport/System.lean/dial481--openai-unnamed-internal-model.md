---
{
  "module": "OAI/LinearAlgebra/MatrixExponent/Transport/System.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Transport/System.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Transport/System.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Local realization of a permutation

An input-dependent controller reads a permutation and an outer
selector. At each site it chooses a local kernel and a configuration
of the incident core slots. Every enabled slot names its opposite end.
A kernel also receives the incoming and outgoing exterior records.


### `Command`

 Enable flag, orientation bit, remote site and remote slot. 

### `LocalProtocol`

 Uniform bound on transported width; all control and local kernel
costs may depend on the chosen height ratio. 
