---
{
  "module": "OAI/Computability/VPVNP/PrimedInputRAMPortCode.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PrimedInputRAMPortCode.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PrimedInputRAMPortCode.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Finite word code for identifying a directed-message sender

This block reads the current site and incident position from registers 23
and 25. Registers 32, 33 and 34 report whether the port is connected and
the site and local offset of the sender. The triangular layer search scans
successive phase sizes using subtraction, so its intermediate counters fit
in a word whenever the ordinal does.


### `Block`

 Structured word code for resolving a message port, with 48 private registers and 16 public
words. 

### `copy`

 Emit one register-copy instruction in the port resolver. 

### `binary`

 Emit one instruction that applies the given binary word operation to two registers. 

### `publicWord`

 Emit one instruction loading a public port-layout word into a private register. 

### `scanStep`

 One iteration removes the next complete triangular row. 

### `scan`

 Register 40 is the residual exchange ordinal, 41 is the current phase.
If the residual is at most the phase, the residual itself is the step. 

### `receiveSort`

 Resolve a sorting receive port by decoding its triangular exchange ordinal, flipping the
partner bit of the site index and subtracting one block from the port offset. 

### `sort`

 Decode the sorting block number from the port offset. An even block uses the sending site,
while an odd block resolves the corresponding receive port to its sender. 

### `successorSend`

 Test whether the site has a successor. Its outgoing port is connected precisely before the
last site. 

### `successorReceive`

 Mark the incoming successor port as disconnected at site zero. At a later site use the
preceding site and its outgoing port offset. 

### `program`

 The instruction table is independent of every word width and loop bound. 

### `result`

 Decode registers 32 through 34 into an optional pair of sender site and local offset. 

### `Input`

 Register contract on entry. The other registers may contain any word. 
