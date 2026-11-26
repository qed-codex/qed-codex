---
{
  "module": "OAI/Computability/VPVNP/PairSimulationMapDirectoryInit.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationMapDirectoryInit.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationMapDirectoryInit.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Initializing the grouped map's incident selector directory

The private directory contains one word for each incident half-wire, in the
order consumed by the selector scanner. A fixed three-instruction block adds
the edge's payload width to that half-wire's bit base, stores the pointer,
and advances the cursor. A self-loop therefore supplies two directory rows.


### `portField`

 The source and target ports refer to different row-bank base registers. 

### `Row`

 Index of an incident supply port in the order scanned by the directory initializer. A
self-loop contributes one source row and one target row. 

### `Address`

 Directory initialization addresses, consisting of a cursor setup followed by three
instructions per incident port to compute, store, and advance. 

### `text`

 Relocatable copy, add, private store and increment instructions. 

### `native`

 Starting with arbitrary private memory, the native instructions write every
selector-start pointer and transfer control to the scanner. The addresses may
wrap around the word modulus, as long as the directory has at most that many rows. 
