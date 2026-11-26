---
{
  "module": "OAI/Computability/VPVNP/PairSimulationLeafFront.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationLeafFront.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationLeafFront.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The deterministic front of a physical cursor leaf

The descriptor pointer determines the cursor, site and shadow header. The
setup then reads the cached virtual dimensions and the four fields of the
stored packet. A passed route enters the private validator at cursor zero
and returns at a transit cursor. An inconsistent route rejects in this call.


### `Program`

 Labels and operand allocations for the decoded-address and routing prefix. 

### `Program.addressPC`

 Leaf-address decode and translated header read. 

### `Program.leaf`

 The address-reader registers, including the persistent input node slot. 

### `Program.addressPub`

 The public address-reader operands. 

### `Program.preparePC`

 The 29 setup instructions after either address-reader exit. 

### `Program.preparePub`

 The public arena and cache pointers. 

### `Program.route`

 The complete route scan. 

### `Program.init`

 Entry to the cursor-zero validator initialization. 

### `Program.transit`

 Return to the caller at a transit cursor. 

### `Program.Linked`

 Both address-reader exits join the setup before the routing test. 

### `trace`

 Exact event list on a passed route. Only the header access may probe
external memory, and the complete list consumes no branch bits. 

### `trace_probes`

 The only external probe in the front is the translated header read, exactly
when the site's address is within the prepared shadow region. 

### `Operands`

 Fixed arena pointers, cursor dimensions and prepared translated shadow
header, all read by the physical prefix. 

### `Cache`

 Geometry words placed in the private operand cache by the enclosing
final-site call. 

### `Cache.of_cached`

 Recover the three geometry operands from the final-site private cache. 

### `Result`

 Successful native return data needed by the stack initializer and the DFS caller. 

### `native`

 The three linked stages implement the physical leaf front on every fitted
stored cursor packet. A failed route cannot return on any branch suffix. 
