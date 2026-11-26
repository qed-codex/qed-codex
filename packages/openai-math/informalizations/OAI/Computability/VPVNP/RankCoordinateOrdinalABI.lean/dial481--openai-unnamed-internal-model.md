---
{
  "module": "OAI/Computability/VPVNP/RankCoordinateOrdinalABI.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RankCoordinateOrdinalABI.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RankCoordinateOrdinalABI.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Returning an original greedy index as a binary word

The caller supplies the dense ordinal on a dedicated port. The fixed adapter
stages it in the five-register prefix scanner, copies out the successful cursor,
and restores the zero-word templates in its scratch registers before returning.


### `Aux`

 The prefix-rank registers and underlying scan workspace mounted inside the ordinal reader. 

### `Host`

 The ordinal reader's public input and output together with its private prefix-scan bank. 

### `machine`

 Copy the requested ordinal into register two, run the supplied prefix scanner, copy its
selected index from register zero to the result, and reset the four mutable prefix
registers. 

### `idle`

 Initial prefix-register values for an idle ordinal reader, retaining its underlying
auxiliary stacks. 

### `overhead`

 Time outside the prefix scanner, including all initialization and reclamation. 

### `correctSpace`

 The fixed five-register scanner supplies a true scalar-index callback,
including its unchanged input and a reusable ready workspace. 
