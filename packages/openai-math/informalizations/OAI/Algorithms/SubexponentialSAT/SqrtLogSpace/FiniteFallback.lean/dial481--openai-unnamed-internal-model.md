---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/FiniteFallback.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/FiniteFallback.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/FiniteFallback.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Generic finite scanner selectively adapted from the reviewed canceled source
`CountingDraft/FiniteWordScanner.lean`; no obsolete endpoint or rate is imported.

Fixed finite control for bounded input prefixes and complete binary output words.
The transition table is chosen before any runtime input. 

### `boundedNext`

 `none` is a single overflow state. Bounded prefes occupy fixed finite control. 

### `labelCount`

 One fixed table contains the complete output word for each finite scanner state. 

### `SmallFormula`

 The finite domain is fixed by the cutoff, before the input. Ambient variables
are part of the domain and therefore contribute their full free-variable factor. 

### `tableCount`

 Finite precomputation forms part of the fixed finite transition table. It is
not an input-dependent runtime loop or a unit-cost semantic query. 

### `countProgram_trace`

 The real scanner consumes the canonical input and emits every count bit. 

### `jointCommand`

 The finite count table is called, then a real scan restores the count word
and writes its positivity to the separate answer stack. 

### `primitive_trace`

 Both physical outputs, real primitive time, and every-prefix visited space
are established for the same guarded execution. This theorem covers only the
fixed finite exceptional range; its constants may depend on the cutoff. 

### `polynomial_trace`

 Explicit fixed positive coefficients give linear input-length resources
for the bounded-variable counter, including the actual SAT positivity output. 

### `resetScannerRegs`

 Only the scanner's two registers are reset; all dispatcher tapes survive. 

### `framedCountCommand_eval`

 The finite scanner is callable after preprocessing, with arbitrary framed
registers and stacks. Its own initial registers are established by real steps. 

### `framedProgram_trace`

 Source execution and every-prefix stack space for the actual framed call.
The bound includes every retained dispatcher stack, including old answer data. 

### `cutoffNext`

 Finite saturated control for the fixed exceptional cutoff; no numeric
cutoff is stored in an input-dependent runtime array. 

### `dispatchCommand`

 The small/large choice is made by the actual cutoff flag. The large branch
is a finite command selected before the input; no execution service is assumed. 

### `dispatch_large_eval`

 The complementary branch uses the same actual cutoff scan and preserves
its input frame before entering the fixed large-input command. 

### `dispatch_large_space`

 A local prefix bound for the dispatcher composes with the proved prefix
bound of its actual large command, independently of the large running time. 
