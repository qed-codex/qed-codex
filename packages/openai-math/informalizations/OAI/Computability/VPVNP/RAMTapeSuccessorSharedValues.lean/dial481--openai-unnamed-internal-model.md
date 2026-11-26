---
{
  "module": "OAI/Computability/VPVNP/RAMTapeSuccessorSharedValues.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeSuccessorSharedValues.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeSuccessorSharedValues.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Successor registers on the shared bits of a RAM transcript

Each interior edge has one send array. The receiving site reads those same
bits at its incoming port. The two endpoints instead read an all-zero field.
Under the local canonicality checks, the physical registers therefore hold
the typed messages parsed from the adjacent send arrays.


### `sharedField`

 Read the outgoing or incoming successor field at a site's incident offset from the shared
send arrays. 

### `sentMessage`

 Return the parsed outgoing message on an interior send edge, or no message at the last
site. 

### `receivedMessage`

 Return the preceding site's parsed send message on an interior receive edge, or no message
at the first site. 

### `sharedFinish`

 The physical reader's final stacks on the full incident vector. Its
remaining input starts at the first sorting field. 
