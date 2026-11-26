---
{
  "module": "OAI/Computability/VPVNP/CompressorRecordsDemandScan.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRecordsDemandScan.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRecordsDemandScan.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Full scan of selected A, B, D and CD records

The scan follows each old outgoing slot. The first probe finds its opposite site,
and later probes follow its selected C and D positions. Old directory cells remain
readable throughout. Each row is written at its own permuted absolute arc ID.


### `fieldAddr`

 Address and value of one output component. 

### `Roles.field`

 Select a field from a demand record in storage order A, B, D, CD. 

### `inputAddr`

 The address of each of the six reads needed for one demand record, including the three
placement reads at its ordered endpoints. 

### `Regions`

 The output family can occupy any disjoint region of the external workspace. 

### `Written`

 The finished prefix contains precisely the rows for the visited source arcs. 

### `scan_run`

 Sequential native execution with four exact output columns, all unrelated cells
framed, and ten probes per directed old port. 
