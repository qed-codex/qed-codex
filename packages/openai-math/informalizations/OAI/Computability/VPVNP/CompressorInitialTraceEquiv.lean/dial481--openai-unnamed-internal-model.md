---
{
  "module": "OAI/Computability/VPVNP/CompressorInitialTraceEquiv.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorInitialTraceEquiv.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorInitialTraceEquiv.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Prepending the four deterministic cursor rows to selected compressor traces

The choice of each later pass is retained. The physical path predicate is
evaluated on all reports, including the initial deterministic rows. The
small-clock core report lists and the accepting path's actual bit stream
are preserved by the same concatenation.


### `withTrace`

 The deterministic cursor prefix followed by the selected compression passes. 

### `accepted`

 The operand-room predicate belongs to the whole run and can depend
on the reports of both the forced prefix and the selected suffix. 

### `allAccepted`

 Bijection with all selected terms when every branch meets the whole-run predicate. 

### `withTrace_stable`

 Any finite successful call prefix through these rows and the recursive
timeline retains all six bank words and the preceding live header. 

### `combinedCore`

 Small-clock inner reports of both the forced cursor interval and the selected tail. 
