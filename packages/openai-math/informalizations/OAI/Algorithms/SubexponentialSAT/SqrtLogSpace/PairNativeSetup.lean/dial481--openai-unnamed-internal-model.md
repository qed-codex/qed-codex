---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/PairNativeSetup.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/PairNativeSetup.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/PairNativeSetup.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Physical pair traversal initialization and ambient-mask expansion. The
five low scratch ports325..329 are reclaimed before the caller returns; the
pair controller and persistent node/layout words are not scratch. 

### `visits`

 Each actual mask pop charges one constant-cost branch; the mathematical
visit list is proof data and is absent from all executable stacks. 

### `trace_space`

 Exact unary false-count and every source-prefix bound on one fixed local
program. Its input and output words both have at most the incoming mask size. 

### `countCommand_cost`

 This setup is polynomial local work, so charging its entire finite run is
valid for all-prefix storage. It never charges a surrounding pair traversal. 

### `false_count_highMask`

 The real descending high mask has exactly one false bit per residual
coordinate, including both empty-coordinate edge cases. 

### `setup_resources`

 Both pair controllers are initialized by executed scans/copies. All
persistent caller ports outside the finite written set are preserved. 

### `fill_resources`

 Copying and zero insertion retain both controller masks and all other
caller data outside the selected output and the five reclaimed scratch ports. 

### `expand_resources`

 One concrete run expands both reversed residual masks to full ambient
masks and returns every allocated scratch stack empty. 

### `setupCaller_eval`

 The real shared-ABI setup call, ready for structured-command sequencing.
The boundary word bound is preserved even though all internal prefixes are charged. 

### `expandCaller_eval`

 The actual shared-ABI mask expansion is directly composable and restores
the same boundary word bound, since the retained high mask already has length n. 

### `setupCaller_resources`

 The fixed shared forty-register leaf ABI invokes the same concrete setup.
The call return and the caller halt are included in the time and prefix bound. 

### `expandCaller_resources`

 Ambient E/U words and controller preservation in the shared leaf ABI.
No callback, decoder oracle or supplied successful layout is assumed. 
