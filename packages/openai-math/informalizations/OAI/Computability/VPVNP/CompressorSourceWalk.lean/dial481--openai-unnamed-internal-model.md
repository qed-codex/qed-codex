---
{
  "module": "OAI/Computability/VPVNP/CompressorSourceWalk.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorSourceWalk.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorSourceWalk.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Chronological source kernels in external memory

The native descriptor recipe consists of heterogeneous kernels, with
each segment starting from the data memory produced by the preceding one.
Packets retain the source ordinal, actual input memory and report list
when the online dispatcher inserts its control calls.


### `SourceWalk`

 A sequence of heterogeneous native source kernels operating on one shared
memory. The join keeps their actual reports, including empty phase segments. 

### `Packet`

 A source stage together with its entry memory and sequence of native reports. 

### `Packet.stage`

 Source stage executed to produce this packet. 

### `Packet.input`

 Memory supplied to the source stage before its first call. 

### `Packet.reports`

 Reports returned by the stage in execution order. 

### `Packet.output`

 Memory obtained by replaying the packet's reports on its entry memory. 

### `Chronological`

 Each packet runs its named stage on the preceding packet's output, beginning with the
supplied memory. 
