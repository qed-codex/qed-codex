---
{
  "module": "OAI/Computability/VPVNP/CompressorPayloadCall.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorPayloadCall.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorPayloadCall.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# A native descriptor call from a stored repetition count

The persistent word gives the first payload address. Its predecessor holds
the repetition word computed for this motif. The call reads that word, sets
the bounds, admits the outer vector, and writes all of its supply coordinates.


### `loadRepetition`

 Read the repetition word immediately preceding the output slice. 

### `storedCall`

 Native flow that reads a motif's stored repetition word, prepares the admission bounds,
chooses its payload, and writes it. 

### `storedMachine`

 Word-width instance of the stored-payload worker with the selected supply order and scaled
admission weights as public operands. 

### `storedFuel`

 Fuel bound for reading the repetition count, preparing bounds, admitting coordinates, and
writing the payload. 

### `storedFuel_le`

 Only the word reader scales with the machine width. The threshold
preparation cost depends on the fixed binary motif coefficients. 

### `stored_outer_paths`

 Starting at reset with the descriptor base as persistent state, the
accepted streams are precisely the motif's outer encodings. On each stream
the output memory contains the chosen coordinates and agrees elsewhere with
the input. The call reads the repetition word once and writes each supply coordinate once. 
