---
{
  "module": "OAI/Computability/VPVNP/RAMProcessorLocalResult.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMProcessorLocalResult.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMProcessorLocalResult.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Exact native result at the external-action boundary

A successful private scan returns a callback and the residual state, fuel and
guess suffix. The caller's permitted probe consumes its charge before looking
at a read value. Resuming this way and prepending the scan's private events
gives exactly the native local report, also on over-cap or truncated streams.


### `Output`

 Optional call report together with the unconsumed suffix of the site's nominated bit
stream. 

### `addEvent`

 Prepend one event to a successful report while retaining its unused bit suffix and
propagating failure. 

### `addEvents`

 Prepend a chronological event prefix to a successful local output, preserving its residual
bits. 

### `resume`

 Resume exactly one pending external or terminal action. 

### `result`

 Resume a yielded local call under the remaining probe allowance and attach the private
events recorded before its callback. 

### `scan_result`

 The caller can consume the generated word and communicate a record at
each callback without losing or multiplying any native successful report. 
