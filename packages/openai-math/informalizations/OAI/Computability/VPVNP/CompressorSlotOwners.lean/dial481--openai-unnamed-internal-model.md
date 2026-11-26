---
{
  "module": "OAI/Computability/VPVNP/CompressorSlotOwners.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorSlotOwners.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorSlotOwners.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Computing endpoint owners in absolute field order

A genuine candidate has an edge type, an original base arc, a subdivision index,
an absolute source lane, and an endpoint side. The scan reads one selected role
from the layout table and follows it to the packed site in the original arc
record. Each missing candidate receives its own auxiliary owner. A separate
scan handles the contiguous dummy fields and uses the cyclic next-site table.


### `genuine`

 Public words are the number of lanes, sum of subdivision counts, number of old
base arcs, starts of the old arc records, role table and subdivision table,
number of real endpoint owners, and start of the output. 

### `Digits`

 The decoded side, role edge type, subdivision, and absolute old arc used to classify one
genuine candidate field. 

### `Digits.side`

 Endpoint bit of the candidate field, zero for the outgoing side and one for the incoming
  side. 

### `Digits.edgeType`

 Index of the role edge type used to select the endpoint roles and subdivision limit. 

### `Digits.subdivision`

 Candidate subdivision index to compare with the selected edge type's subdivision count. 

### `Digits.oldArc`

 Absolute old arc index, with the residual lane as its least significant digit. 

### `digits`

 The original arc keeps its lane as its least significant digit, even though
the subdivision digit lies between the old base arc and lane in the candidate ID. 

### `roleAddress`

 Address of the role selector for the candidate's edge type and endpoint side. 

### `oldAddress`

 Start of the candidate's four-word old arc record, containing the role sites and CD flag. 

### `subdivAddress`

 Address of the subdivision count for the candidate's role edge type. 

### `genuineOwner`

 Word written for a genuine candidate, including candidates that decode to holes. 

### `genuineEvents`

 Trace of one genuine candidate visit, reading its role selector, site, CD flag, and
subdivision count before writing its owner. 

### `genuine_native`

 Four table reads and one write compute the next genuine field. 

### `dummy`

 Dummy public words are the padding degree, cyclic next-site table start, and
start of the dummy output interval. Each dummy pass starts its cursor at zero. 

### `dummySource`

 Recover the padding arc's source site from its field cursor by removing the side and
dummy-slot digits. 

### `dummyOwner`

 Encode the source site and outgoing side for a dummy source field or the cyclic successor
and incoming side for its target field. 

### `dummyEvents`

 Trace of one dummy field visit, reading the source site's cyclic successor and writing the
selected endpoint owner. 

### `dummy_native`

 One next-site read and one write compute the dummy field. 

### `natDigits`

 Natural-number decoding in the same mixed radices as the genuine arc address. 

### `GenuineInput`

 Input words and lookup addresses used by one genuine field. The old record
has three packed sites and a CD indicator. The role lookup always chooses one
of the three site fields, even on a candidate that ultimately becomes a hole. 

### `natGenuineOwner`

 Numeric owner prior to conversion to a RAM word. The hole owner is unique
to the absolute field and starts just beyond the real endpoint owners. 

### `genuineOwner_eq`

 With fitting addresses the native word implements the numerical decoder,
including both reasons a genuine candidate can be absent. 

### `natDummyOwner`

 The dummy source is recovered by stripping the side and padding-copy
digits. The incoming field reads the next site in the cyclic tag order. 
