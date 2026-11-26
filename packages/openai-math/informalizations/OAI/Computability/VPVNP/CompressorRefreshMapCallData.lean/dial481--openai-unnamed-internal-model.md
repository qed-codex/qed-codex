---
{
  "module": "OAI/Computability/VPVNP/CompressorRefreshMapCallData.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRefreshMapCallData.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRefreshMapCallData.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Physical input of the selected refresh map call

The private descriptor and the old and new node frames supply the map's register setup.
Demand reads use their two independent halves. The agreement scan reads each full
supply, including its selector suffix. The private directory follows the complete input
interval, so the directory initializer preserves those data cells.


### `NodeFields.transfer`

 Writes outside a packed node's interval preserve all independent half-wire bits
in its argument bank. 

### `resident`

 The raw data of the selected refresh, before the writer publishes the private
descriptor. Every live cell precedes both the directory and the descriptor. 

### `resident_packed`

 Specialize the resident data contract to the packed workspace. The ordering of
its scratch and operand regions supplies all bit/descriptor and bit/directory separation. 

### `input`

 If the descriptor has already been written, resident fields at the same config
give the ordinary initializer input directly. 
