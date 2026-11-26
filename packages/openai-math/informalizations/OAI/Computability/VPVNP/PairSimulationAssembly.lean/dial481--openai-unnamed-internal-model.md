---
{
  "module": "OAI/Computability/VPVNP/PairSimulationAssembly.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationAssembly.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationAssembly.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Binary readers for the repeated RAM compressor

The branch selectors read the admitted payload coordinates of each motif.
At the selected term, the layout reader consumes the absorbed fields and
checks the local map entries. These choices compose along the same
branch-dependent executions as the monomial witnesses of equation (12.2).


### `Order.fin`

 Enumerate the indices of `Fin n` in increasing order. The position passed to a descriptor
reader is the index itself. 

### `Order.prod`

 Enumerate a pair of ordered sets by dividing a single position among blocks of length
`t.length`. Within the block for an entry of `s`, visit every entry of `t` in order. 

### `Order.restrict`

 Scanning a descriptor list and retaining just the records in one fiber
preserves the relative order of their numerical identifiers. 

### `siteOrder`

 Site order follows the stored base numbering and the binary lane
coordinate. Each site's outgoing slots then occur in slot-number order. 

### `edgeOrder`

 Order all outgoing edges first by their source site's base and lane coordinates, then by
their slot number. The terminal history reader uses this order to read one payload per
edge. 

### `PassReaders`

 A descriptor supplies the selection parser and the ordered data for
each of the resulting local kernel checks. The old arc payloads are the
bit words in the current lifted state. 

### `PassReaders.select`

 Binary reader for the choice of term at this pass. The selected index determines which
  local ordering, kernel readers and successor state apply. 

### `PassReaders.order`

 For each selected term, specify the order of each site's children and the outgoing and
  incoming incidences read at those children. 

### `PassReaders.kernel`

 Reader for the local monomial witness at output site `v` of term `i`, given the old
  half-edge assignments `x` of its children and the new half-edge assignment `z`. 

### `ExecutionReaders`

 All the local parsers, indexed by the original execution and its
monomial witnesses. 

### `executionHistoryReaders`

 At a terminal state, read each arc once and pass the assignment to
all sites. At intermediate states, the output identification transports
the continuation and its parsers together. 

### `bindReaders`

 When two executions are joined, read the continuation selected by the
full choice of the first execution, preserving the same selector stream. 

### `ProcedureReaders`

 Readers on every input with the correct number of lanes. 

### `id`

 Supply the empty execution reader for the identity procedure. Its input is already the
final state, so there is no pass choice or kernel to parse. 

### `ofPass`

 Lift readers for each admissible input of a single pass to readers for its one-step
procedure. Each term uses the supplied pass reader and leads directly to the terminal
execution. 

### `seq`

 Compose two procedure readers along their executions. Each full choice of the first
procedure supplies the final state on which the second procedure's reader starts. 

### `reindex`

 Transport readers and their map witnesses across equalities of the procedure's input and
output exponents, consumed lanes, position factor and energy coefficient. 

### `repeatReaders`

 Build readers for `T` iterations of a procedure that consumes `l` lane bits each time and
leaves `g` at the end. The continuation uses the state selected by the preceding iteration. 

### `assembleReaders`

 Assemble readers for one scheduled block. Compose the readers of all shrink levels in
schedule order, then attach the refresh reader at the state reached by that sequence. 

### `selectorWidth`

 One common word width for all nonzero-demand motifs of the pass. 

### `selectPass`

 Read the admitted coordinates in the fixed motif and supply-edge orders. 

### `shrinkMotifOrder`

 The dense term row is the packed bundle ordinal followed by its CD
rank. This is the same row the native demand and term scans visit. 

### `shrinkPassReaders`

 Construct the selector and kernel readers of shrink level `i`. They enumerate packed motifs
and the eight supply edges, then read each chosen term's absorbed fields and local map
choices in the restricted site orders. 

### `shrinkProcedureReaders`

 Equip the one-pass shrink procedure at level `i` with its concrete binary readers for every
input state satisfying the packing lane count. 

### `refreshProcedureReaders`

 Construct the refresh procedure's readers by enumerating base–lane motifs and port–expander
supply edges. After the admitted payload choice, the local parsers use the restricted site
order to read the selected term. 

### `blockReaders`

 All actual term and entry parsers of the fixed schedule, including
the branch-dependent inputs to its last port refresh. 

### `executeReaders`

 Read the history of `T` concrete compressor blocks from `X`. The repeated shrink and
refresh readers follow the selected branches, and the terminal reader visits the final
state's edges and sites. 

### `compressedReader`

 The binary reader for the occurrence type of the repeated compressor
on the padded RAM cursor network, using its actual branch descriptors. 

### `compressed_weightedStreams`

 The weighted count of complete binary streams is the original capped
path count, with every stream carrying its own parameter exponents. 
