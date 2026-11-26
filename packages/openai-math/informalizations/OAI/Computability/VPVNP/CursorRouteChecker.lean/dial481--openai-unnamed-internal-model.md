---
{
  "module": "OAI/Computability/VPVNP/CursorRouteChecker.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CursorRouteChecker.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CursorRouteChecker.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Reading the routing constraints at one cursor vertex

At most two bit tests per field bit check all the routing constraints of
Section 12. Each test uses the vertex's own outgoing and incoming ports.
A transit comparison probes two bits. A zero check probes one. The program
retains the inactive-successor zero checks at cursor zero.


### `LocalPort`

 The four incident arc slots of a cursor vertex. 

### `LocalAddress`

 A bit address consists of a local port, a mask-system field, and a bit
within that field. 

### `LocalAddress.port`

 Incoming or outgoing arc slot at which the routing checker reads the bit. 

### `LocalAddress.system`

 Mask system identifying the RAM field to be read from that port. 

### `LocalAddress.bit`

 Bit position within the field of the selected RAM system. 

### `BitTest`

 Primitive routing comparisons, with explicit operands. 

### `BitTest.run`

 Evaluate a routing test by skipping it, testing a bit for zero, or comparing two addressed
bits. 

### `BitTest.probes`

 Exact number of bit probes needed for one test. 

### `systemList`

 The sort fields are enumerated by their triangular layer ordinals. 

### `payloadTest`

 The second test at a given bit. 

### `bitTests`

 First zero the unused outgoing field. Then check the site's transit or
inactive-successor constraint at this bit. 

### `routeTests`

 All the local bit tests in contiguous mask-system and bit order. 

### `routeAccept`

 Run the Boolean checker using a reader for the four local ports. 

### `readHalf`

 A reader for independently supplied half-wire indices at a position. 

### `routeAccept_readHalf`

 On all half-wire inputs the local bit program checks precisely the route
conditions and, at cursor zero, the inactive successor fields. 

### `routeTests_length`

 Two instructions per payload bit are enough, even for independently
supplied half-wire assignments that fail one of the comparisons. 

### `routeTests_probes_le`

 Worst-case probes of the test list. Its first instruction per bit is
always a single zero read. Its second instruction reads at most two bits. 
