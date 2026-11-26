---
{
  "module": "OAI/Computability/VPVNP/RAMTapeInputPrefix.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeInputPrefix.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeInputPrefix.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Extracting the literal self-delimiting table prefix

A fixed stack control reads one unary length digit at a time. Each digit
supplies one counter marker, authorizing one payload bit after the zero
delimiter. It copies the entire field, including those length digits and
the delimiter, into the prefix stack in its original order.


### `PrefixPhase`

 Control for reading the unary prefix length, zero delimiter, and the indicated payload
bits, then restoring the whole prefix in order. 

### `prefixCode`

 Length-independent stack instructions for the first field. A missing
delimiter or a truncated table sends control to rejection. 

### `prefix_runs`

 The machine consumes precisely the self-delimiting table prefix. It leaves
the suffix at the input head, restores both scratch stacks and preserves the
values of every other port. The run length depends only on the table length. 
