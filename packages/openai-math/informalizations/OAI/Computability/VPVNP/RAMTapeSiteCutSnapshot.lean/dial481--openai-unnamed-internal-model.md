---
{
  "module": "OAI/Computability/VPVNP/RAMTapeSiteCutSnapshot.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeSiteCutSnapshot.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeSiteCutSnapshot.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The site controller snapshot furnished by the physical parser

The incoming and outgoing cost words are read from the two successor fields.
Missing fields take their canonical endpoint values, and halted cuts carry a
zero state word. The other public words come from the computed site address,
bucket size, public call clock and packed header.


### `Input.summary`

 Successor cuts reconstructed from the incident sort messages. 

### `Input.sideWord`

 The cumulative cost word on the selected side of this site. 

### `Input.addrWord`

 The live site address in the RAM's full word format. 

### `Input.headerWord`

 The four physical header bits packed into one RAM word. 

### `Input.asWordSite`

 A four-bit live header supplies the same verifier as the auxiliary full-word
header once it has been packed in its prescribed RAM word. 

### `Input.bare`

 Initial interpreter snapshot for the selected program, operands and private choices. 
