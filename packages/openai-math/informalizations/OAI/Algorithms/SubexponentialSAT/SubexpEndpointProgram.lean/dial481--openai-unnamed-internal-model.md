---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SubexpEndpointProgram.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpEndpointProgram.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpEndpointProgram.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Binary prime-search endpoints by a fixed finite program

The binary input is the exponent itself, including any leading zeroes.  A
counted loop appends one bit per iteration to the endpoint words.  The final
increment is another finite bit program; the powers below occur only in the
correctness specification.


### `state`

 Ports: exponent, controller scratch, lower, start, fuel, upper. 

### `command`

 A fixed instruction table; the exponent remains input data. 

### `Output`

 Exact generated words, including zero exponent and padded input. 

### `lifted_output`

 Call the same fixed program at arbitrary injective ports in a larger store.
Unassigned stacks and registers are preserved by `embedState`'s frame laws. 

### `schedule_endpoints`

 Specialize to the exponent word produced by the actual parameter prefix. 
