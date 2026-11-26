---
{
  "module": "OAI/Computability/VPVNP/CompressorRecordsBundleRAM.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRecordsBundleRAM.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRecordsBundleRAM.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Native classification of old segments in a shrinking pass

For each old outgoing port, the worker follows the actual incidence once and
reads the shrinking placement at both endpoints. It emits a bundle identifier
and a key for the segment's order within that bundle. Thick-to-thick wires use
the source owner and old outgoing slot. The other wires use the thin endpoint's
assigned bundle. The old width column is already indexed by this same port.


### `Ops`

 Straight-line RAM operations for the old-port classifier, with 24 registers and 11 public
operands. 

### `readColumn`

 Read one external cell at a public column base plus a register offset. 

### `classify`

 Registers 14 through 18 decode the source tag, port label, mask and
base. Registers 19 and 21 collect the thick-to-thick values, and 20 and
22 collect the selected bucket and key. 

### `visit`

 Public words are the degree, residual radix, tag radix, mask radix,
number of external bundles, actual outgoing column, thickness, owner and
assigned columns, and the output bucket and key columns. 

### `Digits`

 The mixed-radix source fields recovered from an old outgoing-port number to compute its
bundle and sorting key. 

### `Digits.base`

 The original base-site index remaining after the lane fields have been divided out. 

### `Digits.tag`

 The source tag digit extracted after discarding the residual lane coordinate. 

### `Digits.slot`

 The outgoing port's slot within the old site. 

### `Digits.mask`

 The source mask digit used in both the thick-wire and CD sort keys. 

### `Digits.label`

 The source slot-label digit, the least significant field of the within-bundle sorting
  key. 

### `decode`

 Recover the source base, tag, outgoing slot, mask, and slot label from a linear old-port
index and the public radices. 

### `sourceSite`

 Remove the outgoing-slot digit to obtain the source site of the current old port. 

### `targetSite`

 Follow the current port's actual incidence and remove its incoming-slot digit to obtain the
target site. 

### `readAddress`

 The destination depends on the first probe. Remaining addresses depend
only on that destination, the persistent index and the public radices. 

### `readValue`

 Read one of the six classification inputs for the old port, including incidence and
endpoint placement data. 

### `bucket`

 Choose the thick source-port bucket when both endpoints are thick, or the assigned thin
endpoint's CD bucket otherwise. 

### `key`

 Encode the old port's sort key, using mask and label for thick wires and the normalized
source fields for CD motifs. 

### `update`

 Write the classified bucket and sort key into separate columns indexed by the old outgoing
port. 

### `events`

 The classifier visit's six input reads, local calculation ticks, and writes of the bucket
and key at the old port index. 

### `visit_native`

 The actual interpreter returns the next source port and the six reads
followed by two writes, with fresh private registers on every call. 
