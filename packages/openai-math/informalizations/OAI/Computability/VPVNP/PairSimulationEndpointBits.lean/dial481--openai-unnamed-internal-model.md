---
{
  "module": "OAI/Computability/VPVNP/PairSimulationEndpointBits.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationEndpointBits.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationEndpointBits.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Reading a final arc inside a vertex call

The five-opcode loop reads a contiguous final arc from external memory and
copies its bits into the private tape of the current vertex. It can be entered
at each source or target incidence with new interval bounds. Its continuation
keeps all private cells outside that interval, and the external memory and
branch stream are available to the rest of the vertex expansion.


### `instruction`

 Registers hold the current source, exclusive source end, current private
destination, one, and a temporary word. 

### `resize_instruction`

 The vertex reader has the same opcodes and jump targets at every word width. 

### `Linked`

 Require the five endpoint-copy instructions at the supplied program counters. Each
iteration loads one external arc cell into the private tape and advances both cursors until
control reaches `done`. 

### `events`

 Actual chronological events, including the loop exit test at width zero. 

### `copySlice`

 Closed form for the private-memory slice after the loop. 

### `execute_arc`

 Exact native execution inside an arbitrary vertex call. There is one
read per incident bit and no private branches. The updated private slice is
available to an arbitrary continuation at the chosen exit. 

### `offset`

 Beginning of an arc relative to the lower address of the bit array. 

### `execute_payload`

 An incidence reader linked inside a final vertex call copies exactly the
edge payload of equation (7.1) into its private workspace. The copy executes
from the first loop opcode, including for a zero-width edge. 

### `endpoint_probe_total`

 Summing the native reader's probe counts at the source and target of
every arc gives twice the total bit width. Loops contribute both incidences. 
