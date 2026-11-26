---
{
  "module": "OAI/Computability/VPVNP/PrimedInputRAMRows.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PrimedInputRAMRows.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PrimedInputRAMRows.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Full coefficient-machine inputs of the two primed groups

Resolving the rectangular scratch or header reference at each bit position
reproduces the exact tape in Section 9.2. The equality is for all shared bit
assignments. The raw sort and successor messages are never parsed here.


### `padding`

 Number of trailing zero bits after the program prefix, site address, four header bits and
incident ports in a length-`n` input row. 

### `RowField`

 Positions in a complete primed input row, including the actual program prefix and the
trailing padding for length `n`. 

### `rowIndex`

 Identify the typed fields of a fitting primed input row with their bit positions in the
length-`n` tape. 

### `incident`

 The untested incident bits of a primed group are precisely its assigned
sending bits, copied to their matching ports and clamped at missing ports. 

### `siteHeader`

 The four one-bit header fields as they appear on a primed tape. 

### `input`

 Full `n`-bit input whose ordered parses occur in (9.4). 

### `input_at`

 Every position enumerated by the counter agrees with the universal
machine's actual input, including the literal self-delimiting prefix and all
trailing padding. 
