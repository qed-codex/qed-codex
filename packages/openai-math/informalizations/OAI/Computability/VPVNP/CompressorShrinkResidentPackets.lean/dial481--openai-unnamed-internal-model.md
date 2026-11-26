---
{
  "module": "OAI/Computability/VPVNP/CompressorShrinkResidentPackets.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorShrinkResidentPackets.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorShrinkResidentPackets.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # The twelve resident-directory visits in the installed compressor script

The old hidden and map directories each use an owner scan, a counter clear
and a guarded append. Six single-word publishers then install their heads
at offsets 30 through 35. The window starts after the 36 preceding visits
of the same shrinking substep.


### `Plan`

 Expressions and degree exponent used to plan the two resident directory builds and their
six header publications for a selected shrink. 

### `Plan.chosen`

 Selected-shrink input formulas supplying the site and motif counts, role-record base and
  layout choice. 

### `Plan.first`

 Expression for the first workspace address assigned to the hidden-field and party-map
  directories. 

### `Plan.oldLevel`

 Expression for the old level header where the six completed directory heads are
  published. 

### `Plan.absoluteCD`

 Expression for the dense motif-indexed array of absolute CD identifiers read by the owner
  scans. 

### `Plan.exponent`

 Old degree exponent used to compute the preimage-row capacity for the collector's operand
  bank. 

### `Stage`

 A resident-directory operation, either writing owners, clearing counts, appending preimages
for one resident kind, or publishing one of the six heads. 

### `scans`

 The three visits that build one resident directory, assigning owners, clearing site counts
and appending occurrence identifiers in order. 

### `order`

 Execution order of the twelve stages, building hidden-field rows, then party-map rows, then
publishing their six pointers. 

### `Stage.visit`

 Translate one resident stage into its scheduled worker, cursor bounds and operand
expressions for this plan. 

### `Plan.visits`

 The ordered block-planner visits that execute both resident directory builds and publish
their heads using the plan's inputs. 

### `plan`

 Recover the resident plan for a particular block substep from its selected inputs, old
level, directory arena, absolute CD table and old degree exponent. 

### `prior`

 The portion of this shrinking substep preceding its resident-directory window, comprising
the first 36 visits. 

### `window`

 Locate the twelve resident visits in the installed block script after the earlier substeps
and this substep's prefix. 

### `Values`

 Concrete resident workspace, header address, source pointers and layout choice used to
instantiate the planned scans at a given word width. 

### `Values.layout`

 The concrete layout of both resident directories, determining their table addresses and
  scan sizes. 

### `Values.level`

 Address of the old level header receiving the six resident directory pointers. 

### `Values.absolute`

 Machine-word pointer to the dense absolute CD identifiers, one per motif. 

### `Values.role`

 Machine-word pointer to the four-word role records indexed by absolute old arc. 

### `Values.side`

 The Boolean shrink layout used to select the resident's packed role when writing owners. 

### `Stage.limit`

 Exclusive cursor bound for this stage, the occurrence count for owners and appends, the
site count for clearing, or one for a head publication. 

### `Stage.fuel`

 Private fuel allowed for one worker call of this stage, determined by its native owner,
clear, append or publication code. 

### `Stage.bank`

 Concrete public operand vector for the stage's worker, using the instantiated directory
addresses, source pointers and selected layout. 

### `OperandValues`

 The planned operands evaluate in the current public words, state and memory to the concrete
resident layout, header address, source pointers and selected side. 

### `OperandReads`

 The only loaded expressions needed for all twelve visits. 
