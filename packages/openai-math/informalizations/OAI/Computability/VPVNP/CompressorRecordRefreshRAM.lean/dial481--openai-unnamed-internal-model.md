---
{
  "module": "OAI/Computability/VPVNP/CompressorRecordRefreshRAM.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRecordRefreshRAM.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRecordRefreshRAM.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Writing external segment records during a degree refresh

Appendix E visits the source ports of each bundle consecutively. The directory stores the
translated destination bundle and the port displacement for each source bundle. Each visit
reads the old width and the running total. It writes the offset at both ends, the incoming
width at the translated port, and the new total. The outgoing width remains directly
available in the old-width array. All addresses below are word addresses.


### `visit`

 Public words, in order, are the degree, old widths, bundle targets, port shifts,
bundle totals, outgoing offsets, incoming offsets and incoming widths. The persistent
state is the source segment number in bundle-major order. 

### `bundle`

 Recover the source bundle from a segment ordinal by dividing by the port count. 

### `destination`

 Find the incoming segment ordinal using the stored target bundle and the source port
translated by the bundle's XOR shift. 

### `update`

 Physical update, including the two offset records in the same source-port order. 

### `events`

 External accesses and local word steps in scan order. 

### `visit_native`

 From zeroed call-local memory the fixed table returns the next source identifier.
Its eight probes cover both ends even for a zero-width wire. 

### `prefix_exact`

 The updated total is the exact right endpoint whenever the bundle fits in one word. 
