---
{
  "module": "OAI/Computability/VPVNP/LiveProgram.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveProgram.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveProgram.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The native control flow of the live group computation

The header program runs first and checks the incident cuts. Three short
routers read its mode, first-tail and last-group flags. Pair groups construct
the shadow of the auxiliary machine, execute the compressed pair routine,
and check the exponent update. Tail groups construct or read the incoming
configuration and check one evaluator transition against the required output.

The compressed pair computation is a separately supplied native instruction
table with eleven operands. Its two literal-prefix operands come from the
processor's own input. The other operands of the live program use the
length-only arithmetic expressions of `LiveProgramLayout`.


### `Stage`

 The twenty-one stage tags of the native live group program, covering header checks, the
pair counter and the evaluator tail. 

### `header`

 Read and validate the incident header and cuts, and publish the mode and endpoint flags. 

### `mode`

 Read the checked mode tag to finish a unit group or enter its pair or evaluator-tail
computation. 

### `nominations`

 Guess the production counts for a primed pair and store one nominated word per grammar
label. 

### `auxiliaryInit`

 Prepare the copy descriptors for the primed pair counter's external header and nominated
histogram. 

### `auxiliaryCopy`

 Copy the recovered header fields and nominated counts into the pair counter's shadow
memory. 

### `pair`

 Execute the supplied compressed pair counter on its shadow header and workspace. 

### `exponents`

 Check that each outgoing exponent equals its incoming exponent plus the increments produced
by the pair path. 

### `firstTail`

 Test whether to initialize the evaluator at the first tail group or gather its incoming
configuration. 

### `initialState`

 Install the initial evaluator control state in the old configuration bank. 

### `prefixLength`

 Pack the prefix length from the header's advice bits into a word for preparing the
evaluator input. 

### `adviceFrames`

 Check the packed prefix length and publish the operand frames for prefix packing, copying,
runtime initialization and exponent scatter. 

### `prefixPack`

 Pack the active prefix bits from the advice into words for the evaluator's input tape. 

### `orderPack`

 Pack the advised label ordering into the lookup table used to reindex exponents. 

### `prefixCopy`

 Copy the packed program prefix into the evaluator's initial tape window. 

### `skeleton`

 Write the evaluator runtime suffix with its width fields, delimiters and initially zero
exponent positions. 

### `scatter`

 Write the incoming exponent bits into the runtime tape using the advised label order. 

### `oldGather`

 Gather the incoming configuration from the left cut into the old evaluator state bank. 

### `last`

 Test whether the outgoing configuration must be the final accepting state or should be
gathered from the right cut. 

### `finalState`

 Install the prescribed accepting evaluator endpoint in the new configuration bank. 

### `newGather`

 Gather the outgoing configuration from the right cut into the new evaluator state bank. 

### `transition`

 Check one evaluator transition against the old and new configurations, including both tape
windows. 

### `modeTarget`

 Decode the mode flag. Zero accepts the unit group, one enters nominations and two enters
the first-tail test. 

### `firstTarget`

 Route flag zero to incoming-state gathering and flag one to evaluator initialization. Flag
two rejects. 

### `lastTarget`

 Route flag zero to outgoing-state gathering and flag one to the prescribed accepting state.
Flag two rejects. 

### `next`

 A router selects its destination by writing the outer tag and returning
zero. Its accepting exit therefore finishes the whole group. The accepting
exit of an ordinary stage transfers to its specified successor. 

### `PairTable`

 The compressed pair's input ABI. The original processor's program prefix
is read from its literal input. Every group-specific value is obtained from
header or workspace addresses. 

### `PairTable.pcs`

 Number of instruction addresses in the supplied compressed pair counter. 

### `PairTable.regs`

 Number of private registers used by the supplied compressed pair counter. 

### `PairTable.table`

 Native instruction template of the compressed pair counter, with eleven public operand
  slots. 

### `router`

 Supply the router with the address of the flag to read and the outer stage-tag address to
update. 

### `nomination`

 Supply the per-label guess width, the nomination counter base and the number of grammar
labels. 

### `auxiliary`

 Fourteen operands describing header sizes, shadow and descriptor bases, and the physical
sources of the primed indices, advice, cuts and histogram. 

### `auxiliaryCopy`

 Supply the copy descriptor table base and the address of the final packed-end word in its
seventh descriptor. 

### `pair`

 Public operands of the compressed pair stage, including the original processor's literal
prefix word and length, workspace and shadow bases, counter and geometry. 

### `exponents`

 The left and right exponent bases, increment counter base, digit width and extent used to
check the exponent update. 

### `control`

 Supply the evaluator control-state writer with its radius, destination bank, zero operand
and machine word width. 

### `lengthPack`

 Five operands for reading one width-`w` prefix length from advice and storing it at offset
22 of the frame area. 

### `adviceFrames`

 Supply the frame publisher with the advice and prefix geometry, evaluator banks, exponent
dimensions and label-order map base. 

### `orderPack`

 Operands for packing one order-map entry per label from the advice interval after the
prefix capacity, using the ceiling binary logarithm of the label count as its bit width. 

### `gather`

 Supply the selected cut's configuration address, destination state bank, word width and
number of configuration words. 

### `transition`

 Supply the evaluator step checker with the tape radius, old and new state bases and
transition scratch address. 

### `rows`

 Each row is a concrete native stage. `O` supplies the separate compressed
pair computation. Its input bank has the same fixed layout for every length. 

### `program`

 The fixed table is independent of input geometry, advice contents, and
own-prefix values. It can be compiled before choosing the eventual length. 

### `operand`

 Flatten the live stages' public operand expressions and append the outer stage-tag address. 

### `publicData`

 Evaluate the flattened operands for the chosen geometry and literal processor prefix as
machine words. 

### `machine`

 Instantiate the linked live group program at the given word width with its evaluated public
operands. 

### `paths`

 Exact native all-path semantics at each length and clock, with choices
retained across all handoffs, including repeated equal evaluator outcomes. 
