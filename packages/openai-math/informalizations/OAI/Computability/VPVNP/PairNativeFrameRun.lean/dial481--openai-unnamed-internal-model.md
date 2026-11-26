---
{
  "module": "OAI/Computability/VPVNP/PairNativeFrameRun.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairNativeFrameRun.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairNativeFrameRun.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Executing the terminal vertex's private geometry installation

The caller supplies two live registers holding the terminal header and its
role offset. The program consumes six external reads, computes all addresses,
and publishes the histogram and scalar-cache pointers in the designated
registers of the enclosing vertex burst.


### `Ports`

 Register allocation for the terminal frame installer, with input and output separation
conditions that protect the role and cache values during handoff. 

### `Ports.work`

 Embedding of the installer's 24 local work registers into the enclosing machine's
  register bank. 

### `Ports.header`

 Caller register supplying the terminal header's external address to the first entry copy. 

### `Ports.role`

 Caller register supplying the role offset to the second entry copy, distinct from the
  destination of the first copy. 

### `Ports.hist`

 Caller register receiving the private histogram base before the cache pointer is copied
  out. 

### `Ports.cache`

 Caller register receiving the scalar-cache base for the next phase of leaf preparation. 

### `Ports.code`

 Frame prelude specialized to the work-register embedding and the caller's two input
registers. 

### `Ports.row`

 Instruction-row emitter that uses these ports for the prelude, private frame stores and
pointer handoff to the caller. 

### `events`

 Trace of the entire frame installation, extending the prelude by 27 local ticks for private
stores, cursor advances and the two output copies. 

### `Result`

 The private memory and register ABI seen by all subsequent visits in
this burst, including visits that fail the route or cursor-zero verifier. 
