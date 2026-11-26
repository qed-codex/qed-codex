---
{
  "module": "OAI/Computability/VPVNP/CompressorRefreshLevelRecipe.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRefreshLevelRecipe.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorRefreshLevelRecipe.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Online row planners for a complete degree refresh

The old base-vertex and residual-lane counts, allocation start, and three
input incidence pointers are expressions over the current level header. The
port degrees, motif strides, role order and expander are fixed for a block.
Every worker's stop cursor and public bank are computed in the planner
before dispatch, in the order used by the native refresh proofs.


### `Input`

 Dynamic values obtained from the current level header or its inputs. 

### `Input.start`

 Expression for the first word of the refresh level's allocation. 

### `Input.vertices`

 Expression for the number of base vertices in the incoming network. 

### `Input.lanes`

 Expression for the number of residual lanes after the port bits have been split off. 

### `Input.oldOut`

 Expression for the head of the incoming state's base outgoing incidence column. 

### `Input.oldShift`

 Expression for the head of the incoming state's lane-shift column. 

### `Input.oldWidth`

 Expression for the head of the incoming state's wire-width column. 

### `Shape`

 The fixed combinatorial and arithmetic parameters of a refresh. 

### `Shape.a`

 Number of port bits split from an incoming lane to form the promoted base vertex. 

### `Shape.a₀`

 Exponent of the dyadic slot degree in the refreshed state. 

### `Shape.dH`

 Degree of the expander on the refresh ports. 

### `Shape.ties`

 Number of demand ties enumerated in each base-vertex and residual-lane block. 

### `Shape.stride`

 Number of words reserved for each block's stored motif term. 

### `Shape.selectors`

 Width in bits of a selector in the fixed refresh template. 

### `Shape.ports`

 The number of promoted ports, equal to two raised to the input port exponent. 

### `Shape.degree`

 The number of output slots per refreshed vertex, equal to two raised to the new degree
exponent. 

### `Tags`

 The dispatcher's physical worker tags. All copies of a fixed worker use
one tag, including every demand row and each public expander ROM row. 

### `Tags.gather`

 Worker tag for gathering old segment widths. 

### `Tags.bundles`

 Worker tag for constructing the directory of external bundles. 

### `Tags.offsets`

 Worker tag for scanning the segment offsets. 

### `Tags.demand`

 Shared worker tag for the demand scans indexed by ties. 

### `Tags.term`

 Worker tag for the strided motif-term pass. 

### `Tags.supply`

 Worker tag for the scan that reads the selected terms and writes expander supply data. 

### `Tags.rom`

 Shared worker tag for publishing the fixed expander's reverse-incidence entries. 

### `Tags.external`

 Worker tag for writing the refreshed external slot. 

### `Tags.expander`

 Worker tag for writing an internal expander slot. 

### `Tags.padding`

 Worker tag for writing a padding slot of the refreshed degree. 

### `Tags.base`

 Worker tag for publishing the refreshed base-incidence columns. 

### `sites`

 Expression counting base-vertex, promoted-port and residual-lane triples. 

### `blocks`

 Expression counting base-vertex and residual-lane pairs, one per motif-term record. 

### `segments`

 Expression counting one old port segment per port at every promoted site. 

### `capacity`

 Expression counting all output incidence slots over the promoted sites. 

### `demandStart`

 Head of the dense demand table, following the seven segment-sized scratch columns. 

### `termStart`

 Head of the strided term records, following all blocks' demand ties. 

### `supplyStart`

 Head of the supply table, following the block term records. 

### `targetPort`

 Head of the expander target-port table, following the site-by-expander-slot supply table. 

### `reverseSlot`

 Head of the expander reverse-slot table, immediately after the target-port table. 

### `outputStart`

 Head of the refreshed incidence output, immediately after the expander reverse-slot table. 

### `allocationStop`

 Exclusive end of the level allocation after all six output columns. 

### `column`

 Base address expression for the indexed output column, spaced by the full incidence
capacity. 

### `scratch`

 The eight scratch operands, consisting of the port count followed by the heads of seven
segment-sized columns. 

### `termHeads`

 The demand head and tie count followed by the term head and stride, supplied to the motif
worker. 

### `Stage`

 A stage of the native refresh calendar, with separate occurrences for each demand tie,
expander ROM entry and output slot. 

### `order`

 The execution order from width gathering and demand scans through term selection, supply,
ROM publication, slot writing and base output. 

### `Stage.tag`

 Selects the dispatch tag for a stage, distinguishing the external, expander and padding
cases of a slot. 

### `Stage.arity`

 Number of public operand words used by a stage's native worker, parameterized by the motif
worker's arity. 

### `Stage.initial`

 Planner expression for the initial worker cursor, equal to the entry ordinal on a ROM stage
and zero on the other stages. 

### `Stage.stop`

 Planner expression for the exclusive stop cursor of a stage, sized to the table it scans. 

### `Stage.bank`

 The public operand expressions of a native stage, including its layout addresses and fixed
expander or tie indices. 

### `Stage.worker`

 Actual native instruction table of this calendar occurrence. The ROM and
demand tables vary their public literals across occurrences. 

### `Stage.workerBank`

 Operand formulas indexed directly by the actual worker table's ports. 

### `phase`

 The phase installed by the expression compiler for one fixed stage. 

### `phases`

 The entire fixed list of online planners, including one strided term scan. 

### `phases_length`

 A refresh adds a fixed number of rows to the block calendar regardless of
the incoming network size and the word width. 

### `Context`

 The public inputs, state word and memory against which a level's planner expressions are
evaluated. 

### `Context.pub`

 The five public input words available to a refresh planner expression. 

### `Context.state`

 The state word available to the refresh planner during expression evaluation. 

### `Context.memory`

 The memory read by load expressions in the refresh level planner. 

### `Context.eval`

 Evaluates a planner expression with the context's public words, state and memory. 

### `Describes`

 Meaning of the six dynamic expressions. The rest of the row values
follow from these six input words and the fixed template. 

### `Addresses`

 Correspondence of the computed addresses with the packed allocation
used by the descriptor correctness proof. Word reduction is valid at every
intermediate arithmetic operation. 

### `Stage.first`

 The natural starting cursor used by the native stage, with a ROM entry starting at its own
ordinal. 

### `Stage.limit`

 The exclusive natural cursor bound for a native stage, computed from the incoming state and
the level allocation. 

### `Stage.nativeBank`

 The public words consumed by the already checked native worker proofs. 

### `Stage.fields`

 Exact field list installed by the compiled planner for this native worker.
The common catalog bank is zero-padded past the worker's own arity. 

### `counter_values`

 With sufficient cursor space, the planner's two counter fields are the
exact natural start and stop, including the singleton ROM interval. 

### `limit_fits`

 Every stop cursor fits whenever the complete level allocation fits. The
proof includes the last expander ROM cursor and the lane-zero base pass. 

### `motifPhases`

 The motif worker supplies one phase for all blocks. Its address prefix is
computed online and the remaining grid and arithmetic operands are fixed
natural literals, independent of word width. 

### `motif_workerBank_eq`

 The occurrence-indexed registry may assign the tag after enumerating the
stages. Its public operands still agree pointwise with the native proof for
the fused motif worker or the selected deterministic worker. 

### `execute_motif_phase`

 The native planner installs the checked public operands, start and stop
for any selected stage of the fixed motif schedule. 
