---
{
  "module": "OAI/Computability/VPVNP/LiveCompressedPairStartupRun.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveCompressedPairStartupRun.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveCompressedPairStartupRun.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Physical cursor startup at the paper's dimensions

The fixed compressed pair executes eight native calls on the actual eleven
public operands. One logarithmic private clock covers every call, uniformly
over the program prefix and incoming memory. The auxiliary shadow-copy stage
supplies the row counter's initial tag by `PreparedBranch.startup_tag`.


### `eventually_physical_startup`

 For the physical pair ABI, one logarithmic clock suffices at every large
input length. The incoming tag condition is the one established by the
preceding auxiliary preparation. 

### `StartupResult.first_online`

 A nonempty calendar runs its first online dispatch directly on the native
pair program, using the memory and tag left by the eight linked startup calls. 
