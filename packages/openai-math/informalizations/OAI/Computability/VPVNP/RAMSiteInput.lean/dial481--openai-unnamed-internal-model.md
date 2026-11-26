---
{
  "module": "OAI/Computability/VPVNP/RAMSiteInput.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMSiteInput.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMSiteInput.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Input string of a live or primed site

Section 9.2 uses a literal self-delimiting program prefix, the site's address,
four header bits, its incident communication bits, and zeros. The full string
is an input to the coefficient machine. The prescribed header word and address
are recovered from exactly the fields that appear on its input tape.


### `Header`

 Four header bits for a site, in the order group index, advice, incoming cut, and outgoing
cut. 

### `header`

 The four header bits are group index, advice, incoming cut, outgoing cut. 

### `headerWord`

 The low four bits of the site's initialized word hold its header. 

### `payload`

 Address, literal index/advice and cut bits, and incident communication fields. 

### `Fits`

 The self-delimiting program prefix, site address, four header bits, and all incident
communication bits fit within the input length. 

### `tape`

 Construct the site’s literal input by concatenating the program prefix, address, header,
and incident bits, then filling the available suffix with zeros. 

### `encode`

 Index the fitted site input tape by its n positions to obtain a Boolean coefficient input. 

### `decode`

 The first field really is the self-delimiting prefix accepted by the
universal coefficient machine, independently of all other sites' choices. 

### `drop_prefix`

 The exact suffix after the literal prefix, including zero padding. 

### `payload_address`

 Every designated address, header, and communication bit can be read
directly at its own offset. 
