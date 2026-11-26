---
{
  "module": "OAI/Computability/VPVNP/RAMTapeVirtualSite.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeVirtualSite.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeVirtualSite.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Full-word inputs to the auxiliary site verifier

Section 12 places the auxiliary verifier at a cursor-zero vertex. Its header
may contain a full histogram word. Its site-address width, machine-word
width and private clock are independent public parameters of the virtual
network.


### `Input`

 Full-word virtual site input, including its independent clock and incident sends. 

### `Input.fuel`

 Private instruction limit for each call of the auxiliary RAM. 

### `Input.v`

 Address of the virtual site. 

### `Input.initialWord`

 Initial persistent state of the auxiliary machine. 

### `Input.headerWord`

 Auxiliary memory word initially stored at this address. 

### `Input.sends`

 All shared successor and sorting messages on the virtual RAM network. 

### `Input.summary`

 Reconstructed incoming and outgoing cuts for the virtual site. 

### `Input.valid`

 Validity of the site's transmitted and received successor messages. 

### `Input.sideWord`

 Word encoding the cumulative cost of the chosen boundary cut. 

### `Input.addrWord`

 Zero-extended virtual site address in the auxiliary word format. 

### `Input.bare`

 Full interpreter snapshot before it emits the initialization record. 
