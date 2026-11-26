---
{
  "module": "OAI/Computability/VPVNP/PairSimulationScanTrace.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationScanTrace.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationScanTrace.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Native final-arc calls inside the compressed occurrence count

A trace retains the selector bit strings by level, the chronological native
calls that write the shared final arcs, and one private expansion string
per final site. The final shared assignment is decoded from the very same
native calls used in the trace. Distinct traces remain distinguishable
even when all their parameter exponents agree.


### `Phases`

 Choice strings observed for a compressed occurrence, grouped into level selectors, shared
final-arc calls and private expansions at the final sites. 

### `Phases.selectors`

 The compact term-selection strings along the chosen history branch, ordered from the
  first pass to the last. 

### `Phases.arcCalls`

 The branch bits of each native call that writes the terminal shared edge payloads, in
  execution order. 

### `Phases.vertices`

 The private expansion strings for the terminal site factors, listed in terminal site
  order. 

### `Phases.prepend`

 Extend a continuation trace by putting the current pass's selector string at the front of
its selector list. 

### `ScanPhase`

 The path type of the native final-arc phase and its reconstruction
of the unique shared payload assignment. 

### `ScanPhase.Path`

 The type of successful paths of the shared final-edge scan on this network. 

### `ScanPhase.payload`

 Bijection decoding a scan path to the shared payload on every edge of the terminal
  network. 

### `ScanPhase.calls`

 The chronological list of burst choice strings emitted by a final-edge scan path. This
  list identifies the path uniquely. 

### `ScanPhases`

 A family of final-edge scans indexed by history leaves. At a branch it supplies a scan
family for each possible term choice. 

### `TraceEncoding`

 An encoding of occurrences by traces, with a bijection to occurrence indices and observable
phase lists that distinguish the traces. 

### `TraceEncoding.Trace`

 The type of traces that encode the given semantic occurrence indices. 

### `TraceEncoding.decode`

 Bijection sending each complete trace to the occurrence it represents. 

### `TraceEncoding.phases`

 Extract the observable selector, shared-arc, and private-site strings from an encoded
  trace. 

### `TraceEncoding.emitted`

 The observable phase lists determine the complete semantic occurrence. 

### `scanTrace`

 Replace just the final shared choice by its native call path. Every
descriptor and site reader still uses the selected term and its exact
map and child arguments. 

### `AtTerminals`

 A property of the chronological selectors and native shared arc calls
at all leaves of a history. 

### `selectorCodes`

 Individual level strings in chronological order along a descriptor path. 

### `stateScanPhase`

 For any linked scan, its successful call sequences are in bijection
with the terminal edge payloads in the physical base, lane and slot order. 

### `executionScanPhases`

 Equip each leaf of a state execution with the linked final-bit scan, using that branch's
final network and its supplied terminal memory. 

### `executionTrace_calls`

 Every observable trace contains the selectors of one actual branch
and an accepted native shared scan on that same branch's output network
and post-descriptor memory. 

### `compressedScanTrace`

 A complete compressed occurrence, with its final shared indices
chosen by the linked machine's actual burst calls. 

### `compressedScanTrace_sum`

 The traced occurrences, with their native shared-arc call streams,
retain exactly the original capped machine's weighted count. 
