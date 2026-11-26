---
{
  "module": "OAI/Computability/VPVNP/LiveProgramNominationPaths.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveProgramNominationPaths.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveProgramNominationPaths.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Bijection between histogram nominations and native stage histories 

### `Nom`

 One fixed-width nominated count at every position of the dense grammar-label array. 

### `activeReport`

 An active nomination call returns a state, uses one probe, and records exactly five times
the nomination width plus fourteen events. 

### `history`

 The source reports, before the dispatch read and closing tag transfer. 

### `equiv`

 Bijection from nomination arrays to complete nomination-stage paths, obtained by encoding
and decoding the guessed words in grammar-label order. 

### `Fits`

 Word, clock and memory layout conditions of the nomination stage. 

### `indexed`

 Index the actual tagged nomination-stage histories by their nomination arrays, using the
cursor bound and the word, address, and clock fits. 

### `logs_lengths`

 Linked active calls have one dispatcher read and one store. The last call
instead transfers the stage tag. Its shorter local run has a fixed length. 
