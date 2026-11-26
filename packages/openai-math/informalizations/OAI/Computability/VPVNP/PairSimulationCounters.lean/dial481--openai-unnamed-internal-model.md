---
{
  "module": "OAI/Computability/VPVNP/PairSimulationCounters.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationCounters.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationCounters.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Flushing a final vertex's gadget histogram

At the end of its burst the vertex has a private array of gadget exponents.
The shared array holds the nominated production histogram first and the
gadget histogram second. Seven fixed instructions loop over the suffix.
Each iteration loads one private count and makes one external read and write.


### `instruction`

 Registers hold external cursor, external end, private cursor, one,
external count, and local count. 

### `Linked`

 Require the seven code rows of the histogram flush at their assigned labels. They
accumulate the local gadget counts into the shared histogram suffix and jump to `done` at
its end. 

### `addRange`

 Accumulation at consecutive addresses with the original memory elsewhere. 

### `events`

 Genuine chronological transcript of all component updates, including the last loop test. 

### `after_events`

 Replaying the burst log at the next call produces exactly the same
memory as the continuation within the current call. 

### `execute_range`

 Run the whole suffix within the current burst, then pass control to any
continuation with the updated external memory and original private histogram. 

### `addHistogram`

 Logical effect of a single successful vertex. The label number is an
offset in the gadget suffix of the contiguous production/gadget array. 

### `execute_vertex_events`

 Native vertex flush with no new branches. The continuation receives
the combined histogram and all private state accumulated by the expansion. 

### `entryCode`

 Entry code from a vertex continuation. Its four parameter words give
the shared base, production count, gadget count, and private histogram base.
The total width is part of the fixed problem's parameters. 

### `execute_flush`

 The full flush starts at its first public-word instruction. Every
register may hold arbitrary data left by the preceding vertex expansion.
The parameter loads cost seven local steps once for the whole suffix. 

### `template`

 Fixed finite table for the complete flush with an accepting exit. The
linked version can replace the exit with the caller's next instruction. 

### `template_execute`

 Concrete instantiation at an arbitrary word width and a vertex's actual
private memory. The deterministic halt includes the final instruction. 

### `visit`

 Fold the effects of the per-vertex continuations in visit order. 

### `nomination_preserved`

 The production nomination at every prefix address survives all vertex bursts. 

### `prefix_fits`

 Any prefix of the selected visit order has exact natural-valued counters.
Bounding the total by R² bounds every intermediate coordinate by the same
2r-bit capacity, independently of the order of the visits. 

### `component_no_overflow`

 At a vertex the old stored word plus the current natural increment is
the next word's natural value. It is at most the total and fits in 2r bits. 

### `initial_suffix_zero`

 Lemma 10.1 initializes every gadget counter to zero when the suffix
starts beyond the prescribed header addresses. 

### `vertexHistograms`

 Final-vertex private histograms in the actual descriptor's visit order.
A selector descends only into its selected term, whose witnesses already
include the local maps and all the children placed at that site. 

### `vertexHistograms_sum`

 Summing the completed private histograms gives the formal monomial
exponent of the selected occurrence, including syntactically nonzero
monomials whose evaluated scalar may vanish. 

### `history_readback`

 The physical suffix and the formal ν(e) agree for every selected
history. A bound on *total* degree gives exact readback of every coordinate
in the 2r-bit output convention. 

### `live_array_readback`

 Readback in the live exponent routine's single contiguous array. Its
first coordinates are the already nominated µ words and the remaining
coordinates are exactly ν(e) for the chosen compression occurrence. 
