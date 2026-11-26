---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SubexpArgumentProgram.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpArgumentProgram.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpArgumentProgram.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Finite-control serialization of marked-incidence arguments

The raw-list ABI is `Encoding.encodeList id` of record bodies
`frame key ++ frame coefficient`. Coefficient payloads are opaque bit strings.
The term writer consumes one coefficient frame and a reversed key, restoring
its scratch stacks. All loops below execute fixed Boolean/stack instructions.


### `writer`

 The existing postfix literal encoder, relocated to the key/body buffers. 

### `emitTerm`

 Build one inner record, reverse it once, and frame it as a list item.
Stacks: 0 coefficient input; 1 reversed key; 2 preserved; 3 raw-list output;
4 copy scratch; 5 inner-record scratch. Both scratch stacks start empty. 
