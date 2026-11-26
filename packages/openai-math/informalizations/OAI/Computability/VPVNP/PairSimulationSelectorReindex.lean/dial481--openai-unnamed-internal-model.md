---
{
  "module": "OAI/Computability/VPVNP/PairSimulationSelectorReindex.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationSelectorReindex.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationSelectorReindex.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Full-word native term tapes and compact semantic selectors

The native ordinal worker guesses each nontrivial coordinate in a machine
word. The local-history reader uses the cap of its current level. Both
choices decode to the same admitted profile at the same physical ordinal.
The resulting equivalence acts only on term selections and preserves each
selected continuation.


### `TermRows`

 The selected term before reading any bits, in physical motif ordinal order. 

### `TermRows.demand`

 The input demand width for each demand edge of each motif, indexed by physical motif
  ordinal. 

### `TermRows.rows`

 Bijection between a pass term choice and the family of admitted supply profiles for its
  motifs' demand rows. 

### `termRows`

 Arrange the shrink or refresh motifs in physical ordinal order, with their demand widths
and the corresponding bijection from pass choices to admitted supply profiles. 

### `termRows_batch`

 The rows used to decode native tapes are the actual demand and supply
coordinates stored by the existing selected term batch. 

### `workerFit`

 The grid-dependent additive word-width constant in the native term scan's bound, before the
logarithmic contribution from the maximum demand width. 

### `WorkerInput`

 Public addressing, input rows, and the integer and instruction bounds
for the fixed ordinal worker on one actual pass. 

### `WorkerInput.layout`

 Addresses and separation bounds for the demand and output term rows of every motif in
  this pass. 

### `WorkerInput.addr`

 The worker's four address words in order, giving the demand base, demand stride, term
  base, and term stride. 

### `WorkerInput.memory`

 The initial worker memory containing the pass's demand widths at their assigned
  addresses. 

### `WorkerInput.fuel`

 Instruction allowance for each native motif call, large enough for the worker at this
  word width and maximum wire width. 

### `WorkerInput.run`

 Run one term-worker call per motif in ordinal order, starting with cursor zero and the
supplied memory. Successful execution returns the reports for all calls. 

### `WorkerInput.Accepted`

 Families of per-motif burst tapes for which the native term-worker scan succeeds on this
input. 

### `workerTapes`

 Encode the selected supply profile at one physical motif ordinal as its native burst tape,
in the grid's supply order and at the worker's coordinate width. 

### `WorkerInput.termEquiv`

 One accepting full-width stream family for every actual term, with
the payload words in their prescribed strided rows. 

### `WorkerInput.recode`

 Change the physical bit widths through their common admitted term.
The original decoder of a semantic stream and the native decoder of
its image return the identical branch index. 

### `WorkerInput.selected_run`

 The concrete native pass updates the physical term rows and returns
exactly the re-encoded choice tapes, one burst per motif ordinal. 

### `WorkerInputs`

 Worker inputs for every pass reachable in an execution, including the input for each
possible continuation after the current term choice. 

### `ordinalTapes`

 One native burst tape per motif, grouped by compression level. 

### `OrdinalPhases`

 Observable trace using one native term-worker tape per motif per pass, together with the
final shared-arc calls and private site expansions. 

### `OrdinalPhases.termCalls`

 Term-selection burst tapes grouped by compression level and ordered by motif ordinal
  within each level. 

### `OrdinalPhases.arcCalls`

 The final shared-edge burst strings belonging to the occurrence selected by the term
  tapes. 

### `OrdinalPhases.vertices`

 The private expansion strings of the terminal sites for this occurrence, in scan order. 

### `SelectorReindex`

 The native emission has one term burst per motif and retains the arc
and vertex bursts of the same monomial occurrence. 

### `SelectorReindex.emit`

 Assign distinct ordinal-phase traces to the observable phase lists in the original trace
  encoding. 

### `SelectorReindex.decode`

 Recover the semantic occurrence from an emitted ordinal trace by inverting the emission and
decoding the original phase lists. 

### `executionReindex`

 Re-encode every compact level selector by the actual ordinal worker
of that level. The chosen continuation, terminal memory and vertex paths
all refer to the decoded semantic branch. 

### `compressedReindex`

 Re-encode the level selectors of a compressed RAM trace as the actual per-motif worker
tapes along its selected execution branch. 

### `compressedReindex_exponents`

 The coordinate expansion in the machine-word tapes preserves the full
parameter exponent vector of every path. 

### `compressedReindex_sum`

 Weighted count with the actual per-motif native selector tapes. 
