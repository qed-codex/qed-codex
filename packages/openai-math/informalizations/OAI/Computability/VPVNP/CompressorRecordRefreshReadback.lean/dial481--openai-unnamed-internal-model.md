---
{
  "module": "OAI/Computability/VPVNP/CompressorRecordRefreshReadback.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRecordRefreshReadback.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRecordRefreshReadback.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Reading the port-local coefficient from a constructed refresh

At the local port, both segment lookups use the same site/port index. The incoming table
already contains the source ordering's offset. Reading the two independent half-words at
these stored intervals supplies the diagonal tests and all external halves of the two
ordered families of ties. The dense demand and selected payload rows determine the
arguments of the scalar-index map for the actual kernel.


### `interval`

 Numerical width and offset of one incident external segment. The direction is local
to the port, so the incoming read needs no inverse translation. 

### `interval_spec`

 The width and offset in each physical half of the table describe the corresponding
source-ordered segment of the incident external word. 

### `bit`

 Read one bit using the stored length and offset. Empty segments have no readable bits. 

### `segments`

 The two lists of segment words produced from physical endpoint records. 

### `segments_eq`

 Physical offsets and widths recover the same bit lists as the exact kernel for
arbitrary independently chosen incoming and outgoing payloads. 

### `payload`

 Read the selected payload vector without any search through a finite enumeration. 

### `indices`

 Port-local scalar indices using the constructed records for segment reads, demand
widths and the admitted supply profile. The ordinary incident half-wires remain inputs. 

### `indices_eq`

 The labels obtained from the physical records are exactly the common parameter
indices of the port kernel, including the failure cases of its diagonal and selector tests. 
